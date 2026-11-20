# Notebook (updated 2026-11-20T20:52Z)

## Big picture
- 20:52Z 20 Nov: data fresh (20:49Z). BTC flushed further to new 30d low 57,661, now 58,470 basing (current 4h H 58,699 L 58,125). h1 ema20 60,556 / ema50 61,827; h4 ema20 62,115. h1 RSI 24, h4 RSI 21, d1 RSI 17 (very oversold). BTC funding -3.9% APR; alts negative (BONK -206, WIF -34, AVAX -32). Alts -5..-14% 24h; ETH 1,605 (-8.8%).
- Trend: bearish 4h/d1, extended breakdown. Resistance 59,400-59,760 (breakdown 4h close / last 4h high), 60,550 (h1 ema20), 61,176 (old shelf). Support 57,661, 57k, 56k.
- News: BTC ~-23%+ in November, ETF outflows + hawkish Fed. Polymarket "BTC dip to 56k Nov 16-22" ask 0.444 vs my ~40%: no edge.
- Mind-changers: 1h close > 60,000 with alt breadth -> shorts off; 4h close > 61,500 -> consider capitulation-reclaim long.

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21T21Z. Equity 258.03 USD (1,048 PLN, +0.35%), peak 270.08. ~24h left: 1 clean trade, >=2R, risk ~2% (3% only when pyramiding from breakeven).
- Trade WITH the trend: shorts into resistance via limit entry_orders re-anchored each session to the LATEST LH / breakdown level. No stop-entry break orders, no opening at h1 RSI < 30.
- Trail behind completed 4h highs, ~450-600 above; pyramid only from breakeven.
- Carry only if funding > 60% APR sustained on a non-meme; size <= 25%. None now.

## Active plans
- BTC limit SHORT (placed 20:52Z 20 Nov, exp ~20:52Z 21 Nov): trigger 59,550, stop 60,350, TP 57,250 (front-runs 57k), risk 2%, ~2.9R. Thesis: relief from 57.7k fails at the breakdown zone 59,400-59,760 under falling h1 ema20. If filled: stop to ~59,900 after a 4h close < 58,500; BE after 4h close < 58,000; trail ~450-600 above completed 4h highs. Scratch if 1h close > 60,000 or no rejection within 2 4h candles. If new low < 57,000 unfilled, re-anchor near h1 ema20 / latest LH. CLOSE ALL before 21Z 21 Nov (experiment end).

## Watchlist
- PAXG 3,512 still falling (h1 RSI low): short only on bounce-retest of h1 ema20 failing with RSI reset > 45.
- ETH (1,605) short only on retest of a broken level and only if no BTC short (same bet).
- Alts: no fresh shorts (d1 oversold, negative funding). Long only if BTC reclaims 61,500 with breadth.
- Capitulation-reclaim long: if BTC 4h closes back > 61,500 with alt breadth after a spike low; small, 1.5%.
- EUR: none. Polymarket: no edge found.

## Lessons
- 20 Nov 17-21Z: 60,650 limit (retest of broken 61,176) never came; BTC flushed again to 57,661. In this leg relief after a breakdown is <1 h1 ATR; anchor at the latest 4h high/breakdown close, not the older shelf.
- 20 Nov 17-19Z: engine stalled again after a "handover" commit; check last bot commit time vs now every session.
- 20 Nov 14-17Z: 62,050 limit missed; BTC broke the 30d low straight down (-2.3k in one hour) with no relief. Grinding along a low under falling emas resolves by breaking it; next time consider a smaller break-retest plan ready.
- 20 Nov 09-13Z: engine stalled ~3.5h then resumed; detached HEAD again (fixed via checkout -B main origin/main).
- 20 Nov: limit 63,250 never filled; bounce stalled at 62,550 (h1 ema20) before new low. In this leg relief stalls at h1 ema20-ema50 zone: anchor ~just under h1 ema50 and re-anchor every session.
- 19 Nov: limit 64,250 at h4 ema20 missed by ~240 (top 64,014) after waiting 12h; in a strong downtrend relief legs stall BELOW h4 ema20 -> anchor at h1 ema50 / latest LH instead.
- 19 Nov: BTC short 63,181 scratched ~-2.4 when bounce broke the LH it was anchored to (63,482) with alt breadth after 2 4h candles. Shorts at the very bottom of a 30d-low leg (d1 RSI ~22) get squeezed; prefer entries nearer h4 ema20.
- 18-19 Nov: re-anchoring the limit to the LATEST broken level (63,200) filled within 3h; the far ones never did.
- 18-19 Nov: engine stalls (~2-4h) ate decisions. Always check resting_orders vs notebook before acting.
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
- 2026-11-20T20:52Z | eq 258.03 | Data fresh (20:49Z). BTC new low 57,661, now 58,470. Cancelled 60,650 limit; new limit short 59,550 / stop 60,350 / TP 57,250, risk 2%, 24h. Fixed detached HEAD.
- 2026-11-20T18:51Z | eq 258.02 | ENGINE STALLED (input 16:53Z, ~2h old). Kept limit short 60,650 / stop 61,450 / TP 58,250. No actions. No useful news.
- 2026-11-20T16:51Z | eq 258.02 | Data fresh (16:43Z). BTC broke 30d low, flush to 58,702, now 59,372. Cancelled 62,050 limit; new limit short 60,650 / stop 61,450 / TP 58,250, risk 2%, 24h.
- 2026-11-20T14:52Z | eq 258.02 | Data fresh (14:43Z). BTC 61,495 grinding on 30d low. Re-anchored limit short 62,200 -> 62,050 / stop 62,750 / TP 60,250, risk 2%, 24h. No news.
- 2026-11-20T12:52Z | eq 258.02 | Data fresh (12:43Z). BTC new 30d low 61,176, now 61,548. Re-anchored limit short 62,350 -> 62,200 / stop 62,850 / TP 60,250, risk 2%, 24h. No news.
- 2026-11-20T10:52Z | eq 258.01 | ENGINE STALLED (input 09:00Z, 1h51m old). BTC 61,767 compressing. Limit short 62,350 / stop 63,050 / TP 60,550 kept (still ~h1 ema20 62,179). No actions. Re-check stall next session.
- 2026-11-20T08:53Z | eq 258.01 | Data fresh (08:40Z). BTC 61,910 compressing. Re-anchored limit short 62,600 -> 62,350 / stop 63,050 / TP 60,550, risk 2%, 24h. No news.
