#!/usr/bin/env python3
"""Import Cambridge-area food businesses from the FSA Food Hygiene Rating open data into ops/crm.csv.

The data is published by the Food Standards Agency under the Open Government Licence.
It lists every registered food business with its name and address. Businesses marked
"Awaiting inspection" are often new openings, which is a strong trigger.

Usage (run on your own computer; the cloud environment this was written in blocks the FSA API):
    python3 ops/outreach/fsa_leads.py                 # Cambridge City + South Cambridgeshire, adds new leads
    python3 ops/outreach/fsa_leads.py --dry           # show what would be added
    python3 ops/outreach/fsa_leads.py --authority "East Cambridgeshire"

NOT YET TESTED against the live API. Check the first run with --dry. API docs: api.ratings.food.gov.uk/help
"""
import csv, json, sys, urllib.request, urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CRM = ROOT / "ops" / "crm.csv"
API = "https://api.ratings.food.gov.uk"
HEADERS = {"x-api-version": "2", "Accept": "application/json", "User-Agent": "lead-import-script"}
# FSA business type IDs: 1 = Restaurant/Cafe/Canteen, 7843 = Pub/bar/nightclub
BUSINESS_TYPES = {1: "restaurant_or_cafe", 7843: "pub_or_bar"}
DEFAULT_AUTHORITIES = ["Cambridge City", "South Cambridgeshire"]

def get(path, params=None):
    url = f"{API}{path}" + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def authority_ids(names):
    data = get("/Authorities/basic")
    found = {a["Name"]: a["LocalAuthorityId"] for a in data.get("authorities", []) if a["Name"] in names}
    missing = set(names) - set(found)
    if missing:
        print(f"Warning: authorities not found: {', '.join(sorted(missing))}")
    return found

def main():
    args = sys.argv[1:]
    dry = "--dry" in args
    names = DEFAULT_AUTHORITIES
    if "--authority" in args:
        names = [args[args.index("--authority") + 1]]

    with open(CRM, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f); fields = reader.fieldnames; rows = list(reader)
    key = lambda name, pc: (name.strip().lower(), (pc or "").replace(" ", "").upper())
    existing = {key(r["venue"], r.get("postcode", "")) for r in rows}
    next_id = 1 + max([int(r["lead_id"][1:]) for r in rows if r["lead_id"][1:].isdigit()] or [0])

    added = []
    for auth_name, auth_id in authority_ids(names).items():
        for bt, kind in BUSINESS_TYPES.items():
            data = get("/Establishments", {"localAuthorityId": auth_id, "businessTypeId": bt, "pageSize": 5000})
            for e in data.get("establishments", []):
                name, pc = e.get("BusinessName", ""), e.get("PostCode", "")
                if not name or key(name, pc) in existing:
                    continue
                existing.add(key(name, pc))
                address = ", ".join(x for x in [e.get(f"AddressLine{i}") for i in range(1, 5)] if x)
                awaiting = str(e.get("RatingValue", "")).lower().startswith("awaiting")
                row = {f: "" for f in fields}
                row.update({
                    "lead_id": f"L{next_id:04d}", "venue": name, "type": kind, "area": auth_name,
                    "address": address, "postcode": pc, "is_ltd": "unknown", "independent": "unknown",
                    "site_status": "unknown", "trigger": "possibly new opening (awaiting first FSA inspection)" if awaiting else "",
                    "stage": "new", "source": "fsa", "touch_count": "0",
                    "notes": f"FSA {e.get('FHRSID')}; rating {e.get('RatingValue')} ({(e.get('RatingDate') or '')[:10]})",
                })
                next_id += 1
                added.append(row)

    print(f"{len(added)} new leads found ({sum(1 for r in added if r['trigger'])} possibly new openings).")
    if dry:
        for r in added[:30]:
            print(f"  {r['venue']}, {r['postcode']} [{r['type']}] {r['trigger']}")
        return
    with open(CRM, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows + added)
    print("Added to ops/crm.csv. Next: remove chains (independent=no), research site_status, then run score_leads.py")

if __name__ == "__main__":
    main()
