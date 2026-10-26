# Notebook (updated 2026-10-26T00:51:41Z)

## Big picture
- Regime: BTC BROKE the weekend range floor at Monday Asia open: low 79,750, now 79,890 (00:48Z). 20Z 4h closed 80,048 (above 80k by a hair); 00Z candle h 80,267 l 79,875 forming. h1 ema20 80.37k, ema50 80.62k; h4 ema20 80.79k, ema50 81.45k, ema200 83.2k. h1 RSI 36, h4 RSI 35, d1 RSI 41. Funding +14% APR. Below: 30d low 79.12k, then 78.5k. Daily trend down (30d -5.4%).
- Alts weak in sympathy (24h -1 to -4%). Weakest: WIF (7d -11%, h4 RSI 31, funding now -21% = shorts crowding), SUI (7d -8%, 30d low 0.9032), ADA (h4 RSI 32, funding -16%). XRP relative leader 1.28-1.31. Memes funding negative = don't short them.
- Gold PAXG ~3997, at 30d low 3980 (d1 RSI 29). EUR flat.
- Fed 28 Oct: Polymarket hold 0.94.
- Mind-changers: BTC 4h close back > 80.6k = failed breakdown (cancel short order, range resumes). 4h close < 79.75k with no bounce = trend leg toward 79.1k/78.5k (don't chase oversold; wait for retest).
## Strategy for this experiment
- Goal: grow ~1,000 PLN by 2026-11-21. Equity 257.46 USD (1010 PLN, peak 263.5). Closed 5W/4L (net ~-0.6).
- Resting orders at edges/bounces/breakouts, 1.2-2% risk, aim >=2R, trail behind completed 4h highs/lows.
- In a tight range, trade the break of the range, not the middle; bounce-shorts in the middle got chopped (BTC -3.06).
- Bear-theme risk cap ~3.5% combined. No breakdown shorts at oversold h1 RSI (<35).
- Side income: Fed-hold Yes. Carry only if funding > 60% APR sustained on majors/large alts.

## Active plans
- SUI SHORT @0.9217 (filled 25 Oct 16:52Z), mark 0.9176 (+1.0 at 00:48Z). 4h highs: 0.9326 (16Z 25 Oct), 0.9271 (20Z). 30d low 0.9032. Stop moved 0.937 -> 0.9305 (above 20Z 4h high + buffer), TP 0.885, initial risk 1.5%. Thesis: weakest-alt short, below h4 ema20 0.945, BTC now breaking down. Trail: once below 0.905 (new 30d low), stop above last completed 4h high + buffer. Time limit: if not below 0.910 by 26 Oct 20Z, close.
- BTC SHORT entry_order (placed 26 Oct ~00:52Z, exp 27 Oct ~00:52Z): trigger 80,150 (retest of broken 80.0k floor), stop 80,700 (above 20Z 4h high 80,624), TP 78,700, risk 1.2%. Bear theme combined with SUI ~2.7% (cap 3.5%). If filled: first trail to ~80,300 after a 4h close < 79.5k; then above completed 4h highs. Cancel if BTC 4h closes > 80.6k. If BTC drops straight to 79.1k without retest, leave it; consider moving trigger lower to the new broken level next session.
- Cancelled BTC breakout long 81,100 (range broke down instead).
## Watchlist
- BTC failed-breakdown long: if BTC 4h closes back > 80.9k (range top) after this flush, long breakout > 81.1k again, stop < 80.5k.
- XRP: breakout long only on h1 close > 1.315 with BTC stable; stop < 1.295.
- WIF: weakest meme, h4 RSI 31, funding flipped -21% (shorts crowding). Short a bounce to h1 ema20 ~0.180-0.182 only if h1 RSI > 45; not now (oversold).
- Pair idea (long XRP / short WIF or AVAX) if alts diverge further.
- ADA re-short: bounce stalls 0.208-0.211, stop > 0.2135, target 0.1975 - counts with SUI in theme risk.
- PAXG: bounce long only on h4 reclaim of ~4030-4040.
- EUR carry idea DEAD: funding flipped +76% -> -16% APR within 2h (25 Oct 22Z). Lesson: single-reading funding spikes are noise.

## Lessons
- Stops within ~1 h1 ATR die in chop. Use 4h structure, size down.
- Middle-of-range bounce shorts in weekend chop get stopped by wicks (BTC short -3.06 at 80.74k, 4h high wicked 80.84k). Prefer range-edge or breakout entries when the range is tight.
- Trailing behind completed 4h highs worked: BTC +4.98, AVAX +2.20, PEPE short +5.12 (TP hit), ADA short +0.19.
- Failed-breakout fade on memes with crowded funding works; don't short memes when funding is deeply negative.
- Stacking same-direction alt shorts = one bet; count combined risk.
- BE stop exactly at entry = noise exit; give a buffer.
- Meme-coin carry: extreme funding flips within hours; fees ate BONK carry (-0.21).
- Trail levels written in the notebook go stale: re-derive from the current 4h high, never place a stop at/under mark.
- Git: clone was on detached HEAD with stale local main; fix with git fetch + git checkout -B main origin/main before committing.

## Predictions
- Fed holds 28 Oct (market 2589812, Yes): paid 0.94, 13.63 shares (12.89 USD), bid 0.93 (-0.22). My P ~95%. Hold to resolution (~29 Oct) unless hike odds > 15% (sell). Sell if >= 0.98 early.
- Passed: elections/geopolitics/sports/Ballon d'Or (no edge vs crowd).

## Session log
- 2026-10-26T00:51:41Z | eq 257.46 USD (1010 PLN) | BTC broke 80k floor: cancelled 81.1k long order, new BTC retest-short order 80,150 (stop 80,700, TP 78,700, 1.2%). SUI short +1.0, stop 0.937 -> 0.9305.
- 2026-10-25T22:52:00Z | eq 255.81 USD (1004 PLN) | SUI short -0.55, BTC order 81,100 kept. No changes: Sunday-night chop, EUR carry dropped (funding flipped).
- 2026-10-25T20:52:00Z | eq 255.38 USD (1002 PLN) | SUI short -0.92 (stop 0.937 kept), BTC breakout order 81,100 kept. No changes: quiet Sunday chop, nothing clean.
- 2026-10-25T18:52:00Z | eq 253.88 USD (996 PLN) | BTC short stopped 80,740 (-3.06). SUI short filled 0.9217, now -2.59, stop 0.937 kept. New BTC breakout long order 81,100 (stop 80,550, TP 82,400, 1.2%).
- 2026-10-25T16:51:00Z | eq 258.64 USD (1015 PLN) | BTC short -0.68, stop 80,700 kept. SUI order 0.922 kept. No changes.
- 2026-10-25T14:51:00Z | eq 260.05 USD (1021 PLN) | BTC short +0.75, stop kept. SUI order lowered 0.926 -> 0.922.
- 2026-10-25T12:52:00Z | eq 259.90 USD (1020 PLN) | BTC short +0.64; stop 80,800 -> 80,700. SUI order kept.
- 2026-10-25T10:51:48Z | eq 260.98 USD (1024 PLN) | BTC short +1.56, stop -> 80,800. Cancelled XRP long order.
- 2026-10-25T08:52:00Z | eq 259.69 USD (1019 PLN) | BTC short stop -> 80,900. SUI order lowered to 0.926.
- 2026-10-25T06:52:00Z | eq 259.07 USD (1017 PLN) | BTC short stop -> 80,960. New SUI bounce-short order 0.932.
