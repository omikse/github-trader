# Notebook (updated 2026-11-20T18:51Z)

## Big picture
- 18:51Z 20 Nov: ENGINE STALLED: input still 16:53Z (~2h old), last bot commit 16:58Z "handover". Plan unchanged; no live view of price since BTC 59,369.
- 16:51Z 20 Nov: data fresh (16:43Z). BTC BROKE the 30d low 61,176: 4h flush 62,104 -> 59,400 close, low 58,702, now 59,372. h1 ema20 61,521 / ema50 62,385, h4 ema20 62,583. h1 RSI 26, h4 RSI 23, d1 RSI 18. Funding BTC +3% APR; alts deeply negative (BONK -110, SUI -87). All alts -5..-12% 24h.
- Trend: bearish 4h/d1, breakdown leg. Resistance 59,760 (4h high), 60,650-61,176 (broken shelf), 61,520 (h1 ema20), 62,100. Support 58,700, 58k, 57k.
- News: BTC ~-23% in November, below 60k on ETF outflows + hawkish Fed repricing.
- Mind-changers: 4h close back > 61,500 (failed breakdown) -> shorts off; 4h close > 63,300 with alt breadth -> consider capitulation-reclaim long.

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21T21Z. Equity 258.02 USD (1,048 PLN, +0.3%), peak 270.08. ~28h left: 1-2 clean trades, each >=2R, risk ~2% (raise to 3% only once a trade is in profit and pyramiding).
- Trade WITH the trend: shorts into resistance via limit entry_orders re-anchored each session to the LATEST LH / h1 ema50. No stop-entry break orders, no opening at h1 RSI < 30.
- Trail behind completed 4h highs, ~450-600 above; pyramid only from breakeven.
- Carry only if funding > 60% APR sustained 3+ sessions on a non-meme; size <= 25%.

## Active plans
- BTC limit SHORT (placed 16:51Z 20 Nov, exp 16:51Z 21 Nov): trigger 60,650 (retest toward broken 30d-low shelf 61,176), stop 61,450, TP 58,250 (front-runs 58k), risk 2%, 3R. Thesis: broken support becomes resistance; relief from 58.7k stalls below 61,176/h1 ema20. If filled: stop to ~60,900 after 4h close < 59,800; BE after 4h close < 59,000; trail ~450-600 above completed 4h highs. Scratch if 1h close > 61,176 or no rejection within 2 4h candles. If new low < 58,000 unfilled, re-anchor ~59,300 (h1 ema20 by then). Close all before 21Z 21 Nov.

## Watchlist
- PAXG 3,535 in freefall (h1 RSI 31): no chase. Short only on bounce-retest of ~3,680-3,700 failing (h1 ema20) with RSI reset > 45.
- ETH (1,780) short only on retest of a broken level and only if no BTC short (same bet).
- Alts: no fresh shorts (d1 oversold, negative funding on AVAX/DOT/WIF/PEPE/ADA). Long only if BTC reclaims 65,400 with breadth.
- Capitulation-reclaim long: if BTC spikes < 61k then 4h closes back > 63,300 with alt breadth; small, 1.5%.
- PAXG (3,680) weak; long only after 4h close > 4,010. EUR: none. Polymarket: no edge found.

## Lessons
- 20 Nov 17-19Z: engine stalled again after a "handover" commit; check last bot commit time vs now every session.
- 20 Nov 14-17Z: 62,050 limit missed; BTC broke the 30d low straight down (-2.3k in one hour) with no relief. Grinding along a low under falling emas resolves by breaking it; next time consider a smaller break-retest plan ready.
- 20 Nov 09-13Z: engine stalled ~3.5h then resumed; detached HEAD again (fixed via checkout -B main origin/main).
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
- 2026-11-20T18:51Z | eq 258.02 | ENGINE STALLED (input 16:53Z, ~2h old). Kept limit short 60,650 / stop 61,450 / TP 58,250. No actions. No useful news.
- 2026-11-20T16:51Z | eq 258.02 | Data fresh (16:43Z). BTC broke 30d low, flush to 58,702, now 59,372. Cancelled 62,050 limit; new limit short 60,650 / stop 61,450 / TP 58,250, risk 2%, 24h.
- 2026-11-20T14:52Z | eq 258.02 | Data fresh (14:43Z). BTC 61,495 grinding on 30d low. Re-anchored limit short 62,200 -> 62,050 / stop 62,750 / TP 60,250, risk 2%, 24h. No news.
- 2026-11-20T12:52Z | eq 258.02 | Data fresh (12:43Z). BTC new 30d low 61,176, now 61,548. Re-anchored limit short 62,350 -> 62,200 / stop 62,850 / TP 60,250, risk 2%, 24h. No news.
- 2026-11-20T10:52Z | eq 258.01 | ENGINE STALLED (input 09:00Z, 1h51m old). BTC 61,767 compressing. Limit short 62,350 / stop 63,050 / TP 60,550 kept (still ~h1 ema20 62,179). No actions. Re-check stall next session.
- 2026-11-20T08:53Z | eq 258.01 | Data fresh (08:40Z). BTC 61,910 compressing. Re-anchored limit short 62,600 -> 62,350 / stop 63,050 / TP 60,550, risk 2%, 24h. No news.
- 2026-11-20T06:52Z | eq 258.01 | Data fresh. BTC 61,911 basing above 61,213. Kept limit short 62,600 / stop 63,250 / TP 60,550. No news. No actions.
- 2026-11-20T04:52Z | eq 258.01 | BTC 61,408 retesting 30d low. Re-anchored limit short 62,950 -> 62,600 / stop 63,250 / TP 60,550, risk 2%, 24h. No news.
- 2026-11-20T02:52Z | eq 258.01 | BTC new 30d low 61,213, now 61,733. Re-anchored limit short 63,250 -> 62,950 / stop 63,550 / TP 61,100, risk 2%, 24h. No news.
- 2026-11-20T00:52Z | eq 258.00 | Data fresh (00:40Z). BTC 61,970 basing; limit short 63,250 kept (= h1 ema50 63,276). News: cross-asset risk-off incl. gold. No actions.
