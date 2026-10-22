"""One-off: fetch samples from the data sources the bot will use and save them for inspection."""
import json
import requests

out = {}


def get(name, url, params=None):
    try:
        r = requests.get(url, params=params, timeout=20)
        out[name] = {"status": r.status_code, "body": r.json() if "json" in r.headers.get("content-type", "") else r.text[:2000]}
    except Exception as e:
        out[name] = {"error": str(e)}


get("kraken_futures_tickers", "https://futures.kraken.com/derivatives/api/v3/tickers")
t = out["kraken_futures_tickers"].get("body") or {}
if isinstance(t, dict) and "tickers" in t:
    perps = [x for x in t["tickers"] if x.get("tag") == "perpetual"]
    out["kraken_futures_tickers"]["body"] = {"n_perpetuals": len(perps), "symbols": [p["symbol"] for p in perps][:400],
                                             "sample": [p for p in perps if p["symbol"] in ("PF_XBTUSD", "PF_ETHUSD", "PF_SOLUSD", "PF_PEPEUSD")]}
get("kraken_futures_funding_hist", "https://futures.kraken.com/derivatives/api/v4/historicalfundingrates", {"symbol": "PF_XBTUSD"})
h = out["kraken_futures_funding_hist"].get("body")
if isinstance(h, dict) and "rates" in h:
    h["rates"] = h["rates"][-6:]
get("gamma_markets", "https://gamma-api.polymarket.com/markets",
    {"closed": "false", "active": "true", "order": "volume24hr", "ascending": "false", "limit": 3})
get("gamma_resolved", "https://gamma-api.polymarket.com/markets", {"closed": "true", "limit": 2, "order": "endDate", "ascending": "false"})
g = out["gamma_markets"].get("body")
if isinstance(g, list) and g:
    tok = json.loads(g[0].get("clobTokenIds") or "[]")
    if tok:
        get("clob_book", "https://clob.polymarket.com/book", {"token_id": tok[0]})
        b = out["clob_book"].get("body")
        if isinstance(b, dict):
            b["bids"] = b.get("bids", [])[-3:]
            b["asks"] = b.get("asks", [])[-3:]
    get("gamma_by_id", f"https://gamma-api.polymarket.com/markets/{g[0]['id']}")
get("treasury_bills", "https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v2/accounting/od/avg_interest_rates",
    {"filter": "security_desc:eq:Treasury Bills", "sort": "-record_date", "page[size]": 2})
open("probe.json", "w").write(json.dumps(out, indent=1)[:900000])
print({k: v.get("status", v.get("error")) for k, v in out.items()})
