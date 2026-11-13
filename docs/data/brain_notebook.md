# Notebook (updated 2026-11-13T02:51Z)

## Big picture
- 02:51Z 13 Nov (input 02:44Z, fresh): BTC 70,125, new 30d low 70,113 (below 70.6k, lowest since Oct 2024). 00-04Z 4h in progress h 71,429 l 70,113; 20-24Z closed h 71,613 c 71,371. RSI h1 16 / h4 21 / d1 28 (extreme oversold; no chase). h1 ema20/50 71.81/72.78k, h4 ema20 73.14k. ETH 1,987, SOL 80.1, PAXG 3,905, EUR funding 84%.
- Trend: bearish 4h/d1 (ETF outflows, leverage unwind, worst-November narrative). Broken shelf 71.0-71.6k = first resistance; then 72.1k, 72.6-73.06k.
- Support: 70k round, 69k, 68k.
- Mind-changers: BTC 4h close > 72,300 = short idea off near-term; > 74,000 bear plan weakening.

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21. Equity 240.90 USD (956 PLN, -6.3%; peak 265.7). Closed 10W/22L. ~9 days left: fewer, cleaner trades, each >=2R, risk 1.5-2%.
- Trade WITH the trend: shorts into resistance / retests of broken levels via limit entry_orders. No stop-entry break orders, no chasing at h1 RSI < 30.
- Trail behind completed 4h highs (~150-200 above); pyramid only from breakeven.
- Carry only if funding > 60% APR sustained 3+ sessions on a non-meme; size <= 25%.

## Active plans
- BTC RETEST SHORT entry_order (placed 02:51Z 13 Nov, expires 36h ~14:51Z 14 Nov): trigger 71,450 (retest of broken 71.0-71.6k shelf), stop 72,300 (~170 above 72,129 4h high), TP 68,900 (~3R), risk 1.5%. Replaced the stale 72,850 order (cancel rule triggered by drop to 70,113). If filled: trail ~200 above each new completed 4h lower high; no rejection within 2 4h candles -> scratch. If BTC bleeds < 69k without retest, cancel and re-anchor to the then-broken level (~70.0-70.5k).
- EUR CARRY (opened 16:52Z 11 Nov, 20% equity, notional 46.5): funding 84% APR now (range 73-227%). earned 0.27, net-if-closed -0.01. Close if funding < +30% APR for 2 sessions or negative, or by 20 Nov. Keep.

## Watchlist
- ETH short only on 2,060-2,100 rejection AND only if no BTC short is open/resting (same bet) -> not now.
- Alts: no fresh shorts (d1 oversold, negative funding = crowded shorts).
- Long reversal only after BTC 4h close > 74,000 with alt breadth; capitulation-reclaim long idea: if BTC wicks < 70.5k then 4h closes back > 72.6k -> consider long (cancel short first).
- PAXG: weak, falling with crypto (3,863). Long only after 4h close > 4,010. EUR directional: none while carry on.
- Polymarket: no edge found.

## Lessons
- 11-12 Nov BTC short (+8.30, TP 71,900 hit): limit short into resistance + trailing ~200 above each completed 4h lower high, extending TP below the 30d low = best trade so far. Repeat this template.
- 10-11 Nov BTC short (+3.22): 4h breakdown + retest short worked; stop 74,050 was clipped by a 74,085 wick after ~18h chop. Profit locked, but a stop just ~40 above a round number in chop gets swept: place trailing stops ~150-200 beyond the level.
- 10 Nov BONK carry: meme funding spikes collapse fast; fees > earnings. Not carry.
- ENGINE DROPS DECISIONS OLDER THAN 45 MIN. During a stall re-send once input is fresh.
- Gold safe-haven bid during crypto dumps is unreliable (6 Nov PAXG -1.88).
- Retest longs need the level above reclaimed. Time-stop rule saves risk.
- Sessions can be missed for days: resting orders need sensible expiry.
- No stop-entry orders for breaks (4 Nov BTC short filled on a sweep, -3.76).
- Retest short that doesn't reject within ~2 4h candles -> exit at scratch.
- Breakouts without alt breadth fail. Stops within ~1 h1 ATR die in chop.
- Don't short memes with deeply negative funding. Stacking same-theme bets = one bet.
- Don't open fresh at h1 RSI < 25-30 or > 74 after a big leg.
- Git: clone may be on detached HEAD; use git fetch && git checkout -B main origin/main, then commit, pull --rebase, push.
- 4h candle list: last item is IN PROGRESS; second-to-last is the latest close.

## Predictions
- None held.

## Session log
- 2026-11-13T02:51Z | eq 240.94 | BTC 70.13k new 30d low 70,113, h1 RSI 16. Cancelled stale 72,850 short entry; placed retest short entry 71,450/72,300/68,900, 1.5%, 36h. EUR carry kept (84%).
- 2026-11-13T00:52Z | eq 240.93 | BTC 70.80k new low 70,605, RSI h1 20. Kept retest short entry 72,850/73,800/70,600 and EUR carry (92% APR). No actions.
- 2026-11-12T22:46Z | eq 240.92 | BTC 71.36k slow bleed, oversold. Kept retest short entry 72,850/73,800/70,600 and EUR carry (88% APR). No actions.
- 2026-11-12T20:52Z | eq 240.90 | Engine fresh again. BTC 71.39k basing, oversold. Kept retest short entry 72,850/73,800/70,600 and EUR carry (82% APR). No actions.
- 2026-11-12T18:52Z | eq 240.88 (input stale ~2h, engine stalled since 17:01Z) | No fresh prices; kept retest short entry 72,850/73,800/70,600 and EUR carry. No actions. Next session: if input fresh, re-check BTC vs 72.6-73.06k zone.
- 2026-11-12T16:51Z | eq 240.88 | BTC 71.59k, new low 71,133, oversold (h1 RSI 21). Kept retest short entry 72,850/73,800/70,600. EUR carry kept (106% APR). No actions.
- 2026-11-12T14:51Z | eq 240.87 | BTC short TP 71,900 hit (+8.30). BTC 71.99k oversold (h1 RSI 22). Placed retest short entry 72,850 / stop 73,800 / TP 70,600, 1.5%. EUR carry kept (73% APR).
- 2026-11-12T12:55Z | eq 238.12 | BTC 72.83k, short +5.70. Trailed stop 73,950 -> 73,790, TP 72,300 -> 71,900. EUR carry kept (84% APR).
- 2026-11-12T10:52Z | eq 236.50 (input stale 85 min) | BTC 73.35k, short +4.09. Trailed stop 74,080 -> 73,950. TP 72,300. EUR carry kept (90% APR).
- 2026-11-12T08:52Z | eq 236.10 | BTC 73.47k, short +3.71. Trailed stop 74,300 -> 74,080 (4th lower 4h high 73,764). TP 72,300. EUR carry kept (200% APR).
