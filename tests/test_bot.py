"""Offline tests: a fake Kraken feed drives the real paper exchange and the real bot code end to end."""
import json
import math
import os
import sys
import tempfile
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
os.environ["DATA_DIR"] = tempfile.mkdtemp()

from bot import config, guard, run  # noqa: E402
from bot.paper import MINUTE, PaperExchange  # noqa: E402

run.pred.Polymarket = lambda: FakePM([])  # tests never touch the real Polymarket

INST = {"qty_step": 0.00001, "min_qty": 0.0, "min_notional": 5, "tick": 0.1}
BASE = {"BTCUSDT": 85000.0, "ETHUSDT": 3000.0, "SOLUSDT": 108.0, "XRPUSDT": 2.4, "DOGEUSDT": 0.2,
        "ADAUSDT": 0.6, "AVAXUSDT": 20.0, "LINKUSDT": 15.0, "SUIUSDT": 3.0, "PEPEUSDT": 0.00001, "WIFUSDT": 0.8,
        "BONKUSDT": 0.00002, "LTCUSDT": 90.0, "DOTUSDT": 4.0, "NEARUSDT": 2.5, "PAXGUSDT": 4000.0, "EURUSDT": 1.16}
T0 = datetime(2026, 10, 22, 8, 0, tzinfo=timezone.utc)
T0_MS = int(T0.timestamp() * 1000)


class FakeKraken:
    """Price = smooth wave, plus an optional crash window. `now_ms` is set by the test."""

    def __init__(self, crash=None):
        self.now_ms = T0_MS
        self.crash = crash or {}  # symbol -> (start_ms, end_ms, depth)

    def p(self, sym, t):
        x = (t - T0_MS) / 3_600_000
        px = BASE[sym] * (1 + 0.03 * math.sin(x / 2) + 0.004 * x)
        if sym in self.crash:
            a, b, depth = self.crash[sym]
            if a <= t:
                px *= 1 - depth * min(1, (t - a) / max(1, b - a))
        return px

    def ohlc(self, sym, minutes, since_s=None):
        dur = minutes * MINUTE
        last_open = self.now_ms // dur * dur
        first = last_open - 719 * dur
        if since_s:
            first = max(first, int(since_s * 1000) // dur * dur)
        out = []
        for t in range(first, last_open + dur, dur):
            end = min(t + dur, self.now_ms)
            pts = [self.p(sym, t + k * (end - t) / 6) for k in range(7)]
            out.append({"t": t, "o": pts[0], "h": max(pts), "l": min(pts), "c": pts[-1], "v": 1.0})
        return out

    def ticker(self, sym):
        last = self.p(sym, self.now_ms)
        return {"last": last, "bid": last * 0.9999, "ask": last * 1.0001}

    def funding_rates(self):
        return {s: 2e-5 for s in BASE}   # 0.002% per hour = 17.5% a year, longs pay shorts

    def cash_rate(self):
        return 0.04


def gamma(mid, q, yes_bid, yes_ask, days, closed=False, final=None, liquidity=50_000):
    """A raw Gamma API market, as the probe saw them."""
    end = datetime.fromtimestamp((T0_MS + days * 86_400_000) / 1000, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    prices = [final, 1 - final] if final is not None else [(yes_bid + yes_ask) / 2, 1 - (yes_bid + yes_ask) / 2]
    return {"id": mid, "question": q, "slug": f"slug-{mid}", "endDate": end, "outcomes": '["Yes", "No"]',
            "outcomePrices": json.dumps([str(x) for x in prices]), "bestBid": yes_bid, "bestAsk": yes_ask,
            "closed": closed, "active": not closed, "acceptingOrders": not closed, "liquidityNum": liquidity,
            "volume24hr": 100_000, "orderMinSize": 5, "feesEnabled": False, "takerBaseFee": 0,
            "umaResolutionStatus": "resolved" if closed else None}


class FakePM:
    def __init__(self, raw):
        self.raw = {m["id"]: m for m in raw}

    def set(self, m):
        self.raw[m["id"]] = m

    def top(self):
        from bot.predictions import normalize
        return [x for x in (normalize(m) for m in self.raw.values() if not m["closed"]) if x]

    def get(self, key):
        from bot.predictions import normalize
        m = self.raw.get(str(key)) or next((m for m in self.raw.values() if m["slug"] == key), None)
        return normalize(m) if m else None


class FakeBrain:
    def __init__(self, plans):
        self.plans, self.contexts = plans, []

    def decide(self, ctx):
        self.contexts.append(ctx)
        plan = self.plans.pop(0) if self.plans else None
        if callable(plan):
            plan = plan(ctx)
        return plan or {"market_view": "nothing", "actions": [], "watch_next": "-"}


def fresh_dir():
    config.DATA_DIR = tempfile.mkdtemp()
    return config.DATA_DIR


def run_series(market, brain, n, step_min=15, mode="api"):
    config.BRAIN_MODE = mode
    for i in range(n):
        now = T0 + timedelta(minutes=step_min * i)
        market.now_ms = int(now.timestamp() * 1000)
        run.main(brain=brain, now=now, fx=3.88, market=market)


def journal(d):
    return [json.loads(x) for x in open(os.path.join(d, "decisions.jsonl"))]


def test_guard_sizes_from_risk_and_rejects_bad_orders():
    ok, why, o = guard.check_open({"symbol": "BTCUSDT", "side": "long", "stop": 83300, "risk_pct": 0.03},
                                  equity=258, price=85000, inst=INST, positions=[])
    assert ok, why
    loss = o["qty"] * (85000 - 83300 + 85000 * config.TAKER_FEE * 2)
    assert 258 * 0.02 < loss <= 258 * 0.03 + 1e-6
    bad = [{"symbol": "BTCUSDT", "side": "long", "stop": 86000},   # wrong side
           {"symbol": "BTCUSDT", "side": "long"},                  # no stop
           {"symbol": "BTCUSDT", "side": "short", "stop": 85100}]  # too tight
    for b in bad:
        assert guard.check_open(b, equity=258, price=85000, inst=INST, positions=[])[0] is False
    ok, _, o = guard.check_open({"symbol": "BTCUSDT", "side": "long", "stop": 80000, "risk_pct": 0.5},
                                equity=258, price=85000, inst=INST, positions=[])
    assert ok and o["risk_pct"] <= config.MAX_RISK_PER_TRADE + 1e-9
    ok, why, o = guard.check_open({"symbol": "BTCUSDT", "side": "long", "stop": 84740, "risk_pct": 0.08},
                                  equity=258, price=85000, inst=INST, positions=[])
    assert ok and o["notional"] <= 258 * config.MAX_LEVERAGE + 1 and "cut" in why


def test_stops_only_tighten_and_halts():
    pos = {"symbol": "BTCUSDT", "side": "long", "stop": 83000}
    assert guard.check_move_stop({"stop": 82000}, price=85000, inst=INST, position=pos)[0] is False
    assert guard.check_move_stop({"stop": 84000}, price=85000, inst=INST, position=pos)[0] is True
    st = {}
    assert guard.check_halts(st, 100, "d1") is None
    assert guard.check_halts(st, 79, "d1") == "daily"
    assert guard.check_halts(st, 90, "d2") is None
    assert guard.check_halts(st, 49, "d2") == "kill"
    assert guard.check_halts(st, 200, "d3") == "kill"


def test_stop_fires_between_runs_on_minute_candles():
    """BTC crashes 6% between two runs; the stop 2% below entry must fire at ~the stop, not at the next run's price."""
    d = fresh_dir()
    crash_start = T0_MS + 20 * MINUTE
    m = FakeKraken(crash={"BTCUSDT": (crash_start, crash_start + 5 * MINUTE, 0.06)})
    entry_px = m.p("BTCUSDT", T0_MS)
    stop = round(entry_px * 0.98, 1)
    brain = FakeBrain([{"market_view": "long", "watch_next": "-", "actions": [
        {"type": "open", "symbol": "BTCUSDT", "side": "long", "stop": stop, "risk_pct": 0.03, "reason": "test"}]}])
    run_series(m, brain, 3)  # runs at 0, 15, 30 min; the crash happens at 20-25 min
    ex = json.load(open(os.path.join(d, "exchange.json")))
    assert not ex["positions"], "stop should have closed the position"
    c = ex["closed"][0]
    assert c["why"] == "stop" and abs(c["exit"] / stop - 1) < 0.001, c
    # the loss is about the planned 3% of equity, not the 6% crash
    start_usd = 1000 / 3.88
    assert -start_usd * 0.04 < c["pnl"] < -start_usd * 0.02, c["pnl"]
    j = journal(d)
    assert j[-1]["trigger"] == "position change" and j[-1]["events"][0]["why"] == "stop"


def test_liquidation_and_funding():
    d = fresh_dir()
    m = FakeKraken(crash={"ETHUSDT": (T0_MS + 10 * MINUTE, T0_MS + 12 * MINUTE, 0.30)})
    m.now_ms = T0_MS
    ex = PaperExchange(os.path.join(d, "x.json"), market=m, start_usd=100, now_ms=T0_MS)
    ex.market_order("ETHUSDT", "long", 1000 / m.p("ETHUSDT", T0_MS))  # 10x, no stop: only possible outside the guard
    m.now_ms = ex.now_ms = T0_MS + 30 * MINUTE
    ex.advance()
    assert not ex.s["positions"] and ex.s["closed"][0]["why"] == "liquidation"
    assert ex.s["cash"] >= 0
    # funding: a long held across the 16:00 UTC boundary pays 0.01% of its size
    ex2 = PaperExchange(os.path.join(d, "y.json"), market=FakeKraken(), start_usd=100, now_ms=T0_MS)
    ex2.market.now_ms = T0_MS
    ex2.market_order("SOLUSDT", "long", 1.0)
    cash0 = ex2.s["cash"]
    ex2.market.now_ms = ex2.now_ms = T0_MS + 9 * 3600_000  # 08:00 -> 17:00 crosses 16:00
    ex2.advance()
    paid = cash0 - ex2.s["cash"]
    assert 0 < paid < 0.02, paid


def test_full_session():
    d = fresh_dir()
    m = FakeKraken()
    brain = FakeBrain([
        lambda ctx: {"market_view": "BTC up", "watch_next": "x", "actions": [
            {"type": "open", "symbol": "BTCUSDT", "side": "long", "stop": ctx["markets"]["BTCUSDT"]["price"] * 0.97,
             "take_profit": ctx["markets"]["BTCUSDT"]["price"] * 1.2, "risk_pct": 0.04, "reason": "trend"},
            {"type": "open", "symbol": "PEPEUSDT", "side": "long", "stop": 1, "reason": "not on list"},
            {"type": "open", "symbol": "ETHUSDT", "side": "short", "reason": "no stop"}]},
        lambda ctx: {"market_view": "trail", "watch_next": "x", "actions": [
            {"type": "move_stop", "symbol": "BTCUSDT", "stop": ctx["markets"]["BTCUSDT"]["price"] * 0.99, "reason": "trail"}]},
        {"market_view": "take it", "watch_next": "x", "actions": [{"type": "close", "symbol": "BTCUSDT", "reason": "done"}]},
    ])
    run_series(m, brain, 13)
    j = journal(d)
    acts = {a["symbol"]: a for a in j[0]["actions"]}
    assert acts["BTCUSDT"]["result"] == "done", acts["BTCUSDT"]
    assert acts["PEPEUSDT"]["result"] == "rejected" and acts["ETHUSDT"]["result"] == "rejected"
    assert j[1]["actions"][0]["result"] == "done", j[1]["actions"]
    assert j[2]["actions"][0]["result"] == "done"
    assert brain.contexts[1]["your_journal"] and len(brain.contexts[0]["markets"]) == len(config.SYMBOLS)
    s = json.load(open(os.path.join(d, "summary.json")))
    assert s["trade_count"] == 1 and s["control_pln"] and s["hodl_pln"] and s["status"] == "live"
    print("summary:", {k: s[k] for k in ("equity_pln", "return_pct", "control_pln", "hodl_pln", "trade_count")})
    print("trade:", s["closed_trades"][0])


def write_decision(d, dec_id, when, actions, view="test"):
    with open(os.path.join(d, "brain_decision.json"), "w") as f:
        json.dump({"id": dec_id, "decided_at": when.strftime("%Y-%m-%dT%H:%M:%SZ"), "model": "test",
                   "market_view": view, "watch_next": "-", "actions": actions}, f)


def test_session_brain_and_resting_orders():
    """Session mode: decisions come from brain_decision.json; a breakout order fills on the minute it is crossed."""
    d = fresh_dir()
    config.BRAIN_MODE = "session"
    m = FakeKraken()
    m.now_ms = T0_MS
    run.main(now=T0, fx=3.88, market=m)  # first run: writes brain_input.json, no decision yet
    inp = json.load(open(os.path.join(d, "brain_input.json")))
    assert inp["markets"]["ETHUSDT"]["price"] and inp["rules"]["max_leverage"] == config.MAX_LEVERAGE
    t1 = T0 + timedelta(minutes=15)
    t1_ms = int(t1.timestamp() * 1000)
    eth, btc = m.p("ETHUSDT", t1_ms), m.p("BTCUSDT", t1_ms)
    trig = round(eth * 1.004, 2)  # the wave pushes ETH through this within the next hour
    write_decision(d, "dec-1", t1, [
        {"type": "open", "symbol": "BTCUSDT", "side": "short", "stop": btc * 1.03, "reason": "fade"},
        {"type": "entry_order", "symbol": "ETHUSDT", "side": "long", "trigger": trig, "stop": trig * 0.97,
         "take_profit": trig * 1.1, "expires_hours": 12, "reason": "breakout"},
        {"type": "entry_order", "symbol": "SOLUSDT", "side": "long", "trigger": 999, "stop": 900, "reason": "too far"}])
    m.now_ms = int(t1.timestamp() * 1000)
    run.main(now=t1, fx=3.88, market=m)
    j = journal(d)
    res = {a["symbol"]: a["result"] for a in j[-1]["actions"]}
    assert res == {"BTCUSDT": "done", "ETHUSDT": "done", "SOLUSDT": "rejected"}, j[-1]["actions"]
    ex = json.load(open(os.path.join(d, "exchange.json")))
    assert ex["orders"][0]["direction"] == "above"
    # later runs: the same decision is never executed twice, and the ETH order fills on its minute
    for k in range(2, 8):
        t = T0 + timedelta(minutes=15 * k)
        m.now_ms = int(t.timestamp() * 1000)
        run.main(now=t, fx=3.88, market=m)
    assert len(journal(d)) == 1
    ex = json.load(open(os.path.join(d, "exchange.json")))
    assert "ETHUSDT" in ex["positions"] and not ex["orders"], ex["orders"]
    fill = ex["positions"]["ETHUSDT"]["entry"]
    assert abs(fill / trig - 1) < 0.002, (fill, trig)
    st = json.load(open(os.path.join(d, "state.json")))
    assert any(e["type"] == "order_filled" for e in st["pending_events"])
    inp = json.load(open(os.path.join(d, "brain_input.json")))
    assert any(e["type"] == "order_filled" for e in inp["events_since_last_decision"])
    assert inp["markets"]["BTCUSDT"]["d1"]["ema20"] and len(inp["markets"]["BTCUSDT"]["last_30_daily_closes"]) == 30
    eth = next(p for p in inp["positions"] if p["symbol"] == "ETHUSDT")
    assert eth["why_opened"] == "breakout"                       # the reason travels with the position

    # a stale decision is journaled but not executed
    t9 = T0 + timedelta(minutes=135)
    write_decision(d, "dec-2", t9 - timedelta(minutes=90), [{"type": "close", "symbol": "ETHUSDT", "reason": "x"}])
    m.now_ms = int(t9.timestamp() * 1000)
    run.main(now=t9, fx=3.88, market=m)
    last = journal(d)[-1]
    assert "not executed" in last["error"] and "ETHUSDT" in json.load(open(os.path.join(d, "exchange.json")))["positions"]
    s = json.load(open(os.path.join(d, "summary.json")))
    assert s["brain_mode"] == "session" and any(p["symbol"] == "ETHUSDT" for p in s["positions"])
    assert s["closed_trades"][0]["why"] == "stop"  # the BTC short was stopped out by the rally
    inp = json.load(open(os.path.join(d, "brain_input.json")))
    closed = inp["recent_closed_trades"][0]
    assert closed["why_opened"] == "fade" and closed["closed_by"] == "stop" and inp["track_record"]["losses"] == 1
    print("session mode ok; ETH filled at", round(fill, 2), "trigger", trig)


def test_minute_ticks():
    """Light 1-minute ticks keep the account and summary current; history rows only on full runs."""
    d = fresh_dir()
    config.BRAIN_MODE = "session"
    m = FakeKraken()
    m.now_ms = T0_MS
    run.main(now=T0, fx=3.88, market=m)
    t1 = T0 + timedelta(minutes=1)
    p = m.p("SOLUSDT", int(t1.timestamp() * 1000))
    write_decision(d, "d1", t1, [{"type": "open", "symbol": "SOLUSDT", "side": "long", "stop": p * 0.95, "reason": "x"}])
    values = []
    for k in range(1, 12):
        t = T0 + timedelta(minutes=k)
        m.now_ms = int(t.timestamp() * 1000)
        run.main(now=t, fx=3.88, market=m, light=True)  # the new decision forces one full run by itself
        s = json.load(open(os.path.join(d, "summary.json")))
        values.append(s["equity_pln"])
        assert s["updated"] == t.strftime("%Y-%m-%dT%H:%M:%SZ")
    assert len(set(values)) > 5, values          # equity moves every minute with the open position
    rows = open(os.path.join(d, "equity.csv")).read().strip().splitlines()
    assert len(rows) == 3, rows                  # header + first run + the forced full run
    s = json.load(open(os.path.join(d, "summary.json")))
    assert s["cash_usd"] is not None and s["pairs"]["BTCUSDT"] == "XBTUSD" and s["positions"][0]["symbol"] == "SOLUSDT"
    # live recomputation in the browser: cash + open P/L must equal the reported equity
    live = s["cash_usd"] + sum(p["upnl"] for p in s["positions"])
    assert abs(live * s["fx_usd_pln"] - s["equity_pln"]) < 0.5, (live * s["fx_usd_pln"], s["equity_pln"])


def test_carry_funding_and_interest():
    """Real hourly funding: a perp long pays it, a carry trade earns it; idle cash earns interest."""
    d = fresh_dir()
    m = FakeKraken()
    ex = PaperExchange(os.path.join(d, "x.json"), market=m, start_usd=1000, now_ms=T0_MS)
    ex.set_market_rates(m.funding_rates(), 0.04)
    m.now_ms = T0_MS
    ex.market_order("SOLUSDT", "long", 1000 / m.p("SOLUSDT", T0_MS))    # 1,000 USD long, 1x
    ex.carry_open("BTCUSDT", 500)                                        # 500 USD carry
    assert abs(ex.s["income"]["carry"] + 500 * 0.003) < 1e-9             # opening cost charged
    m.now_ms = ex.now_ms = T0_MS + 10 * 3_600_000                        # 10 hourly fundings
    ex.advance()
    assert abs(ex.s["income"]["funding"] - (-1000 * 2e-5 * 10)) < 0.02   # long paid ~0.2 USD
    assert abs(ex.s["carry"]["BTCUSDT"]["earned"] - 500 * 2e-5 * 10) < 1e-9
    idle = 1000 - 1000 * config.TAKER_FEE - 1.5 - 1000 / config.MAX_LEVERAGE - 500
    assert abs(ex.s["income"]["interest"] - idle * 0.04 * 10 / 8760) < 0.002
    rec = ex.carry_close("BTCUSDT")
    assert abs(rec["pnl"] - (0.1 - 3.0)) < 1e-6                          # 10 h of funding does not pay 0.6% fees
    print("carry 10h net", rec["pnl"], "interest", round(ex.s["income"]["interest"], 4))


def test_prediction_lifecycle():
    d = fresh_dir()
    pm = FakePM([gamma("1", "Will X happen?", 0.40, 0.42, 5), gamma("2", "Will Y happen?", 0.70, 0.72, 5)])
    ex = PaperExchange(os.path.join(d, "x.json"), market=FakeKraken(), start_usd=200, now_ms=T0_MS)
    m1, m2 = pm.get("1"), pm.get("2")
    r = ex.predict_buy(m1, "Yes", 10)
    assert abs(r["price"] - 0.42) < 1e-9 and abs(ex.s["cash"] - 190) < 1e-9
    assert abs(ex.predictions_value() - 10 / 0.42 * 0.40) < 1e-9            # valued at the bid
    ex.predict_buy(m2, "No", 10)                                            # No costs 1 - yes_bid = 0.30
    assert abs(ex.s["predictions"]["2"]["entry"] - 0.30) < 1e-9
    pm.set(gamma("1", "Will X happen?", 0, 0, 5, closed=True, final=1.0))  # X happened
    pm.set(gamma("2", "Will Y happen?", 0, 0, 5, closed=True, final=1.0))  # Y happened, our No loses
    settled = ex.update_predictions({"1": pm.get("1"), "2": pm.get("2")})
    res = {x["market"]: x for x in settled}
    assert abs(res["1"]["pnl"] - (10 / 0.42 - 10)) < 1e-3 and res["1"]["why"] == "resolved win"
    assert abs(res["2"]["pnl"] + 10) < 1e-3 and res["2"]["why"] == "resolved loss"
    assert not ex.s["predictions"] and abs(ex.s["cash"] - (180 + 10 / 0.42)) < 1e-6
    # guard
    big = guard.check_predict({"outcome": "yes", "stake_pct": 0.5}, equity=200, market=pm.get("1"), open_cost=0,
                              free_cash=200)
    assert big[0] is False  # market is closed now
    pm.set(gamma("3", "Z?", 0.5, 0.52, 3))
    ok, why, o = guard.check_predict({"outcome": "No", "stake_pct": 0.5}, equity=200, market=pm.get("3"), open_cost=0,
                                     free_cash=200)
    assert ok and abs(o["stake"] - 200 * config.PRED_MAX_STAKE) < 1e-9     # capped at 8%
    ok, why, o = guard.check_predict({"outcome": "No", "stake_pct": 0.08}, equity=200, market=pm.get("3"), open_cost=75,
                                     free_cash=200)
    assert ok and abs(o["stake"] - 5) < 1e-9 and "total cap" in why       # 40% total cap leaves 5 USD
    thin = FakePM([gamma("4", "thin?", 0.5, 0.52, 3, liquidity=500)]).get("4")
    assert guard.check_predict({"outcome": "Yes"}, equity=200, market=thin, open_cost=0, free_cash=200)[0] is False


def test_session_uses_everything():
    """One account: a perp, a prediction and a carry trade from one decision; a resolution pays out; the
    dashboard's live formula (cash + perp P/L + other_value) matches the reported equity."""
    d = fresh_dir()
    config.BRAIN_MODE = "session"
    m = FakeKraken()
    pm = FakePM([gamma("77", "Will the Fed hold rates?", 0.80, 0.82, 2), gamma("88", "Long shot?", 0.05, 0.06, 40)])
    m.now_ms = T0_MS
    run.main(now=T0, fx=3.88, market=m, pm=pm)
    inp = json.load(open(os.path.join(d, "brain_input.json")))
    qs = [x["market"] for x in inp["prediction_markets"]]
    assert qs == ["77"], qs                                      # 88 ends after the experiment window
    assert inp["markets"]["BTCUSDT"]["funding_apr_pct"] == 17.5 and inp["cash"]["interest_rate_pct"] == 4.0
    t1 = T0 + timedelta(minutes=5)
    btc = m.p("BTCUSDT", int(t1.timestamp() * 1000))
    write_decision(d, "x1", t1, [
        {"type": "predict", "market": "77", "outcome": "Yes", "stake_pct": 0.05, "reason": "Fed guidance"},
        {"type": "predict", "market": "slug-88", "outcome": "No", "stake_pct": 0.05, "reason": "by slug"},
        {"type": "carry_open", "symbol": "ETHUSDT", "size_pct": 0.3, "reason": "funding 17%/yr"},
        {"type": "carry_open", "symbol": "PEPEUSDT", "size_pct": 0.5, "reason": "too big"},
        {"type": "open", "symbol": "BTCUSDT", "side": "long", "stop": btc * 0.97, "reason": "trend"}])
    m.now_ms = int(t1.timestamp() * 1000)
    run.main(now=t1, fx=3.88, market=m, pm=pm)
    acts = journal(d)[-1]["actions"]
    res = [(x["type"], x.get("symbol") or x.get("market"), x["result"]) for x in acts]
    assert ("predict", "77", "done") in res and ("predict", "88", "done") in res, res
    assert ("carry_open", "ETHUSDT", "done") in res and ("open", "BTCUSDT", "done") in res, res
    pepe = next(x for x in acts if x.get("symbol") == "PEPEUSDT")
    assert pepe["result"] == "done" and "cut" in pepe["detail"], pepe     # cut to the 60% total cap
    for k in range(2, 14):                                                   # an hour of minute ticks
        t = T0 + timedelta(minutes=5 * k)
        m.now_ms = int(t.timestamp() * 1000)
        run.main(now=t, fx=3.88, market=m, pm=pm, light=(k % 3 != 0))
    pm.set(gamma("77", "Will the Fed hold rates?", 0, 0, 2, closed=True, final=1.0))
    t = T0 + timedelta(minutes=75)
    m.now_ms = int(t.timestamp() * 1000)
    run.main(now=t, fx=3.88, market=m, pm=pm)
    st = json.load(open(os.path.join(d, "state.json")))
    assert any(e["type"] == "prediction_settled" and e["why"] == "resolved win" for e in st["pending_events"])
    s = json.load(open(os.path.join(d, "summary.json")))
    assert s["pred_closed"][0]["market"] == "77" and s["pred_closed"][0]["pnl"] > 0
    assert len(s["carry"]) == 2 and s["income_pln"]["carry"] < 0          # 1 h of funding < opening costs, honestly
    assert json.load(open(os.path.join(d, "exchange.json")))["income"]["interest"] > 0   # tiny over 70 minutes
    live = s["cash_usd"] + sum(p["upnl"] for p in s["positions"]) + s["other_value_usd"]
    assert abs(live * s["fx_usd_pln"] - s["equity_pln"]) < 0.5, (live * s["fx_usd_pln"], s["equity_pln"])
    inp = json.load(open(os.path.join(d, "brain_input.json")))
    assert inp["predictions"][0]["market"] == "88" and inp["side_track_record"]["predictions"]["wins"] == 1
    print("everything:", {k: s[k] for k in ("equity_pln", "income_pln")}, "pred pnl", s["pred_closed"][0]["pnl_pln"])


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("PASS", name)
