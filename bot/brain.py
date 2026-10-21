"""The decision maker: one Claude API call per decision, forced to answer through a tool schema."""
import json

from . import config

SYSTEM_PROMPT = """You are the trader of a small crypto futures DEMO account (USDT linear perpetuals on Bybit).
The experiment tests whether you can grow ~1,000 PLN as much as possible by {end_at}. You trade AGGRESSIVELY.

Your style:
- Hunt for asymmetric setups: trend continuations, breakouts with momentum, sharp reversals at extremes, funding-rate squeezes.
- Shorting is as normal as going long.
- Concentrate on your best idea instead of spreading thin. Pyramid into winners by opening again after a close, not by averaging down.
- Let winners run: trail stops behind structure instead of taking small profits early.
- Cut losers fast. A trade whose reason is gone gets closed, even before its stop.
- Standing aside is allowed when nothing is clean. Costs (taker fee ~0.055% per side, plus funding) punish churn.

Hard rules enforced by code after you answer (orders that break them are rejected or resized, so plan within them):
- Every new position needs a stop-loss {min_stop:.1%}-{max_stop:.0%} away from the current price, on the correct side.
- You pick risk_pct = the share of equity lost if the stop is hit: max {max_risk:.0%}, default {default_risk:.0%}. Position size is computed from risk_pct and the stop distance.
- Total position size is capped at {max_lev:.0f}x equity. At most {max_pos} open positions, one per symbol.
- Stops can only be moved to REDUCE risk (up for longs, down for shorts), never widened.
- A {daily:.0%} loss in one UTC day closes everything until the next day. A {kill:.0%} drawdown from peak ends the experiment.

You receive: account state, open positions (their stops and take-profits live on the exchange and fire 24/7 even between your decisions), market snapshots, events since your last decision, and your journal of earlier decisions with outcomes. You have no other memory, so write reasons your future self can check.
Answer ONLY by calling submit_decision."""

DECISION_TOOL = {
    "name": "submit_decision",
    "description": "Submit this round's trading decision.",
    "input_schema": {
        "type": "object",
        "properties": {
            "market_view": {"type": "string", "description": "1-3 sentences: what you see right now."},
            "actions": {
                "type": "array",
                "description": "Empty array = hold everything as is.",
                "items": {
                    "type": "object",
                    "properties": {
                        "type": {"type": "string", "enum": ["open", "close", "move_stop"]},
                        "symbol": {"type": "string"},
                        "side": {"type": "string", "enum": ["long", "short"], "description": "open only"},
                        "stop": {"type": "number", "description": "open: required stop-loss price. move_stop: new stop price."},
                        "take_profit": {"type": ["number", "null"], "description": "optional target price"},
                        "risk_pct": {"type": "number", "description": "open only, fraction of equity, e.g. 0.03"},
                        "reason": {"type": "string"},
                        "invalidation": {"type": "string", "description": "open only: what would prove this trade wrong"},
                    },
                    "required": ["type", "symbol", "reason"],
                },
            },
            "watch_next": {"type": "string", "description": "What you will look for at the next check."},
        },
        "required": ["market_view", "actions", "watch_next"],
    },
}


def system_prompt():
    return SYSTEM_PROMPT.format(
        end_at=config.END_AT, min_stop=config.MIN_STOP_DIST, max_stop=config.MAX_STOP_DIST,
        max_risk=config.MAX_RISK_PER_TRADE, default_risk=config.DEFAULT_RISK, max_lev=config.MAX_LEVERAGE,
        max_pos=config.MAX_OPEN_POSITIONS, daily=config.DAILY_LOSS_LIMIT, kill=config.KILL_DRAWDOWN)


class ClaudeBrain:
    def __init__(self, api_key=None, model=None):
        import anthropic  # imported here so tests can run without the package
        self.client = anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()
        self.model = model or config.CLAUDE_MODEL

    def decide(self, context):
        msg = self.client.messages.create(
            model=self.model,
            max_tokens=2000,
            system=system_prompt(),
            tools=[DECISION_TOOL],
            tool_choice={"type": "tool", "name": "submit_decision"},
            messages=[{"role": "user", "content": "Current state (JSON):\n" + json.dumps(context, separators=(",", ":"))}],
        )
        for block in msg.content:
            if getattr(block, "type", None) == "tool_use" and block.name == "submit_decision":
                decision = dict(block.input)
                decision["_usage"] = {"input_tokens": msg.usage.input_tokens, "output_tokens": msg.usage.output_tokens}
                decision["_model"] = self.model
                return decision
        raise RuntimeError("Claude did not return a decision")
