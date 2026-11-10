# Notebook (updated 2026-11-10T12:54Z)

## Big picture
- 12:54Z 10 Nov (input fresh 12:45Z): BTC 74,115, short +3.39. 08-12Z 4h closed 74,313 (h 74,792, l 74,020): 4th straight lower high (75,474 -> 75,323 -> 74,889 -> 74,792). h1 below ema20 74.59k/ema50 74.90k, h4 ema20 75.13k, h4 RSI 38, d1 RSI 35, d1 ema20 77.7k. Funding +8% APR. Bear regime, grinding toward 30d low 73,444.
- Alts weaker: ETH 2,086 (30d low 2,071), SOL 84.65 (30d low 84.12, d1 RSI 25), XRP 1.076 (30d low 1.0737, d1 RSI 25), DOT at 30d low. Very oversold: bounce risk for fresh alt shorts. PEPE outlier strong (d1 RSI 63).
- Gold PAXG 4,063: lost 4,100 (4h close 4,058). h4 RSI 49. Gold long idea off for now.
- EUR 1.1213, pulled back from 1.1275 30d high; funding +74% APR now (longs pay).
- BTC levels: res 75.3-75.5k, 76.3k, 76.6k; sup 73.6k, 73.4k, 72.5k.
- Mind-changers: BTC 4h close > 76,000 = exit short; > 78.6k = bear plan off.
- No news edge (search 08:51Z found nothing new).

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21. Equity 232.14 USD (910 PLN, -9.7%; peak 265.7). Closed 8W/22L. ~11 days left: fewer, cleaner trades, each >=2R, risk 1.5-2%.
- Trade WITH confirmed 4h-close breaks, on retests not chases. No stop-entry break orders. Stops behind 4h structure.
- Trail behind completed 4h highs/lows; pyramid only from breakeven (if BTC short works, add on next lower-high retest).
- Carry only if funding > 60% APR sustained 3+ sessions; size <= 25%.

## Active plans
- BTC SHORT open (filled 00:08Z 10 Nov @75,277, ~0.0029 BTC). Stop 76,400 -> 75,700 -> 75,500 -> 75,350 -> 74,900 (12:54Z; the 10:58Z 75,000 move never executed, engine stale). 74,900 sits above the last two 4h highs 74,889/74,792 and h1 ema50 74.90k; locks ~+1.1 USD. TP 72,600. Thesis: confirmed 4h breakdown of 74.8k base, retest rejected under h4 ema20, lower highs each 4h. Management: once < 73,400 stop to 74,800; then trail above completed 4h highs. Pyramid only on a lower-high retest now that stop ~ breakeven. Exit on 4h close > 75,400. Time limit: if still 73.6-74.8k by 20:00Z 10 Nov, tighten stop to just above latest completed 4h high.
- BONK CARRY (opened 08:51Z 10 Nov, 20% equity ~46 USD). Funding 159/156/178/208/165/182/155% APR; ~0.2 USD/day, break-even ~1.3 days. Close if funding < 40% APR for 2 sessions or turns negative, or capital needed for a better trade. Hold to ~20 Nov otherwise; close before 21 Nov end.

## Watchlist
- XRP: weakest major but d1 RSI 27 oversold; short only a retest of 1.14-1.15 rejecting (stop > 1.18). Don't stack with BTC short (same bet).
- ETH: short retest 2,190-2,200 only if BTC short closed.
- Long reversal only after BTC 4h close > 78.6k.
- PAXG: lost 4,100; long only after a 4h close back > 4,110 and hold; else ignore. 6 Nov loss: gold failed during crypto dump.
- EUR: long only on 4h close > 1.1275; funding now +74% APR (costly for longs) -> skip unless it flips back.
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
- 2026-11-10T12:54Z | eq 232.50 (input fresh) | BTC short +3.39; stop 75.35k -> 74.9k (10:58Z move was never executed). BONK carry 155%.
- 2026-11-10T10:58Z | eq 232.14 (input 09:25Z, engine stalled) | BTC short +3.07; stop 75.35k -> 75.0k. BONK carry holding (182%). If decision dropped by 45-min rule, re-send stop move.
- 2026-11-10T08:51Z | eq 231.59 | BTC short +2.39; stop 75.5k -> 75.35k after new lower-high 4h. Opened BONK carry 20% (funding 165%).
- 2026-11-10T06:53Z | eq 231.22 | BTC short +2.03; stop 75.7k -> 75.5k. PAXG lost 4.1k on close, no long.
- 2026-11-10T04:51Z | eq 231.12 | BTC short +1.95; stop 76.4k -> 75.7k after lower-high 4h close. BONK carry skipped.
- 2026-11-10T02:52Z | eq 230.74 | BTC short +1.58, holding per plan. No new action.
- 2026-11-10T00:51Z | eq 230.07 | BTC short filled 75,277 (+0.91). Holding.
- 2026-11-09T22:53Z | eq 229.28 | Re-sent BTC short order 75.3k/76.4k/72.6k, 1.5%, 24h (earlier ones dropped by 45-min rule).
- 2026-11-09T20:52Z | eq 229.27 (engine stalled) | Re-sent BTC short order (dropped).
- 2026-11-09T18:51Z | eq 229.27 (stale) | BTC broke 74.79k base on 4h closes. Placed BTC short order 75.3k (dropped).
