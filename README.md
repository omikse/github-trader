# Claude Trader

An aggressive crypto trading bot where Claude makes the decisions and plain code enforces the risk rules.
It trades a **Bybit demo account** (real market prices, play money) sized to **1,000 PLN**, runs on
**GitHub Actions** every 15 minutes, and publishes a live dashboard on **GitHub Pages**.

Next to Claude run two benchmarks with the same starting money: a simple EMA 20/50 rule bot and
"just hold Bitcoin". If Claude can't beat a 20-line rule bot after costs, it isn't adding value.

## How it works

```
every 15 min (GitHub Actions)
  ├─ read balance, positions, trades closed since last run          (Bybit demo API)
  ├─ halts: -15% in a day → close all, pause until tomorrow
  │         -50% from peak → close all, stop for good
  ├─ market data for BTC, ETH, SOL: 15m/1h/4h candles, EMAs, RSI, ATR, funding
  ├─ wake Claude if: an hour passed, a 15-min move ≥ 2.5%, or a position closed
  │    └─ Claude answers in a fixed format: open / close / move stop, with reasons
  ├─ risk guard checks every action (code, not AI):
  │    - every new position has a stop 0.3–12% away, or it is rejected
  │    - size comes from risk: max 5% of equity lost if the stop is hit (default 3%)
  │    - total position size ≤ 10× equity, max 3 positions, one per coin
  │    - stops can only be tightened, never widened
  ├─ orders go to Bybit with the stop-loss and take-profit attached,
  │  so they fire on the exchange 24/7, even between runs
  ├─ update the rule bot and the hold-Bitcoin benchmark
  └─ commit the journal and dashboard data to git (timestamped before outcomes are known)
```

Each Claude call is a fresh model with no memory. The bot sends it its own journal of earlier
decisions and closed trades every time, so it can learn from what it did.

## Setup (about 20 minutes)

### 1. Bybit demo account and API key
1. Sign up at bybit.com. Check first that Bybit is available to you in Poland.
2. Switch to **Demo Trading** (from the account menu).
3. While in demo mode, open **API** and create a system-generated API key with read-write
   permission for **contract / unified trading** (orders and positions). Don't restrict it to an IP
   address, because GitHub's servers change address. It's a demo key, so it can't touch real money.
4. Copy the key and secret.

### 2. Claude API key
1. In the Claude Console (console.anthropic.com), create an API key.
2. Set a monthly spending limit there. API usage is billed separately from a Claude subscription.
   The bot also caps itself at 40 Claude calls per day (`MAX_CALLS_PER_DAY`).

### 3. GitHub repository
1. Create a new **public** repository (public repos get free unlimited Actions minutes and free Pages;
   your keys stay private in secrets, only the trade journal is public).
2. Upload everything from this folder, including the hidden `.github` folder.
3. **Settings → Secrets and variables → Actions → New repository secret**, add three secrets:
   `BYBIT_API_KEY`, `BYBIT_API_SECRET`, `ANTHROPIC_API_KEY`.
4. **Settings → Pages**: source "Deploy from a branch", branch `main`, folder `/docs`.

### 4. Start
1. **Actions** tab → enable workflows if asked.
2. Run **Setup demo account** (Run workflow). It checks the key, shrinks the demo balance to
   1,000 PLN in USDT and sets leverage. Read its log.
3. Run **Trading bot** once by hand. After that it runs every 15 minutes by itself.
   (GitHub sometimes delays scheduled runs by a few minutes; stops on the exchange are not affected.)
4. Open your Pages URL (Settings → Pages shows it) to watch the dashboard.

To stop: Actions → Trading bot → "…" → Disable workflow. On `END_AT` (21 Nov 2026, 21:00 UTC) the bot
closes everything by itself and stops trading.

## Settings

Everything is in `bot/config.py` and can be overridden with environment variables in the workflow.

| Setting | Default | Meaning |
|---|---|---|
| `SYMBOLS` | BTCUSDT,ETHUSDT,SOLUSDT | coins Claude may trade |
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
- `bot/bybit.py` – exchange client (Bybit v5 API, demo domain)
- `bot/market.py` – market data and indicators
- `bot/control.py` – rule-bot and hold-Bitcoin benchmarks
- `docs/` – dashboard; `docs/data/` – journal (`decisions.jsonl`), equity history, state
- `tests/test_bot.py` – offline tests with a fake exchange (`python tests/test_bot.py`)

## Honest limits

- Demo fills use real prices, but a demo order can't move a real order book. At this size that hardly matters.
- One month is short. Luck can decide the result, so judge drawdown and the benchmarks too, not only profit.
- Claude has seen historical prices in training, so only these live, forward results count; there is no backtest.
- Simulation for testing, not financial advice.
