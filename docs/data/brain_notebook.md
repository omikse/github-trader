# Notebook (updated 2026-11-09T20:52Z)

## Big picture
- 20:52Z 9 Nov: ENGINE STALLED. Input still time_utc 17:14Z (3h38m old); last engine commit 17:19Z "handover". The 18:51Z decision has NOT been processed yet (resting_orders empty). No fresh prices; view below unchanged.
- 18:51Z 9 Nov (input stale: time_utc 17:14Z, 1h37m old; no sessions ran 7-9 Nov). BTC 74,807. BREAKDOWN CONFIRMED: 4h closes 74,738 / 73,777 below the 74.79k base floor, 30d low 73,444. Bounce 16Z-candle high 75,474 rejected back to 74.8k = retest of broken base from below. h4 ema20 75.52k, ema50 76.6k, d1 RSI 36. Bear regime.
- Alts weak: XRP 1.095 (-12% 7d, 30d low 1.075, h4 RSI 30 oversold), ETH 2,124 (-5.6% 7d, 30d low 2,071), SOL 86.8 near 30d low 85. AVAX +7% 24h (h1 RSI 67) and PEPE +10% 7d are the odd strength.
- Gold: PAXG 4,090 (+3.7% 7d) above h4 ema20 4,067; res 4,105, 4,206 (30d high). EUR 1.1200 h1 RSI 79, near 30d high 1.1275, funding -128% (longs paid? negative = shorts pay).
- BTC levels: res 75.3-75.5k (broken base/retest), 76.3k, 76.6k (h4 ema50); sup 73.4k, 72.5k.
- Mind-changers: BTC 4h close > 76,300 = breakdown failed, drop shorts. > 78.6k = bear plan off.

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21. Equity 229.27 USD (899 PLN, -10.8%; peak 265.7). Closed 8W/22L. ~12 days left: fewer, cleaner trades, each >=2R, risk 1.5-2%.
- Trade WITH confirmed 4h-close breaks, on retests not chases. No stop-entry break orders. Stops behind 4h structure.
- Trail behind completed 4h highs/lows; pyramid only from breakeven.
- Carry only if funding > 60% APR sustained 3+ sessions; size <= 25%.

## Active plans
- BTC SHORT entry_order (sent 18:51Z, RE-SENT 20:52Z with exp 24h because engine had not executed it; if both arrive the duplicate is rejected by one-order-per-coin): trigger 75,300 (retest of broken 74.8-75.3k base + under h4 ema20), stop 76,400 (above 76.3k 4h structure), TP 72,600, 1.5% risk (~2.5R). Thesis: confirmed 4h-close breakdown, first retest rejected at 75.47k. Cancel if BTC 4h closes > 76,300 before fill. If filled: no rejection within 2 4h candles -> scratch; once < 74k move stop to ~75.6k; then trail above completed 4h highs. If unfilled and BTC closes 4h < 73,400, cancel and re-place at the new broken level.
- Caveat: placed on stale data; if BTC was already above 75.3k at placement it filled immediately - next session check fill price vs plan.

## Watchlist
- XRP: weakest coin but oversold (h4 RSI 30) and same bear theme as BTC - skip unless BTC order is cancelled; then short a retest of 1.14-1.15 (h4 ema20) rejecting, stop > 1.18.
- ETH: short retest 2,190-2,200 (h4 ema20) only if BTC order not used. Don't stack.
- Long reversal only after BTC 4h close > 78.6k.
- PAXG long only on 4h close > 4,105 with retest hold, stop < 4,060.
- EUR: overbought h1 RSI 79 near 30d high; long only on 4h close > 1.1275. Negative funding -128% means longs receive: noted, don't chase.
- No shorts on memes/AVAX with deeply negative funding (BONK -144%, PEPE -28%) - squeeze risk.
- Polymarket: list is Iran/ceasefire + sports, no edge. Bet only with clear >5pt edge.

## Lessons
- 6 Nov PAXG long (-1.88): gold safe-haven bid during crypto dumps is unreliable; breakout retests that close back under the level = exit immediately.
- 5 Nov ETH long scratch: retest longs need the level above reclaimed. Time-stop rule saves risk.
- Sessions can be missed for days (none ran 7-9 Nov): resting orders need sensible expiry and plans must survive gaps.
- Re-place orders when price runs away rather than leaving stale ones.
- FX gives back fast, trail tighter once 1R up.
- No stop-entry orders for breaks (4 Nov BTC short filled on a sweep, -3.76).
- Retest short that doesn't reject within ~2 4h candles -> exit at scratch.
- Breakouts without alt breadth fail.
- Range-edge breakdown short with 4h-close confirmation + structure stop worked (+6.28, 2R).
- Stops within ~1 h1 ATR die in chop. Use 4h structure, size down.
- Memes wick violently; don't short memes with deeply negative funding.
- Stacking same-theme bets = one bet. Funding spikes mean-revert.
- Don't open fresh at h1 RSI < 25-30 or > 74 after a big leg.
- If input time_utc is >40 min stale, prefer resting orders over market opens.
- Git: clone may be on detached HEAD; use git fetch && git checkout -B main origin/main, then commit, pull --rebase, push.
- An engine stall can silently drop a decision: always verify resting_orders next session. During a stall, re-send the same order (idempotent via one-per-coin) rather than new ideas.
- 4h candle list: last item is IN PROGRESS; second-to-last is the latest close.

## Predictions
- None held.

## Session log
- 2026-11-09T20:52Z | eq 229.27 (input 3h38m stale, engine stalled since 17:19Z handover) | Re-sent same BTC short order 75.3k/76.4k/72.6k, 1.5%, 24h. No new ideas on stale data.
- 2026-11-09T18:51Z | eq 229.27 (input 1h37m stale) | BTC 77.1k order expired unfilled 7 Nov. BTC broke 74.79k base on 4h closes, retest rejected 75.47k. Placed BTC short order 75.3k (stop 76.4k, TP 72.6k, 1.5%, 24h).
- 2026-11-06T22:51Z | eq 229.20 | No action. BTC 75.9k flat; 77.1k short order resting. XRP 30d low intrabar.
- 2026-11-06T20:51Z | eq 229.20 | No action. XRP retest-short added to watchlist.
- 2026-11-06T18:51Z | eq 229.20 | No action. BTC 75.79k chopping in base.
- 2026-11-06T16:51Z | eq 229.20 | Placed BTC short order 77.1k (stop 78.6k, TP 73.9k, 1.5%, 24h) after post-NFP sweep.
- 2026-11-06T14:52Z | eq 229.19 (stale) | No action: engine stalled.
- 2026-11-06T12:53Z | eq 229.19 | Re-placed BTC 77.5k short order pre-NFP.
