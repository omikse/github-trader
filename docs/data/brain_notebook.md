# Notebook (updated 2026-11-21T08:53Z)

## Big picture
- 08:53Z 21 Nov: data fresh (08:50Z). BTC capitulation wick 55,100 (06Z) then V-squeeze to 58,579; now 57,930. h1 ema20 58,599 / ema50 60,316; h4 ema20 60,948. h1 RSI 41 (reset), h4 28, d1 17. Funding flipped positive on BTC (+8%) / ETH (+17%); alts still negative. ETH 1,631.
- Trend: bearish on h4/d1, but a capitulation low is likely in for the day. Range now 57,277-58,579. Resistance 58,580-58,600, 59,100-59,360, 59,400. Support 57,277, 56,300, 55,100.
- News: extreme fear, no fresh catalyst (Saturday).
- Mind-changers: 4h close > 59,400 with alt breadth -> shorts off, reclaim long candidate.

## Strategy for this experiment
- Ends 2026-11-21T21Z (~12h left). Equity 252.59 USD (1,025.84 PLN), peak 270.08, today -5.44 (57,432 short stopped by the squeeze). One clean trade max, >=2.3R, risk 2%.
- Lower-high retest shorts within ~1 h1 ATR of price; no chasing, no stop-entry breaks.
- No carry, no Polymarket edge found.
- CLOSE EVERYTHING by ~20:30Z 21 Nov.

## Active plans
- BTC limit SHORT (placed 08:53Z, exp ~19:53Z): trigger 58,500 (retest of 58,579 squeeze high under h1 ema20), stop 59,450, TP 56,350, risk 2%, ~2.3R. If filled: BE after 1h close < 57,300; trail ~500 above completed 4h highs. Scratch on 1h close > 59,450 or no rejection within 2 4h candles. Cancel after ~18Z if unfilled; close any position by 20:30Z.

## Watchlist
- Capitulation-reclaim long: 4h close > 59,400 with alt breadth; 1.5% risk, only if time allows (needs >4h left).
- Alts: no shorts (deeply negative funding). PAXG/EUR: no edge.

## Lessons
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
- 2026-11-21T08:53Z | eq 252.59 | Data fresh (08:50Z). 57,450 limit had filled 06:47 and stopped 07:07 (-5.46) on V-squeeze from 55,100. New limit short 58,500 / stop 59,450 / TP 56,350, risk 2%, 11h. Fixed detached HEAD.
- 2026-11-21T06:51Z | eq 258.04 | Data fresh (06:29Z). BTC new low 55,100, now 56,013. Cancelled 57,450 limit; new limit short 56,750 / stop 57,300 / TP 55,150, risk 2%, 13h. Fixed detached HEAD.
- 2026-11-21T04:51Z | eq 258.04 | Data fresh (04:39Z). BTC new 30d low 55,480, now 55,964. Cancelled 59,350 limit; new limit short 57,450 / stop 58,200 / TP 55,150, risk 2%, 14h. Fixed detached HEAD.
- 2026-11-21T02:52Z | eq 258.03 | Data fresh (02:44Z). BTC 58,552 drifting in base. Re-anchored limit short 59,550 -> 59,350 / stop 60,100 / TP 57,250, risk 2%. No news. Fixed detached HEAD.
- 2026-11-21T00:51Z | eq 258.03 | Data fresh (00:44Z). BTC 58,918 basing under zone. Kept limit short 59,550 / stop 60,350 / TP 57,250. No actions. No new news. Fixed detached HEAD.
- 2026-11-20T22:52Z | eq 258.03 | Data fresh (22:44Z). BTC relief to 59,133, approaching zone. Kept limit short 59,550 / stop 60,350 / TP 57,250. No actions. Fixed detached HEAD.
- 2026-11-20T20:52Z | eq 258.03 | Data fresh (20:49Z). BTC new low 57,661, now 58,470. Cancelled 60,650 limit; new limit short 59,550 / stop 60,350 / TP 57,250, risk 2%, 24h. Fixed detached HEAD.
- 2026-11-20T18:51Z | eq 258.02 | ENGINE STALLED (input 16:53Z, ~2h old). Kept limit short 60,650 / stop 61,450 / TP 58,250. No actions. No useful news.
- 2026-11-20T16:51Z | eq 258.02 | Data fresh (16:43Z). BTC broke 30d low, flush to 58,702, now 59,372. Cancelled 62,050 limit; new limit short 60,650 / stop 61,450 / TP 58,250, risk 2%, 24h.
- 2026-11-20T14:52Z | eq 258.02 | Data fresh (14:43Z). BTC 61,495 grinding on 30d low. Re-anchored limit short 62,200 -> 62,050 / stop 62,750 / TP 60,250, risk 2%, 24h. No news.
