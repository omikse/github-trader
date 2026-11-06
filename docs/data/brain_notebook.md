# Notebook (updated 2026-11-06T12:53Z)

## Big picture
- 12:28Z 6 Nov: BTC 76,201, base 75.1-76.3k holding, h1 RSI 43, h1 ema20 76.33k (reclaiming), h4 ema20 77.36k, h4 ema50 78.08k. ETH 2,245, XRP 1.199 (near 30d low 1.176), PAXG 4,056, EUR 1.1170 (h1 RSI 29). NFP 13:30Z next.
- 10:43Z 6 Nov: BTC 76,147, small bounce off 75.2k (08Z 4h closed 75,517; current 4h 75,374-76,190). h1 RSI 41, h1 ema20 76.39k, h4 ema20 77.50k (= my short trigger), h4 ema50 78.16k. ETH 2,239, XRP 1.198 (new 30d low 1.176 at 04-08Z), PAXG 4,057, EUR 1.1170 (h1 RSI 29, weak). Still bearish regime, coil pre-NFP 13:30Z.
- 5 Nov: BREAKDOWN. 12-16Z 4h candle BTC 80,296 -> low 75,420 (new 30d low) -> close 75,902. Since then a weak bear flag: 16-20Z 4h 75,936/76,963/75,555/76,247; now 76,059, h1 RSI 27. h1 ema20 78.1k and h4 ema20 78.1k falling. ETH 2,247 (low 2,234), alts -4..-8% 24h. The 4 Nov breakout above 78.6k failed -> bearish regime until BTC reclaims 79k on a 4h close.
- Gold: PAXG 4,056, failed to hold h4 ema200 4,082. Res 4,082, 4,105; sup 4,033 (h4 ema20), 4,000. No gold trade until it reclaims 4,082 on a 4h close.
- BTC levels: res 76.96k (bounce high), 77.5k, 78.1-78.6k (emas / old floor), 79.9k; sup 75.4k, then 74k. h4 ema200 81.4k.
- ETH levels: res 2,284, 2,317 (h4 ema20), 2,350; sup 2,234, 2,170 (30d low).
- Mind-changers: BTC 4h close > 79,000 = sweep, drop bear plan. Close < 75,400 = continuation (don't chase; wait for retest of 75.4-76k).
- NFP Fri 6 Nov 13:30Z.

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21. Equity 229.19 USD (896 PLN, -10.9%; peak 265.7). Closed 8W/22L. 15.6 days left: fewer, cleaner trades, each >=2R.
- Trade WITH confirmed breaks, on retests not chases. Entries after 4h CLOSE beyond a level. No stop-entry break orders. Stops behind 4h structure, risk 1-2%.
- Trail behind completed 4h highs/lows; pyramid only from breakeven.
- Carry only if funding > 60% APR sustained 3+ sessions; size <= 25%.

## Active plans
- BTC SHORT entry_order (re-placed 12:53Z 6 Nov, exp ~12:53Z 7 Nov): trigger 77,500 (~h4 ema20), stop 79,000, TP 74,000, 1.5% risk (~2.3R). Thesis: short a post-NFP bounce into falling emas/broken level in bear regime. Cancel if 4h close > 79,000 before fill. If filled: no rejection within 2 4h candles -> scratch; once < 76k move stop to 77.8k; trail above completed 4h highs. If BTC breaks < 75.1k on a 4h close, cancel and switch to the retest-short watchlist idea. If unfilled by expiry, re-evaluate (lower to h4 ema20 if it has fallen).

## Watchlist
- ETH short only if BTC order is not used: retest 2,317-2,350 rejecting (same theme as BTC short, don't stack both).
- Long reversal only after BTC 4h close > 79k (sweep reclaim) -> long retest ~78.6k, stop < 77.5k.
- EUR long only on 4h close > 1.1270.
- No shorts on memes/SOL/SUI/LINK with deeply negative funding (squeeze risk). BONK funding -93% APR.
- NEAR funding now 19% APR (dropped) - no carry.
- EUR perp funding 127% (04:50Z), 89.5% (06/08Z), 115% (10:43Z) - feed is live. Break-even ~2.4 days but on <=25% size the payoff is ~0.3 USD: not worth it before NFP (EUR can move hard). Reconsider after NFP if still >60%. PAXG 25%: no.
- Polymarket: bet only with clear >5pt edge. 12:50Z BTC>74k Nov6 ask 94.7c vs fair ~95%: no. 08:50Z BTC>74k Nov6 ask 87.5c vs fair ~84% (NFP risk): no. 06:50Z checked BTC>78k Nov6 9c (fair ~6%), BTC>74k Nov6 84c (fair ~80%): no edge.
- If BTC 4h closes < 75,100 and then retests 75.1-75.6k from below with rejection -> short retest, stop above 76.3k (4h structure), TP 72.5k, 1.5%. Not if h1 RSI < 30.

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
- Git: clone may be on detached HEAD; checkout main, pull --rebase, commit, push.
- 4h candle list: last item is IN PROGRESS; second-to-last is the latest close.
- Web search for "bitcoin news <date>" mostly returns stale 2025 articles; don't waste searches on it.

## Predictions
- None held.

## Session log
- 2026-11-06T12:53Z | eq 229.19 | Re-placed BTC 77.5k short order (stop 79k, TP 74k, 1.5%, 24h) as old one expired; pre-NFP, BTC 76.2k. No Polymarket edge.
- 2026-11-06T10:51Z | eq 229.19 | No action. BTC 76.1k small bounce, h1 RSI 41. 77.5k short order kept (exp 12:52Z). Next session (~12:50Z, pre-NFP): re-place a 77.5-78.1k short-the-bounce order with ~24h expiry unless BTC has already reclaimed 77.5k on a 4h close.
- 2026-11-06T08:52Z | eq 229.19 | No action. BTC 75.6k coiling into NFP. 77.5k short order kept (exp 12:52Z, = h4 ema20). Next session (10:50Z) is the last before NFP: decide whether to re-place a post-NFP short-the-bounce order.
- 2026-11-06T06:52Z | eq 229.19 | No action (input 40 min stale, BTC 75.4k bleeding toward 75.1k, RSI 28). 77.5k short order kept (exp 12:52Z).
- 2026-11-06T04:52Z | eq 229.18 | No action. BTC 75.7k still coiling, 4h close 75,802. 77.5k short order kept (exp 12:52Z). No Polymarket edge.
- 2026-11-06T02:52Z | eq 229.18 | No action. PAXG long stopped 4,053 (-1.88). BTC coiling 75.1-76.3k; 77.5k short order kept (exp 12:52Z, pre-NFP).
- 2026-11-06T00:51Z | eq 231.15 | No action. BTC swept 75.1k, closed 4h 75,980, bounce 76.2k. BTC 77.5k short order + PAXG long kept. Skipped Polymarket BTC>78k Nov 6 (17c, fair ~15%).
- 2026-11-05T22:52Z | eq 230.59 | No action. BTC 75.7k drifting to flag low, ETH new low 2,215. BTC 77.5k short order + PAXG long kept.
- 2026-11-05T20:51Z | eq 231.22 | BTC bear-flag 75.5-77k. Moved BTC short order 78.3k -> 77.5k (stop 79k, TP 74k, 1.5%). PAXG long held (4,091, stop 4,055).
- 2026-11-05T18:51Z | eq 232.35 (stale) | No action: input 1h51m stale. Orders/positions left as planned.
