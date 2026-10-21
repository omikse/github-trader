"""One run of the bot. GitHub Actions calls this every 15 minutes.

Each run: read the account -> enforce halts -> (when due) ask Claude -> pass every action through
the risk guard -> send orders -> update the control bot -> write the journal and dashboard data.
Stops and take-profits live on the exchange, so they fire 24/7 between runs.
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
from .bybit import Bybit, BybitError
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
        except BybitError as e:
            events.append({"type": "close_failed", "symbol": p["symbol"], "error": str(e)})


def main(client=None, brain=None, now=None, fx=None):
    now = now or datetime.now(timezone.utc)
    now_ms = int(now.timestamp() * 1000)
    day = now.strftime("%Y-%m-%d")
    d = Path(config.DATA_DIR)
    d.mkdir(parents=True, exist_ok=True)
    state_path, journal_path = d / "state.json", d / "decisions.jsonl"
    state = load_json(state_path, {})

    if client is None:
        key, secret = os.getenv("BYBIT_API_KEY"), os.getenv("BYBIT_API_SECRET")
        if not key or not secret:
            log("BYBIT_API_KEY / BYBIT_API_SECRET are not set yet. Add them as repository secrets. Not starting.")
            return None
        client = Bybit(key, secret, config.BYBIT_BASE)
    rate = fx or usd_pln(state)

    # ---- account ---------------------------------------------------------------
    wallet = client.wallet()
    exch_equity = wallet["equity"]
    if "start" not in state:
        if exch_equity > config.START_PLN / rate * 3 and os.getenv("ALLOW_BIG_BALANCE") != "1":
            log(f"Demo balance is {exch_equity:.0f} USD. Run the 'Setup demo account' workflow first "
                "so the account matches 1,000 PLN. Not starting yet.")
            return None
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

    # ---- halts and the end of the experiment --------------------------------------
    ended = now >= parse_iso(config.END_AT)
    halt = None
    if ended:
        if not state.get("ended"):
            close_all(client, positions, "experiment ended", events)
            state["ended"] = iso(now)
    else:
        halt = guard.check_halts(state, equity, day)
        if halt and positions:
            close_all(client, positions, "kill switch: drawdown limit" if halt == "kill" else "daily loss limit", events)
            events.append({"type": "halt", "kind": halt})

    if events:
        positions = client.positions()

    # ---- market data ------------------------------------------------------------
    markets, raw = {}, {}
    for sym in config.SYMBOLS:
        try:
            markets[sym], raw[sym] = snapshot(client, sym)
        except Exception as e:  # one bad symbol must not stop the run
            log(f"snapshot failed for {sym}: {e}")

    # ---- decide whether to wake the brain ---------------------------------------------
    last = state.get("last_brain")
    mins = (now - parse_iso(last)).total_seconds() / 60 if last else 1e9
    trigger = None
    if mins >= config.BRAIN_EVERY_MIN - 3:
        trigger = "scheduled"
    elif any(abs(m.get("change_15m") or 0) >= config.EVENT_MOVE_PCT * 100 for m in markets.values()):
        trigger = "big move"
    elif any(e["type"] == "position_closed" for e in events):
        trigger = "position closed"
    calls_today = state["calls"].get(day, 0)
    if ended or halt or not markets or calls_today >= config.MAX_CALLS_PER_DAY:
        trigger = None

    entry = None
    if trigger:
        state.setdefault("pending_events", []).extend(events)
        context = build_context(state, now, equity, rate, positions, markets, journal_path)
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
            decision = None
        if decision:
            entry.update({"model": decision.get("_model"), "usage": decision.get("_usage"),
                          "market_view": decision.get("market_view"), "watch_next": decision.get("watch_next")})
            entry["actions"] = execute(client, decision.get("actions") or [], equity, positions, markets)
            positions = client.positions()
            equity = state["start_usd"] + (client.wallet()["equity"] - state["exchange_equity_at_start"])
        state["pending_events"] = []
        with open(journal_path, "a") as f:
            f.write(json.dumps(entry, default=str) + "\n")
    elif events:
        state.setdefault("pending_events", []).extend(events)

    # ---- benchmarks, dashboard data, state ------------------------------------------------
    btc_raw = raw.get("BTCUSDT")
    btc_price = markets.get("BTCUSDT", {}).get("price") or state.get("last_btc")
    if btc_raw:
        state["control"] = control.update(state.get("control"), btc_raw["h1"], state["start_usd"])
        state["last_btc"] = btc_price
    ctrl_usd = control.value(state.get("control"), btc_price) if btc_price else None
    hodl_usd = state["start_usd"] * btc_price / state["start_btc"] if btc_price else None

    row = [iso(now), round(equity * rate, 2),
           round(ctrl_usd * rate, 2) if ctrl_usd is not None else "",
           round(hodl_usd * rate, 2) if hodl_usd is not None else ""]
    eq_path = d / "equity.csv"
    new_file = not eq_path.exists()
    with open(eq_path, "a", newline="") as f:
        w = csv.writer(f)
        if new_file:
            w.writerow(["time", "claude_pln", "control_pln", "hodl_pln"])
        w.writerow(row)

    write_summary(d, state, now, equity, rate, positions, exch_equity, ctrl_usd, hodl_usd, journal_path, halt)
    save_json(state_path, state)
    log(f"equity {equity * rate:.2f} PLN | positions {len(positions)} | brain: {trigger or 'not called'}")
    return entry


def build_context(state, now, equity, rate, positions, markets, journal_path):
    start = state["start_usd"]
    used = sum(p["size"] * p["mark"] for p in positions)
    journal = []
    for j in read_journal(journal_path, 10):
        journal.append({"time": j.get("time"), "view": j.get("market_view"),
                        "actions": [{k: a.get(k) for k in ("type", "symbol", "side", "stop", "reason", "result", "detail")}
                                    for a in j.get("actions", [])]})
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
            "stop": p["stop"], "take_profit": p["tp"],
            "opened_utc": iso(datetime.fromtimestamp(p["opened"] / 1000, timezone.utc)) if p["opened"] else None,
        } for p in positions],
        "events_since_last_decision": state.get("pending_events", []),
        "recent_closed_trades": [{k: t[k] for k in ("symbol", "side", "entry", "exit", "pnl")}
                                 for t in state["closed_trades"][-10:]],
        "markets": markets,
        "your_journal": journal,
    }


def execute(client, actions, equity, positions, markets):
    """Run actions through the guard and send what passes. Closes first, then stop moves, then opens."""
    order = {"close": 0, "move_stop": 1, "open": 2}
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
                        client.market_order(sym, o["side"], o["qty"], stop=o["stop"], tp=o["tp"])
                        by_sym[sym] = {"symbol": sym, "side": o["side"], "size": o["qty"],
                                       "mark": markets[sym]["price"], "stop": o["stop"]}
                        a.update(result="done", detail=(
                            f"{o['side']} {o['qty']} (~{o['notional']} USD, risk {o['risk_pct']:.1%}, "
                            f"stop {o['stop']}" + (f", target {o['tp']}" if o["tp"] else "") + f") {why}"))
                    else:
                        a.update(result="rejected", detail=why)
            else:
                a.update(result="rejected", detail=f"unknown action {kind}")
        except BybitError as e:
            a.update(result="failed", detail=str(e))
        results.append(a)
    return results


def write_summary(d, state, now, equity, rate, positions, exch_equity, ctrl_usd, hodl_usd, journal_path, halt):
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
        "balance_warning": exch_equity > state["start_usd"] * 3,
    }
    save_json(d / "summary.json", summary)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        sys.exit(1)
