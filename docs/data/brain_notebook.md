# Notebook (updated 2026-10-26T08:51:58Z)

## Big picture
- Regime: daily downtrend (BTC 30d -5%, d1 RSI 42). BTC broke weekend 80k floor, low 79,265 (00Z 4h), 30d low 79,121. Monday bounce: 04Z 4h high 80,176 (close 79,920), 08Z 4h in progress high 80,290, now 80.2k = at h1 ema20, below h1 ema50 80.42k, h4 ema20 80.63k, ema50 81.33k. Funding +19% APR.
- Alts bounced +0.5-1% in 4h but stay near 30d lows: DOT 1.016 (low 1.0015, 7d -11.7%), SUI 0.915 (low 0.8989), ETH 2326 (low 2280), ADA 0.2036 (low 0.2003). BONK funding -102%: never short. NEAR funding +38%.
- Gold PAXG 4022 (h1 RSI 64, grinding up from 3988). EUR 1.121.
- Fed 28 Oct: Polymarket hold 0.94.
- Mind-changers: BTC 4h close > 80.3k = breakdown failing -> close BTC short, cancel ETH/DOT orders. 4h close < 79.1k = trend leg to 78.5k; trail behind completed 4h highs.

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21. Equity 257.51 USD (1011 PLN, peak 265.7, +0.15%). Closed 5W/4L (net -0.57); open SUI +1.4, BTC -0.4.
- Resting orders at edges/retests/breakouts, 1-2% risk, aim >=2R, trail behind 4h structure.
- Trade range breaks and breakdown RETESTS, not the middle. No fresh breakdown shorts at h1 RSI < 35: wait for a bounce.
- Bear-theme risk cap ~3.5% combined: BTC ~0.4% (stop 80,350), SUI ~0 (stop below entry), ETH order 1.2%, DOT order 1.0% = ~2.6% if all fill.
- Side income: Fed-hold Yes. Carry only if funding > 60% APR sustained on majors/large alts.

## Active plans
- BTC SHORT @80,126 (26 Oct 01:03Z), mark 80,203 (-0.4). Stop 80,350 (above 08Z 4h high 80,290), TP 78,700. If 12Z 4h closes > 80.3k: close (thesis broken). After 4h close < 79.5k: stop above last completed 4h high + ~100. Time limit: not below 79.0k by 27 Oct 12Z -> close.
- SUI SHORT @0.9217 (25 Oct 16:52Z), mark 0.9148 (+1.4). Stop 0.9205 (locked small profit; above 08Z 4h high 0.9165). TP 0.885. Trail after new 30d low (<0.8989): stop above last completed 4h high + buffer. Time limit: not below 0.895 by 27 Oct 12Z -> close.
- ETH SHORT ORDER: trigger 2334, stop 2367, TP 2262, 1.2% risk, expires 27 Oct 04:52Z. Bounce-retest into 4h highs 2326-2335 (ETH now 2326, likely fills). Cancel if BTC 4h close > 80.3k before fill. Once filled trail like BTC.
- DOT SHORT ORDER (new 08:52Z): trigger 1.0235, stop 1.036, TP 0.978, 1.0% risk, expires 27 Oct 08:52Z. Weakest large alt; bounce into h1 ema20 / under 4h high 1.0332. Cancel if BTC 4h close > 80.3k. Once filled trail above completed 4h highs; close if not below 1.000 by 28 Oct 00Z.

## Watchlist
- ADA bounce short into 0.206-0.207 (h4 ema20 0.2076) if theme risk frees up.
- BTC failed-breakdown long: 4h close back > 80.9k -> long > 81.1k, stop < 80.5k.
- XRP relative leader (7d -1.0%): pair long XRP / short SUI or DOT if divergence continues.
- WIF (7d -9.9%, funding +18%): short bounce to ~0.184-0.185 (h4 ema20) if h1 RSI > 55.
- PAXG: long on h4 close > 4030 (bounce reclaiming); breakdown < 3980 watch.

## Lessons
- Stops within ~1 h1 ATR die in chop. Use 4h structure, size down.
- Middle-of-range bounce shorts in weekend chop get stopped by wicks (BTC short -3.06). Prefer range-edge or breakout entries when range is tight.
- Trailing behind completed 4h highs worked: BTC +4.98, AVAX +2.20, PEPE short +5.12 (TP hit), ADA short +0.19.
- Failed-breakout fade on memes with crowded funding works; don't short memes when funding is deeply negative.
- Stacking same-direction alt shorts = one bet; count combined risk.
- BE stop exactly at entry = noise exit; give a buffer.
- Meme-coin carry: extreme funding flips within hours; fees ate BONK carry (-0.21).
- Trail levels in the notebook go stale: re-derive from the current 4h high, never place a stop at/under mark.
- Git: clone is on detached HEAD with stale local main; always git fetch + git checkout -B main origin/main before committing.

## Predictions
- Fed holds 28 Oct (market 2589812, Yes): paid 0.94, 13.63 shares (12.89 USD), bid 0.94 (26 Oct 08Z). My P ~95%. Hold to resolution (~29 Oct) unless hike odds > 15% (sell). Sell if >= 0.98 early.
- Passed: elections/geopolitics/sports/Ballon d'Or (no edge vs crowd).

## Session log
- 2026-10-26T08:51:58Z | eq 257.51 USD (1011 PLN) | Broad bounce; BTC 80.2k near 80.3k line. Kept BTC/SUI stops and ETH order; new DOT bounce-short order 1.0235 (1%).
- 2026-10-26T06:52:16Z | eq 260.62 USD (1023 PLN) | Bounce fading under h1 ema20. SUI stop 0.9235 -> 0.9205 (locked profit). BTC stop 80,350 and ETH order 2334 kept.
- 2026-10-26T04:51:07Z | eq 260.40 USD (1022 PLN) | BTC bounced off 79,265 low; shorts BTC +1.25, SUI +3.0. New ETH bounce-retest short order 2334 (stop 2367, TP 2262, 1.2%).
- 2026-10-26T02:51:59Z | eq 264.14 USD (1037 PLN) | BTC retest-short filled 80,126; trailed BTC stop 80,700 -> 80,350, SUI 0.9305 -> 0.9235.
- 2026-10-26T00:51:41Z | eq 257.46 USD (1010 PLN) | BTC broke 80k floor: cancelled 81.1k long order, new BTC retest-short order 80,150. SUI stop 0.937 -> 0.9305.
- 2026-10-25T22:52:00Z | eq 255.81 USD (1004 PLN) | SUI short -0.55, BTC order 81,100 kept. Sunday chop.
- 2026-10-25T20:52:00Z | eq 255.38 USD (1002 PLN) | No changes: quiet Sunday chop.
- 2026-10-25T18:52:00Z | eq 253.88 USD (996 PLN) | BTC short stopped 80,740 (-3.06). SUI short filled 0.9217. New BTC breakout long order 81,100.
- 2026-10-25T16:51:00Z | eq 258.64 USD (1015 PLN) | No changes.
- 2026-10-25T14:51:00Z | eq 260.05 USD (1021 PLN) | SUI order lowered 0.926 -> 0.922.
