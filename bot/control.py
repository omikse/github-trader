"""Benchmarks that run next to Claude under the same risk budget.

control: a dumb 20/50 EMA crossover bot on BTC (1h candles, 2x ATR trailing stop, 3% risk),
         simulated candle by candle with taker fees and a little slippage.
hodl:    buy Bitcoin with the whole account at the start and never touch it.
If Claude cannot beat the control bot, the brain is not adding value.
"""
from . import config
from .market import atr, ema

SYMBOL = "BTCUSDT"
RISK = 0.03
SLIP = 0.0005


def _fee(notional):
    return notional * config.TAKER_FEE


def _close(c, price):
    p = c["pos"]
    exit_px = price * (1 - SLIP) if p["side"] == "long" else price * (1 + SLIP)
    pnl = (exit_px - p["entry"]) * p["qty"] if p["side"] == "long" else (p["entry"] - exit_px) * p["qty"]
    c["equity"] += pnl - _fee(exit_px * p["qty"])
    c["trades"] += 1
    c["wins"] += 1 if pnl > 0 else 0
    c["pos"] = None


def _open(c, side, price, a):
    if not a or c["equity"] <= 0:
        return
    entry = price * (1 + SLIP) if side == "long" else price * (1 - SLIP)
    stop = entry - 2 * a if side == "long" else entry + 2 * a
    qty = c["equity"] * RISK / (2 * a + entry * config.TAKER_FEE * 2)
    qty = min(qty, c["equity"] * config.MAX_LEVERAGE / entry)
    c["equity"] -= _fee(entry * qty)
    c["pos"] = {"side": side, "entry": entry, "qty": qty, "stop": stop}


def update(c, h1, start_usd):
    """Advance the control bot through every newly CLOSED hourly candle. Returns the state dict."""
    closed = h1[:-1]  # the last kline is still forming
    if not closed:
        return c
    if not c:
        c = {"equity": start_usd, "pos": None, "last_t": closed[-1]["t"], "trades": 0, "wins": 0}
        return c
    for i, k in enumerate(closed):
        if k["t"] <= c["last_t"] or i < 51:
            continue
        p = c["pos"]
        if p:  # stop hit inside the candle?
            if p["side"] == "long" and k["l"] <= p["stop"]:
                _close(c, p["stop"])
            elif p["side"] == "short" and k["h"] >= p["stop"]:
                _close(c, p["stop"])
        closes = [x["c"] for x in closed[: i + 1]]
        prev = [x["c"] for x in closed[:i]]
        f, s = ema(closes, 20), ema(closes, 50)
        pf, ps = ema(prev, 20), ema(prev, 50)
        a = atr(closed[max(0, i - 60): i + 1])
        if c["pos"] and a:  # trail the stop
            if c["pos"]["side"] == "long":
                c["pos"]["stop"] = max(c["pos"]["stop"], k["c"] - 2 * a)
            else:
                c["pos"]["stop"] = min(c["pos"]["stop"], k["c"] + 2 * a)
        if None not in (f, s, pf, ps):
            if pf <= ps and f > s:
                if c["pos"] and c["pos"]["side"] == "short":
                    _close(c, k["c"])
                if not c["pos"]:
                    _open(c, "long", k["c"], a)
            elif pf >= ps and f < s:
                if c["pos"] and c["pos"]["side"] == "long":
                    _close(c, k["c"])
                if not c["pos"]:
                    _open(c, "short", k["c"], a)
        c["last_t"] = k["t"]
    return c


def value(c, price):
    if not c:
        return None
    eq = c["equity"]
    p = c.get("pos")
    if p:
        eq += (price - p["entry"]) * p["qty"] if p["side"] == "long" else (p["entry"] - price) * p["qty"]
    return eq
