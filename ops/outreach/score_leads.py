#!/usr/bin/env python3
"""Score and tier leads in ops/crm.csv (rubric: docs/06-acquisition.md §4).

Usage: python3 ops/outreach/score_leads.py          # rewrites the score and tier columns, prints the A-list
       python3 ops/outreach/score_leads.py --dry    # print only, don't write
Also marks any lead on ops/outreach/do-not-contact.csv as stage=do_not_contact.
"""
import csv, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CRM = ROOT / "ops" / "crm.csv"
DNC = ROOT / "ops" / "outreach" / "do-not-contact.csv"

SITE_POINTS = {"none": 30, "linktree": 30, "pdf_menu": 25, "broken_mobile": 25, "outdated": 20, "fine": 0, "unknown": 10}

def yes(v): return (v or "").strip().lower() in ("yes", "y", "true", "1")

def score(r):
    if (r.get("independent") or "").strip().lower() == "no":
        return 0
    s = SITE_POINTS.get((r.get("site_status") or "unknown").strip().lower(), 10)
    s += 10 if yes(r.get("hours_mismatch")) else 0
    s += 5 if yes(r.get("no_booking")) else 0
    s += 10  # independent
    try:
        reviews = int(float(r.get("review_count") or 0))
    except ValueError:
        reviews = 0
    s += 10 if reviews >= 150 else 6 if reviews >= 50 else 2
    s += 10 if yes(r.get("events_private_hire")) else 0
    s += 15 if (r.get("trigger") or "").strip() else 0
    s += 10 if yes(r.get("reachable")) else 0
    return min(s, 100)

def tier(n): return "A" if n >= 65 else "B" if n >= 40 else "C"

def main():
    dry = "--dry" in sys.argv
    with open(CRM, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f); fields = reader.fieldnames; rows = list(reader)
    dnc = set()
    if DNC.exists():
        dnc = {r["venue"].strip().lower() for r in csv.DictReader(open(DNC, newline="", encoding="utf-8")) if r.get("venue")}
    for r in rows:
        n = score(r)
        r["score"], r["tier"] = str(n), tier(n)
        if r["venue"].strip().lower() in dnc:
            r["stage"] = "do_not_contact"
    if not dry:
        with open(CRM, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
    active = [r for r in rows if r["stage"] not in ("won", "lost", "do_not_contact")]
    active.sort(key=lambda r: -int(r["score"]))
    counts = {t: sum(1 for r in active if r["tier"] == t) for t in "ABC"}
    print(f"Scored {len(rows)} leads. Active: A={counts['A']} B={counts['B']} C={counts['C']}")
    print("\nA-list (visit this week):")
    for r in [r for r in active if r["tier"] == "A"][:25]:
        print(f"  {r['score']:>3}  {r['venue']} ({r['area']})  best time: {r['best_time'] or '?'}  next: {r['next_action'] or '-'}")

if __name__ == "__main__":
    main()
