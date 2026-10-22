"""Risk guard: plain deterministic rules between the brain and the exchange.

Nothing the brain says can bypass these checks. Every function returns (ok, reason, order).
"""
import math

from . import config


def round_down(x, step):
    if step <= 0:
        return x
    return math.floor(x / step + 1e-9) * step


def round_price(x, tick):
    if tick <= 0:
        return x
    return round(round(x / tick) * tick, 10)


def check_open(action, *, equity, price, inst, positions, locked=0.0):
    """Validate and size a new position. Returns (ok, reason, order)."""
    sym, side = action.get("symbol"), action.get("side")
    stop = action.get("stop")
    tp = action.get("take_profit")
    if side not in ("long", "short"):
        return False, "side must be long or short", None
    if any(p["symbol"] == sym for p in positions):
        return False, f"already holding {sym}; close it or move its stop instead", None
    if len(positions) >= config.MAX_OPEN_POSITIONS:
        return False, f"max {config.MAX_OPEN_POSITIONS} open positions", None
    if not stop or stop <= 0:
        return False, "every new position needs a stop-loss", None
    if equity <= 0:
        return False, "no equity", None

    dist = (price - stop) / price if side == "long" else (stop - price) / price
    if dist <= 0:
        return False, "stop is on the wrong side of the price", None
    if dist < config.MIN_STOP_DIST:
        return False, f"stop too tight ({dist:.2%} < {config.MIN_STOP_DIST:.1%})", None
    if dist > config.MAX_STOP_DIST:
        return False, f"stop too wide ({dist:.2%} > {config.MAX_STOP_DIST:.0%})", None
    if tp is not None and tp > 0:
        if (side == "long" and tp <= price) or (side == "short" and tp >= price):
            tp = None  # a target on the wrong side is dropped, the trade itself is fine

    risk_pct = action.get("risk_pct") or config.DEFAULT_RISK
    risk_pct = max(0.0, min(float(risk_pct), config.MAX_RISK_PER_TRADE))
    risk_usd = equity * risk_pct
    # loss per unit if stopped: the move to the stop plus taker fees in and out
    loss_per_unit = abs(price - stop) + price * config.TAKER_FEE * 2
    qty = risk_usd / loss_per_unit
    notes = []

    used = sum(p["size"] * p["mark"] for p in positions)
    room = max(0.0, equity - locked) * config.MAX_LEVERAGE - used
    if room <= 0:
        return False, "leverage cap reached", None
    if qty * price > room:
        qty = room / price
        notes.append(f"size cut to fit the {config.MAX_LEVERAGE:.0f}x cap")

    qty = round_down(qty, inst["qty_step"])
    if qty < inst["min_qty"] or qty * price < inst["min_notional"]:
        return False, f"size {qty} below the exchange minimum", None

    order = {
        "symbol": sym, "side": side, "qty": qty,
        "stop": round_price(stop, inst["tick"]),
        "tp": round_price(tp, inst["tick"]) if tp else None,
        "risk_pct": round(qty * loss_per_unit / equity, 4),
        "notional": round(qty * price, 2),
        "leverage_used": round((used + qty * price) / equity, 2),
    }
    return True, "; ".join(notes) or "ok", order


def check_move_stop(action, *, price, inst, position):
    if position is None:
        return False, "no open position to move a stop on", None
    new = action.get("stop")
    if not new or new <= 0:
        return False, "new stop missing", None
    old = position.get("stop")
    side = position["side"]
    if side == "long":
        if new >= price:
            return False, "long stop must stay below the price", None
        if old and new < old:
            return False, "stops can only be tightened", None
    else:
        if new <= price:
            return False, "short stop must stay above the price", None
        if old and new > old:
            return False, "stops can only be tightened", None
    tp = action.get("take_profit")
    if tp is not None and tp > 0 and ((side == "long" and tp <= price) or (side == "short" and tp >= price)):
        tp = None
    return True, "ok", {"symbol": position["symbol"], "stop": round_price(new, inst["tick"]),
                        "tp": round_price(tp, inst["tick"]) if tp else None}


def check_halts(state, equity, day):
    """Return 'kill', 'daily' or None, updating peak / day bookkeeping in state."""
    if state.get("halted"):
        return "kill"
    if state.get("day") != day:
        state["day"] = day
        state["day_start_equity"] = equity
        state["paused_day"] = None
    state["peak_equity"] = max(state.get("peak_equity", equity), equity)
    if equity <= state["peak_equity"] * (1 - config.KILL_DRAWDOWN) or equity <= 0:
        state["halted"] = True
        return "kill"
    if state.get("paused_day") == day:
        return "daily"
    if equity <= state["day_start_equity"] * (1 - config.DAILY_LOSS_LIMIT):
        state["paused_day"] = day
        return "daily"
    return None


def check_predict(action, *, equity, market, open_cost, free_cash):
    """Validate a prediction-market buy. Returns (ok, reason, order)."""
    from .predictions import buy_price
    outcome = str(action.get("outcome", "")).strip().capitalize()
    if outcome not in ("Yes", "No"):
        return False, "outcome must be Yes or No", None
    if not market:
        return False, "market not found (use the market id from prediction_markets, or a Polymarket slug)", None
    if not market["accepting"]:
        return False, "market is closed for trading", None
    if market["liquidity"] < 2_000:
        return False, "market too thin (liquidity under $2,000)", None
    px = buy_price(market, outcome)
    if px is None or not 0.01 <= px <= 0.99:
        return False, f"price {px} is outside 0.01-0.99", None
    pct = min(float(action.get("stake_pct") or 0.03), config.PRED_MAX_STAKE)
    stake = equity * pct
    notes = []
    room = equity * config.PRED_MAX_TOTAL - open_cost
    if stake > room:
        stake = room
        notes.append(f"stake cut to fit the {config.PRED_MAX_TOTAL:.0%} total cap")
    if stake > free_cash:
        stake = free_cash
        notes.append("stake cut to the free cash")
    if stake <= 0 or stake / px < market["min_shares"]:
        return False, "stake too small for the market minimum", None
    return True, "; ".join(notes) or "ok", {"market": market, "outcome": outcome, "stake": round(stake, 4), "price": px}


def check_carry(action, *, equity, symbol, open_total, free_cash, rate):
    """Validate a carry trade (long coin + short perp). Returns (ok, reason, notional)."""
    if rate is None:
        return False, "no funding rate for this coin", None
    pct = float(action.get("size_pct") or 0.2)
    notional = equity * pct
    notes = []
    room = equity * config.CARRY_MAX_TOTAL - open_total
    if notional > room:
        notional = room
        notes.append(f"size cut to fit the {config.CARRY_MAX_TOTAL:.0%} total cap")
    if notional > free_cash:
        notional = free_cash
        notes.append("size cut to the free cash")
    if notional < 10:
        return False, "not enough room or free cash for a carry trade", None
    if rate <= 0:
        notes.append("warning: funding is negative now, so this carry PAYS until it turns")
    return True, "; ".join(notes) or "ok", round(notional, 2)
