"""Polymarket market data (public Gamma API, no account needed).

Only binary Yes/No markets are used. Gamma's bestBid/bestAsk are for the "Yes" share; a "No" share is
the mirror image: buying No costs 1 - bestBid(Yes), selling No pays 1 - bestAsk(Yes).
"""
import json
import time
from datetime import datetime, timezone

import requests

GAMMA = "https://gamma-api.polymarket.com"


def _f(x, default=None):
    try:
        return float(x)
    except (TypeError, ValueError):
        return default


def _iso_ms(s):
    if not s:
        return None
    try:
        return int(datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp() * 1000)
    except ValueError:
        return None


def normalize(m):
    """Compact market dict, or None when the market is not a usable binary market."""
    try:
        outcomes = json.loads(m.get("outcomes") or "[]")
        prices = [float(p) for p in json.loads(m.get("outcomePrices") or "[]")]
    except (ValueError, TypeError):
        return None
    if [o.lower() for o in outcomes] != ["yes", "no"] or len(prices) != 2:
        return None
    bid, ask = _f(m.get("bestBid")), _f(m.get("bestAsk"))
    resolved = bool(m.get("closed")) and max(prices) >= 0.99 or m.get("umaResolutionStatus") == "resolved"
    return {
        "id": str(m["id"]), "slug": m.get("slug"), "question": m.get("question"),
        "end_ms": _iso_ms(m.get("endDate")), "end": m.get("endDate"),
        "yes_bid": bid, "yes_ask": ask, "yes_price": prices[0],
        "closed": bool(m.get("closed")), "resolved": bool(resolved),
        "final_yes": prices[0] if resolved else None,
        "accepting": bool(m.get("acceptingOrders")) and bool(m.get("active")) and not m.get("closed"),
        "liquidity": _f(m.get("liquidityNum"), 0.0), "volume24h": _f(m.get("volume24hr"), 0.0),
        "fees_enabled": bool(m.get("feesEnabled")), "taker_bps": _f(m.get("takerBaseFee"), 0.0),
        "min_shares": _f(m.get("orderMinSize"), 5.0),
        "change_1d": _f(m.get("oneDayPriceChange")), "change_1w": _f(m.get("oneWeekPriceChange")),
    }


def buy_price(m, outcome):
    if m["yes_bid"] is None or m["yes_ask"] is None:
        return None
    return m["yes_ask"] if outcome == "Yes" else 1 - m["yes_bid"]


def sell_price(m, outcome):
    if m["yes_bid"] is None or m["yes_ask"] is None:
        return None
    return m["yes_bid"] if outcome == "Yes" else 1 - m["yes_ask"]


def fee(m, price, shares):
    """Polymarket's taker fee formula: rate x min(price, 1 - price) x shares (zero on fee-free markets)."""
    if not m.get("fees_enabled") or not m.get("taker_bps"):
        return 0.0
    return m["taker_bps"] / 10_000 * min(price, 1 - price) * shares


class Polymarket:
    def __init__(self):
        self.http = requests.Session()

    def _get(self, path, params=None):
        last = None
        for attempt in range(3):
            try:
                r = self.http.get(f"{GAMMA}{path}", params=params, timeout=20)
                if r.status_code == 200:
                    return r.json()
                last = f"HTTP {r.status_code}"
            except (requests.RequestException, ValueError) as e:
                last = str(e)
            time.sleep(2 * (attempt + 1))
        raise RuntimeError(f"Polymarket {path}: {last}")

    def top(self, limit=200):
        rows = self._get("/markets", {"closed": "false", "active": "true", "order": "volume24hr",
                                      "ascending": "false", "limit": limit})
        return [m for m in (normalize(x) for x in rows) if m]

    def get(self, key):
        """Look a market up by numeric id or by slug."""
        key = str(key).strip()
        if key.isdigit():
            return normalize(self._get(f"/markets/{key}"))
        rows = self._get("/markets", {"slug": key})
        return normalize(rows[0]) if rows else None


def shortlist(markets, now_ms, end_ms, n=40):
    """Markets worth showing the brain: open, liquid, not already decided, resolving before the experiment ends."""
    out = []
    for m in markets:
        if not m["accepting"] or m["liquidity"] < 5_000 or not m["end_ms"]:
            continue
        if not (now_ms < m["end_ms"] <= end_ms + 3 * 86_400_000):
            continue
        if m["yes_ask"] is None or not (0.03 <= m["yes_price"] <= 0.97):
            continue
        out.append(m)
    out.sort(key=lambda m: -m["volume24h"])
    return out[:n]


def brief(m, now_ms):
    days = (m["end_ms"] - now_ms) / 86_400_000 if m.get("end_ms") else None
    return {"market": m["id"], "question": m["question"], "yes_bid": m["yes_bid"], "yes_ask": m["yes_ask"],
            "days_left": round(days, 1) if days is not None else None, "volume_24h": round(m["volume24h"]),
            "liquidity": round(m["liquidity"]), "change_1d": m["change_1d"], "change_1w": m["change_1w"],
            "fee": "yes" if m["fees_enabled"] and m["taker_bps"] else "no"}
