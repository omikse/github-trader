# Notebook (updated 2026-11-18T18:52Z)

## Big picture
- 18:42Z 18 Nov: BTC 63,198 bouncing off 62,213 low (16-20Z 4h so far h 63,482). h1 RSI 37 recovering, h1 ema20 63,854. Alts green 4h (NEAR/SOL/XRP +2-3% 24h). Funding BTC +6% APR. No new catalyst (hawkish Fed, worst November in years narrative).
- 16:42Z 18 Nov (engine fresh again; 12:52Z/14:52Z decisions never executed, old 64,750 order was still resting): BTC BROKE the 63,272 range low. 12-16Z 4h closed 63,052 (h 64,319), 16Z candle low 62,213, price 62,340. h1 ema20 63,982 / ema50 64,384; h4 ema20 64,664. RSI h1 24, h4 31, d1 21 -> stretched, near 61,970 30d low. Funding +12% APR. ETH 1,737 same shape; alts weaker but less (SOL/XRP/NEAR flat 24h).
- News: no single catalyst; ongoing November risk-off / hawkish Fed.
- Trend: bearish 4h/d1. Resistance 63.27-63.6k (broken range low), 64.0k (h1 ema20), 64.3-64.4k. Support 61,970, 61k, 60k.
- Mind-changers: 4h close > 64,400 -> breakdown failed, stand aside; 4h close > 65,400 -> range back, consider long only with alt breadth.

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21T21Z. Equity 260.48 USD (1,046 PLN; +1.3%; peak 270.08). ~3.2 days left: fewer, cleaner trades, each >=2R, risk ~2%.
- Trade WITH the trend: shorts into resistance via limit entry_orders re-anchored each session. No stop-entry break orders, no opening at h1 RSI < 30.
- Trail behind completed 4h highs, ~450-600 above; pyramid only from breakeven.
- Carry only if funding > 60% APR sustained 3+ sessions on a non-meme; size <= 25%.

## Active plans
- BTC SHORT ENTRY ORDER (placed 16:52Z, 64,750 cancelled): trigger 63,550 (retest of broken 63,272 low, below h1 ema20), stop 64,400 (above 64,319 4h high, 850 risk), TP 60,300 (~3.8R), risk 2%, expires ~22:52Z 19 Nov. Once filled: stop to ~63,900 after a 4h close < 62,500; BE after 4h close < 61,900; then trail ~450-600 above completed 4h highs. Scratch if 2 consecutive 4h closes > 63,800 without rejection. Cancel if a 4h closes > 64,400 pre-fill. If BTC flushes < 61,000 without filling, re-anchor to ~62,000 (61,970 retest), stop ~62,900.

## Watchlist
- ETH (1,737) short only on retest of a broken level and only if no BTC short (same bet).
- Alts: no fresh shorts (d1 oversold, deeply negative funding on AVAX/SUI/DOT/NEAR/PEPE/WIF). NEAR/SOL/XRP relative strength - long only if BTC reclaims 65,400.
- Capitulation-reclaim long: if BTC spikes < 61k then 4h closes back > 63,300 with alt breadth; small, 1.5%.
- PAXG (3,728) weak; long only after 4h close > 4,010. EUR: none. Polymarket: no edge found.

## Lessons
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
- 2026-11-18T18:52Z | eq 260.48 | Engine fresh (18:42Z). BTC 63,198 relief bounce toward 63,550 trigger. No actions; limit short 63,550/64,400/60,300 risk 2% stays (exp 22:52Z 19 Nov).
- 2026-11-18T16:52Z | eq 260.48 | Engine fresh (16:42Z). BTC broke range low, 62,340, h1 RSI 24 - no chase. Cancelled stale 64,750; limit short 63,550 / stop 64,400 / TP 60,300, risk 2%, 30h.
- 2026-11-18T14:52Z | eq 260.47 (stale) | ENGINE STALLED (data 12:31Z, last bot commit 12:36Z). Re-sent cancel + limit short 64,600 / 65,300 / 62,300, risk 2%, 22h.
- 2026-11-18T12:52Z | eq 260.47 | BTC 64,082 drifting, no bounce to 64,750 trigger. Re-anchored limit short to 64,600 / stop 65,300 / TP 62,300, risk 2%, 24h. No news catalyst.
- 2026-11-18T10:51Z | eq 260.47 | BTC 64,232, 4h LH 64,805. Cancelled 65,350 limit; new limit short 64,750 / stop 65,450 / TP 62,300, risk 2%, 24h.
- 2026-11-18T08:52Z | eq 260.47 | Engine fresh (08:47Z). BTC 64,698 coiling, 4-8Z 4h LH 64,874. No actions; limit short 65,350/66,000/62,300 stays (exp 20:51Z). News: no new catalyst.
- 2026-11-18T06:51Z | eq 260.46 (stale) | ENGINE STALLED (data 05:26Z, last commit 05:31Z handover). BTC 64,714 bouncing toward trigger. No actions; limit short 65,350/66,000/62,300 stays (exp 20:51Z).
- 2026-11-18T04:45Z | eq 260.46 | BTC 64,400 coiling, 0-4Z 4h LH 64,928. Flat; kept limit short 65,350/66,000/62,300 (exp 20:51Z). News: no new catalyst.
- 2026-11-18T02:52Z | eq 260.46 | BTC 64,307 rolling over below h1 ema50; flat. Kept limit short 65,350/66,000/62,300 (exp 20:51Z). No new news edge.
- 2026-11-18T00:52Z | eq 260.46 | Short stopped 23:08Z at 64,982 (+1.85). 20-24Z 4h closed 64,877 (<65,400). Placed limit short 65,350 / stop 66,000 / TP 62,300, risk 2%, 20h.
