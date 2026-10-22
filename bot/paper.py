"""Paper futures exchange driven by real Kraken prices.

No account or API key needed: market data comes from Kraken's public REST API. The exchange
itself is simulated, with the same interface the bot used for Bybit, so the rest of the bot is unchanged.

What is simulated, and how:
- Market orders fill at the live best bid/ask plus SLIPPAGE, and pay TAKER_FEE.
- Stop-losses and take-profits are checked against EVERY 1-minute candle since the last run,
  so a stop that would have fired between runs fires here too. A candle that opens beyond the
  stop (a gap) fills at the open, which is worse. If stop and target sit in the same candle,
  the stop is assumed to hit first (pessimistic).
- Funding: every hour, at Kraken Futures' REAL current rate for that coin (positive: longs pay shorts).
- Carry trades: buy the coin and short the same amount of its perpetual future. Price moves cancel out;
  the position earns (or pays) the hourly funding on its size. Costs CARRY_COST_PER_SIDE of the size to
  open and again to close (spot maker fee + futures taker fee). The size is locked capital.
- Prediction shares (Polymarket): bought at the live ask, valued at the live bid, sold at the bid,
  or paid out at 1 or 0 when the market resolves. The stake is spent from cash.
- Interest: cash that is not locked (not perp margin, not carry capital) earns the average US Treasury bill rate.
- Liquidation: cross margin. If equity at the worst price of a minute drops to the maintenance
  margin (MAINT_MARGIN of total position size), every position is closed at that price.
- Resting entry orders: a buy/sell that triggers when the price reaches a level (above the price at
  placement = stop-entry, below = limit). Checked every minute; filled at the level, or at the
  candle open when the market gaps through it (worse for stop-entries, better for limits).
"""
import json
import math
import time
from pathlib import Path

import requests

from . import config

KRAKEN = "https://api.kraken.com/0/public"
PAIRS = {"BTCUSDT": "XBTUSD", "ETHUSDT": "ETHUSD", "SOLUSDT": "SOLUSD", "XRPUSDT": "XRPUSD",
         "DOGEUSDT": "XDGUSD", "ADAUSDT": "ADAUSD", "AVAXUSDT": "AVAXUSD", "LINKUSDT": "LINKUSD",
         "SUIUSDT": "SUIUSD", "PEPEUSDT": "PEPEUSD", "WIFUSDT": "WIFUSD", "BONKUSDT": "BONKUSD",
         "LTCUSDT": "XLTCZUSD", "DOTUSDT": "DOTUSD", "NEARUSDT": "NEARUSD",
         "PAXGUSDT": "PAXGUSD",  # tokenised gold: one token = one troy ounce
         "EURUSDT": "EURUSD"}    # the euro against the dollar
SLIPPAGE = 0.0003
STOP_SLIPPAGE = 0.0005
FUNDING_RATE = 0.0001 / 8      # per hour; only used when Kraken Futures has no rate for a coin
CARRY_COST_PER_SIDE = 0.0025 + 0.0005  # Kraken spot maker 0.25% + futures taker 0.05%, each way
HOUR = 3_600_000
YEAR = 365 * 24 * HOUR
FUTURES = "https://futures.kraken.com/derivatives/api/v3/tickers"
TREASURY = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/avg_interest_rates"
MAINT_MARGIN = 0.005
MINUTE = 60_000


class ExchangeError(Exception):
    pass


class Kraken:
    """Public market data only."""

    def __init__(self):
        self.http = requests.Session()
        self._last = 0.0

    def _get(self, path, params):
        for attempt in range(4):
            wait = 0.35 - (time.time() - self._last)  # stay well under the public rate limit
            if wait > 0:
                time.sleep(wait)
            self._last = time.time()
            try:
                r = self.http.get(f"{KRAKEN}/{path}", params=params, timeout=15)
                data = r.json()
            except (requests.RequestException, ValueError) as e:
                err = str(e)
            else:
                if not data.get("error"):
                    return data["result"]
                err = ", ".join(data["error"])
            time.sleep(2 * (attempt + 1))
        raise ExchangeError(f"Kraken {path} {params.get('pair')}: {err}")

    @staticmethod
    def _first(result):
        return next(v for k, v in result.items() if k != "last")

    def ohlc(self, symbol, minutes, since_s=None):
        params = {"pair": PAIRS[symbol], "interval": minutes}
        if since_s:
            params["since"] = int(since_s)
        rows = self._first(self._get("OHLC", params))
        return [{"t": int(r[0]) * 1000, "o": float(r[1]), "h": float(r[2]), "l": float(r[3]),
                 "c": float(r[4]), "v": float(r[6])} for r in rows]

    def ticker(self, symbol):
        t = self._first(self._get("Ticker", {"pair": PAIRS[symbol]}))
        return {"last": float(t["c"][0]), "ask": float(t["a"][0]), "bid": float(t["b"][0])}

    def funding_rates(self):
        """Current hourly funding rate (fraction of position size) per symbol, from Kraken Futures."""
        r = self.http.get(FUTURES, timeout=15).json()
        by_sym = {t["symbol"].upper(): t for t in r.get("tickers", []) if t.get("tag") == "perpetual"}
        out = {}
        for sym in PAIRS:
            base = sym[:-4]
            t = by_sym.get(f"PF_{'XBT' if base == 'BTC' else base}USD")
            if t and t.get("relativeFundingRate") is not None:
                out[sym] = float(t["relativeFundingRate"])
        return out

    def cash_rate(self):
        """Average interest rate on US Treasury bills (latest month), as a fraction per year."""
        r = self.http.get(TREASURY, params={"filter": "security_desc:eq:Treasury Bills", "sort": "-record_date",
                                            "page[size]": 1}, timeout=15).json()
        return float(r["data"][0]["avg_interest_rate_amt"]) / 100


class PaperExchange:
    def __init__(self, state_path, market=None, start_usd=None, now_ms=None):
        self.path = Path(state_path)
        self.market = market or Kraken()
        self.now_ms = now_ms or int(time.time() * 1000)
        self._tick_cache = {}
        try:
            self.s = json.loads(self.path.read_text())
        except (FileNotFoundError, ValueError):
            self.s = None
        if self.s is None and start_usd is not None:
            self.s = {"cash": start_usd, "positions": {}, "closed": [], "fills": [],
                      "last_ms": self.now_ms, "next_id": 1}
        if self.s is not None:
            for k, v in (("orders", []), ("order_events", []), ("funding_rates", {}), ("carry", {}),
                         ("carry_closed", []), ("predictions", {}), ("pred_closed", []), ("cash_rate", 0.0387),
                         ("income", {"funding": 0.0, "carry": 0.0, "interest": 0.0})):
                self.s.setdefault(k, v)

    @property
    def ready(self):
        return self.s is not None

    def save(self):
        self.path.write_text(json.dumps(self.s, indent=1))

    # -- market data -----------------------------------------------------------------
    def klines(self, symbol, interval, limit=200):
        return self.market.ohlc(symbol, int(interval))[-limit:]

    def ticker(self, symbol):
        t = self.market.ticker(symbol)
        self._tick_cache[symbol] = t
        return {"last": t["last"], "mark": t["last"], "funding_rate": self.funding_rate(symbol),
                "open_interest": None, "change_24h": None}

    def funding_rate(self, symbol):
        return self.s["funding_rates"].get(symbol, FUNDING_RATE) if self.s else FUNDING_RATE

    def set_market_rates(self, funding=None, cash_rate=None):
        if funding:
            self.s["funding_rates"].update(funding)
        if cash_rate is not None:
            self.s["cash_rate"] = cash_rate

    def _quote(self, symbol):
        return self._tick_cache.get(symbol) or self.market.ticker(symbol)

    def instrument(self, symbol):
        px = self._quote(symbol)["last"]
        tick = 10 ** (math.floor(math.log10(px)) - 5)
        return {"qty_step": 10 ** (math.floor(math.log10(5 / px)) - 3), "min_qty": 0.0, "min_notional": 5.0, "tick": tick}

    # -- replay the minutes since the last run -------------------------------------------
    def advance(self):
        """Apply every 1-minute candle since the last run: stops, targets, funding, liquidation."""
        start = first = self.s["last_ms"]
        watch = set(self.s["positions"]) | {o["symbol"] for o in self.s["orders"]}
        if watch:
            candles = {}
            for sym in sorted(watch):
                mins = 1 if self.now_ms - start < 11 * 3600_000 else 5  # Kraken keeps 720 candles
                rows = self.market.ohlc(sym, mins, since_s=start / 1000 - 60)
                # every candle that finished after the last run and before now, exactly once
                candles[sym] = {r["t"]: r for r in rows if start < r["t"] + mins * MINUTE <= self.now_ms}
            times = sorted({t for c in candles.values() for t in c})
            for t in times:
                self._funding(start, t)
                start = t
                bars = {s: candles[s].get(t) for s in candles}
                for sym, bar in bars.items():
                    if bar and sym in self.s["positions"]:
                        self._check_exits(sym, bar)
                self._check_liquidation(bars)
                self._check_orders(bars, t)
            self._funding(start, self.now_ms)
        else:
            self._funding(start, self.now_ms)
        self._interest(first, self.now_ms)
        self.s["last_ms"] = self.now_ms

    def _funding(self, a, b):
        """Hourly funding at each full hour in (a, b]: perps pay or receive, carry trades (short perp) receive."""
        for _ in range(a // HOUR + 1, b // HOUR + 1):
            for sym, p in self.s["positions"].items():
                flow = p["qty"] * p.get("mark", p["entry"]) * self.funding_rate(sym)
                flow = -flow if p["side"] == "long" else flow
                self.s["cash"] += flow
                self.s["income"]["funding"] += flow
            for sym, c in self.s["carry"].items():
                flow = c["notional"] * self.funding_rate(sym)
                self.s["cash"] += flow
                c["earned"] += flow
                self.s["income"]["carry"] += flow

    def locked(self):
        """Capital that is not idle: perp margin at the leverage cap, plus carry capital."""
        margin = sum(p["qty"] * p.get("mark", p["entry"]) for p in self.s["positions"].values()) / config.MAX_LEVERAGE
        return margin + sum(c["notional"] for c in self.s["carry"].values())

    def _interest(self, a, b):
        if b <= a:
            return
        idle = max(0.0, self.s["cash"] - self.locked())
        x = idle * self.s["cash_rate"] * (b - a) / YEAR
        self.s["cash"] += x
        self.s["income"]["interest"] += x

    def _check_exits(self, sym, bar):
        p = self.s["positions"][sym]
        stop, tp = p.get("stop"), p.get("tp")
        p["mark"] = bar["c"]
        if p["side"] == "long":
            if stop and bar["o"] <= stop:
                return self._exit(sym, bar["o"] * (1 - STOP_SLIPPAGE), "stop (gap)", bar["t"])
            if stop and bar["l"] <= stop:
                return self._exit(sym, stop * (1 - STOP_SLIPPAGE), "stop", bar["t"])
            if tp and bar["h"] >= tp:
                return self._exit(sym, max(tp, bar["o"]), "target", bar["t"])
        else:
            if stop and bar["o"] >= stop:
                return self._exit(sym, bar["o"] * (1 + STOP_SLIPPAGE), "stop (gap)", bar["t"])
            if stop and bar["h"] >= stop:
                return self._exit(sym, stop * (1 + STOP_SLIPPAGE), "stop", bar["t"])
            if tp and bar["l"] <= tp:
                return self._exit(sym, min(tp, bar["o"]), "target", bar["t"])

    def _check_liquidation(self, bars):
        pos = self.s["positions"]
        if not pos:
            return
        worst, notional = {}, 0.0
        for sym, p in pos.items():
            bar = bars.get(sym)
            px = (bar["l"] if p["side"] == "long" else bar["h"]) if bar else p.get("mark", p["entry"])
            worst[sym] = px
            notional += p["qty"] * px
        eq = self.s["cash"] - sum(c["notional"] for c in self.s["carry"].values()) \
            + sum(self._upnl(p, worst[s]) for s, p in pos.items())
        if eq <= notional * MAINT_MARGIN:
            t = max((b["t"] for b in bars.values() if b), default=self.now_ms)
            for sym in list(pos):
                self._exit(sym, worst[sym], "liquidation", t, fee=True)
            self.s["cash"] = max(0.0, self.s["cash"])

    def _order_event(self, o, status, t, detail=""):
        self.s["order_events"].append({"id": o["id"], "symbol": o["symbol"], "side": o["side"], "status": status,
                                       "trigger": o["trigger"], "time": int(t), "detail": detail})
        self.s["order_events"] = self.s["order_events"][-200:]

    def _check_orders(self, bars, t):
        keep = []
        for o in self.s["orders"]:
            bar = bars.get(o["symbol"])
            if t >= o["expires"]:
                self._order_event(o, "expired", t)
                continue
            if not bar:
                keep.append(o)
                continue
            lvl, above, long = o["trigger"], o["direction"] == "above", o["side"] == "long"
            hit = bar["h"] >= lvl if above else bar["l"] <= lvl
            if not hit:
                keep.append(o)
                continue
            gapped = bar["o"] >= lvl if above else bar["o"] <= lvl
            px = bar["o"] if gapped else lvl
            px *= (1 + SLIPPAGE) if long else (1 - SLIPPAGE)
            why = self._fill_blocker(o, bars)
            if why:
                self._order_event(o, "cancelled", t, why)
                continue
            fee = px * o["qty"] * config.TAKER_FEE
            self.s["cash"] -= fee
            self.s["positions"][o["symbol"]] = {"side": o["side"], "qty": o["qty"], "entry": px, "stop": o["stop"],
                                                "tp": o.get("tp"), "opened": int(t), "entry_fee": fee, "mark": px,
                                                "note": o.get("note", "")}
            self._order_event(o, "filled", t, f"filled at {px:.6g}")
            # the stop can be hit inside the same minute that filled the entry
            self._check_exits(o["symbol"], {**bar, "o": px})
        self.s["orders"] = keep

    def _fill_blocker(self, o, bars):
        if o["symbol"] in self.s["positions"]:
            return "already holding this coin"
        if len(self.s["positions"]) >= config.MAX_OPEN_POSITIONS:
            return "max open positions reached"
        marks = {s: (bars[s]["c"] if bars.get(s) else p.get("mark", p["entry"])) for s, p in self.s["positions"].items()}
        eq = self.s["cash"] + sum(self._upnl(p, marks[s]) for s, p in self.s["positions"].items())
        used = sum(p["qty"] * marks[s] for s, p in self.s["positions"].items())
        if eq <= 0 or used + o["qty"] * o["trigger"] > eq * config.MAX_LEVERAGE * 1.02:
            return "leverage cap would be exceeded at fill"
        return None

    @staticmethod
    def _upnl(p, px):
        return (px - p["entry"]) * p["qty"] if p["side"] == "long" else (p["entry"] - px) * p["qty"]

    def _exit(self, sym, px, why, t, fee=True):
        p = self.s["positions"].pop(sym)
        pnl = self._upnl(p, px)
        fee_paid = px * p["qty"] * config.TAKER_FEE if fee else 0.0
        self.s["cash"] += pnl - fee_paid
        rec = {"id": f"t{self.s['next_id']}", "symbol": sym, "side": p["side"], "qty": p["qty"],
               "entry": p["entry"], "exit": round(px, 8), "pnl": round(pnl - fee_paid - p.get("entry_fee", 0), 4),
               "time": int(t), "why": why, "opened": p.get("opened"), "reason": p.get("note", "")}
        self.s["next_id"] += 1
        self.s["closed"].append(rec)

    # -- account ------------------------------------------------------------------------
    def wallet(self):
        eq = self.s["cash"]
        for sym, p in self.s["positions"].items():
            q = self._quote(sym)
            eq += self._upnl(p, q["bid"] if p["side"] == "long" else q["ask"])
        eq += self.predictions_value()
        return {"equity": eq, "coins": {"USD": self.s["cash"]}}

    # -- carry trades -----------------------------------------------------------------------
    def carry_open(self, symbol, notional, note=""):
        if symbol in self.s["carry"]:
            raise ExchangeError(f"already running a carry trade on {symbol}")
        cost = notional * CARRY_COST_PER_SIDE
        self.s["cash"] -= cost
        self.s["income"]["carry"] -= cost
        self.s["carry"][symbol] = {"notional": notional, "opened": self.now_ms, "earned": 0.0, "fees": cost,
                                   "rate_at_open": self.funding_rate(symbol), "note": note}
        return cost

    def carry_close(self, symbol, why="manual close"):
        c = self.s["carry"].pop(symbol, None)
        if not c:
            raise ExchangeError(f"no carry trade on {symbol}")
        cost = c["notional"] * CARRY_COST_PER_SIDE
        self.s["cash"] -= cost
        self.s["income"]["carry"] -= cost
        rec = {"id": f"c{self.s['next_id']}", "symbol": symbol, "notional": c["notional"], "opened": c["opened"],
               "time": self.now_ms, "earned": round(c["earned"], 4), "fees": round(c["fees"] + cost, 4),
               "pnl": round(c["earned"] - c["fees"] - cost, 4), "why": why, "reason": c.get("note", "")}
        self.s["next_id"] += 1
        self.s["carry_closed"].append(rec)
        return rec

    def carry_list(self):
        out = []
        for sym, c in self.s["carry"].items():
            r = self.funding_rate(sym)
            out.append({"symbol": sym, "notional": round(c["notional"], 2), "earned": round(c["earned"], 4),
                        "fees": round(c["fees"], 4), "net_if_closed_now": round(c["earned"] - c["fees"] - c["notional"] * CARRY_COST_PER_SIDE, 4),
                        "funding_pct_per_hour": round(r * 100, 5), "funding_apr_pct": round(r * 24 * 365 * 100, 1),
                        "opened": c["opened"], "reason": c.get("note", "")})
        return out

    # -- prediction markets -------------------------------------------------------------------
    def predictions_value(self):
        return sum(p["shares"] * p["mark"] for p in self.s["predictions"].values())

    def predict_buy(self, m, outcome, stake, note=""):
        from .predictions import buy_price, fee
        if m["id"] in self.s["predictions"]:
            raise ExchangeError("already holding this market; sell it first")
        px = buy_price(m, outcome)
        if not px or not 0 < px < 1:
            raise ExchangeError("no usable ask price")
        shares = stake / px
        f = fee(m, px, shares)
        self.s["cash"] -= stake + f
        self.s["predictions"][m["id"]] = {"question": m["question"], "outcome": outcome, "shares": shares,
                                          "entry": px, "cost": stake + f, "mark": px, "end": m.get("end"),
                                          "opened": self.now_ms, "note": note}
        self._mark_prediction(m["id"], m)
        return {"price": px, "shares": shares, "fee": f}

    def predict_sell(self, market_id, m, why="sold"):
        from .predictions import fee, sell_price
        p = self.s["predictions"].get(market_id)
        if not p:
            raise ExchangeError("no position in this market")
        px = sell_price(m, p["outcome"])
        if px is None:
            raise ExchangeError("no usable bid price")
        f = fee(m, px, p["shares"])
        return self._settle_prediction(market_id, px, why, f)

    def _settle_prediction(self, market_id, px, why, f=0.0):
        p = self.s["predictions"].pop(market_id)
        proceeds = p["shares"] * px - f
        self.s["cash"] += proceeds
        rec = {"id": f"p{self.s['next_id']}", "market": market_id, "question": p["question"], "outcome": p["outcome"],
               "shares": p["shares"], "entry": p["entry"], "exit": round(px, 4), "cost": round(p["cost"], 4),
               "pnl": round(proceeds - p["cost"], 4), "time": self.now_ms, "opened": p["opened"], "why": why,
               "reason": p.get("note", "")}
        self.s["next_id"] += 1
        self.s["pred_closed"].append(rec)
        return rec

    def _mark_prediction(self, market_id, m):
        from .predictions import sell_price
        p = self.s["predictions"][market_id]
        px = sell_price(m, p["outcome"])
        if px is not None:
            p["mark"] = px
        p["yes_bid"], p["yes_ask"] = m.get("yes_bid"), m.get("yes_ask")

    def update_predictions(self, markets):
        """markets: id -> normalized market. Marks open positions at the bid; pays out resolved markets."""
        settled = []
        for mid in list(self.s["predictions"]):
            m = markets.get(mid)
            if not m:
                continue
            p = self.s["predictions"][mid]
            if m["resolved"] and m["final_yes"] is not None:
                px = m["final_yes"] if p["outcome"] == "Yes" else 1 - m["final_yes"]
                settled.append(self._settle_prediction(mid, px, "resolved " + ("win" if px > 0.5 else "loss")))
            else:
                self._mark_prediction(mid, m)
        return settled

    def prediction_list(self):
        return [{"market": mid, **{k: p[k] for k in ("question", "outcome", "entry", "mark", "end", "opened")},
                 "shares": round(p["shares"], 4), "cost": round(p["cost"], 4),
                 "value": round(p["shares"] * p["mark"], 4), "pnl": round(p["shares"] * p["mark"] - p["cost"], 4),
                 "reason": p.get("note", "")} for mid, p in self.s["predictions"].items()]

    def positions(self):
        out = []
        for sym, p in self.s["positions"].items():
            q = self._quote(sym)
            mark = q["last"]
            p["mark"] = mark
            out.append({"symbol": sym, "side": p["side"], "size": p["qty"], "entry": p["entry"], "mark": mark,
                        "upnl": self._upnl(p, mark), "stop": p.get("stop"), "tp": p.get("tp"), "liq": None,
                        "leverage": None, "opened": p["opened"], "reason": p.get("note", "")})
        return out

    def closed_pnl(self, start_ms):
        return [c for c in self.s["closed"] if c["time"] >= start_ms]

    # -- trading --------------------------------------------------------------------------
    def set_leverage(self, symbol, lev):
        pass  # leverage is enforced by the risk guard; margin is cross

    def market_order(self, symbol, side, qty, stop=None, tp=None, reduce_only=False, note=""):
        q = self.market.ticker(symbol)  # fresh quote at the moment of the order
        self._tick_cache[symbol] = q
        if reduce_only:
            p = self.s["positions"].get(symbol)
            if not p:
                raise ExchangeError(f"no position in {symbol}")
            px = q["bid"] * (1 - SLIPPAGE) if p["side"] == "long" else q["ask"] * (1 + SLIPPAGE)
            self._exit(symbol, px, "manual close", self.now_ms)
            return {"price": px}
        if symbol in self.s["positions"]:
            raise ExchangeError(f"already holding {symbol}")
        px = q["ask"] * (1 + SLIPPAGE) if side == "long" else q["bid"] * (1 - SLIPPAGE)
        fee = px * qty * config.TAKER_FEE
        self.s["cash"] -= fee
        self.s["positions"][symbol] = {"side": side, "qty": qty, "entry": px, "stop": stop, "tp": tp,
                                       "opened": self.now_ms, "entry_fee": fee, "mark": px, "note": note}
        self.s["fills"].append({"time": self.now_ms, "symbol": symbol, "side": side, "qty": qty, "price": px, "fee": fee})
        self.s["fills"] = self.s["fills"][-200:]
        return {"price": px}

    def place_order(self, symbol, side, qty, trigger, stop, tp, expires_ms, note=""):
        if any(o["symbol"] == symbol for o in self.s["orders"]):
            raise ExchangeError(f"there is already a resting order for {symbol}; cancel it first")
        last = self._quote(symbol)["last"]
        o = {"id": f"o{self.s['next_id']}", "symbol": symbol, "side": side, "qty": qty, "trigger": trigger,
             "direction": "above" if trigger > last else "below", "stop": stop, "tp": tp,
             "placed": self.now_ms, "expires": expires_ms, "note": note}
        self.s["next_id"] += 1
        self.s["orders"].append(o)
        return o

    def cancel_orders(self, symbol):
        gone = [o for o in self.s["orders"] if o["symbol"] == symbol]
        self.s["orders"] = [o for o in self.s["orders"] if o["symbol"] != symbol]
        for o in gone:
            self._order_event(o, "cancelled", self.now_ms, "cancelled by the brain")
        return len(gone)

    def open_orders(self):
        return list(self.s["orders"])

    def order_events(self, start_ms):
        return [e for e in self.s["order_events"] if e["time"] >= start_ms]

    def set_stops(self, symbol, stop=None, tp=None):
        p = self.s["positions"].get(symbol)
        if not p:
            raise ExchangeError(f"no position in {symbol}")
        if stop:
            p["stop"] = stop
        if tp:
            p["tp"] = tp

    def close_position(self, pos):
        return self.market_order(pos["symbol"], "short" if pos["side"] == "long" else "long",
                                 pos["size"], reduce_only=True)
