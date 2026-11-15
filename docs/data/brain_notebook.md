# Notebook (updated 2026-11-15T20:46Z)

## Big picture
- 20:46Z 15 Nov (input 20:43Z): BTC 65,022, drifting up. 16-20Z 4h closed 64,907 with LH 65,167 (< 65,781 < 66,087): LH sequence intact. h1 RSI 48.5, price back above h1 ema20 64,965, under h1 ema50 66,056; h4 RSI 31.5, h4 ema20 67,052. Short order 65,450 now ~0.65 h1 ATR above, between h1 ema20 and ema50 -> kept (stop 66,250 above 66,087 high). Alt funding still negative (BONK -73%, NEAR -62%, WIF -58%).
- 18:51Z 15 Nov (input 18:42Z): BTC 64,615, quiet Sunday drift. 16-20Z 4h so far H 64,905 L 64,229 (inside 12-16Z range, no new LH yet). h1 RSI 44, h1 ema20 64,957 / ema50 66,144; h4 RSI 28.8, ema20 67,238. Alts flat; meme/NEAR funding very negative (PEPE/BONK -84..-86%, NEAR -78%). LH structure intact. Short order 65,450 sits ~1.2 h1 ATR above, just above h1 ema20 -> kept.
- Trend: bearish 4h/d1 (7d -12%, 30d -20%, d1 RSI 25). Resistance 66.1k, 66.6-66.9k (h1 ema50 / broken 66.8k), 67.3k (24h high), 67.8k (h4 ema20). Support 65k, 63.8k, 62k, 61,970 low, 60k.
- Mind-changers: BTC 4h close > 66,300 (above LH 66,087) = LH structure broken -> cancel short; 4h close > 67,500 = relief rally in play -> no shorts, consider reclaim long only with alt breadth.

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21. Equity 257.51 USD (1,026 PLN; +0.14%; peak 265.7). Flat, one resting order (re-anchored 16:51Z). ~6 days left: fewer, cleaner trades, each >=2R, risk 1.5-2%.
- Trade WITH the trend: shorts into resistance / retests of broken levels via limit entry_orders re-anchored each session ~1.5-2.5 h1 ATR above price. No stop-entry break orders, no opening at h1 RSI < 30.
- Trail behind completed 4h highs (~150-250 above); pyramid only from breakeven.
- Carry only if funding > 60% APR sustained 3+ sessions on a non-meme; size <= 25%.

## Active plans
- BTC RETEST SHORT ORDER (placed 16:51Z 15 Nov, expires ~16:51Z 16 Nov): trigger 65,450, stop 66,250, TP 62,400, risk 1.5% (~3.8R). Re-anchored from 65,850/66,650 after new 4h LH 65,781. Thesis: bounce into h1 ema20 / under latest 4h LH in 4h/d1 downtrend. Once filled: trail ~200 above each new completed 4h LH; if a 4h closes < 62,500 extend TP to ~60,300. Exit at scratch if no rejection within two 4h candles. Cancel if BTC 4h closes > 66,300 before fill; re-anchor lower if BTC loses 63.8k without filling.

## Watchlist
- ETH (1,805) short only on retest of a broken level AND only if no BTC short is open/resting (same bet) -> not now.
- Alts: no fresh shorts (d1 oversold, deeply negative funding = crowded shorts). BONK -177% APR: squeeze risk, avoid.
- Capitulation-reclaim long: only if BTC 4h closes back > 67,500 with alt breadth (cancel short first); small, stop under the low.
- PAXG weak (3,797, falling with crypto). Long only after 4h close > 4,010. EUR: none.
- Polymarket: no edge found.

## Lessons
- 15 Nov: BE-trailed short (65,230) stopped at 65,362 (-0.69) by the post-capitulation relief bounce. Trailing to ~BE right after a capitulation wick is fine (small loss) but expect relief legs to retest h1 ema50; re-enter higher, don't chase.
- 15 Nov: capitulation wicks below round numbers (62k swept to 61,970) snap back 3%+ in an hour; keep short triggers/stops beyond the last 4h lower high, not inside the bounce range.
- 14 Nov: BTC retest short from 70,029 -> TP 65,300 (+17.22, best trade). Template confirmed: re-anchored limit short at broken level + trailing behind 4h lower highs + TP front-running round-number support.
- 14 Nov: TP 66,800 missed by 40 at the 66,840 sweep low. Set TPs ABOVE round numbers/obvious lows (front-run them by ~0.2-0.3%), not just below.
- EUR carry: 3 days, +0.35 funding vs 0.14+0.14 fees -> barely positive. EUR funding is erratic; size small or skip.
- 13 Nov: re-anchored retest short (1.5 h1 ATR above price, at h1 ema20 / round 70k) filled on the relief bounce and rejected within 2h -> works. Keep this re-anchor template.
- 13 Nov: 71,450 retest order was left behind by a 2.9k flush (TP passed before trigger). In fast bleeds retest levels must be re-anchored each session; consider placing them closer (~1-1.5 h1 ATR above price).
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
- 2026-11-15T20:46Z | eq 257.52 | BTC 65.0k, 4h LH 65,167 closed. Kept short order 65,450/66,250/62,400 (expires 16 Nov 16:51Z). No actions.
- 2026-11-15T18:51Z | eq 257.51 | BTC 64.6k quiet, inside 4h range. Kept short order 65,450/66,250/62,400. No actions. Polymarket: BTC weekly-dip markets no clear edge.
- 2026-11-15T16:51Z | eq 257.51 | BTC 64.5k, new 4h LH 65,781. Re-anchored short order 65,850->65,450 / stop 66,250 / TP 62,400, 1.5%, 24h.
- 2026-11-15T14:52Z | eq 257.51 | BTC rolled over to 64.6k, new 4h LH 66,087. Cancelled 66,900 order; new short order 65,850/stop 66,650/TP 62,400, 1.5%, 24h.
- 2026-11-15T12:52Z | eq 257.51 | BTC 65.4k chop under 66.1k. Kept short order 66,900/67,950/64,150 (h1 ema50 66.5k, ~1.9 ATR above). No actions.
- 2026-11-15T10:50Z | eq 257.51 | Short stopped 65,362 (-0.69) on relief bounce to 66,087. New retest short order 66,900/stop 67,950/TP 64,150, 1.5%, 18h.
- 2026-11-15T08:51Z | eq 259.75 | BTC 64.7k, short +1.7. 04-08Z 4h closed LH 65,127 -> trailed stop 65,800->65,330 (~BE), TP 62,350 kept.
- 2026-11-15T06:52Z | eq 260.90 | BTC 64.4k, short +2.8. 04-08Z 4h forming LH 65,127 (not closed). Kept stop 65,800/TP 62,350. No actions.
- 2026-11-15T04:52Z | eq 259.56 | Short order filled 65,230; BTC 64.8k. Trailed stop 66,330->65,800 (above 65,593 4h LH), TP 62,350.
- 2026-11-15T02:53Z | eq 258.19 | BTC swept 62k (61,970), V to 64.5k. Re-anchored short order to 65,250/stop 66,330/TP 62,350, 1.5%.
