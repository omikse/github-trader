"""Offline tests: a fake exchange and a fake brain drive the real bot code end to end."""
import json
import math
import os
import sys
import tempfile
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
os.environ["DATA_DIR"] = tempfile.mkdtemp()

from bot import config, guard, run  # noqa: E402
from bot.bybit import Bybit, fmt_num  # noqa: E402

INST = {"qty_step": 0.001, "min_qty": 0.001, "min_notional": 5, "tick": 0.1}
BASE = {"BTCUSDT": 85000.0, "ETHUSDT": 3000.0, "SOLUSDT": 108.0}


class FakeBybit:
    """Deterministic price path; tracks one-way positions and equity like the exchange would."""

    def __init__(self, equity=258.0):
        self.equity0 = equity
        self.realized = 0.0
        self.pos = {}
        self.closed = []
        self.step = 0
        self.orders = []

    def px(self, sym, offset=0):
        i = self.step + offset
        return BASE[sym] * (1 + 0.04 * math.sin(i / 9) + 0.0006 * i)

    def klines(self, sym, interval, limit=200):
        mins = {"15": 15, "60": 60, "240": 240}[interval]
        now = 1_790_000_000_000 + self.step * 15 * 60_000
        out = []
        for j in range(limit):
            back = (limit - 1 - j) * mins // 15
            c = self.px(sym, -back)
            out.append({"t": now - back * 15 * 60_000, "o": c * 0.999, "h": c * 1.004, "l": c * 0.996, "c": c, "v": 100})
        return out

    def ticker(self, sym):
        p = self.px(sym)
        return {"last": p, "mark": p, "funding_rate": 0.0001, "open_interest": 1e6, "change_24h": 0.01}

    def instrument(self, sym):
        return INST

    def _upnl(self, p):
        m = self.px(p["symbol"])
        return (m - p["entry"]) * p["size"] if p["side"] == "long" else (p["entry"] - m) * p["size"]

    def wallet(self):
        return {"equity": self.equity0 + self.realized + sum(self._upnl(p) for p in self.pos.values()), "coins": {}}

    def positions(self):
        out = []
        for p in self.pos.values():
            q = dict(p)
            q.update(mark=self.px(p["symbol"]), upnl=self._upnl(p), liq=None, leverage=10, opened=1)
            out.append(q)
        return out

    def closed_pnl(self, start_ms):
        return list(self.closed)

    def set_leverage(self, sym, lev):
        pass

    def market_order(self, sym, side, qty, stop=None, tp=None, reduce_only=False):
        self.orders.append((sym, side, qty, stop, tp, reduce_only))
        assert reduce_only or stop, "guard must always attach a stop"
        self.pos[sym] = {"symbol": sym, "side": side, "size": qty, "entry": self.px(sym), "stop": stop, "tp": tp}

    def set_stops(self, sym, stop=None, tp=None):
        self.pos[sym]["stop"] = stop

    def close_position(self, p):
        q = self.pos.pop(p["symbol"])
        pnl = self._upnl(q)
        self.realized += pnl
        self.closed.append({"id": f"c{len(self.closed)}", "symbol": q["symbol"], "side": q["side"], "qty": q["size"],
                            "entry": q["entry"], "exit": self.px(q["symbol"]), "pnl": pnl, "time": 1_800_000_000_000 + self.step * 900_000})


class FakeBrain:
    def __init__(self, plans):
        self.plans = plans
        self.contexts = []

    def decide(self, ctx):
        self.contexts.append(ctx)
        return self.plans.pop(0) if self.plans else {"market_view": "nothing", "actions": [], "watch_next": "-"}


def test_signature_matches_manual_hmac():
    import hashlib
    import hmac
    c = Bybit("KEY", "SECRET", "https://x")
    want = hmac.new(b"SECRET", b"1700000000000KEY10000category=linear", hashlib.sha256).hexdigest()
    assert c.sign("1700000000000", "category=linear") == want
    assert fmt_num(0.00100) == "0.001" and fmt_num(85000.0) == "85000"


def test_guard_sizes_from_risk_and_rejects_bad_orders():
    ok, why, o = guard.check_open({"symbol": "BTCUSDT", "side": "long", "stop": 83300, "risk_pct": 0.03},
                                  equity=258, price=85000, inst=INST, positions=[])
    assert ok, why
    # loss at stop must be close to 3% of equity (rounded down, so never above)
    loss = o["qty"] * (85000 - 83300 + 85000 * config.TAKER_FEE * 2)
    assert loss <= 258 * 0.03 + 1e-6 and loss > 258 * 0.02
    assert guard.check_open({"symbol": "BTCUSDT", "side": "long", "stop": 86000}, equity=258, price=85000, inst=INST, positions=[])[0] is False
    assert guard.check_open({"symbol": "BTCUSDT", "side": "long"}, equity=258, price=85000, inst=INST, positions=[])[0] is False
    assert guard.check_open({"symbol": "BTCUSDT", "side": "short", "stop": 85100}, equity=258, price=85000, inst=INST, positions=[])[0] is False  # too tight
    # risk is capped at 5% even if the brain asks for 50%
    ok, _, o = guard.check_open({"symbol": "BTCUSDT", "side": "long", "stop": 80000, "risk_pct": 0.5},
                                equity=258, price=85000, inst=INST, positions=[])
    assert ok and o["risk_pct"] <= config.MAX_RISK_PER_TRADE + 1e-9
    # leverage cap: a very tight stop would want a huge size, guard cuts it to 10x
    ok, why, o = guard.check_open({"symbol": "BTCUSDT", "side": "long", "stop": 84700, "risk_pct": 0.05},
                                  equity=258, price=85000, inst=INST, positions=[])
    assert ok and o["notional"] <= 258 * config.MAX_LEVERAGE + 1 and "cut" in why


def test_stops_only_tighten():
    pos = {"symbol": "BTCUSDT", "side": "long", "stop": 83000}
    assert guard.check_move_stop({"stop": 82000}, price=85000, inst=INST, position=pos)[0] is False
    assert guard.check_move_stop({"stop": 84000}, price=85000, inst=INST, position=pos)[0] is True
    assert guard.check_move_stop({"stop": 85500}, price=85000, inst=INST, position=pos)[0] is False


def test_halts():
    st = {}
    assert guard.check_halts(st, 100, "d1") is None
    assert guard.check_halts(st, 84, "d1") == "daily"
    assert guard.check_halts(st, 90, "d1") == "daily"      # stays paused the rest of the day
    assert guard.check_halts(st, 90, "d2") is None          # new day resumes
    assert guard.check_halts(st, 49, "d2") == "kill"
    assert guard.check_halts(st, 200, "d3") == "kill"       # kill is permanent


def test_full_runs():
    ex = FakeBybit()
    brain = FakeBrain([
        {"market_view": "BTC trending up", "watch_next": "x", "actions": [
            {"type": "open", "symbol": "BTCUSDT", "side": "long", "stop": ex.px("BTCUSDT") * 0.98, "take_profit": ex.px("BTCUSDT") * 1.06, "risk_pct": 0.04, "reason": "trend"},
            {"type": "open", "symbol": "DOGEUSDT", "side": "long", "stop": 0.1, "reason": "not allowed"},
            {"type": "open", "symbol": "ETHUSDT", "side": "short", "reason": "no stop"}]},
        {"market_view": "trail", "watch_next": "x", "actions": [
            {"type": "move_stop", "symbol": "BTCUSDT", "stop": ex.px("BTCUSDT", 4) * 0.99, "reason": "trail"}]},
        {"market_view": "take it", "watch_next": "x", "actions": [{"type": "close", "symbol": "BTCUSDT", "reason": "done"}]},
    ])
    t0 = datetime(2026, 10, 22, 8, 0, tzinfo=timezone.utc)
    for i in range(13):  # 13 runs, 15 minutes apart
        ex.step = i
        run.main(client=ex, brain=brain, now=t0 + timedelta(minutes=15 * i), fx=3.88)
    d = config.DATA_DIR
    journal = [json.loads(line) for line in open(os.path.join(d, "decisions.jsonl"))]
    assert len(journal) == 4, len(journal)  # runs 0, 4, 8 (hourly) and 9 (woken by the closed trade)
    assert journal[3]["trigger"] == "position closed"
    first = {a["symbol"]: a for a in journal[0]["actions"]}
    assert first["BTCUSDT"]["result"] == "done"
    assert first["DOGEUSDT"]["result"] == "rejected" and first["ETHUSDT"]["result"] == "rejected"
    assert journal[1]["actions"][0]["result"] == "done"
    assert journal[2]["actions"][0]["result"] == "done" and not ex.pos
    # the brain saw its own journal and the closed trade on later calls
    assert brain.contexts[1]["your_journal"] and brain.contexts[3]["recent_closed_trades"]
    s = json.load(open(os.path.join(d, "summary.json")))
    assert s["trade_count"] == 1 and s["control_pln"] and s["hodl_pln"] and s["status"] == "live"
    rows = open(os.path.join(d, "equity.csv")).read().strip().splitlines()
    assert len(rows) == 14
    print("summary:", {k: s[k] for k in ("equity_pln", "return_pct", "control_pln", "hodl_pln", "trade_count")})
    print("first decision:", json.dumps(journal[0]["actions"], indent=1)[:900])


def test_refuses_to_start_with_huge_demo_balance():
    os.environ["DATA_DIR"] = config.DATA_DIR = tempfile.mkdtemp()
    assert run.main(client=FakeBybit(equity=50000), brain=FakeBrain([]),
                    now=datetime(2026, 10, 22, tzinfo=timezone.utc), fx=3.88) is None
    assert not os.path.exists(os.path.join(config.DATA_DIR, "state.json"))


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("PASS", name)
