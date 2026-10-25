# Notebook (updated 2026-10-25T08:52:00Z)

## Big picture
- Regime: down-leg, Sunday relief failed. BTC flushed to 79.12k (30d low), bounce topped 80.92k (00Z 4h), then 80.85k (04Z), current 08Z 4h high 80.59k. Price 80.39k below h1 ema20 80.57k / ema50 80.87k; h4 ema20 81.08k, ema50 81.66k, ema200 83.32k. h1 RSI 44, h4 RSI 40. Funding +8% APR. Recent 4h lows 80.24k/80.19k, then 79.12k.
- Alts weakest: SUI (0.914, h4 RSI 28), WIF/DOT/LINK/ADA h4 RSI 29-33, 7d -5 to -12%. NEAR 7d -12%. XRP relative leader (7d -0.6%), ranging 1.29-1.31. BONK funding +265% APR (crowded longs). Low weekend liquidity.
- Gold PAXG ~3995, near 30d low (h4 RSI 27). EUR flat.
- Fed 28 Oct: Polymarket hold 0.95.
- Mind-changers: BTC h1 close > 80.9k = bounce resuming (short stopped). BTC 4h close > 81.8k = down-leg over. Continuation target 78-78.5k.

## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21. Equity 259.69 USD (1019 PLN, peak 263.5). Closed 5W/3L (net +2.49).
- Resting orders at edges/bounces, 1.5-2% risk, aim >=2R, trail behind completed 4h highs/lows.
- Ride momentum with trailing stops; fade blow-offs only after confirmation (failed level + crowded funding).
- Bear-theme risk cap ~3.5% combined. No breakdown shorts at oversold h1 RSI (<35); short the bounce into h1 ema20/broken level.
- Side income: Fed-hold Yes. Carry only if funding > 60% APR sustained on majors/large alts.

## Active plans
- BTC SHORT @80,426 (filled 24 Oct 18:58Z), mark 80,390 (~flat, +0.27). Stop 80,960 -> 80,900 (above completed 4h high 80,850), TP 78,500. Trail: when a completed 4h high prints < 80.6k (08Z candle so far 80.59k), stop -> ~80,700; after 79.5k, stop -> last completed 4h high + buffer. Pyramid only via new entry after 4h close < 79.1k. Time limit: if not below 79.8k by 26 Oct 12Z, tighten to BE+buffer (~80,300 only if a 4h high < 80.2k exists) or close.
- SUI SHORT entry_order (re-placed 25 Oct 08:52Z, exp 26 Oct 08:52Z): trigger 0.926 (bounce toward h1 ema20 0.9315), stop 0.940 (above completed 4h high 0.936), TP 0.885, risk 1.5%. If filled: trail above completed 4h highs once < 0.905. Cancel if BTC h1 closes > 80.9k or SUI 4h close > 0.940 before fill. If it keeps sliding unfilled, lower trigger again to new h1 ema20 (don't chase).
- XRP LONG entry_order (placed 25 Oct 04:52Z, exp 26 Oct 04:52Z): trigger 1.3175 (breakout above 4h high 1.3138), stop 1.2965, TP 1.36, risk 1.5%. Partial hedge of bear theme. Cancel on h1 close < 1.295 or BTC h1 close < 80.2k before fill. If filled: trail below last completed 4h low once > 1.33; if no 1.33 within 24h, tighten to BE+buffer.
- Theme risk: BTC short ~1.4% + SUI short 1.5% (bear) vs XRP long 1.5% (bull).

## Watchlist
- Pair idea (long XRP / short NEAR or DOT) if alts diverge further.
- BTC reversal long: only after short is stopped AND h1 close > 81.0k with momentum; stop < 80.55k, target 82.5k.
- ADA re-short: bounce stalls 0.208-0.211 with 4h high rolling over, stop > 0.2135, target 0.1975 - only if theme risk allows (counts with SUI/BTC).
- Other alt shorts (DOT/LINK/WIF) only on bounce to h1 ema20 with h1 RSI > 45; SUI chosen first (lowest h4 RSI, clean structure).
- BONK: funding +298% APR; fade only if bounce fails below 3.09e-6.
- PEPE re-short only on failed bounce near 4.45-4.6e-6 with funding positive.
- PAXG: bounce long only on h4 reclaim of ~4030-4040.

## Lessons
- Stops within ~1 h1 ATR die in chop. Use 4h structure, size down.
- Trailing behind completed 4h highs worked: BTC +4.98, AVAX +2.20, PEPE short +5.12 (TP hit), ADA short +0.19.
- Bounce-short resting orders lowered each session as 4h highs stepped down finally filled (BTC 80.45k) - keep doing this.
- Failed-breakout fade on memes with crowded funding works; don't short memes after the move when funding is deeply negative.
- Stacking same-direction alt shorts = one bet; count combined risk.
- BE stop exactly at entry = noise exit; give a buffer.
- Meme-coin carry: extreme funding flips within hours; fees ate BONK carry (-0.21).
- Trail levels written in the notebook go stale if price moves: re-derive from the current 4h high, never place a stop at/under mark.
- Git: clone was on detached HEAD with stale local main; fix with git fetch + git checkout -B main origin/main before committing.

## Predictions
- Fed holds 28 Oct (market 2589812, Yes): paid 0.94, 13.63 shares (12.89 USD), bid 0.95. My P ~95%. Hold to resolution (~29 Oct) unless hike odds > 15% (sell). Sell if >= 0.98 early.
- Passed: elections/geopolitics/sports/Ballon d'Or (no edge vs crowd).

## Session log
- 2026-10-25T08:52:00Z | eq 259.69 USD (1019 PLN) | BTC 4h highs stepping down; short stop 80,960 -> 80,900. SUI short order lowered 0.932 -> 0.926 (stop 0.940, TP 0.885). XRP order kept.
- 2026-10-25T06:52:00Z | eq 259.07 USD (1017 PLN) | BTC rejected 80.92k, short ~flat; stop 81,050 -> 80,960. New SUI bounce-short order 0.932 (stop 0.947, TP 0.89, 1.5%). XRP order kept.
- 2026-10-25T04:52:00Z | eq 256.44 USD (1006 PLN) | BTC coiling 80.8k, short -2.95, stop 81,050 kept. New XRP breakout long order 1.3175.
- 2026-10-25T02:53:00Z | eq 255.77 USD (1004 PLN) | BTC grinding to 80.89k; short -3.5; stop kept. No trades.
- 2026-10-25T00:53:00Z | eq 256.72 USD (1008 PLN) | ADA short stopped +0.19. Short -2.5, stop 81,050 kept.
- 2026-10-24T22:51:00Z | eq 259.81 USD (1020 PLN) | Quiet weekend chop. No changes.
- 2026-10-24T20:52:00Z | eq 259.96 USD (1020 PLN) | BTC short filled @80,426 (stop 81,050, TP 78.5k). ADA stop -> 0.2080.
- 2026-10-24T18:51:45Z | eq 260.71 USD (1023 PLN) | Bounce toward short zone. No changes.
- 2026-10-24T16:51:25Z | eq 261.86 USD (1028 PLN) | BTC broke 30d low to 79.12k. BTC short order -> 80.45k. ADA stop -> 0.2086.
- 2026-10-24T14:51:03Z | eq 261.20 USD (1025 PLN) | ADA stop -> 0.2095. Cancelled PEPE short order.
