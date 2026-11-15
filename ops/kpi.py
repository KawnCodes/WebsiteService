#!/usr/bin/env python3
"""Running Tab KPI dashboard. The spec is in docs/07-scale.md §3.

Reads:  ops/clients.csv, ops/crm.csv, ops/delivery/edits/edit-log.csv,
        ops/time-log.csv, ops/spend-log.csv
Prints: MRR, growth, churn, ARPU, gross margin, LTV, CAC, LTV:CAC, funnel conversion
        rates, hours per client, edits per client, and progress against the revenue targets.

Usage:  python3 ops/kpi.py                 # current month
        python3 ops/kpi.py 2027-01         # a given month
        python3 ops/kpi.py 2027-01 --md    # also write ops/kpi-report.md
        python3 ops/kpi.py --data DIR      # read the CSVs from another folder (for testing)
Standard library only.
"""
import csv, sys
from datetime import date, datetime
from pathlib import Path

OPS = Path(__file__).resolve().parent

# Assumptions (keep in step with ops/pricing-model.csv)
STRIPE_PCT, STRIPE_FIX, BILLING_PCT = 0.015, 0.20, 0.007
OTHER_VARIABLE_COST = 1.5          # £/client/month: contingency, domain average
ASSUMED_CHURN = 0.03               # used until there's enough real churn data
FOUNDER_HOURLY_VALUE = 15.0        # £/hour, for the "including your time" CAC. Change this to what your time is worth.
TARGETS = {"2027-05": 2250, "2027-11": 3750}
FUNNEL = [("Contacted", "last_touch_date"), ("Conversation", "conversation_date"), ("Mockup sent", "mockup_date"), ("Won", "won_date")]


def read(path):
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if any((v or "").strip() for v in r.values())]


def d(s):
    s = (s or "").strip()[:10]
    try:
        return date.fromisoformat(s) if s else None
    except ValueError:
        return None


def month_bounds(ym):
    y, m = map(int, ym.split("-"))
    start = date(y, m, 1)
    end = date(y + (m == 12), m % 12 + 1, 1)
    return start, end


def money(x):
    return "n/a" if x is None else f"£{x:,.2f}"


def pct(x):
    return "n/a" if x is None else f"{x * 100:.1f}%"


def active_on(c, day):
    """Was this client paying on this day? Paying runs from launch_date to cancelled_date."""
    start, end = d(c.get("launch_date")), d(c.get("cancelled_date"))
    return start is not None and start <= day and (end is None or end > day)


def main():
    args = sys.argv[1:]
    data = OPS
    if "--data" in args:
        i = args.index("--data"); data = Path(args[i + 1]); del args[i:i + 2]
    write_md = "--md" in args
    args = [a for a in args if a != "--md"]
    ym = args[0] if args else date.today().strftime("%Y-%m")
    start, end = month_bounds(ym)
    last_day = date.fromordinal(end.toordinal() - 1)

    clients = read(data / "clients.csv")
    crm = read(data / "crm.csv")
    edits = read(data / ("delivery/edits/edit-log.csv" if data == OPS else "edit-log.csv"))
    time_log = read(data / "time-log.csv")
    spend = read(data / "spend-log.csv")

    price = lambda c: float(c.get("monthly_price") or 0)
    live_end = [c for c in clients if active_on(c, last_day)]
    live_start = [c for c in clients if active_on(c, date.fromordinal(start.toordinal() - 1))]
    new_clients = [c for c in clients if (ld := d(c.get("launch_date"))) and start <= ld < end]
    churned = [c for c in clients if (cd := d(c.get("cancelled_date"))) and start <= cd < end and d(c.get("launch_date")) and d(c.get("launch_date")) < start]

    mrr = sum(price(c) for c in live_end)
    mrr_start = sum(price(c) for c in live_start)
    new_mrr = sum(price(c) for c in new_clients)
    churned_mrr = sum(price(c) for c in churned)
    arpu = mrr / len(live_end) if live_end else None
    var_cost = (arpu * (STRIPE_PCT + BILLING_PCT) + STRIPE_FIX + OTHER_VARIABLE_COST) if arpu else None
    gm = (arpu - var_cost) / arpu if arpu else None

    churn = len(churned) / len(live_start) if live_start else None
    # Average churn over all months with clients, to smooth the noise of small numbers
    months_seen, churn_events = 0, 0
    for c in clients:
        ld = d(c.get("launch_date"))
        if not ld:
            continue
        cd = d(c.get("cancelled_date")) or last_day
        months_seen += max(0, (min(cd, last_day).year - ld.year) * 12 + (min(cd, last_day).month - ld.month))
        churn_events += 1 if d(c.get("cancelled_date")) and d(c.get("cancelled_date")) <= last_day else 0
    avg_churn = churn_events / months_seen if months_seen >= 12 and churn_events else None
    churn_for_ltv = avg_churn or ASSUMED_CHURN
    ltv = arpu * gm / churn_for_ltv if arpu else None

    acq_spend = sum(float(s.get("amount_gbp") or 0) for s in spend if s.get("category") == "acquisition" and (sd := d(s.get("date"))) and start <= sd < end)
    sales_hours = sum(float(t.get("hours") or 0) for t in time_log if t.get("category") in ("sales", "content") and (td := d(t.get("date"))) and start <= td < end)
    won = [l for l in crm if (wd := d(l.get("won_date"))) and start <= wd < end]
    n_won = len(won) or len(new_clients)
    cac_cash = acq_spend / n_won if n_won else None
    cac_full = (acq_spend + sales_hours * FOUNDER_HOURLY_VALUE) / n_won if n_won else None
    ltv_cac = ltv / cac_full if ltv and cac_full else None

    funnel = []
    for label, col in FUNNEL:
        funnel.append((label, sum(1 for l in crm if (x := d(l.get(col))) and start <= x < end)))

    delivery_hours = sum(float(t.get("hours") or 0) for t in time_log if t.get("category") in ("delivery", "admin") and (td := d(t.get("date"))) and start <= td < end)
    hrs_per_client = delivery_hours / len(live_end) if live_end else None
    edits_month = [e for e in edits if (e.get("received_at") or "").startswith(ym) and (e.get("counts") or "").lower() == "yes"]
    edits_per_client = len(edits_month) / len(live_end) if live_end else None

    tools_spend = sum(float(s.get("amount_gbp") or 0) for s in spend if s.get("category") != "acquisition" and (sd := d(s.get("date"))) and start <= sd < end)
    profit = mrr - (var_cost or 0) * len(live_end) - tools_spend - acq_spend

    lines = [f"# Running Tab KPIs: {ym}", f"_Generated {datetime.now():%Y-%m-%d %H:%M} by ops/kpi.py_", ""]
    lines += ["## Revenue", "| Metric | Value |", "|---|---|",
              f"| **MRR (end of month)** | **{money(mrr)}** |",
              f"| MRR at start of month | {money(mrr_start)} |",
              f"| New MRR / churned MRR | {money(new_mrr)} / {money(churned_mrr)} |",
              f"| MRR growth | {pct((mrr - mrr_start) / mrr_start) if mrr_start else 'n/a'} |",
              f"| Live clients | {len(live_end)} (new {len(new_clients)}, cancelled {len(churned)}) |",
              f"| ARPU | {money(arpu)} |",
              f"| Gross margin (after Stripe fees and variable costs) | {pct(gm)} |",
              f"| Rough profit this month (MRR - variable - logged spend) | {money(profit)} |", ""]
    lines += ["## Retention", "| Metric | Value |", "|---|---|",
              f"| Logo churn this month | {pct(churn)} ({len(churned)} of {len(live_start)}) |",
              f"| Average monthly churn (all time) | {pct(avg_churn) + ' (real data)' if avg_churn else 'not enough data yet: using ' + pct(ASSUMED_CHURN) + ' (assumed)'} |",
              f"| LTV (ARPU x margin / churn) | {money(ltv)} |", ""]
    lines += ["## Acquisition", "| Metric | Value |", "|---|---|",
              f"| Won this month | {n_won} |",
              f"| Acquisition cash spend | {money(acq_spend)} |",
              f"| Sales and content hours | {sales_hours:.1f} h |",
              f"| CAC (cash only) | {money(cac_cash)} |",
              f"| CAC (including your time at £{FOUNDER_HOURLY_VALUE:.0f}/h) | {money(cac_full)} |",
              f"| LTV : CAC | {f'{ltv_cac:.1f} : 1' if ltv_cac else 'n/a'} (aim for 3 : 1 or better) |", ""]
    lines += ["## Funnel (events dated this month)", "| Stage | Count | Conversion from previous stage |", "|---|---|---|"]
    prev = None
    for label, n in funnel:
        lines.append(f"| {label} | {n} | {pct(n / prev) if prev else '-'} |")
        prev = n if n else None
    lines += ["", "## Delivery", "| Metric | Value |", "|---|---|",
              f"| Delivery and admin hours | {delivery_hours:.1f} h |",
              f"| Hours per client per month | {f'{hrs_per_client:.2f} h' if hrs_per_client is not None else 'n/a'} (plan: about 0.6 h) |",
              f"| Edit requests per client | {f'{edits_per_client:.1f}' if edits_per_client is not None else 'n/a'} |", ""]
    lines += ["## Targets", "| Target | MRR needed | Now | Gap |", "|---|---|---|---|"]
    for t_month, t_mrr in TARGETS.items():
        gap = t_mrr - mrr
        clients_needed = f"about {int(-(-gap // arpu))} more clients at current ARPU" if arpu and gap > 0 else ("hit ✅" if gap <= 0 else "")
        lines.append(f"| {t_month} | £{t_mrr:,} | {money(mrr)} | {clients_needed} |")
    out = "\n".join(lines)
    print(out)
    if write_md:
        (OPS / "kpi-report.md").write_text(out + "\n", encoding="utf-8")
        print("\nWritten to ops/kpi-report.md")


if __name__ == "__main__":
    main()
