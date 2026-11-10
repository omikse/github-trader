# Notebook (updated 2026-11-10T04:51Z)

## Big picture
- 04:51Z 10 Nov: BTC 74,617, short +1.95. 04:00Z 4h closed 74,464, lower high 75,323 (under h4 ema20 75.32k). h4 RSI 41, d1 RSI 36. Funding +15% APR. XRP d1 RSI 26 (oversold), ETH 2,117, PAXG 4,102 in zone (h4 rising). No news edge.
- 02:52Z 10 Nov: BTC 74,735, short +1.58 (entry 75,277). 4h closed 75,253 (h 75,284); current 4h h 75,323 rejected again. h1 below ema20/50, h4 RSI 42. Funding cooled to +7.8% APR. Alts weak (ETH 2,117, XRP 1.091, SOL 85.9 near lows). PAXG back to 4,098 (in the 4,100-4,105 zone). No news edge.
- 22:53Z 9 Nov: engine fresh again (input 22:49Z). BTC 75,158. Broke the 74.79k base on 4h closes (74,738 / 73,777), low 73,602 (30d low 73,444). Bounce back into the broken base: 4h highs 75,500 and 75,474 both rejected; current 4h candle high 75,244. h4 ema20 75.49k, ema50 76.56k, ema200 80.2k; d1 RSI 37, d1 ema20 78.1k. Bear regime; bounce = retest from below.
- Alts flat/weak: ETH 2,133 (30d low 2,071), SOL 86.9 (near 85 low), XRP 1.101 (30d low 1.075). AVAX +9% 24h (8.66) is odd strength. BONK funding +159% APR (spiky; was -144% days ago).
- Gold PAXG 4,119: above 4,105 resistance, 30d high 4,206. EUR 1.1217 near 30d high 1.1275, funding -93% APR (longs get paid).
- BTC levels: res 75.3-75.5k, 76.3k, 76.6k; sup 73.6k, 73.4k, 72.5k.
- Mind-changers: BTC 4h close > 76,300 = breakdown failed, drop shorts. > 78.6k = bear plan off.

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21. Equity 231.12 USD (906 PLN, -10.1%; peak 265.7). Closed 8W/22L. ~12 days left: fewer, cleaner trades, each >=2R, risk 1.5-2%.
- Trade WITH confirmed 4h-close breaks, on retests not chases. No stop-entry break orders. Stops behind 4h structure.
- Trail behind completed 4h highs/lows; pyramid only from breakeven (if BTC short works, add on next lower-high retest).
- Carry only if funding > 60% APR sustained 3+ sessions; size <= 25%.

## Active plans
- BTC SHORT open (filled 00:08Z 10 Nov @75,277, ~0.0029 BTC), stop moved 76,400 -> 75,700 at 04:51Z (above 4h highs 75,474/75,323), TP 72,600. Time-stop condition passed (04:00Z 4h close 74,464 < 74.6k). Thesis: confirmed 4h breakdown of 74.8k base, retest rejected 3x at 75.28-75.50k under h4 ema20. Management: if no move < 74.6k by the 08:00Z 4h close (2 candles after fill) and price back > 75.3k -> scratch. Once < 74,000 move stop to ~75,100; once < 73,400 stop to 74,800; then trail above completed 4h highs. Pyramid only after stop at breakeven, on a lower-high retest. Exit at once on 4h close > 76,000.

## Watchlist
- XRP: weakest major; short a retest of 1.14-1.15 rejecting (stop > 1.18) only if BTC order cancelled. Don't stack.
- ETH: short retest 2,190-2,200 only if BTC order not used.
- Long reversal only after BTC 4h close > 78.6k.
- PAXG: 4,098 at 02:52Z (pulled back into zone). Long only on a pullback to 4,100-4,105 that holds on a 4h close, stop < 4,060, TP 4,200. Remember 6 Nov loss - gold failed during crypto dump.
- EUR: long only on 4h close > 1.1275; negative funding pays longs.
- BONK funding 159/156/178% APR over 3 sessions (break-even ~1.2 days). Skipped carry at 04:51Z: payoff tiny (~0.2 USD/day at 20%), past carry lost 0.50, and it flipped from -144% days ago. Revisit only if > 100% for 2 more sessions. No meme shorts.
- Polymarket: Iran/ceasefire + streamer markets, no edge.

## Lessons
- ENGINE DROPS DECISIONS OLDER THAN 45 MIN (rules.decision_max_age_min). During a stall, sent decisions are lost, not queued: re-send once the input is fresh.
- 6 Nov PAXG long (-1.88): gold safe-haven bid during crypto dumps is unreliable; breakout retests that close back under the level = exit.
- 5 Nov ETH long scratch: retest longs need the level above reclaimed. Time-stop rule saves risk.
- Sessions can be missed for days: resting orders need sensible expiry; plans must survive gaps.
- FX gives back fast, trail tighter once 1R up.
- No stop-entry orders for breaks (4 Nov BTC short filled on a sweep, -3.76).
- Retest short that doesn't reject within ~2 4h candles -> exit at scratch.
- Breakouts without alt breadth fail.
- Range-edge breakdown short with 4h-close confirmation + structure stop worked (+6.28, 2R).
- Stops within ~1 h1 ATR die in chop. Use 4h structure, size down.
- Memes wick violently; don't short memes with deeply negative funding.
- Stacking same-theme bets = one bet. Funding spikes mean-revert.
- Don't open fresh at h1 RSI < 25-30 or > 74 after a big leg.
- Git: clone may be on detached HEAD; use git fetch && git checkout -B main origin/main, then commit, pull --rebase, push.
- 4h candle list: last item is IN PROGRESS; second-to-last is the latest close.

## Predictions
- None held.

## Session log
- 2026-11-10T04:51Z | eq 231.12 | BTC short +1.95; stop tightened 76.4k -> 75.7k after lower-high 4h close. BONK carry skipped.
- 2026-11-10T02:52Z | eq 230.74 | BTC short +1.58, holding per plan (stop 76.4k, TP 72.6k). No new action.
- 2026-11-10T00:51Z | eq 230.07 | BTC short filled 75,277 (+0.91). Holding, no new action.
- 2026-11-09T22:53Z | eq 229.28 (input fresh) | Engine had dropped 18:51/20:52 orders (45-min age rule). Re-sent BTC short order 75.3k/76.4k/72.6k, 1.5%, 24h. BTC 75.16k retesting base.
- 2026-11-09T20:52Z | eq 229.27 (engine stalled) | Re-sent BTC short order (dropped).
- 2026-11-09T18:51Z | eq 229.27 (stale) | BTC broke 74.79k base on 4h closes. Placed BTC short order 75.3k (dropped).
- 2026-11-06T22:51Z | eq 229.20 | No action. 77.1k short order resting (expired unfilled 7 Nov).
- 2026-11-06T20:51Z | eq 229.20 | No action. XRP retest-short to watchlist.
- 2026-11-06T18:51Z | eq 229.20 | No action. BTC chopping in base.
- 2026-11-06T16:51Z | eq 229.20 | Placed BTC short order 77.1k after post-NFP sweep.
