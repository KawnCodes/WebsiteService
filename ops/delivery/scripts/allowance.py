#!/usr/bin/env python3
"""Edit allowance and turnaround report for Running Tab.

Reads ops/clients.csv and ops/delivery/edits/edit-log.csv and prints, for one month:
  - change requests used vs the plan allowance, per client
  - requests that missed the turnaround promise (which means a £10 credit, once per client per month)
  - open requests and when each one is due

Usage:  python3 ops/delivery/scripts/allowance.py [YYYY-MM] [--now "YYYY-MM-DD HH:MM"]
Standard library only. Times are UK local time as written in the CSV.
"""
import csv, sys
from datetime import datetime, date, time, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CLIENTS = ROOT / "ops" / "clients.csv"
EDITS = ROOT / "ops" / "delivery" / "edits" / "edit-log.csv"

ALLOWANCE = {"core": 5, "founding": 5, "plus": 15, "group": 40}  # group = "unlimited small edits", fair use
FAST_TYPES = {"menu", "hours", "closure"}  # same-day types on Plus and Group
FAST_CUTOFF = time(15, 0)
WORK_START, WORK_END = time(9, 0), time(17, 0)

# England & Wales bank holidays. Check gov.uk/bank-holidays each year and add the next year's dates.
BANK_HOLIDAYS = {date.fromisoformat(d) for d in [
    "2026-01-01", "2026-04-03", "2026-04-06", "2026-05-04", "2026-05-25", "2026-08-31", "2026-12-25", "2026-12-28",
    "2027-01-01", "2027-03-26", "2027-03-29", "2027-05-03", "2027-05-31", "2027-08-30", "2027-12-27", "2027-12-28",
]}

def is_working_day(d: date) -> bool:
    return d.weekday() < 5 and d not in BANK_HOLIDAYS

def next_working_day(d: date) -> date:
    d += timedelta(days=1)
    while not is_working_day(d):
        d += timedelta(days=1)
    return d

def end_of(d: date) -> datetime:
    return datetime.combine(d, time(23, 59))

def add_working_hours(start: datetime, hours: float) -> datetime:
    t = start
    remaining = timedelta(hours=hours)
    while True:
        if not is_working_day(t.date()) or t.time() >= WORK_END:
            t = datetime.combine(next_working_day(t.date()), WORK_START)
            continue
        if t.time() < WORK_START:
            t = datetime.combine(t.date(), WORK_START)
        left_today = datetime.combine(t.date(), WORK_END) - t
        if remaining <= left_today:
            return t + remaining
        remaining -= left_today
        t = datetime.combine(next_working_day(t.date()), WORK_START)

def due_at(plan: str, kind: str, received: datetime) -> datetime:
    """When a request must be done, according to docs/02-offer.md."""
    if plan in ("plus", "group") and kind in FAST_TYPES:
        if received.time() < FAST_CUTOFF:
            return end_of(received.date())              # same day, 7 days a week
        return end_of(received.date() + timedelta(days=1))  # sent after 3pm: next day
    if plan == "group":
        return add_working_hours(received, 4)
    # Core / founding, and non-urgent Plus changes: within 1 working day
    return end_of(next_working_day(received.date()))

def parse_dt(s: str):
    s = (s or "").strip()
    return datetime.strptime(s, "%Y-%m-%d %H:%M") if s else None

def main():
    args = sys.argv[1:]
    now = datetime.now()
    if "--now" in args:
        i = args.index("--now"); now = parse_dt(args[i + 1]); del args[i:i + 2]
    month = args[0] if args else now.strftime("%Y-%m")

    clients = {r["client_id"]: r for r in csv.DictReader(open(CLIENTS, newline="", encoding="utf-8"))}
    edits = list(csv.DictReader(open(EDITS, newline="", encoding="utf-8")))

    print(f"Running Tab: edit report for {month} (as of {now:%Y-%m-%d %H:%M})\n")
    print(f"{'Client':<28}{'Plan':<10}{'Used':>6}{'Allow':>7}  Flags")
    open_items, credits = [], []
    for cid, c in clients.items():
        if c["status"] not in ("live", "onboarding"):
            continue
        plan = c["plan"].strip().lower()
        mine = [e for e in edits if e["client_id"] == cid and e["received_at"].startswith(month)]
        used = sum(1 for e in mine if e["counts"].strip().lower() == "yes")
        allow = ALLOWANCE.get(plan, 5)
        flags = []
        if used > allow:
            flags.append(f"OVER by {used - allow}: suggest upgrading plan or an edit pack")
        elif used >= allow * 0.8 and allow:
            flags.append("near allowance")
        missed = []
        for e in mine:
            if e["status"].strip().lower() == "declined":
                continue
            rec = parse_dt(e["received_at"])
            due = due_at(plan, e["type"].strip().lower(), rec)
            done = parse_dt(e["done_at"])
            if done is None:
                open_items.append((due, cid, e["request_id"], e["summary"], due < now))
                if due < now:
                    missed.append(e["request_id"])
            elif done > due:
                missed.append(e["request_id"])
        if missed:
            flags.append(f"MISSED turnaround: {', '.join(missed)}")
            credits.append((cid, c["venue"]))
        print(f"{c['venue'][:27]:<28}{plan:<10}{used:>6}{allow:>7}  {'; '.join(flags)}")

    print("\nOpen requests (oldest due first):")
    if not open_items:
        print("  none")
    for due, cid, rid, summary, late in sorted(open_items):
        print(f"  {'LATE ' if late else ''}{rid} {cid}: {summary} (due {due:%a %d %b %H:%M})")

    print("\n£10 credits to apply to next month's invoice (max one per client per month):")
    if not credits:
        print("  none")
    for cid, venue in credits:
        print(f"  {venue} ({cid}): apply a £10 one-off discount in Stripe")

if __name__ == "__main__":
    main()
