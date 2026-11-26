# Notebook (updated 2026-11-26T04:50:50Z)

## Big picture
- 18:51Z 21 Nov: BTC 60,088, above h1 ema20 59,181, at h1 ema50 60,010, under h4 ema20 60,785. Funding +5.5% APR. Pullback to 59,550 never came.
- 16:50Z 21 Nov: engine running again (input 16:41Z). BTC 59,860 coiling after +3.8% squeeze (high 60,883): above h1 ema20 58,985, under h1 ema50 60,005 / h4 ema20 60,763. h1 RSI 55, h4 41, d1 22. Funding +9% APR.
- Regime: d1 bearish, h1 flipped up after 55,100 capitulation. Short bias OFF for the rest of the experiment.
- Levels: support 59,750/59,360, 58,985 (h1 ema20), 58,050. Resistance 60,005, 60,763, 60,883.

## Strategy for this experiment
- Ends 2026-11-21T21Z. FINAL: flat, all orders cancelled at 18:51Z. Equity 247.31 USD (1,004.42 PLN, +0.44% vs 1,000 PLN start). Any later session: do nothing.

## Active plans
- None. BTC 59,550 entry cancelled/expired 18:51Z unfilled.

## Watchlist
- No chase above 60,500. Alts/PAXG/EUR: no edge in remaining time.

## Lessons
- 21 Nov 11-14Z: BTC LH short 58,482 stopped at 59,480 (-5.29) by squeeze through h1 ema50 with alt breadth and funding flipping positive. Once funding flips positive after capitulation, the squeeze is NOT finished; don't short the first bounce to h1 ema20.
- 21 Nov 06-07Z: 57,450 limit filled AFTER a capitulation wick (55,100) and got stopped in 20 min by a +3.5k V-squeeze (-5.46). After a fresh 30d-low wick with d1 RSI ~15 and negative funding, wait for the squeeze to finish (funding to flip) before re-shorting; stops < 1 ATR get run.
- 21 Nov: cancel orders sent at 06:51Z did not stop a fill at 06:47Z; the engine also logged the 06:51 decision with no actions at 08:10. Check events/resting_orders every session.
- 21 Nov 05-06Z: 57,450 limit (1.7 ATR away) missed again; BTC flushed to 55,100 instead. Keep anchors within ~1 h1 ATR.
- 21 Nov 03-05Z: base 58.1-59.4k broke down again (-3.4k) with no relief toward 59,350 limit; a 6-hour base under falling emas resolved lower again. Re-anchor tighter (within ~1 h1 ATR of price) each session.
- 20 Nov 17-19Z: engine stalled again after a "handover" commit; check last bot commit time vs now every session.
- 20 Nov 14-17Z: 62,050 limit missed; BTC broke the 30d low straight down (-2.3k in one hour) with no relief. Grinding along a low under falling emas resolves by breaking it; next time consider a smaller break-retest plan ready.
- 19 Nov: BTC short 63,181 scratched ~-2.4 when bounce broke the LH it was anchored to (63,482) with alt breadth after 2 4h candles. Shorts at the very bottom of a 30d-low leg (d1 RSI ~22) get squeezed; prefer entries nearer h4 ema20.
- 18-19 Nov: re-anchoring the limit to the LATEST broken level (63,200) filled within 3h; the far ones never did.
- 15 Nov: capitulation wicks below round numbers snap back 3%+ in an hour; relief legs retest h1 ema50/h4 ema20.
- 14 Nov: best trade (+17.22): re-anchored limit short at broken level + trailing behind 4h LHs + TP front-running round-number support (~0.2-0.3% above).
- Stops ~40 above round numbers in chop get swept: keep ~150+ beyond levels.
- Meme carry: funding spikes collapse fast; fees > earnings.
- ENGINE DROPS DECISIONS OLDER THAN 45 MIN (confirmed again 21 Nov 14:51 order lost). During a stall re-send once input is fresh.
- Gold safe-haven bid during crypto dumps is unreliable.
- No stop-entry orders for breaks. Retest short that doesn't reject within ~2 4h candles -> scratch.
- Breakouts without alt breadth fail. Don't short memes with deeply negative funding. Stacking same-theme bets = one bet.
- Don't open fresh at h1 RSI < 25-30 or > 74 after a big leg.
- Git: if detached HEAD, git fetch && git checkout -B main origin/main, then commit, pull --rebase, push.
- 4h candle list: last item is IN PROGRESS; second-to-last is the latest close.

## Predictions
- None held.

## Session log
- 2026-11-26T04:50:50Z | eq 247.43 | Experiment ended 21Z 21 Nov. Input 23:15Z 25 Nov (~5.6h old, engine idle post-end). Flat, no orders, no action. Mark 1,013.62 PLN (FX drift). Fixed detached HEAD.
- 2026-11-26T02:50:47Z | eq 247.43 | Experiment ended 21Z 21 Nov. Input 23:15Z 25 Nov (~3.6h old, engine idle post-end). Flat, no orders, no action. Mark 1,013.62 PLN (FX drift). Fixed detached HEAD.
- 2026-11-26T00:51:23Z | eq 247.43 | Experiment ended 21Z 21 Nov. Input 23:15Z 25 Nov (~1.6h old, engine idle post-end). Flat, no orders, no action. Mark 1,013.62 PLN (FX drift). Fixed detached HEAD.
- 2026-11-25T22:51:26Z | eq 247.42 | Experiment ended 21Z 21 Nov. Input 14:28Z 25 Nov (stale ~8.4h, engine idle post-end). Flat, no orders, no action. Mark 1,013.57 PLN (FX drift). Fixed detached HEAD.
- 2026-11-25T20:51:19Z | eq 247.42 | Experiment ended 21Z 21 Nov. Input 14:28Z 25 Nov (stale ~6.4h, engine idle post-end). Flat, no orders, no action. Mark 1,013.57 PLN (FX drift). Fixed detached HEAD.
- 2026-11-25T18:50:42Z | eq 247.42 | Experiment ended 21Z 21 Nov. Input 14:28Z 25 Nov (stale ~4.4h, engine idle post-end). Flat, no orders, no action. Mark 1,013.57 PLN (FX drift). Fixed detached HEAD.
- 2026-11-25T16:51:18Z | eq 247.42 | Experiment ended 21Z 21 Nov. Input 14:28Z 25 Nov (stale ~2.3h, engine idle post-end). Flat, no orders, no action. Mark 1,013.57 PLN (FX drift). Fixed detached HEAD.
- 2026-11-25T14:51:05Z | eq 247.42 | Experiment ended 21Z 21 Nov. Input 14:28Z 25 Nov (fresh). Flat, no orders, no action. Mark 1,013.57 PLN (FX drift). Fixed detached HEAD.
- 2026-11-25T12:51:27Z | eq 247.41 | Experiment ended 21Z 21 Nov. Input 04:03Z 25 Nov (stale, engine idle post-end). Flat, no orders, no action. Mark 1,009.89 PLN (FX drift). Fixed detached HEAD.
- 2026-11-25T10:51:29Z | eq 247.41 | Experiment ended 21Z 21 Nov. Input 04:03Z 25 Nov (stale, engine idle post-end). Flat, no orders, no action. Mark 1,009.89 PLN (FX drift). Fixed detached HEAD.
