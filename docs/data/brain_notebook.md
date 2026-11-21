# Notebook (updated 2026-11-21T16:50Z)

## Big picture
- 16:50Z 21 Nov: engine running again (input 16:41Z). BTC 59,860 coiling after +3.8% squeeze (high 60,883): above h1 ema20 58,985, under h1 ema50 60,005 / h4 ema20 60,763. h1 RSI 55, h4 41, d1 22. Funding +9% APR.
- Regime: d1 bearish, h1 flipped up after 55,100 capitulation. Short bias OFF for the rest of the experiment.
- Levels: support 59,750/59,360, 58,985 (h1 ema20), 58,050. Resistance 60,005, 60,763, 60,883.

## Strategy for this experiment
- Ends 2026-11-21T21Z (~4h left). Equity 247.31 USD (1,004 PLN), peak 270.08. Flat.
- Only small, clean pullback longs (2% risk). No carry, no Polymarket (too little time).
- CLOSE EVERYTHING at the ~18:50Z session: close any position, cancel any order. That session is the last one that acts.

## Active plans
- BTC LONG entry_order 59,550 (retest of reclaimed 59,360-59,750 zone), stop 58,650, TP 60,800, risk 2%, expires 2h (~18:51Z). The 14:51Z version was dropped by the stall (journal shows no actions); re-sent 16:50Z. If filled and 1h closes > 60,300: stop to BE. HARD EXIT at ~18:50Z session.

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
- 2026-11-21T16:50Z | eq 247.31 | Engine resumed (16:41Z); 14:51 order had been dropped. Re-sent BTC pullback long entry 59,550 / stop 58,650 / TP 60,800, risk 2%, 2h. Fixed detached HEAD.
- 2026-11-21T14:51Z | eq 247.31 | ENGINE STALLED (input 13:45Z). Short stopped 13:23Z (-5.29). Placed BTC pullback long entry 59,600 / stop 58,450 / TP 61,900, risk 2%, 5h.
- 2026-11-21T12:51Z | eq 251.18 | Data fresh (12:40Z). 58,500 limit filled 11:33 (58,482). BTC bounced to 59,084, now 58,733. Holding short, stop 59,450 / TP 56,350. No actions. Fixed detached HEAD.
- 2026-11-21T10:52Z | eq 252.59 | Data fresh (10:40Z). BTC 57,817 coiling under h1 ema20. Kept limit short 58,500 / stop 59,450 / TP 56,350. No actions. Fixed detached HEAD.
- 2026-11-21T08:53Z | eq 252.59 | Data fresh (08:50Z). 57,450 limit had filled 06:47 and stopped 07:07 (-5.46) on V-squeeze from 55,100. New limit short 58,500 / stop 59,450 / TP 56,350, risk 2%, 11h. Fixed detached HEAD.
- 2026-11-21T06:51Z | eq 258.04 | Data fresh (06:29Z). BTC new low 55,100, now 56,013. Cancelled 57,450 limit; new limit short 56,750 / stop 57,300 / TP 55,150, risk 2%, 13h. Fixed detached HEAD.
- 2026-11-21T04:51Z | eq 258.04 | Data fresh (04:39Z). BTC new 30d low 55,480, now 55,964. Cancelled 59,350 limit; new limit short 57,450 / stop 58,200 / TP 55,150, risk 2%, 14h. Fixed detached HEAD.
- 2026-11-21T02:52Z | eq 258.03 | Data fresh (02:44Z). BTC 58,552 drifting in base. Re-anchored limit short 59,550 -> 59,350 / stop 60,100 / TP 57,250, risk 2%. No news. Fixed detached HEAD.
- 2026-11-21T00:51Z | eq 258.03 | Data fresh (00:44Z). BTC 58,918 basing under zone. Kept limit short 59,550 / stop 60,350 / TP 57,250. No actions. No new news. Fixed detached HEAD.
- 2026-11-20T22:52Z | eq 258.03 | Data fresh (22:44Z). BTC relief to 59,133, approaching zone. Kept limit short 59,550 / stop 60,350 / TP 57,250. No actions. Fixed detached HEAD.
