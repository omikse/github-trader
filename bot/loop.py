"""Always-on engine: one GitHub Actions job runs this for almost 6 hours, then the next job takes over.

Every minute:  pull new brain decisions, replay the last minute (stops, targets, orders, funding,
               liquidation), refresh the account and the dashboard data.
Every 5 min:   full scan of all markets, benchmarks, equity history, brain input.
Every 8 min:   commit and push the data to main (history, GitHub Pages rebuilds ~10 times/hour max),
               and right away after a decision was executed.
Every minute:  also force-push the current summary and equity history as a single commit to the `live`
               branch, which Pages does not serve; the dashboard reads it through GitHub's API, so the
               page is about a minute behind instead of up to 8.
"""
import os
import subprocess
import time
import traceback
from datetime import datetime, timezone

from . import config, run

RUN_MINUTES = float(os.getenv("LOOP_MINUTES", "340"))   # GitHub's job limit is 360
FULL_EVERY = 5 * 60
PUSH_EVERY = 8 * 60


def git(*args, check=False):
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    if check and r.returncode:
        raise RuntimeError(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r


def pull():
    git("pull", "--rebase", "--autostash", "-q")


def push(msg):
    git("add", config.DATA_DIR)
    if git("diff", "--cached", "--quiet").returncode == 0:
        return
    git("commit", "-q", "-m", msg)
    for _ in range(3):
        pull()
        if git("push", "-q").returncode == 0:
            return
        time.sleep(5)
    print("::warning::push failed three times; will retry next cycle", flush=True)


def publish_live():
    """Overwrite branch `live` with one commit holding summary.json and equity.csv (no history kept)."""
    entries = []
    for name in ("summary.json", "equity.csv"):
        path = os.path.join(config.DATA_DIR, name)
        if os.path.exists(path):
            blob = git("hash-object", "-w", path).stdout.strip()
            entries.append(f"100644 blob {blob}\t{name}")
    if not entries:
        return
    tree = subprocess.run(["git", "mktree"], input="\n".join(entries) + "\n",
                          capture_output=True, text=True).stdout.strip()
    commit = git("commit-tree", tree, "-m", "live data").stdout.strip()
    if git("push", "-q", "-f", "origin", f"{commit}:refs/heads/live").returncode:
        print("::warning::could not update the live branch", flush=True)


def main():
    git("config", "user.name", "trading-bot")
    git("config", "user.email", "trading-bot@users.noreply.github.com")
    end = time.time() + RUN_MINUTES * 60
    last_full = last_push = 0.0
    while time.time() < end:
        tick = time.time()
        pull()
        full = tick - last_full >= FULL_EVERY
        try:
            entry = run.main(light=not full)
        except Exception as e:
            traceback.print_exc()
            print(f"::warning::cycle failed: {e.__class__.__name__}: {e}", flush=True)
            entry = None
        if full:
            last_full = tick
        publish_live()
        if entry or tick - last_push >= PUSH_EVERY:
            push("bot " + datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"))
            last_push = tick
        state = run.load_json(os.path.join(config.DATA_DIR, "state.json"), {})
        if state.get("ended"):
            push("bot: experiment ended")
            return
        time.sleep(max(1.0, 60 - (time.time() - tick)))
    push("bot " + datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ") + " (handover)")


if __name__ == "__main__":
    main()
