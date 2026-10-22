"""Market snapshot and indicators, computed in plain Python so the brain gets clean numbers."""


def ema(values, n):
    if len(values) < n:
        return None
    k = 2 / (n + 1)
    e = sum(values[:n]) / n
    for v in values[n:]:
        e = v * k + e * (1 - k)
    return e


def rsi(values, n=14):
    if len(values) <= n:
        return None
    gains, losses = 0.0, 0.0
    for i in range(1, n + 1):
        d = values[i] - values[i - 1]
        gains += max(d, 0)
        losses += max(-d, 0)
    ag, al = gains / n, losses / n
    for i in range(n + 1, len(values)):
        d = values[i] - values[i - 1]
        ag = (ag * (n - 1) + max(d, 0)) / n
        al = (al * (n - 1) + max(-d, 0)) / n
    if al == 0:
        return 100.0
    return 100 - 100 / (1 + ag / al)


def atr(candles, n=14):
    if len(candles) <= n:
        return None
    trs = []
    for i in range(1, len(candles)):
        c, p = candles[i], candles[i - 1]
        trs.append(max(c["h"] - c["l"], abs(c["h"] - p["c"]), abs(c["l"] - p["c"])))
    a = sum(trs[:n]) / n
    for t in trs[n:]:
        a = (a * (n - 1) + t) / n
    return a


def pct(a, b):
    return (a / b - 1) if b else 0.0


def _r(x, d=2):
    return None if x is None else round(x, d)


def snapshot(client, symbol):
    """Everything the brain needs about one market, as a compact dict."""
    m15 = client.klines(symbol, "15", 96)
    h1 = client.klines(symbol, "60", 200)
    h4 = client.klines(symbol, "240", 200)
    d1 = client.klines(symbol, "1440", 120)
    t = client.ticker(symbol)
    price = t["last"]
    c1 = [k["c"] for k in h1]
    c4 = [k["c"] for k in h4]
    cd = [k["c"] for k in d1]
    a1 = atr(h1)
    day = h1[-24:]
    snap = {
        "symbol": symbol,
        "price": price,
        "change_15m": _r(pct(price, m15[-2]["c"]) * 100) if len(m15) > 1 else None,
        "change_1h": _r(pct(price, c1[-2]) * 100) if len(c1) > 1 else None,
        "change_4h": _r(pct(price, c4[-2]) * 100) if len(c4) > 1 else None,
        "change_24h": _r(pct(price, c1[-25]) * 100) if len(c1) > 25 else None,
        "high_24h": max(k["h"] for k in day),
        "low_24h": min(k["l"] for k in day),
        "h1": {"ema20": _r(ema(c1, 20), 4), "ema50": _r(ema(c1, 50), 4), "ema200": _r(ema(c1, 200), 4),
               "rsi14": _r(rsi(c1)), "atr14": _r(a1, 4), "atr_pct": _r(a1 / price * 100 if a1 else None)},
        "h4": {"ema20": _r(ema(c4, 20), 4), "ema50": _r(ema(c4, 50), 4), "ema200": _r(ema(c4, 200), 4),
               "rsi14": _r(rsi(c4))},
        "funding_pct_per_hour": _r(t["funding_rate"] * 100, 5),
        "funding_apr_pct": _r(t["funding_rate"] * 24 * 365 * 100, 1),
        "d1": {"ema20": _r(ema(cd, 20), 4), "ema50": _r(ema(cd, 50), 4), "rsi14": _r(rsi(cd)),
               "change_7d": _r(pct(price, cd[-8]) * 100) if len(cd) > 8 else None,
               "change_30d": _r(pct(price, cd[-31]) * 100) if len(cd) > 31 else None,
               "high_30d": max(k["h"] for k in d1[-30:]) if d1 else None,
               "low_30d": min(k["l"] for k in d1[-30:]) if d1 else None},
        "last_30_daily_closes": [_r(c, 6) for c in cd[-30:]],
        "last_24_hourly_closes": [_r(c, 4) for c in c1[-24:]],
        "last_6_4h_candles": [{"o": k["o"], "h": k["h"], "l": k["l"], "c": k["c"]} for k in h4[-6:]],
    }
    return snap, {"m15": m15, "h1": h1, "mark": t["mark"]}
