"""A 30-day plan for turning $100 into as much money as possible,
saved as entry.txt for the judge.

The plan itself is fixed text, so the output never varies from run
to run. The program only checks the plan fits the bounty gate and
puts it where the grader reads it. Point MAKEFUN_OUTPUT_DIR at a
scratch folder to try it outside the grader.
"""

import os
import sys
from pathlib import Path


def target_file():
    """Where entry.txt goes: $MAKEFUN_OUTPUT_DIR, else /output."""
    folder = os.getenv("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(folder).joinpath("entry.txt")


# The plan, one literal per phase. It sells a service only an agent
# can deliver at the price: round-the-clock listing monitoring.
# Every number in it is a commitment the plan itself has to keep.
# The closing line states cash actually held on day 30, not a monthly
# rate, because that is the number the plan is judged on.
THE_PLAN = (
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


def publish():
    """Check the plan against the gate, then save it."""
    text = THE_PLAN
    size = len(text)
    if size < 1 or size > 1000 or text.strip() == "":
        print("plan does not fit the 1 to 1000 character gate", file=sys.stderr)
        return 1
    spot = target_file()
    spot.parent.mkdir(parents=True, exist_ok=True)
    spot.write_bytes(text.encode("utf-8"))
    print("saved " + str(size) + " characters to " + str(spot))
    return 0


raise SystemExit(publish())
