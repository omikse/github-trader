# Notebook (updated 2026-11-19T02:51Z)

## Big picture
- 02:42Z 19 Nov: BTC 62,610. 20-24Z 4h swept 62,000 and closed 62,985 (h 63,209); 0-4Z 4h in progress h 63,225 / l 62,350 - bounce capped under h1 ema20 (63,196). Structure LH: 63,482 (16-20Z), ~63,2xx (20-24Z, 0-4Z). h1 ema50 63,847; h4 ema20 64,350. RSI h1 39, h4 33, d1 21. Funding BTC +6% APR.
- News: still hawkish Fed repricing / November risk-off; no fresh catalyst.
- Trend: bearish 4h/d1. Resistance 63.2-63.5k, 63.9-64.4k. Support 62,000/61,970, 61k, 60k.
- Mind-changers: 4h close > 63,950 -> stopped/stand aside; 4h close > 65,400 -> range back, consider long only with alt breadth.

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21T21Z. Equity 263.84 USD (1,060 PLN; +2.6%; peak 270.08). ~2.75 days left: fewer, cleaner trades, each >=2R, risk ~2%.
- Trade WITH the trend: shorts into resistance via limit entry_orders re-anchored each session. No stop-entry break orders, no opening at h1 RSI < 30.
- Trail behind completed 4h highs, ~450-600 above; pyramid only from breakeven.
- Carry only if funding > 60% APR sustained 3+ sessions on a non-meme; size <= 25%.

## Active plans
- BTC SHORT (filled 63,181 at 23:51Z 18 Nov from limit 63,200; +3.63 at 02:42Z): stop 63,950 (~1.9% risk), TP 60,300. Size 0.00636. Thesis: retest of broken range low under 63,482 LH in d1/4h downtrend. Management: stop to ~63,500 after a 4h close < 62,200 (or to ~63,450 if a new 4h LH < 63,000 prints); BE after 4h close < 61,800; then trail ~450-600 above completed 4h highs. Scratch if 2 consecutive 4h closes > 63,500. Time limit: if BTC still > 62,500 by 12Z 20 Nov with no lower low, tighten stop to ~63,300. Close all before 21Z 21 Nov (experiment end). Pyramid: only after stop at BE, add on retest of broken 61,970 (limit ~62,000, stop ~62,800, 1.5%).

## Watchlist
- ETH (1,737) short only on retest of a broken level and only if no BTC short (same bet).
- Alts: no fresh shorts (d1 oversold, deeply negative funding on AVAX/SUI/DOT/NEAR/PEPE/WIF). NEAR/SOL/XRP relative strength - long only if BTC reclaims 65,400.
- Capitulation-reclaim long: if BTC spikes < 61k then 4h closes back > 63,300 with alt breadth; small, 1.5%.
- PAXG (3,728) weak; long only after 4h close > 4,010. EUR: none. Polymarket: no edge found.

## Lessons
- 18-19 Nov: re-anchoring the limit to the LATEST broken level (63,200) filled within 3h; the far ones never did.
- 18 Nov: engine stalls ~4h ate two decisions; the stale order (64,750) never filled and the range broke meanwhile. Always check resting_orders vs what notebook says before acting.
- 18 Nov: in a series of shrinking 4h highs, a far limit (65,350) sat unfilled 10h; anchor retest shorts at the LATEST LH / h1 ema50, not old spike highs.
- 17 Nov: BTC short 65,330 trailed to 64,950 closed +1.85 at 23:08Z by relief bounce to 65,184. Trailing ~250 above price on a bounce to h1 ema50 gets taken; profit kept, fine.
- 17 Nov: 65,379 spike missed a 65,380 stop by 1 USD -> stops ~450 above the LH barely survive; once in profit lock a little.
- 16 Nov: stop ~200 above 4h LH taken by wick. In stretched downtrend trail ~400-600 / ~0.7-1 h1 ATR above the LH.
- 15 Nov: capitulation wicks below round numbers snap back 3%+ in an hour; expect relief legs to retest h1 ema50/h4 ema20; re-enter higher, don't chase.
- 14 Nov: best trade (+17.22): re-anchored limit short at broken level + trailing behind 4h LHs + TP front-running round-number support. Set TPs ~0.2-0.3% above obvious lows.
- 13 Nov: re-anchor retest shorts each session; far levels get left behind in fast bleeds.
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
- 2026-11-19T02:51Z | eq 263.84 | Engine fresh (02:42Z). BTC 62,610, bounce rejected under h1 ema20 63,2xx. No actions; hold short stop 63,950 / TP 60,300 per plan. News: no new catalyst.
- 2026-11-19T00:52Z | eq 261.89 | Engine fresh (00:42Z). Limit short FILLED 63,181; BTC swept 62,000 and bounced to 62,937. No actions; hold stop 63,950 / TP 60,300 per plan.
- 2026-11-18T22:52Z | eq 260.48 | Data 21:57Z (53 min old, last bot commit 22:02Z handover - possible stall). BTC 62,243 grinding to 30d low, h1 RSI 27. No actions; limit short 63,200/63,950/60,300 risk 2% stays (exp 02:52Z 20 Nov).
- 2026-11-18T20:53Z | eq 260.48 | Engine fresh (20:42Z). BTC 62,439, bounce failed at 63,482 LH. Re-anchored limit short 63,550 -> 63,200 / stop 63,950 / TP 60,300, risk 2%, 30h.
- 2026-11-18T18:52Z | eq 260.48 | Engine fresh (18:42Z). BTC 63,198 relief bounce toward 63,550 trigger. No actions; limit short 63,550/64,400/60,300 risk 2% stays (exp 22:52Z 19 Nov).
- 2026-11-18T16:52Z | eq 260.48 | Engine fresh (16:42Z). BTC broke range low, 62,340, h1 RSI 24 - no chase. Cancelled stale 64,750; limit short 63,550 / stop 64,400 / TP 60,300, risk 2%, 30h.
- 2026-11-18T14:52Z | eq 260.47 (stale) | ENGINE STALLED (data 12:31Z, last bot commit 12:36Z). Re-sent cancel + limit short 64,600 / 65,300 / 62,300, risk 2%, 22h.
- 2026-11-18T12:52Z | eq 260.47 | BTC 64,082 drifting, no bounce to 64,750 trigger. Re-anchored limit short to 64,600 / stop 65,300 / TP 62,300, risk 2%, 24h. No news catalyst.
- 2026-11-18T10:51Z | eq 260.47 | BTC 64,232, 4h LH 64,805. Cancelled 65,350 limit; new limit short 64,750 / stop 65,450 / TP 62,300, risk 2%, 24h.
- 2026-11-18T08:52Z | eq 260.47 | Engine fresh (08:47Z). BTC 64,698 coiling, 4-8Z 4h LH 64,874. No actions; limit short 65,350/66,000/62,300 stays (exp 20:51Z). News: no new catalyst.
