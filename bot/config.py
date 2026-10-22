"""All tunable settings in one place. Values can be overridden with environment variables."""
import os


def _f(name, default):
    return float(os.getenv(name, default))


# --- Account -----------------------------------------------------------------
START_PLN = _f("START_PLN", "1000")          # simulated starting capital
SYMBOLS = [s.strip() for s in os.getenv("SYMBOLS", "BTCUSDT,ETHUSDT,SOLUSDT,XRPUSDT,DOGEUSDT,ADAUSDT,AVAXUSDT,LINKUSDT,SUIUSDT,PEPEUSDT,WIFUSDT,BONKUSDT,LTCUSDT,DOTUSDT,NEARUSDT,PAXGUSDT,EURUSDT").split(",") if s.strip()]
END_AT = os.getenv("END_AT", "2026-11-21T21:00:00Z")  # experiment ends, everything is closed

# --- Brain -------------------------------------------------------------------
# "session": a Claude scheduled task (on the Claude subscription) writes docs/data/brain_decision.json.
# "api": the bot calls the paid Claude API itself (needs ANTHROPIC_API_KEY).
BRAIN_MODE = os.getenv("BRAIN_MODE", "session")
DECISION_MAX_AGE_MIN = _f("DECISION_MAX_AGE_MIN", "45")  # older decisions are not executed
ORDER_MAX_HOURS = _f("ORDER_MAX_HOURS", "72")            # resting orders expire after at most this
ORDER_MAX_DIST = _f("ORDER_MAX_DIST", "0.15")            # trigger at most 15% from the current price
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-opus-5-5")
BRAIN_EVERY_MIN = _f("BRAIN_EVERY_MIN", "60")     # routine decision interval
EVENT_MOVE_PCT = _f("EVENT_MOVE_PCT", "0.025")    # a 15-minute move this big wakes the brain early
MAX_CALLS_PER_DAY = int(_f("MAX_CALLS_PER_DAY", "40"))  # hard budget cap on Claude API calls

# --- Risk guard (aggressive profile; enforced in code, the brain cannot override) --
DEFAULT_RISK = _f("DEFAULT_RISK", "0.03")         # 3% of equity lost if the stop is hit
MAX_RISK_PER_TRADE = _f("MAX_RISK_PER_TRADE", "0.08")  # never more than 8% per trade
MAX_LEVERAGE = _f("MAX_LEVERAGE", "15")           # total position size <= 15x equity
MAX_OPEN_POSITIONS = int(_f("MAX_OPEN_POSITIONS", "5"))
MIN_STOP_DIST = _f("MIN_STOP_DIST", "0.003")      # stop at least 0.3% from price
MAX_STOP_DIST = _f("MAX_STOP_DIST", "0.12")       # and at most 12%
DAILY_LOSS_LIMIT = _f("DAILY_LOSS_LIMIT", "0.20") # -20% in a UTC day: close all, pause until tomorrow
KILL_DRAWDOWN = _f("KILL_DRAWDOWN", "0.50")       # -50% from peak: close all, stop for good

# --- Predictions and carry (same account) ------------------------------------------
PRED_MAX_STAKE = _f("PRED_MAX_STAKE", "0.08")    # one prediction stake <= 8% of equity (it is the max loss)
PRED_MAX_TOTAL = _f("PRED_MAX_TOTAL", "0.40")    # all open predictions together <= 40% of equity
CARRY_MAX_TOTAL = _f("CARRY_MAX_TOTAL", "0.60")  # all carry trades together <= 60% of equity

# --- Costs (taker fee charged by the paper exchange and the control bot) ----------
TAKER_FEE = _f("TAKER_FEE", "0.00055")

DATA_DIR = os.getenv("DATA_DIR", "docs/data")
