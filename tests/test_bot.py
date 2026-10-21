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

INST = {"qty_step": 0.00001, "min_qty": 0.0, "min_notional": 5, "tick": 0.1}
BASE = {"BTCUSDT": 85000.0, "ETHUSDT": 3000.0, "SOLUSDT": 108.0, "XRPUSDT": 2.4, "DOGEUSDT": 0.2}
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


def run_series(market, brain, n, step_min=15):
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
    ok, why, o = guard.check_open({"symbol": "BTCUSDT", "side": "long", "stop": 84700, "risk_pct": 0.05},
                                  equity=258, price=85000, inst=INST, positions=[])
    assert ok and o["notional"] <= 258 * config.MAX_LEVERAGE + 1 and "cut" in why


def test_stops_only_tighten_and_halts():
    pos = {"symbol": "BTCUSDT", "side": "long", "stop": 83000}
    assert guard.check_move_stop({"stop": 82000}, price=85000, inst=INST, position=pos)[0] is False
    assert guard.check_move_stop({"stop": 84000}, price=85000, inst=INST, position=pos)[0] is True
    st = {}
    assert guard.check_halts(st, 100, "d1") is None
    assert guard.check_halts(st, 84, "d1") == "daily"
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
    assert j[-1]["trigger"] == "position closed" and j[-1]["events"][0]["why"] == "stop"


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
    assert brain.contexts[1]["your_journal"] and len(brain.contexts[0]["markets"]) == 5
    s = json.load(open(os.path.join(d, "summary.json")))
    assert s["trade_count"] == 1 and s["control_pln"] and s["hodl_pln"] and s["status"] == "live"
    print("summary:", {k: s[k] for k in ("equity_pln", "return_pct", "control_pln", "hodl_pln", "trade_count")})
    print("trade:", s["closed_trades"][0])


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("PASS", name)
