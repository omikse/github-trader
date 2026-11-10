# Notebook (updated 2026-11-10T08:51Z)

## Big picture
- 08:51Z 10 Nov: BTC 74,454, short +2.39. 08:00Z 4h closed 74,748 (lower highs 75,474 -> 75,323 -> 74,889). h1 below ema20 74.75k/ema50 75.0k, h4 ema20 75.25k, h4 RSI 41, d1 RSI 36, d1 ema20 77.8k. Funding +14% APR. Bear regime; bounce = retest from below.
- Alts weak: ETH 2,111 (30d low 2,071, d1 RSI 33), SOL 85.6 (30d low 85.0, d1 RSI 26), XRP 1.085 (d1 RSI 26, h4 RSI 30, 30d low 1.075). Oversold: bounce risk for fresh shorts.
- Gold PAXG 4,103: 08:00Z 4h closed 4,099 (still hugging 4,100). h4 RSI 59, 30d high 4,206.
- EUR 1.1243 (30d high 1.1275), h4 RSI 77 (stretched), funding -50% APR (longs paid).
- BTC levels: res 75.3-75.5k, 76.3k, 76.6k; sup 73.6k, 73.4k, 72.5k.
- Mind-changers: BTC 4h close > 76,000 = exit short; > 78.6k = bear plan off.
- No news edge (search 08:51Z found nothing new).

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21. Equity 231.59 USD (908 PLN, -9.9%; peak 265.7). Closed 8W/22L. ~11 days left: fewer, cleaner trades, each >=2R, risk 1.5-2%.
- Trade WITH confirmed 4h-close breaks, on retests not chases. No stop-entry break orders. Stops behind 4h structure.
- Trail behind completed 4h highs/lows; pyramid only from breakeven (if BTC short works, add on next lower-high retest).
- Carry only if funding > 60% APR sustained 3+ sessions; size <= 25%.

## Active plans
- BTC SHORT open (filled 00:08Z 10 Nov @75,277, ~0.0029 BTC). Stop 76,400 -> 75,700 -> 75,500 -> 75,350 (08:51Z, above 4h lower highs 75,323/74,889, ~breakeven). TP 72,600. Thesis: confirmed 4h breakdown of 74.8k base, retest rejected under h4 ema20, lower highs each 4h. Management: once < 74,000 stop to ~75,000; once < 73,400 stop to 74,800; then trail above completed 4h highs. Pyramid only on a lower-high retest now that stop ~ breakeven. Exit on 4h close > 75,400. Time limit: if still 74.0-75.3k by 20:00Z 10 Nov, tighten stop to just above latest 4h high.
- BONK CARRY (opened 08:51Z 10 Nov, 20% equity ~46 USD). Funding 159/156/178/208/165% APR over 5 sessions; ~0.2 USD/day, break-even ~1.3 days. Close if funding < 40% APR for 2 sessions or turns negative, or capital needed for a better trade. Hold to ~20 Nov otherwise; close before 21 Nov end.

## Watchlist
- XRP: weakest major but d1 RSI 27 oversold; short only a retest of 1.14-1.15 rejecting (stop > 1.18). Don't stack with BTC short (same bet).
- ETH: short retest 2,190-2,200 only if BTC short closed.
- Long reversal only after BTC 4h close > 78.6k.
- PAXG: long only after a 4h close back > 4,105 then a hold of 4,100 on retest; stop < 4,060, TP 4,200. 6 Nov loss: gold failed during crypto dump.
- EUR: long only on 4h close > 1.1275; negative funding pays longs.
- PEPE funding 75% APR (h4 RSI 63, trending up): second carry candidate only if > 100% for 3 sessions. No meme shorts.
- Polymarket: no edge found.

## Lessons
- ENGINE DROPS DECISIONS OLDER THAN 45 MIN (rules.decision_max_age_min). During a stall, sent decisions are lost: re-send once input is fresh.
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
- 2026-11-10T08:51Z | eq 231.59 | BTC short +2.39; stop 75.5k -> 75.35k after new lower-high 4h. Opened BONK carry 20% (funding 165%).
- 2026-11-10T06:53Z | eq 231.22 | BTC short +2.03; stop 75.7k -> 75.5k. PAXG lost 4.1k on close, no long.
- 2026-11-10T04:51Z | eq 231.12 | BTC short +1.95; stop 76.4k -> 75.7k after lower-high 4h close. BONK carry skipped.
- 2026-11-10T02:52Z | eq 230.74 | BTC short +1.58, holding per plan. No new action.
- 2026-11-10T00:51Z | eq 230.07 | BTC short filled 75,277 (+0.91). Holding.
- 2026-11-09T22:53Z | eq 229.28 | Re-sent BTC short order 75.3k/76.4k/72.6k, 1.5%, 24h (earlier ones dropped by 45-min rule).
- 2026-11-09T20:52Z | eq 229.27 (engine stalled) | Re-sent BTC short order (dropped).
- 2026-11-09T18:51Z | eq 229.27 (stale) | BTC broke 74.79k base on 4h closes. Placed BTC short order 75.3k (dropped).
- 2026-11-06T22:51Z | eq 229.20 | No action. 77.1k short order resting (expired 7 Nov).
- 2026-11-06T20:51Z | eq 229.20 | No action. XRP retest-short to watchlist.
