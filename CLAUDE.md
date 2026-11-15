# Running Tab: operating notes for the AI agent

Running Tab is a website-subscription business for independent cafés, pubs and restaurants in Cambridge, UK. The founder handles sales, approvals and client relationships. You (the agent) do the delivery and admin work. Start with `PROGRESS.md`.

## Ground rules
- **Nothing reaches a client or a prospect without founder approval.** That means messages, emails and outreach. You draft them, and the founder sends them. The exception is routine edits that the founder has marked as pre-approved.
- **Copy prices, allergen statements and dietary tags exactly as the client gave them.** If something is unclear, ask; never guess.
- **Only do what was requested.** Out-of-scope work gets a quote (see `docs/02-offer.md`), never a free extra.
- **Never put secrets in a repo.** Site settings in `.env` are public `PUBLIC_*` values only, and there are no Stripe secret keys anywhere.
- **Be honest in reports and marketing.** No invented statistics, reviews or results. Demo venues must stay clearly labelled as fictional.
- **Write in UK English and use £.** Keep the tone warm, plain and short (see `docs/03-setup.md` §4).

## Where things are
- Strategy: `docs/01-concept.md` to `docs/0x-*.md`
- Agency site and the master venue template: `site/` (`site/src/templates/venue/VenueSite.astro`, demo data in `site/demos/*.json`)
- Delivery: `ops/delivery/README.md` (launch SOP, edit workflow, maintenance, offboarding)
- Trackers: `ops/clients.csv`, `ops/delivery/edits/edit-log.csv`, `ops/validation-log.csv`, `ops/pricing-model.csv`

## Common jobs
- **New client:** `ops/delivery/scripts/new-client.sh <slug>`, then follow `ops/delivery/launch-sop.md`.
- **Edit request:** follow `ops/delivery/edits/edit-workflow.md`, logging it in `edit-log.csv` and as a GitHub issue.
- **Allowance and turnaround report:** `python3 ops/delivery/scripts/allowance.py [YYYY-MM]`
- **Leads:** `python3 ops/outreach/score_leads.py`, and check `ops/outreach/do-not-contact.csv` before drafting any outreach. Channel rules are in `docs/06-acquisition.md` §3.
- **Check the agency site builds:** `cd site && npm run build`
