# Delivery system

This is how Running Tab turns a signed venue into a live site in 5 working days, then looks after it every month.

**Who does what:** the **agent** (Claude) does the work. The **founder** approves anything a client will see and handles conversations. Anything marked 👤 needs the founder. Anything marked 🤖 the agent can do.

| Stage | Document | Tools and trackers |
|---|---|---|
| 1. Onboarding | [`onboarding/welcome-email.md`](onboarding/welcome-email.md), [`onboarding/intake-questionnaire.md`](onboarding/intake-questionnaire.md), [`onboarding/kickoff-checklist.md`](onboarding/kickoff-checklist.md) | `ops/clients.csv` |
| 2. Launch in 5 days | [`launch-sop.md`](launch-sop.md) | `scripts/new-client.sh`, [`client-template/`](client-template/) |
| 3. Edit requests | [`edits/edit-workflow.md`](edits/edit-workflow.md) | `edits/edit-log.csv`, `scripts/allowance.py`, GitHub Issues |
| 4. Monthly care | [`maintenance/monthly-checklist.md`](maintenance/monthly-checklist.md), [`maintenance/report-template.md`](maintenance/report-template.md) | UptimeRobot, PageSpeed Insights |
| 5. Offboarding | [`offboarding/offboarding.md`](offboarding/offboarding.md) | Stripe, the client's repo |

## How a client site is put together

- **One private GitHub repo per client**, named `client-<slug>`, created by `scripts/new-client.sh`.
  - Keeping each client separate makes it simple to hand over their site files for free when they leave, and limits mistakes to one client.
- **Nearly all the content is in `venue.json`**: menu, hours, notice banner, events, private hire, colours and contact details.
  - A typical edit request is a small change to that one file, which is quick and low-risk for the agent.
- **The template is `VenueSite.astro`.** The master copy is in `site/src/templates/venue/`. The 3 demo sites on the Running Tab website use the same file, so the portfolio always shows exactly what clients get.
- **Each client site is its own Cloudflare Pages project** on the free tier. Each branch gets a preview URL, so changes can be checked before going live.

## Known limits of template v1 (backlog)

- **The template is a single scrolling page with sections** (menu, about, events, private hire, visit). The plans promise "up to 5 pages" on Core and "up to 10" on Plus. Until v2, explain that these are delivered as sections of one page, or build extra pages by hand. **v2 should split out `/menu`, `/events` and `/private-hire` as separate pages**, which is also better for Google.
- **Photos:** gallery items can be real photos (`{ "src": "/images/bar.jpg", "alt": "…" }`, with files in `public/images/`) or coloured placeholder tiles. Compress photos to about 1600px wide and under 300 KB before adding them. v2 could use Astro's `<Image>` to optimise them automatically.
- **The private-hire form needs a Web3Forms key on the client's email** (free), set in `venue.json` as `formAccessKey`.
