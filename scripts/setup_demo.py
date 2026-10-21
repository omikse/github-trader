"""One-time setup and diagnosis for the Bybit demo account. Run it from GitHub Actions ("Setup demo account").

1. Tests whether Bybit answers GitHub's servers at all (Bybit blocks some countries).
2. Checks that the API key works on the demo domain and what it can do.
3. Shrinks the demo balance to the simulated starting capital (1,000 PLN in USDT).
4. Sets leverage on every traded symbol (futures only).

Findings are printed as GitHub annotations (::notice:: / ::error::) so they show on the run's summary page.
"""
import os
import sys

import requests

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from bot import config  # noqa: E402
from bot.bybit import Bybit, BybitError  # noqa: E402


def note(msg):
    print(f"::notice::{msg}", flush=True)


def err(msg):
    print(f"::error::{msg}", flush=True)


def probe(url):
    try:
        r = requests.get(url, timeout=15)
        body = r.text[:160].replace("\n", " ")
        return f"HTTP {r.status_code}: {body}"
    except requests.RequestException as e:
        return f"no connection: {e.__class__.__name__}"


def main():
    try:
        ip = requests.get("https://api.ipify.org", timeout=10).text
    except requests.RequestException:
        ip = "unknown"
    note(f"Runner IP {ip}")
    note("Bybit demo public API -> " + probe(f"{config.BYBIT_BASE}/v5/market/time"))
    note("Bybit main public API -> " + probe("https://api.bybit.com/v5/market/time"))
    note("Kraken public API -> " + probe("https://api.kraken.com/0/public/Time"))

    key, secret = os.getenv("BYBIT_API_KEY"), os.getenv("BYBIT_API_SECRET")
    if not key or not secret:
        err("BYBIT_API_KEY / BYBIT_API_SECRET secrets are missing.")
        sys.exit(1)
    c = Bybit(key, secret, config.BYBIT_BASE)

    try:
        w = c.wallet()
    except BybitError as e:
        err(f"Demo API key check failed: {e}. If this says 'API key is invalid', the key was probably "
            "created outside Demo Trading mode.")
        sys.exit(1)
    except Exception as e:
        err(f"Could not reach Bybit with the key: {e}")
        sys.exit(1)
    note(f"Key works on the demo domain. Equity {w['equity']:.2f} USD, coins {w['coins']}")

    try:
        c.positions()
        note("Futures (linear) access: OK")
        futures = True
    except BybitError as e:
        err(f"Futures (linear) access refused: {e}")
        futures = False

    rate = float(requests.get("https://api.nbp.pl/api/exchangerates/rates/a/usd/?format=json",
                              timeout=10).json()["rates"][0]["mid"])
    target = round(config.START_PLN / rate, 2)
    note(f"Target balance: {config.START_PLN:.0f} PLN = {target} USDT (NBP rate {rate})")

    for coin, bal in w["coins"].items():
        if coin == "USDT" or bal <= 0:
            continue
        try:
            c.demo_adjust(coin, bal, add=False)
            note(f"Removed {bal} {coin}")
        except BybitError as e:
            err(f"Could not remove {coin}: {e}")

    usdt = w["coins"].get("USDT", 0)
    try:
        if usdt > target:
            c.demo_adjust("USDT", round(usdt - target, 2), add=False)
        elif usdt < target:
            c.demo_adjust("USDT", round(target - usdt, 2), add=True)
        note(f"Balance adjusted. Demo equity now {c.wallet()['equity']:.2f} USD")
    except BybitError as e:
        err(f"Balance adjustment failed: {e}")

    if futures:
        for sym in config.SYMBOLS:
            try:
                c.set_leverage(sym, config.MAX_LEVERAGE)
                note(f"{sym}: leverage {config.MAX_LEVERAGE:.0f}x")
            except BybitError as e:
                err(f"{sym}: could not set leverage: {e}")


if __name__ == "__main__":
    main()
