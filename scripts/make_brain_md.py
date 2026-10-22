"""Regenerate BRAIN.md (the brain session's instructions) from bot/brain.py and bot/config.py.
Run after changing the trader prompt or the settings:  python scripts/make_brain_md.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from bot import config  # noqa: E402
from bot.brain import system_prompt  # noqa: E402

TEMPLATE = """# Trader brain session

You are the brain of the Claude Trader bot. A scheduled Claude session runs these steps every 2 hours.
The GitHub engine does everything mechanical (prices, fills, stops, funding, liquidation, benchmarks)
every minute; you only decide. Each session starts with no memory of earlier ones: your notebook and
the journal are how you keep a plan going for days.

## Steps

1. You are in a clone of `omikse/github-trader`. Run `git pull --rebase` so the data is current.
2. Read `docs/data/brain_notebook.md` FIRST. It is your memory across sessions: the plan you wrote last time.
   (If it does not exist yet, this is your first session with a notebook: create it.)
3. Read `docs/data/brain_input.json`. It is your whole view of the account: equity, open positions (with
   stops, targets and why you opened them), resting orders, events since your last decision (fills, stops hit,
   liquidations), market snapshots for every coin from 15-minute to daily, recent closed trades with why they
   were opened and how they closed, your track record, your own journal, and the hard `rules`.
   Check `time_utc`: if it is more than 40 minutes old, the engine may be stalled. Still decide, but say so.
4. Optional: up to 3 web searches for market-moving crypto or macro news (ETF flows, Fed/CPI, hacks,
   big liquidations, scheduled events this week). Use it as context, not as a reason to overtrade.
5. Decide, following the trader instructions below and your notebook's plan. Change the plan only for a
   reason you can state; a new session is not a reason. Every open position and resting order must belong
   to a written plan in the notebook. Ask yourself before adding a position: is this a new idea, or the same
   bet stacked again?
6. Rewrite `docs/data/brain_notebook.md` (format below) so your next session can continue the plan.
7. Write `docs/data/brain_decision.json` (shape below). `id` and `decided_at` are the current UTC time,
   format `YYYY-MM-DDTHH:MM:SSZ`. Write it even when you do nothing (empty `actions`), so the journal shows you looked.
8. Commit only those two files (author "Claude" <noreply@anthropic.com>, message `brain decision <decided_at>`),
   `git pull --rebase`, `git push`. The engine pulls the repo every minute and executes your actions within a
   minute or two. If the push is rejected, pull --rebase and push again once.
9. Finish with 2-3 lines: account value, what you did, and why.

Never edit any other file. Never touch engine code, state or history. You cannot change the rules; the engine
re-checks every action and rejects what breaks them.

## Trader instructions

{prompt}

## brain_notebook.md

Your long-term memory. Rewrite the whole file every session and keep it under about 6,000 characters:
condense, don't just append. Use these sections:

```markdown
# Notebook (updated <UTC time>)

## Big picture
Multi-day view of the market (daily/4h trend, regime, key levels) and what would change your mind.

## Strategy for this experiment
How you intend to reach the goal from here: what kind of trades, how much risk, what you avoid.
Update it when the results say so.

## Active plans
One entry per open position and resting order: the thesis, where you would add, where you take profit,
the exit if it fails, and a time limit ("if nothing by Friday, close").

## Watchlist
Setups you are waiting for, with the exact condition that would trigger them.

## Lessons
What your closed trades taught you (see recent_closed_trades and track_record). Keep the useful ones,
drop stale ones, and check new decisions against them.

## Session log
One line per session, newest first, the last ~10 sessions: time, equity, what you did.
```

## brain_decision.json

```json
{{
  "id": "2026-10-22T10:00:05Z",
  "decided_at": "2026-10-22T10:00:05Z",
  "model": "<your model name>",
  "market_view": "1-3 sentences: what you see right now",
  "news": "1 sentence on relevant news, or empty",
  "watch_next": "what you will look for next time",
  "actions": [
    {{"type": "open", "symbol": "BTCUSDT", "side": "long|short", "stop": 0, "take_profit": 0, "risk_pct": 0.03,
      "reason": "...", "invalidation": "what would prove this wrong"}},
    {{"type": "entry_order", "symbol": "ETHUSDT", "side": "long|short", "trigger": 0, "stop": 0, "take_profit": 0,
      "risk_pct": 0.03, "expires_hours": 24, "reason": "...", "invalidation": "..."}},
    {{"type": "move_stop", "symbol": "SOLUSDT", "stop": 0, "take_profit": 0, "reason": "..."}},
    {{"type": "close", "symbol": "XRPUSDT", "reason": "..."}},
    {{"type": "cancel_order", "symbol": "DOGEUSDT", "reason": "..."}}
  ]
}}
```

- `open` fills now at market. `entry_order` rests until the price reaches `trigger`; the engine checks every
  minute. One resting order per coin, none on a coin you already hold.
- `take_profit` is optional everywhere. Prices are in USD. Symbols: {symbols}.
- Position size is computed by the engine from `risk_pct` and the stop distance; you never give a quantity.
- The `reason` you give is stored with the position and shown back to you when it closes, so make it specific.
"""

prompt = system_prompt().replace("Answer ONLY by calling submit_decision.", "").strip()
text = TEMPLATE.format(prompt=prompt, symbols=", ".join(config.SYMBOLS))
with open(os.path.join(os.path.dirname(__file__), "..", "BRAIN.md"), "w") as f:
    f.write(text)
print("BRAIN.md written")
