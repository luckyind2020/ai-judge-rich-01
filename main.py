#!/usr/bin/env python3
"""Entry for make.fun's ai-judge-rich-01: "Make the AI judge rich".

The program does one thing: write a single money plan to entry.txt.
No network, no randomness, no arguments, no input files. The plan is
a fixed string, so every run writes exactly the same bytes.

Run it outside the grader with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import sys

# The grader reads /output/entry.txt; MAKEFUN_OUTPUT_DIR stands in
# for /output when the program runs outside the grader container.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_FILENAME = "entry.txt"

# The gate for this bounty: UTF-8 text of 1 to 1,000 characters.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 1000

# The plan, one literal per phase. It sells a service only an agent
# can deliver at the price: round-the-clock listing monitoring.
# Every number in it is a commitment the plan itself has to keep.
# The closing line states cash actually held on day 30, not a monthly
# rate, because that is the number the plan is judged on.
PLAN = (
    "Sell 24/7 competitor watchdogs to small online sellers. "
    "Day 1: pick Etsy print-on-demand sellers and build a Python monitor on a free hosting tier "
    "that checks each shop's top 20 rival listings hourly and emails price and stock changes every morning. "
    "Days 2-7: offer it free for a week in Etsy seller forums and subreddits; onboard 5 shops, spend nothing. "
    "Days 8-14: convert trials to $19 a month; spend $30 on targeted ads only after the first 2 pay. "
    "Days 15-30: add Amazon handmade sellers as a second niche, raise new signups to $29 a month, "
    "and sell a $49 one-time competitor teardown to existing users. "
    "A human freelancer cannot watch listings hourly for $19; a script can, forever, so churn stays low. "
    "Expected day 30: roughly $300-450 held, from first $19 fees of 10-15 shops plus $100-200 in teardown reports, "
    "about $60 spent, $40 reserve untouched. Kill any channel with no paying user in 7 days."
)


def check_plan(text):
    """Refuse to write a plan the bounty gate would reject."""
    size = len(text)
    if not GATE_MIN_CHARS <= size <= GATE_MAX_CHARS:
        return f"plan is {size} characters, gate needs 1-1000"
    if not text.strip():
        return "plan is only whitespace"
    return None


def main():
    problem = check_plan(PLAN)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(PLAN)
    print(f"wrote {len(PLAN)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
