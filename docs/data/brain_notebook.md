# Notebook (updated 2026-11-20T12:52Z)

## Big picture
- 12:52Z 20 Nov: engine fresh again (12:43Z). BTC 61,548, new 30d low 61,176 this 4h. Latest closed 4h 61,745 (H 62,273 = LH). h1 ema20 62,054 / ema50 62,711, h4 ema20 63,126, h1 RSI 41, h4 RSI 31, d1 RSI 20. Funding BTC +10% APR; alts negative (BONK -163, SUI -46, PEPE -43). PEPE -12%, NEAR -13% 24h. No news.
- Trend: bearish 4h/d1. Resistance 62,050-62,300 (h1 ema20/LH 62,273), 62,710 (h1 ema50), 62,550, 63,357 LH, 64,014. Support 61,176 (30d low), 61k, 60k.
- News: hawkish Fed repricing (FOMC minutes hike-leaning); nothing new 16:50Z.
- Mind-changers: 4h close > 64,100 -> shorts off, stand aside; 4h close > 65,400 with alt breadth -> consider longs.

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21T21Z. Equity 258.02 USD (1,048 PLN, +0.3%), peak 270.08. ~32h left: 1-2 clean trades, each >=2R, risk ~2% (raise to 3% only once a trade is in profit and pyramiding).
- Trade WITH the trend: shorts into resistance via limit entry_orders re-anchored each session to the LATEST LH / h1 ema50. No stop-entry break orders, no opening at h1 RSI < 30.
- Trail behind completed 4h highs, ~450-600 above; pyramid only from breakeven.
- Carry only if funding > 60% APR sustained 3+ sessions on a non-meme; size <= 25%.

## Active plans
- BTC limit SHORT (placed 12:52Z 20 Nov, exp 12:52Z 21 Nov): trigger 62,200 (h1 ema20 62,054 / under LH 62,273), stop 62,850 (above h1 ema50 62,711), TP 60,250 (front-runs 60k), risk 2%, ~3R. Thesis: relief from 30d-low grind stalls at h1 ema20 as before. If filled: stop to ~62,550 after 4h close < 61,700; BE after 4h close < 61,100; trail ~450-600 above completed 4h highs. Scratch if 4h close > 62,750 or no rejection within 2 4h candles. If BTC breaks < 61,000 unfilled, re-anchor ~61,700 (to h1 ema20). Close all before 21Z 21 Nov.

## Watchlist
- PAXG 3,593 in freefall (h1 RSI 20): no chase. Short only on bounce-retest of ~3,680-3,700 failing (h1 ema20) with RSI reset > 45.
- ETH (1,780) short only on retest of a broken level and only if no BTC short (same bet).
- Alts: no fresh shorts (d1 oversold, negative funding on AVAX/DOT/WIF/PEPE/ADA). Long only if BTC reclaims 65,400 with breadth.
- Capitulation-reclaim long: if BTC spikes < 61k then 4h closes back > 63,300 with alt breadth; small, 1.5%.
- PAXG (3,680) weak; long only after 4h close > 4,010. EUR: none. Polymarket: no edge found.

## Lessons
- 20 Nov 09-13Z: engine stalled ~3.5h then resumed; detached HEAD again (fixed via checkout -B main origin/main).
- 20 Nov 09-11Z: engine stall again (~2h). Resting order still valid; sent empty decision only.
- 20 Nov 04-08Z: 62,600 limit untouched; price compressed under 62,090. Keep re-anchoring to the falling h1 ema20, not old LHs.
- 20 Nov 02-04Z: 62,950 limit not reached; bounce from 61,213 stalled at 62,550 (h1 ema20) again. Anchor at latest LH / h1 ema20 while d1 RSI ~20.
- 20 Nov: limit 63,250 never filled; bounce stalled at 62,550 (h1 ema20) before new low. In this leg relief stalls at h1 ema20-ema50 zone: anchor ~just under h1 ema50 and re-anchor every session.
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
- 2026-11-20T12:52Z | eq 258.02 | Data fresh (12:43Z). BTC new 30d low 61,176, now 61,548. Re-anchored limit short 62,350 -> 62,200 / stop 62,850 / TP 60,250, risk 2%, 24h. No news.
- 2026-11-20T10:52Z | eq 258.01 | ENGINE STALLED (input 09:00Z, 1h51m old). BTC 61,767 compressing. Limit short 62,350 / stop 63,050 / TP 60,550 kept (still ~h1 ema20 62,179). No actions. Re-check stall next session.
- 2026-11-20T08:53Z | eq 258.01 | Data fresh (08:40Z). BTC 61,910 compressing. Re-anchored limit short 62,600 -> 62,350 / stop 63,050 / TP 60,550, risk 2%, 24h. No news.
- 2026-11-20T06:52Z | eq 258.01 | Data fresh. BTC 61,911 basing above 61,213. Kept limit short 62,600 / stop 63,250 / TP 60,550. No news. No actions.
- 2026-11-20T04:52Z | eq 258.01 | BTC 61,408 retesting 30d low. Re-anchored limit short 62,950 -> 62,600 / stop 63,250 / TP 60,550, risk 2%, 24h. No news.
- 2026-11-20T02:52Z | eq 258.01 | BTC new 30d low 61,213, now 61,733. Re-anchored limit short 63,250 -> 62,950 / stop 63,550 / TP 61,100, risk 2%, 24h. No news.
- 2026-11-20T00:52Z | eq 258.00 | Data fresh (00:40Z). BTC 61,970 basing; limit short 63,250 kept (= h1 ema50 63,276). News: cross-asset risk-off incl. gold. No actions.
- 2026-11-19T22:52Z | eq 258.00 | Engine fresh (22:45Z). BTC new 30d low 61,353, bounce to 62,181. Re-anchored limit short 63,600 -> 63,250 / stop 64,150 / TP 61,100, risk 2%, 24h.
- 2026-11-19T20:51Z | eq 258.00 | ENGINE STALLED (input 19:04Z, 1h47m old). BTC last 62,725 under h1 ema20. No actions; limit short 63,600 kept (still = h1 ema50). Re-check stall next session.
- 2026-11-19T18:51Z | eq 258.00 | Data fresh. BTC swept 62,170, bounced to 62,985; no news. Re-anchored limit short 63,700 -> 63,600 (falling h1 ema50), stop 64,350, TP 61,300, risk 2%, 24h.
