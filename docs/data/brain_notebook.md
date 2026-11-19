# Notebook (updated 2026-11-19T06:52Z)

## Big picture
- 06:47Z 19 Nov: BTC 63,472, 4h relief candle h 63,683 (last close 63,135). h1 RSI 51 just above ema20 63,246, under ema50 63,772; h4 ema20 64,311; d1 RSI 24. Alts mildly green (ETH 1,804, NEAR/XRP leading). Funding BTC +1.8% APR. Bounce is slow/grinding, no breakout.
- Trend: still bearish 4h/d1 (lower daily closes, 30d -23%). Resistance 63.8-64.4k, 64,874 (24h high), 65.4k. Support 62,000/61,970, 61k, 60k.
- News: hawkish Fed repricing / November risk-off; no fresh catalyst.
- Mind-changers: 4h close > 64,900 -> no shorts, stand aside; 4h close > 65,400 with alt breadth -> range back, consider longs.

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21T21Z. Equity 257.89 USD (1,036 PLN, +0.3%) before the scratch, peak 270.08. ~2.7 days left: few clean trades, each >=2R, risk ~2%.
- Trade WITH the trend: shorts into resistance via limit entry_orders re-anchored each session. No stop-entry break orders, no opening at h1 RSI < 30.
- Trail behind completed 4h highs, ~450-600 above; pyramid only from breakeven.
- Carry only if funding > 60% APR sustained 3+ sessions on a non-meme; size <= 25%.

## Active plans
- BTC limit SHORT (placed 04:52Z 19 Nov, exp 04:52Z 20 Nov): trigger 64,250, stop 65,000, TP 61,300, risk 2%. Thesis: relief bounce into h4 ema20 / 63.9-64.4k resistance fails in d1 downtrend. If filled: stop to ~64,500 after 4h close < 63,200; BE after 4h close < 62,500; then trail ~450-600 above completed 4h highs. Scratch if 2 consecutive 4h closes > 64,400 or no rejection within 2 4h candles. If price stalls below 63,9xx and rolls over without filling, consider re-anchoring lower to the new LH next session. Close all before 21Z 21 Nov.

## Watchlist
- ETH (1,801) short only on retest of a broken level and only if no BTC short (same bet).
- Alts: no fresh shorts (d1 oversold, negative funding on ADA/SUI/NEAR/WIF/LINK). NEAR/SOL/XRP relative strength - long only if BTC reclaims 65,400.
- Capitulation-reclaim long: if BTC spikes < 61k then 4h closes back > 63,300 with alt breadth; small, 1.5%.
- PAXG (3,718) weak; long only after 4h close > 4,010. EUR: none. Polymarket: no edge found.

## Lessons
- 19 Nov: BTC short 63,181 scratched ~-2.4 when bounce broke the LH it was anchored to (63,482) with alt breadth after 2 4h candles. Shorts at the very bottom of a 30d-low leg (d1 RSI ~22) get squeezed; prefer entries nearer h4 ema20.
- 18-19 Nov: re-anchoring the limit to the LATEST broken level (63,200) filled within 3h; the far ones never did.
- 18 Nov: engine stalls ~4h ate two decisions. Always check resting_orders vs notebook before acting.
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
- 2026-11-19T06:52Z | eq 257.98 | BTC 63,472 grinding bounce under h1 ema50; no news. No actions; limit short 64,250 kept.
- 2026-11-19T04:52Z | eq 257.89 | Engine fresh (04:47Z). BTC 63,552 broke 63,482 LH with alt breadth. Closed BTC short (~-2.4, thesis gone). New limit short 64,250 / stop 65,000 / TP 61,300, risk 2%, 24h.
- 2026-11-19T02:51Z | eq 263.84 | BTC 62,610, bounce rejected under h1 ema20. No actions; hold short.
- 2026-11-19T00:52Z | eq 261.89 | Limit short FILLED 63,181; BTC swept 62,000 and bounced. No actions.
- 2026-11-18T22:52Z | eq 260.48 | Data 53 min old (possible stall). BTC 62,243. No actions.
- 2026-11-18T20:53Z | eq 260.48 | BTC 62,439, bounce failed at 63,482 LH. Re-anchored limit short 63,550 -> 63,200.
- 2026-11-18T18:52Z | eq 260.48 | BTC 63,198 relief bounce. No actions.
- 2026-11-18T16:52Z | eq 260.48 | BTC broke range low 62,340. Cancelled stale 64,750; limit short 63,550.
- 2026-11-18T14:52Z | eq 260.47 (stale) | ENGINE STALLED. Re-sent cancel + limit short 64,600.
- 2026-11-18T12:52Z | eq 260.47 | Re-anchored limit short to 64,600.
