# Notebook (updated 2026-11-21T06:51Z)

## Big picture
- 06:51Z 21 Nov: data fresh (06:29Z). BTC 56,013 after yet another new 30d low 55,100. h1 ema20 58,565 / ema50 60,440; h4 ema20 61,088. h1 RSI 22, h4 RSI 17, d1 RSI 15 (extreme). Funding negative (BTC -7%, alts -15 to -47% APR): shorts crowded -> squeeze risk. ETH 1,567.
- Trend: bearish all timeframes, very extended. Resistance 56,736 (in-progress 4h high), 57,300, 58,100-58,500. Support 55,100, 55k, 54k.
- News: extreme fear, BTC ~-31% in 30d; no fresh catalyst.
- Mind-changers: 1h close > 57,300 -> shorts off; 4h close > 59,400 -> capitulation-reclaim long candidate.

## Strategy for this experiment
- Goal ends 2026-11-21T21Z (~14h left). Equity 258.04 USD (1,048 PLN, +0.35%), peak 270.08. One clean trade max, >=2.5R, risk 2%.
- Trade WITH the trend: limit short at the latest broken level/4h high, re-anchored each session within ~1 h1 ATR of price. No stop-entry break orders, no fresh opens at h1 RSI < 30.
- Trail behind completed 4h highs ~450-600 above; pyramid only from breakeven.
- No carry (funding negative). No Polymarket edge found.
- CLOSE EVERYTHING by ~20:30Z 21 Nov.

## Active plans
- BTC limit SHORT (placed 06:51Z, exp ~19:51Z): trigger 56,750 (retest of in-progress 4h high 56,736), stop 57,300, TP 55,150 (front-runs 55k / 55,100 low), risk 2%, ~2.9R. If filled: BE after 1h close < 55,800; trail ~500 above completed 4h highs. Scratch if no rejection within 2 4h candles or 1h close > 57,300. If BTC breaks < 55,000 unfilled, re-anchor to latest LH (~1 h1 ATR above). Cancel after ~18Z if not filled with room to TP; close any position by 20:30Z.

## Watchlist
- Capitulation-reclaim long: 4h close > 59,400 with alt breadth after spike low; small, 1.5%.
- ETH short only on retest of a broken level and only if no BTC short (same bet).
- Alts: no fresh shorts (deeply negative funding, d1 oversold).
- PAXG 3,505 drifting: no edge. EUR: none.

## Lessons
- 21 Nov 05-06Z: 57,450 limit (1.7 ATR away) missed again; BTC flushed to 55,100 instead. Keep anchors within ~1 h1 ATR.
- 21 Nov 03-05Z: base 58.1-59.4k broke down again (-3.4k) with no relief toward 59,350 limit; a 6-hour base under falling emas resolved lower again. Re-anchor tighter (within ~1 h1 ATR of price) each session.
- 20 Nov 17-21Z: 60,650 limit (retest of broken 61,176) never came; BTC flushed again to 57,661. In this leg relief after a breakdown is <1 h1 ATR; anchor at the latest 4h high/breakdown close, not the older shelf.
- 20 Nov 17-19Z: engine stalled again after a "handover" commit; check last bot commit time vs now every session.
- 20 Nov 14-17Z: 62,050 limit missed; BTC broke the 30d low straight down (-2.3k in one hour) with no relief. Grinding along a low under falling emas resolves by breaking it; next time consider a smaller break-retest plan ready.
- 20 Nov: limit 63,250 never filled; bounce stalled at 62,550 (h1 ema20) before new low. In this leg relief stalls at h1 ema20-ema50 zone: anchor ~just under h1 ema50 and re-anchor every session.
- 19 Nov: limit 64,250 at h4 ema20 missed by ~240 (top 64,014) after waiting 12h; in a strong downtrend relief legs stall BELOW h4 ema20 -> anchor at h1 ema50 / latest LH instead.
- 19 Nov: BTC short 63,181 scratched ~-2.4 when bounce broke the LH it was anchored to (63,482) with alt breadth after 2 4h candles. Shorts at the very bottom of a 30d-low leg (d1 RSI ~22) get squeezed; prefer entries nearer h4 ema20.
- 18-19 Nov: re-anchoring the limit to the LATEST broken level (63,200) filled within 3h; the far ones never did.
- 18 Nov: anchor retest shorts at the LATEST LH / h1 ema50 / h4 ema20, not old spike highs.
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
- 2026-11-21T06:51Z | eq 258.04 | Data fresh (06:29Z). BTC new low 55,100, now 56,013. Cancelled 57,450 limit; new limit short 56,750 / stop 57,300 / TP 55,150, risk 2%, 13h. Fixed detached HEAD.
- 2026-11-21T04:51Z | eq 258.04 | Data fresh (04:39Z). BTC new 30d low 55,480, now 55,964. Cancelled 59,350 limit; new limit short 57,450 / stop 58,200 / TP 55,150, risk 2%, 14h. Fixed detached HEAD.
- 2026-11-21T02:52Z | eq 258.03 | Data fresh (02:44Z). BTC 58,552 drifting in base. Re-anchored limit short 59,550 -> 59,350 / stop 60,100 / TP 57,250, risk 2%. No news. Fixed detached HEAD.
- 2026-11-21T00:51Z | eq 258.03 | Data fresh (00:44Z). BTC 58,918 basing under zone. Kept limit short 59,550 / stop 60,350 / TP 57,250. No actions. No new news. Fixed detached HEAD.
- 2026-11-20T22:52Z | eq 258.03 | Data fresh (22:44Z). BTC relief to 59,133, approaching zone. Kept limit short 59,550 / stop 60,350 / TP 57,250. No actions. Fixed detached HEAD.
- 2026-11-20T20:52Z | eq 258.03 | Data fresh (20:49Z). BTC new low 57,661, now 58,470. Cancelled 60,650 limit; new limit short 59,550 / stop 60,350 / TP 57,250, risk 2%, 24h. Fixed detached HEAD.
- 2026-11-20T18:51Z | eq 258.02 | ENGINE STALLED (input 16:53Z, ~2h old). Kept limit short 60,650 / stop 61,450 / TP 58,250. No actions. No useful news.
- 2026-11-20T16:51Z | eq 258.02 | Data fresh (16:43Z). BTC broke 30d low, flush to 58,702, now 59,372. Cancelled 62,050 limit; new limit short 60,650 / stop 61,450 / TP 58,250, risk 2%, 24h.
- 2026-11-20T14:52Z | eq 258.02 | Data fresh (14:43Z). BTC 61,495 grinding on 30d low. Re-anchored limit short 62,200 -> 62,050 / stop 62,750 / TP 60,250, risk 2%, 24h. No news.
- 2026-11-20T12:52Z | eq 258.02 | Data fresh (12:43Z). BTC new 30d low 61,176, now 61,548. Re-anchored limit short 62,350 -> 62,200 / stop 62,850 / TP 60,250, risk 2%, 24h. No news.
