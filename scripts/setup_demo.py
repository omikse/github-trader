"""One-time setup for the Bybit demo account. Run it from GitHub Actions ("Setup demo account" workflow).

1. Checks that the API key works on the demo domain.
2. Shrinks the demo balance to the simulated starting capital (1,000 PLN in USDT), so margin and
   liquidation behave like a small real account. Other demo coins are removed.
3. Sets leverage on every traded symbol.
"""
import os
import sys

import requests

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from bot import config  # noqa: E402
from bot.bybit import Bybit, BybitError  # noqa: E402


def main():
    key, secret = os.getenv("BYBIT_API_KEY"), os.getenv("BYBIT_API_SECRET")
    if not key or not secret:
        sys.exit("Set BYBIT_API_KEY and BYBIT_API_SECRET first.")
    c = Bybit(key, secret, config.BYBIT_BASE)

    try:
        w = c.wallet()
    except BybitError as e:
        sys.exit(f"API key check failed: {e}\nMake sure the key was created in DEMO trading mode.")
    print(f"Key works. Demo equity now: {w['equity']:.2f} USD, coins: {w['coins']}")

    if c.positions():
        sys.exit("Close all demo positions first, then run setup again.")

    rate = float(requests.get("https://api.nbp.pl/api/exchangerates/rates/a/usd/?format=json",
                              timeout=10).json()["rates"][0]["mid"])
    target = round(config.START_PLN / rate, 2)
    print(f"Target balance: {config.START_PLN:.0f} PLN = {target} USDT (NBP rate {rate})")

    for coin, bal in w["coins"].items():
        if coin == "USDT" or bal <= 0:
            continue
        try:
            c.demo_adjust(coin, bal, add=False)
            print(f"Removed {bal} {coin}")
        except BybitError as e:
            print(f"Could not remove {coin}: {e}")

    usdt = w["coins"].get("USDT", 0)
    try:
        if usdt > target:
            c.demo_adjust("USDT", round(usdt - target, 2), add=False)
        elif usdt < target:
            c.demo_adjust("USDT", round(target - usdt, 2), add=True)
    except BybitError as e:
        print(f"Balance adjustment failed: {e}\nThe bot still works: it tracks its own 1,000 PLN equity, "
              "but liquidation prices on the exchange will be unrealistically far away.")

    for sym in config.SYMBOLS:
        try:
            c.set_leverage(sym, config.MAX_LEVERAGE)
            print(f"{sym}: leverage set to {config.MAX_LEVERAGE:.0f}x")
        except BybitError as e:
            print(f"{sym}: could not set leverage: {e}")

    print(f"Done. Demo equity now: {c.wallet()['equity']:.2f} USD")


if __name__ == "__main__":
    main()
