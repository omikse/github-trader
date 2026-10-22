# Claude Trader

An aggressive crypto futures trading bot where Claude makes the decisions and plain code enforces
the risk rules. It trades a **simulated futures account on live Kraken prices**, starting at
**1,000 PLN**, runs on **GitHub Actions** continuously (one tick per minute), and publishes a live dashboard on **GitHub Pages**.

Next to Claude run two benchmarks with the same starting money: a simple EMA 20/50 rule bot and
"just hold Bitcoin". If Claude can't beat a 20-line rule bot after costs, it isn't adding value.

No exchange account and no paid API are needed. Market data comes from Kraken's free public API, and the
brain is a **Claude scheduled task running on a Claude subscription**: every 2 hours it reads
`docs/data/brain_input.json`, decides, and pushes `docs/data/brain_decision.json`, following `BRAIN.md`.
The engine pulls the repo every minute and executes the decision within a minute or two.
(Set `BRAIN_MODE=api` and the secret `ANTHROPIC_API_KEY` to have the bot call the paid Claude API itself instead.)

## How it works

```
every minute (one GitHub Actions job runs ~5h40m, then the next takes over)
  ├─ paper exchange replays every 1-minute candle since the last run:
  │    stop-losses, take-profits, funding every 8h, liquidation
  ├─ halts: -15% in a day → close all, pause until tomorrow
  │         -50% from peak → close all, stop for good
  ├─ every 5 min: full scan of 17 markets (15m/1h/4h candles, EMAs, RSI, ATR)
  ├─ write brain_input.json (account, positions, orders, events, markets, journal)
  ├─ if Claude pushed a new brain_decision.json (≤ 45 min old): execute it
  │    actions: open / close / move stop / resting entry order / cancel order, long or short
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
- **Resting entry orders:** Claude can leave "buy if BTC breaks 86,500, stop 85,200" style orders.
  They are checked every minute and filled at the trigger (or at the open if the market gaps through it),
  so the bot catches moves between Claude's 2-hourly looks.
- **Liquidation:** cross margin. If equity at the worst price of any minute falls to 0.5% of total
  position size, everything is closed at that price.
- **Not simulated:** order-book depth (irrelevant at this size) and variable funding rates.

Each Claude session starts with no memory. It keeps plans going for days through `docs/data/brain_notebook.md`,
a notebook it reads first and rewrites every session (big picture, strategy, a plan for every position and order,
watchlist, lessons, session log). It also gets its last 12 decisions, every closed trade with the reason it was
opened and how it closed, and its track record. The notebook is shown on the dashboard.

## Setup

1. Settings → Pages: source "Deploy from a branch", branch `main`, folder `/docs`.
2. Actions tab → **Trading bot** → Run workflow. The 15-minute schedule keeps a next job queued, so the engine never stops.
3. Create the Claude scheduled task (every 2 hours) that clones this repo and follows `BRAIN.md`.

To stop: Actions → Trading bot → "…" → Disable workflow. On `END_AT` (21 Nov 2026, 21:00 UTC) the bot
closes everything and stops trading. To restart from 1,000 PLN, delete `docs/data/state.json`,
`docs/data/exchange.json`, `docs/data/equity.csv` and `docs/data/decisions.jsonl`.

## The dashboard

`docs/index.html` loads the engine's saved data every minute (the engine saves every 8 minutes) and, every
10 seconds, fetches live prices straight from Kraken (Binance as a fallback) to recompute the account,
open positions and benchmarks in the browser. The line under the title says how fresh both are.

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

- `bot/loop.py` – the always-on loop (minute ticks, full scans, saving to the dashboard)
- `bot/run.py` – one cycle of the bot
- `BRAIN.md` – what the scheduled Claude session does each time it wakes up
- `bot/brain.py` – the trader instructions (and the paid-API call, for `BRAIN_MODE=api`)
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
