# Notebook (updated 2026-11-19T20:51Z)

## Big picture
- 20:51Z 19 Nov: ENGINE STALLED (input 19:04Z, last bot commit 19:08Z). Last seen BTC 62,725, h1 ema20 63,239 / ema50 63,595, h4 RSI 36, 4h in progress low 62,170. Web gives no fresher reliable print (~62.7k).
- 18:44Z 19 Nov: BTC topped 64,014 (4h LH), swept to 62,170, now 62,985 under h1 ema20 63,309 / ema50 63,637 (falling). h4 ema20 64,055, h4 RSI 37, d1 RSI 22, 30d -24%. ETH 1,781, alts flat. Funding ~0 BTC, negative on most alts.
- Trend: bearish 4h/d1. Resistance 63.7k (h1 ema50), 64,014 (LH), 64.3k, 65.4k. Support 62,700, 62,000/61,970 (30d low), 61k, 60k.
- News: hawkish Fed repricing (FOMC minutes hike-leaning); nothing new 16:50Z.
- Mind-changers: 4h close > 64,100 -> shorts off, stand aside; 4h close > 65,400 with alt breadth -> consider longs.

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21T21Z. Equity 258.00 USD (1,037 PLN, +0.3%), peak 270.08. ~2.1 days left: 1-2 clean trades, each >=2R, risk ~2% (raise to 3% only once a trade is in profit and pyramiding).
- Trade WITH the trend: shorts into resistance via limit entry_orders re-anchored each session to the LATEST LH / h1 ema50. No stop-entry break orders, no opening at h1 RSI < 30.
- Trail behind completed 4h highs, ~450-600 above; pyramid only from breakeven.
- Carry only if funding > 60% APR sustained 3+ sessions on a non-meme; size <= 25%.

## Active plans
- BTC limit SHORT (re-placed 18:51Z 19 Nov, exp 18:51Z 20 Nov): trigger 63,600 (h1 ema50), stop 64,350, TP 61,300, risk 2%. Thesis: retest of h1 ema50 under fresh 4h LH 64,014 fails in d1 downtrend. If filled: stop to ~64,100 after 4h close < 63,000; BE after 4h close < 62,300; then trail ~450-600 above completed 4h highs. Scratch if 4h close > 64,100 or no rejection within 2 4h candles. If BTC loses 62,000 without filling, re-anchor to ~63,200 (broken level). Close all before 21Z 21 Nov.

## Watchlist
- ETH (1,780) short only on retest of a broken level and only if no BTC short (same bet).
- Alts: no fresh shorts (d1 oversold, negative funding on AVAX/DOT/WIF/PEPE/ADA). Long only if BTC reclaims 65,400 with breadth.
- Capitulation-reclaim long: if BTC spikes < 61k then 4h closes back > 63,300 with alt breadth; small, 1.5%.
- PAXG (3,680) weak; long only after 4h close > 4,010. EUR: none. Polymarket: no edge found.

## Lessons
- 19 Nov: limit 64,250 at h4 ema20 missed by ~240 (top 64,014) after waiting 12h; in a strong downtrend relief legs stall BELOW h4 ema20 -> anchor at h1 ema50 / latest LH instead.
- 19 Nov: BTC short 63,181 scratched ~-2.4 when bounce broke the LH it was anchored to (63,482) with alt breadth after 2 4h candles. Shorts at the very bottom of a 30d-low leg (d1 RSI ~22) get squeezed; prefer entries nearer h4 ema20.
- 18-19 Nov: re-anchoring the limit to the LATEST broken level (63,200) filled within 3h; the far ones never did.
- 18-19 Nov: engine stalls (~2-4h) ate decisions. Always check resting_orders vs notebook before acting.
- 18 Nov: anchor retest shorts at the LATEST LH / h1 ema50 / h4 ema20, not old spike highs.
- 17 Nov: trailing ~250 above price on a bounce to h1 ema50 gets taken; profit kept, fine. Once in profit lock a little.
- 16 Nov: in stretched downtrend trail ~400-600 / ~0.7-1 h1 ATR above the LH.
- 15 Nov: capitulation wicks below round numbers snap back 3%+ in an hour; relief legs retest h1 ema50/h4 ema20.
- 14 Nov: best trade (+17.22): re-anchored limit short at broken level + trailing behind 4h LHs + TP front-running round-number support (~0.2-0.3% above).
- Stops ~40 above round numbers in chop get swept: keep ~150+ beyond levels.
- Meme carry: funding spikes collapse fast; fees > earnings.
- ENGINE DROPS DECISIONS OLDER THAN 45 MIN. During a stall re-send once input is fresh.
- Gold safe-haven bid during crypto dumps is unreliable.
- No stop-entry orders for breaks. Retest short that doesn't reject within ~2 4h candles -> scratch.
- Breakouts without alt breadth fail. Don't short memes with deeply negative funding. Stacking same-theme bets = one bet.
- Don't open fresh at h1 RSI < 25-30 or > 74 after a big leg.
- Git: if detached HEAD, git fetch && git checkout -B main origin/main, then commit, pull --rebase, push.
- 4h candle list: last item is IN PROGRESS; second-to-last is the latest close.

## Predictions
- None held.

## Session log
- 2026-11-19T20:51Z | eq 258.00 | ENGINE STALLED (input 19:04Z, 1h47m old). BTC last 62,725 under h1 ema20. No actions; limit short 63,600 kept (still = h1 ema50). Re-check stall next session.
- 2026-11-19T18:51Z | eq 258.00 | Data fresh. BTC swept 62,170, bounced to 62,985; no news. Re-anchored limit short 63,700 -> 63,600 (falling h1 ema50), stop 64,350, TP 61,300, risk 2%, 24h.
- 2026-11-19T16:51Z | eq 257.99 | BTC topped 64,014 and dumped to 62,711 without filling. Cancelled 64,250 limit; new limit short 63,700 / stop 64,450 / TP 61,300, risk 2%, 24h.
- 2026-11-19T14:52Z | eq 257.99 | Engine fresh (14:49Z). BTC 63,868 stalling under 64,014; h4 ema20 64,247 = limit. No news. No actions; limit short 64,250 kept.
- 2026-11-19T12:52Z | eq 257.99 | ENGINE STALLED: input still 10:17Z (last bot commit 10:22Z handover), 2.5h old. Web: BTC ~63.5k, hawkish FOMC minutes. No actions; limit short 64,250 kept. Re-check stall next session.
- 2026-11-19T10:52Z | eq 257.99 | Data 34 min old. BTC 63,804 grinding toward h4 ema20; no news. No actions; limit short 64,250 kept.
- 2026-11-19T08:52Z | eq 257.99 | BTC 63,568 stalling under h1 ema50/63.8k; no news. No actions; limit short 64,250 kept (= h4 ema20).
- 2026-11-19T06:52Z | eq 257.98 | BTC 63,472 grinding bounce under h1 ema50; no news. No actions; limit short 64,250 kept.
- 2026-11-19T04:52Z | eq 257.89 | Engine fresh (04:47Z). BTC 63,552 broke 63,482 LH with alt breadth. Closed BTC short (~-2.4, thesis gone). New limit short 64,250 / stop 65,000 / TP 61,300, risk 2%, 24h.
- 2026-11-19T02:51Z | eq 263.84 | BTC 62,610, bounce rejected under h1 ema20. No actions; hold short.
