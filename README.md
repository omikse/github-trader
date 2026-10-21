# Claude Trader

An aggressive crypto futures trading bot where Claude makes the decisions and plain code enforces
the risk rules. It trades a **simulated futures account on live Kraken prices**, starting at
**1,000 PLN**, runs on **GitHub Actions** every 15 minutes, and publishes a dashboard on **GitHub Pages**.

Next to Claude run two benchmarks with the same starting money: a simple EMA 20/50 rule bot and
"just hold Bitcoin". If Claude can't beat a 20-line rule bot after costs, it isn't adding value.

No exchange account is needed. Market data comes from Kraken's free public API; the only key is the Claude API key.

## How it works

```
every 15 min (GitHub Actions)
  ├─ paper exchange replays every 1-minute candle since the last run:
  │    stop-losses, take-profits, funding every 8h, liquidation
  ├─ halts: -15% in a day → close all, pause until tomorrow
  │         -50% from peak → close all, stop for good
  ├─ market data for BTC, ETH, SOL, XRP, DOGE: 15m/1h/4h candles, EMAs, RSI, ATR
  ├─ wake Claude if: an hour passed, a 15-min move ≥ 2.5%, or a position closed
  │    └─ Claude answers in a fixed format: open / close / move stop, long or short, with reasons
  ├─ risk guard checks every action (code, not AI):
  │    - every new position has a stop 0.3–12% away, or it is rejected
  │    - size comes from risk: max 5% of equity lost if the stop is hit (default 3%)
  │    - total position size ≤ 10× equity, max 3 positions, one per coin
  │    - stops can only be tightened, never widened
  ├─ orders fill at the live Kraken bid/ask plus slippage and a 0.055% fee
  ├─ update the rule bot and the hold-Bitcoin benchmark
  └─ commit the journal and dashboard data to git (timestamped before outcomes are known)
```

### How realistic the paper exchange is

- **Fills:** live best bid/ask from Kraken at the moment of the order, plus 0.03% slippage and a 0.055% taker fee.
- **Stops and targets:** checked against every 1-minute candle between runs, so a stop that would have
  fired at 3:07 fires at 3:07. A candle that gaps past the stop fills at its open. If stop and target sit
  in the same minute, the stop is assumed to hit first.
- **Funding:** 0.01% of position size every 8 hours; longs pay, shorts receive.
- **Liquidation:** cross margin. If equity at the worst price of any minute falls to 0.5% of total
  position size, everything is closed at that price.
- **Not simulated:** order-book depth (irrelevant at this size) and variable funding rates.

Each Claude call is a fresh model with no memory. The bot sends it its own journal of earlier
decisions and closed trades every time, so it can learn from what it did.

## Setup

1. Add the repository secret `ANTHROPIC_API_KEY` (Settings → Secrets and variables → Actions).
   API usage is billed separately from a Claude subscription; prepaid credit is the safest limit.
   The bot also caps itself at 40 Claude calls per day (`MAX_CALLS_PER_DAY`).
2. Settings → Pages: source "Deploy from a branch", branch `main`, folder `/docs`.
3. Actions tab → **Trading bot** → Run workflow. After that it runs every 15 minutes by itself.

To stop: Actions → Trading bot → "…" → Disable workflow. On `END_AT` (21 Nov 2026, 21:00 UTC) the bot
closes everything and stops trading. To restart from 1,000 PLN, delete `docs/data/state.json`,
`docs/data/exchange.json`, `docs/data/equity.csv` and `docs/data/decisions.jsonl`.

## Settings

Everything is in `bot/config.py` and can be overridden with environment variables in the workflow.

| Setting | Default | Meaning |
|---|---|---|
| `SYMBOLS` | BTC, ETH, SOL, XRP, DOGE | coins Claude may trade (`bot/paper.py` maps them to Kraken pairs) |
| `CLAUDE_MODEL` | claude-opus-5-5 | model used for decisions |
| `BRAIN_EVERY_MIN` | 60 | routine decision interval |
| `EVENT_MOVE_PCT` | 0.025 | a 15-minute move that wakes Claude early |
| `DEFAULT_RISK` / `MAX_RISK_PER_TRADE` | 3% / 5% | equity lost if a stop is hit |
| `MAX_LEVERAGE` | 10 | total position size vs equity |
| `DAILY_LOSS_LIMIT` | 15% | pause for the rest of the UTC day |
| `KILL_DRAWDOWN` | 50% | end the experiment |
| `END_AT` | 2026-11-21T21:00:00Z | close all and stop |

## Files

- `bot/run.py` – one run of the bot
- `bot/brain.py` – the Claude call and its instructions
- `bot/guard.py` – risk rules
- `bot/paper.py` – Kraken market data and the simulated futures exchange
- `bot/market.py` – indicators and the market snapshot sent to Claude
- `bot/control.py` – rule-bot and hold-Bitcoin benchmarks
- `docs/` – dashboard; `docs/data/` – journal (`decisions.jsonl`), equity history, account state
- `tests/test_bot.py` – offline tests with a fake price feed (`python tests/test_bot.py`)

## Honest limits

- One month is short. Luck can decide the result, so judge drawdown and the benchmarks too, not only profit.
- Claude has seen historical prices in training, so only these live, forward results count; there is no backtest.
- Simulation for testing, not financial advice.
