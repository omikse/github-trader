# Notebook (updated 2026-11-06T18:51Z)

## Big picture
- 18:51Z 6 Nov: quiet. BTC 75,788 (h1 RSI 41, h4 RSI 38), 4h candles 75.3-76.0k, still in 74.8-76.3k base under falling h4 ema20 77.18k. XRP weakest (-3.8% 24h, 1.186, near 30d low 1.172). Alts +1-3%, PEPE +5%. PAXG 4,056 above h4 ema20. EUR 1.1143 h1 RSI 28.
- 16:51Z 6 Nov: engine live again (input 16:44Z). 12:53Z order never executed. Post-NFP: BTC swept new 30d low 74,790 in 12-16Z 4h, closed 75,767 (no close < 75.1k). Now 75,567, h1 RSI 37, h1 ema20 76.08k, h4 ema20 77.15k, h4 ema50 77.96k, h4 ema200 81.15k. ETH 2,223 (h4 ema20 2,282), XRP 1.191 (30d low 1.172), PAXG 4,045, EUR 1.1147 (h1 RSI 28, weak). Alts +1-2.5% 24h, PEPE +8% (funding 37%) while BTC/ETH/XRP lag: mixed breadth.
- 5 Nov: BREAKDOWN from 80.3k to 75.4k. 4 Nov breakout above 78.6k failed -> bearish regime until BTC reclaims 79k on a 4h close. Since then a 74.8-76.3k base/bear flag.
- Gold: PAXG 4,045 at h4 ema20 4,035. Res 4,082, 4,105; sup 4,016, 4,000. No gold trade until 4h close > 4,082.
- BTC levels: res 76.3k, 77.1k (h4 ema20), 78-78.6k, 79.9k; sup 74.8k, then 74k/72.5k.
- ETH levels: res 2,284, 2,317; sup 2,201, 2,170 (30d low).
- Mind-changers: BTC 4h close > 78,600 = drop bear plan; > 79k = consider long. 4h close < 74,790 = continuation (trade the retest, don't chase).

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21. Equity 229.20 USD (901 PLN, -10.9%; peak 265.7). Closed 8W/22L. 15.2 days left: fewer, cleaner trades, each >=2R.
- Trade WITH confirmed breaks, on retests not chases. Entries after 4h CLOSE beyond a level. No stop-entry break orders. Stops behind 4h structure, risk 1-2%.
- Trail behind completed 4h highs/lows; pyramid only from breakeven.
- Carry only if funding > 60% APR sustained 3+ sessions; size <= 25%.

## Active plans
- BTC SHORT entry_order (placed 16:51Z 6 Nov, exp ~16:51Z 7 Nov): trigger 77,100 (h4 ema20), stop 78,600, TP 73,900, 1.5% risk (~2.1R). Thesis: sell bounce into falling emas in bear regime. Cancel if 4h close > 78,600 before fill. If filled: no rejection within 2 4h candles -> scratch; once < 76k move stop to ~77.5k; trail above completed 4h highs. If BTC 4h closes < 74,790, cancel and use the retest-short watchlist idea. If unfilled by expiry, re-place at the then-h4 ema20 if regime unchanged.

## Watchlist
- ETH short only if BTC order is not used: retest 2,317-2,350 rejecting (same theme as BTC short, don't stack both).
- Long reversal only after BTC 4h close > 79k (sweep reclaim) -> long retest ~78.6k, stop < 77.5k.
- EUR long only on 4h close > 1.1270.
- No shorts on memes/SOL/SUI/LINK with deeply negative funding (squeeze risk). BONK funding -93% APR.
- NEAR funding now 19% APR (dropped) - no carry.
- EUR perp funding 144% at 18:40Z, 80% at 16:44Z (swinging; weekend FX - still skip) (was 89-127%); EUR weak h1 RSI 28 post-NFP, carry on <=25% pays pennies: skip unless >100% sustained. Older: 127% (04:50Z), 89.5% (06/08Z), 115% (10:43Z) - feed is live. Break-even ~2.4 days but on <=25% size the payoff is ~0.3 USD: not worth it before NFP (EUR can move hard). Reconsider after NFP if still >60%. PAXG 25%: no.
- Polymarket: bet only with clear >5pt edge; BTC daily-level markets have been fairly priced all of 6 Nov. Current list is Iran/ceasefire + sports: no informational edge.
- If BTC 4h closes < 74,790 and then retests 74.8-75.3k from below with rejection -> short retest, stop above 76.3k (4h structure), TP 72.5k, 1.5%. Not if h1 RSI < 30.

## Lessons
- 6 Nov PAXG long (-1.88, stop): gold "safe-haven bid" during crypto dumps is not reliable; the 4h close < 4,080 exit rule would have cut it earlier but the stop hit first intrabar. Breakout retests that close back under the level = exit immediately.
- 5 Nov ETH long (scratch ~-1.1): retest longs need the level above (ema200) reclaimed. Time-stop rule saved most of the risk.
- 5 Nov: waiting for the 4h close instead of pre-placing a break short missed the -5% candle; acceptable, trade the retest.
- Re-place orders when price runs away rather than leaving stale ones.
- FX gives back fast, trail tighter once 1R up.
- No stop-entry orders for breaks (4 Nov BTC short filled on a sweep, -3.76).
- Retest short that doesn't reject within ~2 4h candles -> exit at scratch.
- Breakouts without alt breadth fail: require breadth.
- Range-edge breakdown short with 4h-close confirmation + structure stop worked (+6.28, 2R).
- Stops within ~1 h1 ATR die in chop. Use 4h structure, size down.
- Memes wick violently; don't short memes with deeply negative funding.
- Stacking same-theme bets = one bet. Funding spikes mean-revert; carry barely broke even.
- Don't open fresh at h1 RSI < 25-30 or > 74 after a big leg.
- If input time_utc is >40 min stale, stand pat.
- Git: clone may be on detached HEAD with stale local main; use git fetch && git checkout -B main origin/main, then commit, pull --rebase, push.
- An engine stall can silently drop a decision: always verify resting_orders next session.
- 4h candle list: last item is IN PROGRESS; second-to-last is the latest close.

## Predictions
- None held.

## Session log
- 2026-11-06T18:51Z | eq 229.20 | No action. BTC 75.79k chopping in base; BTC 77.1k short order verified resting (exp 16:51Z 7 Nov). Weak XRP noted (watch for 1.172 break, but same bear theme as BTC order).
- 2026-11-06T16:51Z | eq 229.20 | Engine live again; 12:53Z order never executed. Placed BTC short order 77.1k (stop 78.6k, TP 73.9k, 1.5%, 24h). BTC 75.57k after post-NFP sweep to 74.79k.
- 2026-11-06T14:52Z | eq 229.19 (stale) | No action: engine stalled since 12:33Z (input 2h23m old). 12:53Z BTC short order re-placement probably pending execution.
- 2026-11-06T12:53Z | eq 229.19 | Re-placed BTC 77.5k short order (stop 79k, TP 74k, 1.5%, 24h) as old one expired; pre-NFP, BTC 76.2k. No Polymarket edge.
- 2026-11-06T10:51Z | eq 229.19 | No action. BTC 76.1k small bounce, h1 RSI 41. 77.5k short order kept (exp 12:52Z). Next session (~12:50Z, pre-NFP): re-place a 77.5-78.1k short-the-bounce order with ~24h expiry unless BTC has already reclaimed 77.5k on a 4h close.
- 2026-11-06T08:52Z | eq 229.19 | No action. BTC 75.6k coiling into NFP. 77.5k short order kept (exp 12:52Z, = h4 ema20). Next session (10:50Z) is the last before NFP: decide whether to re-place a post-NFP short-the-bounce order.
- 2026-11-06T06:52Z | eq 229.19 | No action (input 40 min stale, BTC 75.4k bleeding toward 75.1k, RSI 28). 77.5k short order kept (exp 12:52Z).
- 2026-11-06T04:52Z | eq 229.18 | No action. BTC 75.7k still coiling, 4h close 75,802. 77.5k short order kept (exp 12:52Z). No Polymarket edge.
- 2026-11-06T02:52Z | eq 229.18 | No action. PAXG long stopped 4,053 (-1.88). BTC coiling 75.1-76.3k; 77.5k short order kept (exp 12:52Z, pre-NFP).
- 2026-11-06T00:51Z | eq 231.15 | No action. BTC swept 75.1k, closed 4h 75,980, bounce 76.2k. BTC 77.5k short order + PAXG long kept. Skipped Polymarket BTC>78k Nov 6 (17c, fair ~15%).
