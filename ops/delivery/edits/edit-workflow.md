# Edit request workflow

**Goal:** every request is logged, counted against the plan's allowance, done on time and confirmed back to the client. This is where the agent saves the most time.

## Turnaround standards (from `docs/02-offer.md`)

| Plan | Menu, hours, closures | Everything else | Allowance a month |
|---|---|---|---|
| Core / Founding | Within 1 working day | Within 1 working day | 5 |
| Plus | **Same day, 7 days a week**, if sent before 3pm (otherwise by the end of the next day) | Within 1 working day | 15 |
| Group | Same as Plus | About 4 working hours | Unlimited small changes (fair use, about 40) |

- "Within 1 working day" means by 23:59 on the next working day. Working days are Monday to Friday, excluding England & Wales bank holidays.
- The clock starts when we have **everything needed**: the text, the photo, the prices.
- If we miss a turnaround: **£10 off next month**, once per client per month. `scripts/allowance.py` lists who is owed a credit.

## The flow

```
Client sends a WhatsApp, email or form message
   │
   ▼  🤖 / 👤 log it: one row in edits/edit-log.csv, one GitHub issue in client-<slug> (Edit request template)
   │
   ├── Out of scope? ──► 👤 reply with an add-on quote (template C), set counts=no, status=declined
   ├── Missing info?  ──► 👤 ask for it (template D); the clock hasn't started
   │
   ▼  🤖 acknowledge (template A), within 1 hour during 8am–8pm
   ▼  🤖 make the change on a branch (usually just venue.json); Cloudflare builds a preview URL
   ▼  🤖 self-check: build passes, the changed section looks right on a phone, prices and tags match the request exactly
   ▼  👤 approve: open the preview, about 2 minutes (skipped for routine hours or closure banners once trusted)
   ▼  🤖 merge to main, which goes live; check the live page
   ▼  🤖 reply "Done" with the link (template B); close the issue; fill in done_at in edit-log.csv
```

**Rules for the agent:**
- **Only ever change what was asked.** Prices, allergen information and dietary tags must be copied **exactly** from the client's message. If anything is unclear, ask; don't guess.
- **One request is one issue**, even if the client sends several messages about it.
- **A whole new menu counts as one request.** Several small changes in one message count as one request, if together they take about 30 minutes or less.
- **Anything that needs a new page, feature or integration is out of scope.** Never do it quietly for free. Quote it.
- **Allergen statements and anything legal-sounding** always need 👤 approval before going live.

## Tracking allowances

- Log every request in `edits/edit-log.csv`. `counts=yes` means it uses up allowance; use `no` for our own fixes, declined requests and changes before launch.
- Run the report weekly, and on the 1st of each month for the previous month:
  ```bash
  python3 ops/delivery/scripts/allowance.py            # this month
  python3 ops/delivery/scripts/allowance.py 2026-12    # a given month
  ```
  The report shows how many requests each client has used out of their allowance, flags anyone near or over it, lists open requests with their due times, and lists any £10 credits owed.
- **When a client goes over the allowance:**
  - first time, do it anyway and mention it kindly;
  - second month in a row, suggest an extra pack of 5 (£15) or upgrading their plan (template E).
  - Never stop work in the middle of a request.

## Message templates

**A. Acknowledge**
> Got it 👍 I'll have {short summary} live {by tonight / by end of {day}}.

**B. Done**
> Done ✅ {summary} is live: {link to the section}. That's {n} of your {allowance} changes this month.

**C. Out of scope**
> Happy to do that! A {new page / feature} is outside the monthly changes, but it's a one-off £{price}. Shall I go ahead? It'll be live within {x} working days of your go-ahead.

**D. Need info**
> On it. Quick check before I publish: {question}? (e.g. Is the new burger gluten-free, or should I leave the GF tag off?)

**E. Over allowance**
> Quick heads-up: you've sent {n} changes this month against {allowance} on {plan}, which is great, it means the site's being used! If that's normal for you, {Plus at £79 gives you 15 plus same-day menu changes / a 5-change pack is £15}. No pressure, just let me know.

## Weekly 15-minute review (👤)
- Run `allowance.py`. Check there's nothing late and nothing waiting on you.
- Look over 2–3 of the agent's merged changes at random, as a quality check.
- Note any client who's gone quiet, meaning no requests in 6 weeks or more. That's a churn warning sign, so send them a friendly check-in.
