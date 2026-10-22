"""One run of the bot. GitHub Actions calls this every 15 minutes.

Each run: read the account -> enforce halts -> (when due) ask Claude -> pass every action through
the risk guard -> send orders -> update the control bot -> write the journal and dashboard data.
Stops and take-profits are checked against every 1-minute candle between runs by the paper exchange.
"""
import csv
import json
import os
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

import requests

from . import config, control, guard
from .paper import PAIRS, ExchangeError, PaperExchange
from .market import snapshot


def log(*a):
    print(datetime.now(timezone.utc).strftime("%H:%M:%S"), *a, flush=True)


def load_json(path, default):
    try:
        return json.loads(Path(path).read_text())
    except (FileNotFoundError, ValueError):
        return default


def save_json(path, obj):
    Path(path).write_text(json.dumps(obj, indent=1, default=str))


def usd_pln(state):
    """Official NBP mid rate; falls back to the last known one."""
    try:
        r = requests.get("https://api.nbp.pl/api/exchangerates/rates/a/usd/?format=json", timeout=10)
        rate = float(r.json()["rates"][0]["mid"])
        state["fx"] = rate
        return rate
    except Exception:
        return state.get("fx", 3.88)


def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_iso(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def read_journal(path, n):
    try:
        lines = Path(path).read_text().splitlines()
    except FileNotFoundError:
        return []
    out = []
    for line in lines[-n:]:
        try:
            out.append(json.loads(line))
        except ValueError:
            pass
    return out


def close_all(client, positions, why, events):
    for p in positions:
        try:
            client.close_position(p)
            events.append({"type": "forced_close", "symbol": p["symbol"], "why": why})
        except ExchangeError as e:
            events.append({"type": "close_failed", "symbol": p["symbol"], "error": str(e)})


def main(client=None, brain=None, now=None, fx=None, market=None, light=False):
    """light=True: a quick 1-minute tick (exchange, stops, account, dashboard) without the full market scan."""
    now = now or datetime.now(timezone.utc)
    now_ms = int(now.timestamp() * 1000)
    day = now.strftime("%Y-%m-%d")
    d = Path(config.DATA_DIR)
    d.mkdir(parents=True, exist_ok=True)
    state_path, journal_path = d / "state.json", d / "decisions.jsonl"
    state = load_json(state_path, {})

    if light and "start" in state:
        dec = load_json(d / "brain_decision.json", None)
        if dec and dec.get("id") and dec["id"] != state.get("last_decision_id"):
            light = False  # a new decision needs fresh market data
    rate = fx or (state.get("fx") if light and state.get("fx") else usd_pln(state))
    if client is None:
        start_usd = None if "start" in state else round(config.START_PLN / rate, 2)
        client = PaperExchange(d / "exchange.json", market=market, start_usd=start_usd, now_ms=now_ms)
        if not client.ready:
            log("state.json exists but exchange.json is missing; delete docs/data/state.json to restart.")
            return None
    if hasattr(client, "advance"):
        client.advance()  # replay the minutes since the last run: stops, targets, funding, liquidation

    # ---- account ---------------------------------------------------------------
    wallet = client.wallet()
    exch_equity = wallet["equity"]
    if "start" not in state:
        btc = client.ticker("BTCUSDT")["last"]
        state.update({
            "start": iso(now), "start_ms": now_ms, "start_fx": rate,
            "start_usd": round(config.START_PLN / rate, 2),
            "exchange_equity_at_start": exch_equity, "start_btc": btc,
            "peak_equity": round(config.START_PLN / rate, 2), "calls": {}, "closed_trades": [],
        })
        log(f"initialised: {config.START_PLN} PLN = {state['start_usd']} USD, exchange equity {exch_equity}")
    # The bot's own equity: virtual start + everything the exchange account gained or lost since.
    equity = state["start_usd"] + (exch_equity - state["exchange_equity_at_start"])
    positions = client.positions()

    events = []
    since = state.get("last_closed_check_ms", state["start_ms"])
    known = {t["id"] for t in state["closed_trades"]}
    for t in client.closed_pnl(since - 120_000):
        if t["id"] not in known and t["time"] >= state["start_ms"]:
            state["closed_trades"].append(t)
            events.append({"type": "position_closed", **t})
    state["last_closed_check_ms"] = now_ms
    if hasattr(client, "order_events"):
        seen = state.setdefault("seen_order_events", [])
        for e in client.order_events(since - 120_000):
            k = f"{e['id']}:{e['status']}"
            if k not in seen:
                seen.append(k)
                events.append({"type": "order_" + e["status"], **e})
        state["seen_order_events"] = seen[-300:]

    # ---- halts and the end of the experiment --------------------------------------
    ended = now >= parse_iso(config.END_AT)
    halt = None
    if ended:
        if not state.get("ended"):
            close_all(client, positions, "experiment ended", events)
            cancel_all_orders(client)
            state["ended"] = iso(now)
    else:
        halt = guard.check_halts(state, equity, day)
        if halt and (positions or open_orders(client)):
            close_all(client, positions, "kill switch: drawdown limit" if halt == "kill" else "daily loss limit", events)
            cancel_all_orders(client)
            events.append({"type": "halt", "kind": halt})

    if events:
        positions = client.positions()

    # ---- market data ------------------------------------------------------------
    markets, raw = {}, {}
    for sym in ([] if light else config.SYMBOLS):
        try:
            markets[sym], raw[sym] = snapshot(client, sym)
        except Exception as e:  # one bad symbol must not stop the run
            log(f"snapshot failed for {sym}: {e}")
            print(f"::warning::no market data for {sym}: {e}", flush=True)

    entry, trigger = None, None
    if light:
        state.setdefault("pending_events", []).extend(events)
    elif config.BRAIN_MODE == "session":
        state.setdefault("pending_events", []).extend(events)
        entry = take_session_decision(client, state, d, now, equity, rate, positions, markets, journal_path,
                                      blocked="experiment ended" if ended else ("trading halted" if halt else None))
        if entry:
            trigger = "brain session"
            positions = client.positions()
            equity = state["start_usd"] + (client.wallet()["equity"] - state["exchange_equity_at_start"])
        ctx = build_context(state, now, equity, rate, positions, markets, journal_path, open_orders(client))
        ctx["rules"] = brain_rules()
        save_json(d / "brain_input.json", ctx)
    else:
        entry, trigger = api_brain(client, brain, state, now, day, events, equity, rate, positions, markets,
                                   journal_path, ended, halt)
        if entry and entry.get("actions") is not None:
            positions = client.positions()
            equity = state["start_usd"] + (client.wallet()["equity"] - state["exchange_equity_at_start"])

    # ---- benchmarks, dashboard data, state ------------------------------------------------
    btc_raw = raw.get("BTCUSDT")
    btc_price = markets.get("BTCUSDT", {}).get("price")
    if not btc_price:
        try:
            btc_price = client.ticker("BTCUSDT")["last"]
        except Exception:
            btc_price = state.get("last_btc")
    if btc_raw:
        state["control"] = control.update(state.get("control"), btc_raw["h1"], state["start_usd"])
    if btc_price:
        state["last_btc"] = btc_price
    ctrl_usd = control.value(state.get("control"), btc_price) if btc_price else None
    hodl_usd = state["start_usd"] * btc_price / state["start_btc"] if btc_price else None

    row = [iso(now), round(equity * rate, 2),
           round(ctrl_usd * rate, 2) if ctrl_usd is not None else "",
           round(hodl_usd * rate, 2) if hodl_usd is not None else ""]
    eq_path = d / "equity.csv"
    if not light or not eq_path.exists():
        new_file = not eq_path.exists()
        with open(eq_path, "a", newline="") as f:
            w = csv.writer(f)
            if new_file:
                w.writerow(["time", "claude_pln", "control_pln", "hodl_pln"])
            w.writerow(row)

    cash_usd = client.s["cash"] if hasattr(client, "s") else None
    if cash_usd is not None:  # convert exchange cash into the bot's own equity frame
        cash_usd += state["start_usd"] - state["exchange_equity_at_start"]
    write_summary(d, state, now, equity, rate, positions, exch_equity, ctrl_usd, hodl_usd, journal_path, halt,
                  open_orders(client), cash_usd)
    if hasattr(client, "save"):
        client.save()
    save_json(state_path, state)
    if not light:
        log(f"equity {equity * rate:.2f} PLN | positions {len(positions)} | decision: {trigger or 'none'}")
    return entry


def open_orders(client):
    return client.open_orders() if hasattr(client, "open_orders") else []


def cancel_all_orders(client):
    for o in open_orders(client):
        client.cancel_orders(o["symbol"])


def brain_rules():
    return {
        "symbols": config.SYMBOLS, "default_risk": config.DEFAULT_RISK, "max_risk_per_trade": config.MAX_RISK_PER_TRADE,
        "max_leverage": config.MAX_LEVERAGE, "max_open_positions": config.MAX_OPEN_POSITIONS,
        "stop_distance": [config.MIN_STOP_DIST, config.MAX_STOP_DIST], "daily_loss_limit": config.DAILY_LOSS_LIMIT,
        "kill_drawdown": config.KILL_DRAWDOWN, "order_max_hours": config.ORDER_MAX_HOURS,
        "order_max_distance": config.ORDER_MAX_DIST, "decision_max_age_min": config.DECISION_MAX_AGE_MIN,
        "taker_fee": config.TAKER_FEE, "funding_per_8h": 0.0001,
    }


def take_session_decision(client, state, d, now, equity, rate, positions, markets, journal_path, blocked=None):
    """Execute docs/data/brain_decision.json once, if it is new and fresh. Returns the journal entry or None."""
    dec = load_json(d / "brain_decision.json", None)
    if not dec or not dec.get("id") or dec["id"] == state.get("last_decision_id"):
        return None
    state["last_decision_id"] = dec["id"]
    entry = {"time": iso(now), "trigger": "brain session", "decided_at": dec.get("decided_at"),
             "model": dec.get("model"), "equity_usd": round(equity, 2), "equity_pln": round(equity * rate, 2),
             "events": state.get("pending_events", []), "market_view": dec.get("market_view"),
             "watch_next": dec.get("watch_next"), "news": dec.get("news")}
    try:
        age = (now - parse_iso(dec["decided_at"])).total_seconds() / 60
    except (KeyError, ValueError):
        age = 1e9
    if blocked:
        entry["error"] = f"not executed: {blocked}"
    elif age > config.DECISION_MAX_AGE_MIN:
        entry["error"] = f"not executed: decision is {age:.0f} min old (limit {config.DECISION_MAX_AGE_MIN:.0f})"
    else:
        entry["actions"] = execute(client, dec.get("actions") or [], equity, positions, markets, now)
    state["pending_events"] = []
    state["calls"][now.strftime("%Y-%m-%d")] = state["calls"].get(now.strftime("%Y-%m-%d"), 0) + 1
    with open(journal_path, "a") as f:
        f.write(json.dumps(entry, default=str) + "\n")
    return entry


def api_brain(client, brain, state, now, day, events, equity, rate, positions, markets, journal_path, ended, halt):
    """Paid-API mode: the bot calls Claude itself, hourly or when something happens."""
    last = state.get("last_brain")
    mins = (now - parse_iso(last)).total_seconds() / 60 if last else 1e9
    trigger = None
    if mins >= config.BRAIN_EVERY_MIN - 3:
        trigger = "scheduled"
    elif any(abs(m.get("change_15m") or 0) >= config.EVENT_MOVE_PCT * 100 for m in markets.values()):
        trigger = "big move"
    elif any(e["type"] in ("position_closed", "order_filled") for e in events):
        trigger = "position change"
    calls_today = state["calls"].get(day, 0)
    if ended or halt or not markets or calls_today >= config.MAX_CALLS_PER_DAY:
        trigger = None
    state.setdefault("pending_events", []).extend(events)
    if not trigger:
        return None, None
    context = build_context(state, now, equity, rate, positions, markets, journal_path, open_orders(client))
    if brain is None:
        from .brain import ClaudeBrain
        brain = ClaudeBrain()
    state["calls"][day] = calls_today + 1
    state["last_brain"] = iso(now)
    entry = {"time": iso(now), "trigger": trigger, "equity_usd": round(equity, 2),
             "equity_pln": round(equity * rate, 2), "events": state["pending_events"]}
    try:
        decision = brain.decide(context)
    except Exception as e:
        entry["error"] = f"brain failed: {e}"
        print(f"::warning::Claude call failed: {e}", flush=True)
        decision = None
    if decision:
        entry.update({"model": decision.get("_model"), "usage": decision.get("_usage"),
                      "market_view": decision.get("market_view"), "watch_next": decision.get("watch_next")})
        entry["actions"] = execute(client, decision.get("actions") or [], equity, positions, markets, now)
    state["pending_events"] = []
    with open(journal_path, "a") as f:
        f.write(json.dumps(entry, default=str) + "\n")
    return entry, trigger


def build_context(state, now, equity, rate, positions, markets, journal_path, orders=()):
    start = state["start_usd"]
    used = sum(p["size"] * p["mark"] for p in positions)
    journal = []
    for j in read_journal(journal_path, 12):
        journal.append({"time": j.get("time"), "view": j.get("market_view"), "watch_next": j.get("watch_next"),
                        "actions": [{k: a.get(k) for k in ("type", "symbol", "side", "trigger", "stop", "reason",
                                                           "invalidation", "result", "detail") if a.get(k) is not None}
                                    for a in j.get("actions", [])]})
    closed = state["closed_trades"]
    wins = [t["pnl"] for t in closed if t["pnl"] > 0]
    losses = [t["pnl"] for t in closed if t["pnl"] <= 0]
    return {
        "time_utc": iso(now),
        "experiment_ends_utc": config.END_AT,
        "account": {
            "equity_usd": round(equity, 2), "equity_pln": round(equity * rate, 2),
            "start_pln": config.START_PLN, "return_pct": round((equity / start - 1) * 100, 2),
            "peak_equity_usd": round(state.get("peak_equity", start), 2),
            "today_start_equity_usd": round(state.get("day_start_equity", equity), 2),
            "position_size_vs_equity": round(used / equity, 2) if equity > 0 else None,
        },
        "positions": [{
            "symbol": p["symbol"], "side": p["side"], "size": p["size"], "entry": p["entry"], "mark": p["mark"],
            "pnl_usd": round(p["upnl"], 2), "pnl_pct_of_equity": round(p["upnl"] / equity * 100, 2) if equity else None,
            "stop": p["stop"], "take_profit": p["tp"], "why_opened": p.get("reason"),
            "opened_utc": iso(datetime.fromtimestamp(p["opened"] / 1000, timezone.utc)) if p["opened"] else None,
        } for p in positions],
        "resting_orders": [{k: o.get(k) for k in ("symbol", "side", "trigger", "direction", "stop", "tp", "qty")}
                           | {"expires_utc": iso(datetime.fromtimestamp(o["expires"] / 1000, timezone.utc))}
                           for o in orders],
        "events_since_last_decision": state.get("pending_events", []),
        "recent_closed_trades": [{"symbol": t["symbol"], "side": t["side"], "entry": t["entry"], "exit": t["exit"],
                                  "pnl_usd": round(t["pnl"], 2), "closed_by": t.get("why"), "why_opened": t.get("reason"),
                                  "opened_utc": iso(datetime.fromtimestamp(t["opened"] / 1000, timezone.utc)) if t.get("opened") else None,
                                  "closed_utc": iso(datetime.fromtimestamp(t["time"] / 1000, timezone.utc))}
                                 for t in closed[-15:]],
        "track_record": {"closed_trades": len(closed), "wins": len(wins), "losses": len(losses),
                         "avg_win_usd": round(sum(wins) / len(wins), 2) if wins else None,
                         "avg_loss_usd": round(sum(losses) / len(losses), 2) if losses else None,
                         "net_usd": round(sum(t["pnl"] for t in closed), 2)},
        "markets": markets,
        "your_journal": journal,
    }


def execute(client, actions, equity, positions, markets, now=None):
    """Run actions through the guard and send what passes.
    Order: closes, order cancels, stop moves, market entries, resting entry orders."""
    now = now or datetime.now(timezone.utc)
    order = {"close": 0, "cancel_order": 1, "move_stop": 2, "open": 3, "entry_order": 4}
    results = []
    by_sym = {p["symbol"]: p for p in positions}
    for a in sorted(actions, key=lambda x: order.get(x.get("type"), 9)):
        a = dict(a)
        sym, kind = a.get("symbol"), a.get("type")
        try:
            if sym not in config.SYMBOLS:
                a.update(result="rejected", detail=f"{sym} is not on the trading list")
            elif kind == "close":
                p = by_sym.get(sym)
                if not p:
                    a.update(result="rejected", detail="no open position")
                else:
                    client.close_position(p)
                    by_sym.pop(sym)
                    a.update(result="done", detail=f"closed {p['size']} at ~{markets.get(sym, {}).get('price')}")
            elif kind == "move_stop":
                if sym not in markets:
                    ok, why, o = False, "no fresh market data", None
                else:
                    ok, why, o = guard.check_move_stop(a, price=markets[sym]["price"], inst=client.instrument(sym),
                                                       position=by_sym.get(sym))
                if ok:
                    client.set_stops(sym, o["stop"], o["tp"])
                    a.update(result="done", detail=f"stop {o['stop']}" + (f", target {o['tp']}" if o["tp"] else ""))
                else:
                    a.update(result="rejected", detail=why)
            elif kind == "open":
                if sym not in markets:
                    a.update(result="rejected", detail="no fresh market data")
                else:
                    ok, why, o = guard.check_open(a, equity=equity, price=markets[sym]["price"],
                                                  inst=client.instrument(sym), positions=list(by_sym.values()))
                    if ok:
                        client.set_leverage(sym, config.MAX_LEVERAGE)
                        client.market_order(sym, o["side"], o["qty"], stop=o["stop"], tp=o["tp"],
                                            note=a.get("reason", ""))
                        by_sym[sym] = {"symbol": sym, "side": o["side"], "size": o["qty"],
                                       "mark": markets[sym]["price"], "stop": o["stop"]}
                        a.update(result="done", detail=(
                            f"{o['side']} {o['qty']} (~{o['notional']} USD, risk {o['risk_pct']:.1%}, "
                            f"stop {o['stop']}" + (f", target {o['tp']}" if o["tp"] else "") + f") {why}"))
                    else:
                        a.update(result="rejected", detail=why)
            elif kind == "cancel_order":
                n = client.cancel_orders(sym) if hasattr(client, "cancel_orders") else 0
                a.update(result="done" if n else "rejected", detail=f"cancelled {n} order(s)" if n else "no resting order")
            elif kind == "entry_order":
                trig = a.get("trigger")
                px = markets.get(sym, {}).get("price")
                if not hasattr(client, "place_order"):
                    a.update(result="rejected", detail="resting orders not supported here")
                elif not px or not trig or trig <= 0:
                    a.update(result="rejected", detail="needs a trigger price and fresh market data")
                elif abs(trig / px - 1) > config.ORDER_MAX_DIST:
                    a.update(result="rejected", detail=f"trigger more than {config.ORDER_MAX_DIST:.0%} from the price")
                else:
                    ok, why, o = guard.check_open(a, equity=equity, price=trig, inst=client.instrument(sym),
                                                  positions=list(by_sym.values()))
                    if ok:
                        hours = min(float(a.get("expires_hours") or 24), config.ORDER_MAX_HOURS)
                        exp = int(now.timestamp() * 1000 + hours * 3600_000)
                        placed = client.place_order(sym, o["side"], o["qty"], trig, o["stop"], o["tp"], exp,
                                                    a.get("reason", ""))
                        a.update(result="done", detail=(
                            f"{o['side']} {o['qty']} when price goes {placed['direction']} {trig} "
                            f"(risk {o['risk_pct']:.1%}, stop {o['stop']}" + (f", target {o['tp']}" if o["tp"] else "")
                            + f", expires in {hours:.0f}h) {why}"))
                    else:
                        a.update(result="rejected", detail=why)
            else:
                a.update(result="rejected", detail=f"unknown action {kind}")
        except ExchangeError as e:
            a.update(result="failed", detail=str(e))
        results.append(a)
    return results


def write_summary(d, state, now, equity, rate, positions, exch_equity, ctrl_usd, hodl_usd, journal_path, halt,
                  orders=(), cash_usd=None):
    vals = []
    try:
        with open(d / "equity.csv") as f:
            vals = [float(r["claude_pln"]) for r in csv.DictReader(f) if r["claude_pln"]]
    except FileNotFoundError:
        pass
    peak, mdd = 0, 0
    for v in vals:
        peak = max(peak, v)
        mdd = max(mdd, 1 - v / peak if peak else 0)
    closed = state["closed_trades"]
    wins = sum(1 for t in closed if t["pnl"] > 0)
    last = read_journal(journal_path, 1)
    c = state.get("control") or {}
    status = "ended" if state.get("ended") else ("halted" if halt == "kill" else ("paused" if halt == "daily" else "live"))
    summary = {
        "updated": iso(now), "status": status, "start": state["start"], "end_at": config.END_AT,
        "start_pln": config.START_PLN, "fx_usd_pln": rate,
        "equity_pln": round(equity * rate, 2), "return_pct": round((equity / state["start_usd"] - 1) * 100, 2),
        "max_drawdown_pct": round(mdd * 100, 2),
        "control_pln": round(ctrl_usd * rate, 2) if ctrl_usd is not None else None,
        "control_trades": c.get("trades", 0),
        "hodl_pln": round(hodl_usd * rate, 2) if hodl_usd is not None else None,
        "positions": [{**p, "upnl_pln": round(p["upnl"] * rate, 2)} for p in positions],
        "closed_trades": [{**t, "pnl_pln": round(t["pnl"] * rate, 2)} for t in closed[-50:]][::-1],
        "trade_count": len(closed), "win_rate_pct": round(wins / len(closed) * 100, 1) if closed else None,
        "brain_calls_today": state["calls"].get(now.strftime("%Y-%m-%d"), 0),
        "last_decision": last[0] if last else None,
        "brain_mode": config.BRAIN_MODE,
        "cash_usd": round(cash_usd, 6) if cash_usd is not None else None,
        "start_usd": state["start_usd"], "start_btc": state["start_btc"],
        "control_live": ({"equity": c.get("equity"), "pos": c.get("pos")} if c else None),
        "pairs": PAIRS,
        "orders": [{k: o.get(k) for k in ("symbol", "side", "trigger", "direction", "stop", "tp", "qty", "expires", "note")}
                   for o in orders],
        "balance_warning": False,
    }
    save_json(d / "summary.json", summary)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        print(f"::error::{e.__class__.__name__}: {e}", flush=True)  # shows on the run's summary page
        sys.exit(1)
