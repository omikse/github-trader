"""Minimal Bybit v5 REST client (linear USDT perpetuals, unified account).

Talks to the demo-trading domain by default. Signing follows Bybit's v5 HMAC scheme:
sign = HMAC_SHA256(secret, timestamp + api_key + recv_window + payload), where payload is
the query string for GET and the raw JSON body for POST.
"""
import hashlib
import hmac
import json
import time

import requests


class BybitError(Exception):
    def __init__(self, path, code, msg):
        super().__init__(f"{path}: retCode {code} {msg}")
        self.code = code


class Bybit:
    def __init__(self, api_key, api_secret, base_url, recv_window="10000"):
        self.key = api_key or ""
        self.secret = api_secret or ""
        self.base = base_url.rstrip("/")
        self.recv = recv_window
        self.http = requests.Session()
        self._instruments = {}

    # -- transport ----------------------------------------------------------------
    def sign(self, ts, payload):
        msg = f"{ts}{self.key}{self.recv}{payload}"
        return hmac.new(self.secret.encode(), msg.encode(), hashlib.sha256).hexdigest()

    def _request(self, method, path, params=None, auth=False, ok_codes=(0,)):
        params = params or {}
        url = self.base + path
        body = None
        if method == "GET":
            payload = "&".join(f"{k}={v}" for k, v in params.items())
            if payload:
                url = f"{url}?{payload}"
        else:
            body = json.dumps(params, separators=(",", ":"))
            payload = body
        last_err = None
        for attempt in range(3):
            headers = {"Content-Type": "application/json"}
            if auth:
                ts = str(int(time.time() * 1000))
                headers.update({
                    "X-BAPI-API-KEY": self.key,
                    "X-BAPI-TIMESTAMP": ts,
                    "X-BAPI-RECV-WINDOW": self.recv,
                    "X-BAPI-SIGN": self.sign(ts, payload),
                })
            try:
                r = self.http.request(method, url, headers=headers, data=body, timeout=15)
                if r.status_code >= 500:
                    raise requests.HTTPError(f"HTTP {r.status_code}")
                data = r.json()
            except (requests.RequestException, ValueError) as e:
                last_err = e
                time.sleep(1.5 * (attempt + 1))
                continue
            if data.get("retCode") not in ok_codes:
                raise BybitError(path, data.get("retCode"), data.get("retMsg"))
            return data.get("result") or {}
        raise BybitError(path, -1, f"network error after retries: {last_err}")

    # -- market data (public) -------------------------------------------------------
    def klines(self, symbol, interval, limit=200):
        """Oldest-first list of dicts. interval: '15', '60', '240', 'D'."""
        res = self._request("GET", "/v5/market/kline",
                            {"category": "linear", "symbol": symbol, "interval": interval, "limit": limit})
        rows = [{"t": int(k[0]), "o": float(k[1]), "h": float(k[2]), "l": float(k[3]),
                 "c": float(k[4]), "v": float(k[5])} for k in res.get("list", [])]
        rows.sort(key=lambda k: k["t"])
        return rows

    def ticker(self, symbol):
        res = self._request("GET", "/v5/market/tickers", {"category": "linear", "symbol": symbol})
        t = res["list"][0]
        return {
            "last": float(t["lastPrice"]),
            "mark": float(t.get("markPrice") or t["lastPrice"]),
            "funding_rate": float(t.get("fundingRate") or 0),
            "open_interest": float(t.get("openInterest") or 0),
            "change_24h": float(t.get("price24hPcnt") or 0),
        }

    def instrument(self, symbol):
        if symbol not in self._instruments:
            res = self._request("GET", "/v5/market/instruments-info", {"category": "linear", "symbol": symbol})
            i = res["list"][0]
            self._instruments[symbol] = {
                "qty_step": float(i["lotSizeFilter"]["qtyStep"]),
                "min_qty": float(i["lotSizeFilter"]["minOrderQty"]),
                "min_notional": float(i["lotSizeFilter"].get("minNotionalValue") or 0),
                "tick": float(i["priceFilter"]["tickSize"]),
            }
        return self._instruments[symbol]

    # -- account (private) ----------------------------------------------------------
    def wallet(self):
        res = self._request("GET", "/v5/account/wallet-balance", {"accountType": "UNIFIED"}, auth=True)
        acct = res["list"][0]
        coins = {c["coin"]: float(c.get("walletBalance") or 0) for c in acct.get("coin", [])}
        return {"equity": float(acct.get("totalEquity") or 0), "coins": coins}

    def positions(self):
        res = self._request("GET", "/v5/position/list", {"category": "linear", "settleCoin": "USDT"}, auth=True)
        out = []
        for p in res.get("list", []):
            size = float(p.get("size") or 0)
            if size <= 0:
                continue
            out.append({
                "symbol": p["symbol"],
                "side": "long" if p["side"] == "Buy" else "short",
                "size": size,
                "entry": float(p.get("avgPrice") or 0),
                "mark": float(p.get("markPrice") or 0),
                "upnl": float(p.get("unrealisedPnl") or 0),
                "stop": float(p.get("stopLoss") or 0) or None,
                "tp": float(p.get("takeProfit") or 0) or None,
                "liq": float(p.get("liqPrice") or 0) or None,
                "leverage": float(p.get("leverage") or 0),
                "opened": int(p.get("createdTime") or 0),
            })
        return out

    def closed_pnl(self, start_ms):
        res = self._request("GET", "/v5/position/closed-pnl",
                            {"category": "linear", "startTime": int(start_ms), "limit": 100}, auth=True)
        out = []
        for c in res.get("list", []):
            out.append({
                "id": c.get("orderId"),
                "symbol": c["symbol"],
                # closed-pnl reports the CLOSING order's side, so Sell means a long was closed
                "side": "long" if c.get("side") == "Sell" else "short",
                "qty": float(c.get("closedSize") or c.get("qty") or 0),
                "entry": float(c.get("avgEntryPrice") or 0),
                "exit": float(c.get("avgExitPrice") or 0),
                "pnl": float(c.get("closedPnl") or 0),
                "time": int(c.get("updatedTime") or c.get("createdTime") or 0),
            })
        return out

    # -- trading (private) ----------------------------------------------------------
    def set_leverage(self, symbol, lev):
        lev = str(int(lev))
        # 110043 = leverage not modified, which is fine
        self._request("POST", "/v5/position/set-leverage",
                      {"category": "linear", "symbol": symbol, "buyLeverage": lev, "sellLeverage": lev},
                      auth=True, ok_codes=(0, 110043))

    def market_order(self, symbol, side, qty, stop=None, tp=None, reduce_only=False):
        params = {"category": "linear", "symbol": symbol, "side": "Buy" if side == "long" else "Sell",
                  "orderType": "Market", "qty": fmt_num(qty), "positionIdx": 0}
        if reduce_only:
            params["reduceOnly"] = True
        else:
            params["tpslMode"] = "Full"
            if stop:
                params["stopLoss"] = fmt_num(stop)
                params["slTriggerBy"] = "MarkPrice"
            if tp:
                params["takeProfit"] = fmt_num(tp)
                params["tpTriggerBy"] = "MarkPrice"
        return self._request("POST", "/v5/order/create", params, auth=True)

    def set_stops(self, symbol, stop=None, tp=None):
        params = {"category": "linear", "symbol": symbol, "tpslMode": "Full", "positionIdx": 0}
        if stop:
            params["stopLoss"] = fmt_num(stop)
            params["slTriggerBy"] = "MarkPrice"
        if tp:
            params["takeProfit"] = fmt_num(tp)
            params["tpTriggerBy"] = "MarkPrice"
        # 34040 = not modified
        return self._request("POST", "/v5/position/trading-stop", params, auth=True, ok_codes=(0, 34040))

    def close_position(self, pos):
        side = "short" if pos["side"] == "long" else "long"
        return self.market_order(pos["symbol"], side, pos["size"], reduce_only=True)

    def demo_adjust(self, coin, amount, add):
        """Add (add=True) or remove demo funds. Only works on the demo domain."""
        return self._request("POST", "/v5/account/demo-apply-money",
                             {"adjustType": 0 if add else 1,
                              "utaDemoApplyMoney": [{"coin": coin, "amountStr": fmt_num(amount)}]},
                             auth=True)


def fmt_num(x):
    """Plain decimal string without exponent or trailing zeros."""
    s = f"{x:.10f}".rstrip("0").rstrip(".")
    return s or "0"
