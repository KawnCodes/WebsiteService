# 07: Launch, metrics & scaling

_Status: draft v1, 15 Nov 2026. Your week-by-week to-do list is in [`MONDAY.md`](../MONDAY.md)._

## 1. Launch checklist (before the first walk-in that includes a price)

**Business** (`docs/03-setup.md`)
- [ ] Name checks done; domain bought; Instagram and TikTok handles claimed
- [ ] Registered for Self Assessment; separate bank account open
- [ ] ICO self-assessment done (fee paid if needed)
- [ ] Insurance quotes ready (buy before the first client launches)

**Website** (`site/README.md`)
- [ ] Placeholders replaced (your name, address, first name)
- [ ] Deployed on Cloudflare Pages with the custom domain and HTTPS
- [ ] Contact form working (Web3Forms key added, test enquiry received)
- [ ] Booking link (Cal.com) and WhatsApp number set
- [ ] Analytics turned on; sitemap submitted to Google Search Console
- [ ] Checked on your own phone, every page

**Payments**
- [ ] Stripe account verified, linked to the business bank account
- [ ] Payment Links for Core, Plus, Group and Founding, each with a 14-day trial and a terms checkbox
- [ ] Customer Portal turned on

**Sales kit**
- [ ] 20 health checks printed for the first A-list (`ops/outreach/health-check-template.md`)
- [ ] Business cards: 100 cheap ones with a QR code to `/contact`
- [ ] Demo sites open on your phone; the founding offer memorised
- [ ] `ops/crm.csv` has the first 40 leads; `do-not-contact.csv` exists

**Tracking**
- [ ] Log your time in `ops/time-log.csv` (sales, content, delivery, admin) and spending in `ops/spend-log.csv`. Do it daily; it takes 1 minute.

## 2. "First 5 clients" sprint (founding venues, 16 Nov to about 18 Dec)

**Goal:** 5 founding venues signed, and at least 3 live, by 18 December. That gives you real case studies for the January push.

| Week | Outcome | Key actions |
|---|---|---|
| 1 (16 Nov) | 6+ conversations, 2+ mockups sent | Validation walk-ins (Phase 1 plan); site live by Wednesday |
| 2 (23 Nov) | 2 founding venues say yes | Show mockups, close, send welcome emails; go/no-go on Sunday |
| 3 (30 Nov) | Founding venue #1 live, #2 in build | 5-day launch SOP; keep 4 walk-in sessions going |
| 4 (7 Dec) | 5 founding venues signed, 3 live | Close the last spots ("only 2 left" — say it only if it's true) |
| 5 (14 Dec) | Reviews and case studies | Ask for Google reviews; write before/after stories; book January chats |

**Rules for the sprint:**
- Say yes to venues that fit the ideal customer (`docs/01-concept.md` §3), not to anyone at all. A difficult founding venue costs you weeks.
- Launch fast and well rather than slow and perfect. Ship in 5 days, then improve.
- Every founding venue must give a review, a quote and permission to share the before/after. That's the deal.

## 3. KPI dashboard

Run `python3 ops/kpi.py [YYYY-MM] [--md]` every Monday, and on the 1st of each month for the month before. With `--md` it also writes `ops/kpi-report.md`. Data comes from `clients.csv`, `crm.csv`, `edit-log.csv`, `time-log.csv` and `spend-log.csv`.

| KPI | Definition | Target / healthy range | If it's off |
|---|---|---|---|
| **MRR** | Sum of monthly prices for clients live at month end | £2,250 by May 2027, £3,750 by Nov 2027 | Check whether closes or churn are the problem |
| **New / churned MRR** | MRR added by launches, and lost to cancellations | New > 5× churned while growing | Retention playbook (§4) |
| **Logo churn** | Clients cancelled ÷ clients live at the start of the month | Under 3% a month | Exit interviews; save offers |
| **ARPU** | MRR ÷ live clients | £55–£65 | Upsell Plus and add-ons |
| **Gross margin** | (ARPU − Stripe fees − variable costs) ÷ ARPU | Over 90% | Check tool costs |
| **LTV** | ARPU × gross margin ÷ monthly churn | Over £1,000 | Churn is the lever |
| **CAC** | (acquisition spend + sales/content hours × £15) ÷ new clients | Under £200 including your time | Improve conversion rates, referrals |
| **LTV : CAC** | | 3 : 1 or better | |
| **Funnel** | contacted → conversation → mockup → won | ~35% → 50% → 25% (planning guesses) | Find the weakest step and fix only that one |
| **Hours per client** | Delivery + admin hours ÷ live clients | Under 0.75 h a month | Automate the most common edit type |
| **Edits per client** | Requests that count toward allowance ÷ live clients | 1–4 a month | Under 1 is a churn risk; over 5, upsell |

**Founder hourly value:** the "including your time" CAC uses £15/h. Change `FOUNDER_HOURLY_VALUE` in `ops/kpi.py` to whatever your time is worth to you.

## 4. Retention playbook

**Churn is the lever.** At about £60 ARPU, each 1% of monthly churn you avoid is worth hundreds of pounds of LTV per client.

**The first 30 days** (when a client decides whether they love it):
- Launch on time, then make their **first edit fast**. That's the moment they get it.
- Day 7: "How's it going? Anything you'd change?"
- Day 25: guarantee check-in, then ask for a review.

**Every month:**
- The monthly report (`ops/delivery/maintenance/report-template.md`). Showing value that nobody sees otherwise is the strongest retention tool.
- A seasonal nudge 4–6 weeks before each moment (Christmas, Valentine's, Mother's Day, summer, term time).

**Every quarter:**
- Founder check-in, personal and not templated. Group clients get a 20-minute call.

**Warning signs** (check them in the Monday review):
- No edit requests for 6+ weeks.
- A failed payment.
- A missed turnaround.
- A complaint.
- A change of owner or manager.
- The venue advertising for sale or a refurb.

When you spot one, contact them within 48 hours, personally.

**Ways to save a client** (offer one, never push):

| Reason they want to leave | Offer |
|---|---|
| Price | Drop Plus to Core, or switch to annual (2 months free) |
| Seasonal closure or refurb | **Pause** at £15/month for up to 3 months: the site stays up with a "back soon" banner |
| "Not using it" | A free 30-minute refresh session and a seasonal page |
| Service problem | Fix it, plus a free month |

**Upsells** (they also lower churn, because clients who use more leave less):
- Core venues doing events or private hire → **Plus**.
- Seasonal landing pages (£39) every October and January.
- At **month 3**, offer annual billing: 2 months free, paid upfront. That's great cash flow and locks in 12 months.
- Group, for owners opening a second venue.

**Win-back:**
- 3 and 6 months after a client leaves, send a friendly check-in.
- Venues that closed often reopen under new owners. Watch the food hygiene data and walk in.

## 5. Scaling path

| Trigger | Move |
|---|---|
| **More than 40% of mockups turn into clients** for 4 weeks, or you have a waiting list | **Raise prices for new clients only.** Core £49 → £59, Plus £79 → £89. Existing clients keep their price for at least 12 months (the price-lock promise), then get 60 days' notice. |
| **25 live clients** (around Mar–Apr 2027) | Move to Claude Max (already budgeted). Build template v2 (multi-page). Build an **intake form that writes `venue.json` automatically**. |
| **Menu edits are over 50% of all edits** | **Menu from a photo:** the agent turns a photo of the menu straight into structured `venue.json`, the founder approves with one tap, and it deploys. Keep a human check on prices and allergen information. |
| **Founder delivery and admin time over 10 hours a week**, or sales capacity is capped | **Hire a contractor** (§6). First choice: a part-time *site producer* (onboarding visits, photos, QA, client messages), around 5–10 h/week. Check local rates; budget about £15–£20/h. |
| **About 40 clients, or you can't do enough walk-ins** | Add a **commission-only sales partner**: for example, one month's fee per signed client, plus 10% for 12 months. Check the legal and tax position first. ⚖️ |
| **Cambridge food & drink getting saturated** (A-list empty, close rate falling) | Add **Plan B: guest accommodation** using the same template with a rooms section. Expand to Ely, St Ives, Saffron Walden and Newmarket. |
| **Profit of about £30–50k a year** | Talk to an accountant about switching to a **limited company**. Check whether VAT registration is getting close (threshold currently £90k). ⚖️ |

**Automation roadmap** (in order of hours saved):
1. Pre-approved edit types (hours, closures, banners) go live automatically, and the founder gets notified.
2. WhatsApp Business messages are turned into GitHub issues automatically (needs the WhatsApp Business API, which has a cost; check first).
3. Monthly reports drafted automatically from Cloudflare analytics, UptimeRobot and `edit-log.csv`.
4. Health checks and mockups generated in batches for the weekly A-list.
5. Allowance and turnaround tracking (`allowance.py`), KPIs (`kpi.py`) and lead scoring (`score_leads.py`) run on a schedule, with alerts.

**What stays human, always:** sales conversations, approving prices, allergen information and anything legal, the first message to any new prospect, and handling complaints.

## 6. SOPs a contractor can follow

Everything is already written as a step-by-step checklist:

| Task | SOP |
|---|---|
| Start here | [`ops/sops/contractor-handbook.md`](../ops/sops/contractor-handbook.md) |
| Onboard a client | `ops/delivery/onboarding/` (welcome email, intake questionnaire, kickoff checklist) |
| Launch a site in 5 days | `ops/delivery/launch-sop.md` (with QA checklist) |
| Handle an edit request | `ops/delivery/edits/edit-workflow.md` |
| Monthly maintenance and reports | `ops/delivery/maintenance/` |
| Offboard a client | `ops/delivery/offboarding/offboarding.md` |
| Walk-ins and outreach | `ops/outreach/scripts.md`, `sales-call.md` |
