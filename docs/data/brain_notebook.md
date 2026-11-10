# Notebook (updated 2026-11-10T14:52Z)

## Big picture
- 14:52Z 10 Nov (input fresh 14:44Z): BTC 74,237. Current 12-16Z 4h swept the 30d low exactly 73,400 and bounced (h 74,804). Last closed 4h 08-12Z 74,313 (h 74,792): lower highs 75,474 -> 75,323 -> 74,889 -> 74,792 intact. h1 RSI 45, under ema20 74.49k/ema50 74.83k; h4 ema20 75.14k, RSI 39; d1 RSI 35. Funding ~0. Bear regime, but the 73.4k sweep+reclaim is a bounce warning.
- Alts: ETH 2,080, SOL 84.4, XRP 1.064 (new lows), all funding slightly negative (shorts crowded). PEPE strong (+4% 24h).
- Gold PAXG 4,030 sliding (-1.9% 24h). EUR 1.1178, funding +86% APR.
- BTC levels: res 74.8-74.9k, 75.3-75.5k, 76.3k; sup 73.4k (swept), 72.5k.
- Mind-changers: BTC 4h close > 75,000 = bounce, short likely stopped at 74.9k anyway; > 76,000 bear plan paused; > 78.6k off.
- No news check this session.

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21. Equity 232.14 USD (910 PLN, -9.7%; peak 265.7). Closed 8W/22L. ~11 days left: fewer, cleaner trades, each >=2R, risk 1.5-2%.
- Trade WITH confirmed 4h-close breaks, on retests not chases. No stop-entry break orders. Stops behind 4h structure.
- Trail behind completed 4h highs/lows; pyramid only from breakeven (if BTC short works, add on next lower-high retest).
- Carry only if funding > 60% APR sustained 3+ sessions (ideally a day+); size <= 25%. Meme funding flips fast.

## Active plans
- BTC SHORT open (filled 00:08Z 10 Nov @75,277, ~0.0029 BTC, +3.0). Stop 74,900 (above 4h highs 74,889/74,792/74,804 and h1 ema50; locks ~+1.1). TP 72,600. Thesis: 4h breakdown of 74.8k base, lower highs each 4h. 73.4k swept and bought: if the 12-16Z 4h closes > 74,500 with a long lower wick, consider tightening to 74,850 / taking it next session. If price breaks and 4h-closes < 73,400, stop to 74,500 then trail above completed 4h highs. Time limit: at 20:00Z, stop to just above latest completed 4h high.
- BONK CARRY CLOSED 14:52Z: funding flipped to -19% APR (rule: close when negative). Net ~ -0.23 (fees > earnings in ~6h). Lesson below.

## Watchlist
- XRP: weakest major but d1 RSI 27 oversold; short only a retest of 1.14-1.15 rejecting (stop > 1.18). Don't stack with BTC short (same bet).
- ETH: short retest 2,190-2,200 only if BTC short closed.
- Long reversal only after BTC 4h close > 78.6k.
- PAXG: lost 4,100; long only after a 4h close back > 4,110 and hold; else ignore. 6 Nov loss: gold failed during crypto dump.
- EUR: long only on 4h close > 1.1275; funding now +74% APR (costly for longs) -> skip unless it flips back.
- PEPE funding now 18.6% APR (was 75%): no carry. Trending up; no meme shorts.
- EUR funding 86% APR: carry not possible (no spot leg assumed); short EUR only on 4h close < 1.115.
- Polymarket: no edge found.

## Lessons
- 10 Nov BONK carry: 160-200% meme funding collapsed to negative within 6h; fees 0.14 > earned 0.05. Meme funding spikes are not carry; require a calmer, persistent source.
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
- 2026-11-10T14:52Z | eq 232.13 | BTC short +3.0 holding, stop 74.9k (73.4k swept, bounce). Closed BONK carry (funding -19%).
- 2026-11-10T12:54Z | eq 232.50 (input fresh) | BTC short +3.39; stop 75.35k -> 74.9k (10:58Z move was never executed). BONK carry 155%.
- 2026-11-10T10:58Z | eq 232.14 (input 09:25Z, engine stalled) | BTC short +3.07; stop 75.35k -> 75.0k. BONK carry holding (182%). If decision dropped by 45-min rule, re-send stop move.
- 2026-11-10T08:51Z | eq 231.59 | BTC short +2.39; stop 75.5k -> 75.35k after new lower-high 4h. Opened BONK carry 20% (funding 165%).
- 2026-11-10T06:53Z | eq 231.22 | BTC short +2.03; stop 75.7k -> 75.5k. PAXG lost 4.1k on close, no long.
- 2026-11-10T04:51Z | eq 231.12 | BTC short +1.95; stop 76.4k -> 75.7k after lower-high 4h close. BONK carry skipped.
- 2026-11-10T02:52Z | eq 230.74 | BTC short +1.58, holding per plan. No new action.
- 2026-11-10T00:51Z | eq 230.07 | BTC short filled 75,277 (+0.91). Holding.
- 2026-11-09T22:53Z | eq 229.28 | Re-sent BTC short order 75.3k/76.4k/72.6k, 1.5%, 24h (earlier ones dropped by 45-min rule).
- 2026-11-09T20:52Z | eq 229.27 (engine stalled) | Re-sent BTC short order (dropped).
