"""All tunable settings in one place. Values can be overridden with environment variables."""
import os


def _f(name, default):
    return float(os.getenv(name, default))


# --- Account -----------------------------------------------------------------
START_PLN = _f("START_PLN", "1000")          # simulated starting capital
SYMBOLS = [s.strip() for s in os.getenv("SYMBOLS", "BTCUSDT,ETHUSDT,SOLUSDT,XRPUSDT,DOGEUSDT").split(",") if s.strip()]
END_AT = os.getenv("END_AT", "2026-11-21T21:00:00Z")  # experiment ends, everything is closed

# --- Brain -------------------------------------------------------------------
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-opus-5-5")
BRAIN_EVERY_MIN = _f("BRAIN_EVERY_MIN", "60")     # routine decision interval
EVENT_MOVE_PCT = _f("EVENT_MOVE_PCT", "0.025")    # a 15-minute move this big wakes the brain early
MAX_CALLS_PER_DAY = int(_f("MAX_CALLS_PER_DAY", "40"))  # hard budget cap on Claude API calls

# --- Risk guard (aggressive profile; enforced in code, the brain cannot override) --
DEFAULT_RISK = _f("DEFAULT_RISK", "0.03")         # 3% of equity lost if the stop is hit
MAX_RISK_PER_TRADE = _f("MAX_RISK_PER_TRADE", "0.05")  # never more than 5% per trade
MAX_LEVERAGE = _f("MAX_LEVERAGE", "10")           # total position size <= 10x equity
MAX_OPEN_POSITIONS = int(_f("MAX_OPEN_POSITIONS", "3"))
MIN_STOP_DIST = _f("MIN_STOP_DIST", "0.003")      # stop at least 0.3% from price
MAX_STOP_DIST = _f("MAX_STOP_DIST", "0.12")       # and at most 12%
DAILY_LOSS_LIMIT = _f("DAILY_LOSS_LIMIT", "0.15") # -15% in a UTC day: close all, pause until tomorrow
KILL_DRAWDOWN = _f("KILL_DRAWDOWN", "0.50")       # -50% from peak: close all, stop for good

# --- Costs (taker fee charged by the paper exchange and the control bot) ----------
TAKER_FEE = _f("TAKER_FEE", "0.00055")

DATA_DIR = os.getenv("DATA_DIR", "docs/data")
