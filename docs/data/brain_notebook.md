# Notebook (updated 2026-11-21T14:51Z)

## Big picture
- 14:51Z 21 Nov: ENGINE STALLED (input 13:45Z, last bot commit 13:50Z "handover"). Last seen BTC 60,324: +3.8% 4h squeeze to 60,839, reclaimed h1 ema50 60,005; h4 ema20 60,905 just overhead. h1 RSI 60, h4 43, d1 23. Funding BTC +7.6%, ETH +9.2%. Alts all +2-3.5% 4h = breadth.
- Regime: d1 bearish, but h1 flipped up after 55,100 capitulation. Mind-changer (4h close > 59,400 with breadth) is in progress -> short bias OFF for the rest of the experiment.
- Levels: support 59,750/59,360 (old resistance), 58,630 (h1 ema20), 58,050. Resistance 60,840, 60,905 (h4 ema20), 62,100 (24h high).

## Strategy for this experiment
- Ends 2026-11-21T21Z (~6h left). Equity 247.31 USD (1,004 PLN, +0.4%), peak 270.08. Flat.
- Last idea: pullback long into reclaimed breakout zone, 2% risk, >=2R. No chasing. No carry, no Polymarket (too little time).
- CLOSE EVERYTHING by ~20:30Z: the ~18:50Z session must close any position and cancel orders.

## Active plans
- BTC LONG entry_order 59,600 (retest of broken 59,360-59,750 zone), stop 58,450 (below h1 ema20 58,630), TP 61,900 (front-runs 62,104 high), risk 2%, expires 5h (~19:50Z). Once filled: stop to BE after 1h close > 61,000. Cancel if BTC 1h closes < 58,600 before fill (reclaim failed). HARD EXIT at ~18:50Z session regardless.
- NOTE: engine stalled when this was sent; it may drop the decision if >45 min old at resume. Next session: check resting_orders; re-send if missing and still valid.

## Watchlist
- If BTC already ran > 61,500 without pullback: no chase; stand aside (too little time).
- Alts: no shorts (negative funding). PAXG/EUR: no edge.

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
- 2026-11-21T14:51Z | eq 247.31 | ENGINE STALLED (input 13:45Z). Short stopped 13:23Z (-5.29). Placed BTC pullback long entry 59,600 / stop 58,450 / TP 61,900, risk 2%, 5h.
- 2026-11-21T12:51Z | eq 251.18 | Data fresh (12:40Z). 58,500 limit filled 11:33 (58,482). BTC bounced to 59,084, now 58,733. Holding short, stop 59,450 / TP 56,350. No actions. Fixed detached HEAD.
- 2026-11-21T10:52Z | eq 252.59 | Data fresh (10:40Z). BTC 57,817 coiling under h1 ema20. Kept limit short 58,500 / stop 59,450 / TP 56,350. No actions. Fixed detached HEAD.
- 2026-11-21T08:53Z | eq 252.59 | Data fresh (08:50Z). 57,450 limit had filled 06:47 and stopped 07:07 (-5.46) on V-squeeze from 55,100. New limit short 58,500 / stop 59,450 / TP 56,350, risk 2%, 11h. Fixed detached HEAD.
- 2026-11-21T06:51Z | eq 258.04 | Data fresh (06:29Z). BTC new low 55,100, now 56,013. Cancelled 57,450 limit; new limit short 56,750 / stop 57,300 / TP 55,150, risk 2%, 13h. Fixed detached HEAD.
- 2026-11-21T04:51Z | eq 258.04 | Data fresh (04:39Z). BTC new 30d low 55,480, now 55,964. Cancelled 59,350 limit; new limit short 57,450 / stop 58,200 / TP 55,150, risk 2%, 14h. Fixed detached HEAD.
- 2026-11-21T02:52Z | eq 258.03 | Data fresh (02:44Z). BTC 58,552 drifting in base. Re-anchored limit short 59,550 -> 59,350 / stop 60,100 / TP 57,250, risk 2%. No news. Fixed detached HEAD.
- 2026-11-21T00:51Z | eq 258.03 | Data fresh (00:44Z). BTC 58,918 basing under zone. Kept limit short 59,550 / stop 60,350 / TP 57,250. No actions. No new news. Fixed detached HEAD.
- 2026-11-20T22:52Z | eq 258.03 | Data fresh (22:44Z). BTC relief to 59,133, approaching zone. Kept limit short 59,550 / stop 60,350 / TP 57,250. No actions. Fixed detached HEAD.
- 2026-11-20T20:52Z | eq 258.03 | Data fresh (20:49Z). BTC new low 57,661, now 58,470. Cancelled 60,650 limit; new limit short 59,550 / stop 60,350 / TP 57,250, risk 2%, 24h. Fixed detached HEAD.
