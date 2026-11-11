# Notebook (updated 2026-11-11T14:52Z)

## Big picture
- 14:52Z 11 Nov: ENGINE STALLED - input still 12:52Z (2h old), last bot commit 12:57Z "handover". No fresh prices; plan unchanged. Next session: check time_utc first; if fresh, re-evaluate resting order vs any 4h close > 75k.
- 12:53Z 11 Nov (input 12:47Z, fresh): BTC 73,966. 30d low 72,585. Chop 73.1-74.1k for ~22h; latest closed 4h c 73,921 (h 74,085), in-progress 12-16Z h 74,014. Under h1 ema50 74.14k, h4 ema20 74.48k, h4 ema50 75.69k, d1 ema20 77.3k. RSI h1 52 / h4 42 / d1 35. Bear trend intact, coiling under resistance where the resting short sits.
- Alts: ETH 2,055 (d1 RSI 30, h4 ema20 2,109), SOL 83.9 (d1 RSI 26), XRP 1.058 (d1 RSI 24) - oversold, no fresh shorts. AVAX cooled to 8.55 (+2.3%, h1 RSI 57) above h4 ema20 8.40. NEAR 3.755 +3.5% (funding -53%). PEPE -5.9%.
- Funding modest; BONK 140% (meme, ignore), EUR +81%, PAXG +48%, NEAR -42%.
- PAXG 4,029 drifting lower. EUR 1.1132 (h1 RSI 26 oversold, funding +99%) - at 1.112-1.113 support; no chase short here.
- BTC levels: res 74.0-74.1k, 74.5-74.8k, 75.75k; sup 73.1k, 72.6k, then ~71.5-72k.
- Mind-changers: BTC 4h close > 75,000 = bear plan weakening; > 76,000 bear plan off.
- News: nothing new ("trades heavily under 74.6k, risk mood wary"; worst-November narrative, ~$1.3B weekly outflows).

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21. Equity 232.42 USD (909 PLN, -9.6%; peak 265.7). Closed 9W/22L. ~10 days left: fewer, cleaner trades, each >=2R, risk 1.5-2%.
- Trade WITH the trend: shorts into resistance or on retests of confirmed 4h-close breaks. No stop-entry break orders. Stops behind 4h structure, not inside 1 h1 ATR (~490 on BTC).
- Trail behind completed 4h highs; pyramid only from breakeven.
- Carry only if funding > 60% APR sustained 3+ sessions on a non-meme; size <= 25%.

## Active plans
- BTC short ENTRY ORDER (placed 08:51Z 11 Nov, expires ~08:51Z 12 Nov): trigger 74,700 (h4 ema20 + 24h high 74.8k), stop 75,750 (above h4 ema50), TP 72,300, risk 1.5%. If filled: trail stop to ~150 above latest completed 4h high once >= 0.8% from price; on a new low < 72.5k move stop to ~73,900. Cancel if a 4h closes > 75,000 before fill (fill then is a fight against reclaim) or if BTC first breaks < 72.5k (plan changes to breakdown-retest).
- No positions open.

## Watchlist
- BTC breakdown: 4h close < 72,500 -> short the retest of 72.6-73.0k (rejection), stop above 73.6k, TP ~70.5k. Cancel the 74.7k resting order if this happens.
- Alts: no fresh shorts at d1 RSI < 30 (SOL, XRP, DOT oversold). ETH short only on a 2,100-2,115 rejection and only if no BTC short is open/resting (same bet).
- AVAX: relative-strength long only if BTC reclaims 74.8k with alt breadth; alone, breakouts without breadth fail. Do not chase at h1 RSI > 70. Pullback long idea: 8.45-8.50 (h1 ema20/ema50) holding + BTC not breaking down; would conflict with BTC short only loosely (different coin, but same market) - max 1.5% risk.
- Long reversal only after BTC 4h close > 74,800 with alt breadth.
- PAXG: long only after 4h close > 4,110. EUR: no longs (funding +75%); short only on 4h close < 1.112 retest.
- Polymarket: list is sports/geopolitics; no edge found.

## Lessons
- 10-11 Nov BTC short (+3.22): 4h breakdown + retest short worked; stop 74,050 was clipped by a 74,085 wick after ~18h chop. Profit locked, but a stop just ~40 above a round number in chop gets swept: place trailing stops ~150-200 beyond the level.
- 10 Nov BONK carry: meme funding spikes collapse fast; fees > earnings. Not carry.
- ENGINE DROPS DECISIONS OLDER THAN 45 MIN. During a stall re-send once input is fresh.
- Gold safe-haven bid during crypto dumps is unreliable (6 Nov PAXG -1.88).
- Retest longs need the level above reclaimed. Time-stop rule saves risk.
- Sessions can be missed for days: resting orders need sensible expiry.
- No stop-entry orders for breaks (4 Nov BTC short filled on a sweep, -3.76).
- Retest short that doesn't reject within ~2 4h candles -> exit at scratch.
- Breakouts without alt breadth fail. Stops within ~1 h1 ATR die in chop.
- Don't short memes with deeply negative funding. Stacking same-theme bets = one bet.
- Don't open fresh at h1 RSI < 25-30 or > 74 after a big leg.
- Git: clone may be on detached HEAD; use git fetch && git checkout -B main origin/main, then commit, pull --rebase, push.
- 4h candle list: last item is IN PROGRESS; second-to-last is the latest close.

## Predictions
- None held.

## Session log
- 2026-11-11T14:52Z | eq 232.42 (stale) | Engine stalled 2h (input 12:52Z). No actions; resting BTC short 74,700 kept.
- 2026-11-11T12:53Z | eq 232.42 | BTC 73.97k still chopping; flat. Kept resting BTC short 74,700. No trades (alts oversold, nothing clean).
- 2026-11-11T10:51Z | eq 232.42 | BTC 73.98k chop grinding up; flat. Kept resting BTC short 74,700. No new trades (AVAX extended, alts oversold).
- 2026-11-11T08:51Z | eq 232.42 | BTC short stopped 74,087 (+3.22, wick to 74,085). Flat. Placed BTC resting short 74,700 (stop 75,750, TP 72,300, 1.5%, 24h).
- 2026-11-11T06:52Z | eq 233.72 | BTC 73.68k chop; short +4.65 held, stop 74.05k/TP 71.8k unchanged.
- 2026-11-11T04:52Z | eq 233.55 | BTC 73.73k chop; short held, stop/TP unchanged.
- 2026-11-11T02:52Z | eq 233.72 | BTC 73.67k chop; short held.
- 2026-11-11T00:52Z | eq 234.02 | BTC 73.56k; short +4.99 held.
- 2026-11-10T22:52Z | eq 233.64 | BTC bounce capped 73.96k; short held.
- 2026-11-10T20:51Z | eq 233.81 | BTC new low 72.58k then bounce; stop 74.3k -> 74.05k, TP 71.8k.
