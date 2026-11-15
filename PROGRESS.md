# PROGRESS

**Business:** a website-as-a-subscription service for independent hospitality venues in Cambridge, UK.
**Operating model:** the AI agent does the work, and the founder owns the relationships.
**Goals (revised):** £2,250 MRR by May 2027, £3,750 MRR by Nov 2027. Budget: £100 upfront, £50/month.

## Decisions log
| Date | Decision |
|---|---|
| 2026-11-15 | Location: Cambridge, UK. Brand to be chosen in Phase 3. Separate repo `WebsiteService`. |
| 2026-11-15 | Operating model: the agent handles delivery and admin, and the human handles sales, approvals and video. |
| 2026-11-15 | Niche **approved**: independent food & drink (Plan B: guest accommodation). |
| 2026-11-15 | Goals cut to 75% of the original (£2,250 / £3,750 MRR). Strategy: lower price, more volume. Provisional core price £49/month (no VAT, 3-month minimum); founding venues £29/month. |
| 2026-11-15 | Founder approved £49 core price with a 3-month minimum. Draft tiers: Core £49 / Plus £79 / Group £129. |
| 2026-11-15 | Tiers approved (revisit after validation). Plus includes same-day changes 7 days a week. Site files are free whenever a client leaves. |
| 2026-11-15 | Phase 5 defaults: WhatsApp for edit requests; routine hours/closure changes skip founder approval after a client's first 2 weeks; template v2 after the founding venues. |
| 2026-11-15 | Name chosen: **Running Tab** (domain and trademark checks still to run). Earlier recommendation was Housemade. Recommended stack: Cloudflare + GitHub + Stripe + WhatsApp Business. |

## Phase 1: Concept & validation (`docs/01-concept.md`)
- [x] 3 niches scored, with a recommendation
- [x] Ideal customer profile
- [x] Positioning statement and one-line offer (price provisional)
- [x] Competitor scan template (`ops/competitor-scan.csv`)
- [x] 14-day validation plan and script (`ops/validation-log.csv`)
- [x] Founder approves the niche and provisional offer
- [x] Market price check (in `docs/01-concept.md` §4)
- [ ] Validation run: 10 conversations logged
- [ ] Go or no-go recorded

## Phase 2: Offer, pricing & unit economics
- [x] `docs/02-offer.md`: 3 tiers, scope rules, cancellation and ownership, guarantee
- [x] `ops/pricing-model.csv` with formulas (including AI agent running costs), checked by recalculating in LibreOffice
- [x] Founder approves tier names and prices, ownership terms, and 7-day turnaround on Plus

## Phase 3: Brand & business setup
- [x] `docs/03-setup.md`: 5 names and checks, UK legal and admin checklist, tool stack, brand kit
- [x] Founder picks a name: Running Tab
- [ ] Founder runs the name checks (domain, Companies House, trademarks, social handles)
- [ ] Register with HMRC, open a bank account, ICO fee, Stripe, insurance quotes

## Phase 4: Agency website (`/site`)
- [x] Stack chosen and justified (Astro, static); runs with one command: `cd site && npm install && npm run dev`
- [x] Pages: Home, How it works, Pricing, Work, FAQ, Contact, Terms (draft), Privacy (draft), Thanks, 404
- [x] Stripe Payment Links via `.env` (no secrets); lead form (Web3Forms); cookieless analytics; meta, Open Graph, JSON-LD, sitemap and robots.txt
- [x] Deploy guide (Cloudflare Pages) and domain guide in `site/README.md`
- [x] 3 demo sites for fictional venues from one reusable template (`site/demos/*.json`)
- [x] Build passes; checked at phone and desktop widths with no sideways scrolling
- [ ] Founder: fill in placeholders (name, address), create Stripe links, Web3Forms key, Cal.com link, then deploy
- [ ] Solicitor review of Terms and Privacy

## Phase 5: Delivery system (`/ops/delivery`)
- [x] Client site template (`ops/delivery/client-template/` + `scripts/new-client.sh`, tested: generates and builds) and 5-day launch SOP with QA checklist
- [x] Onboarding: welcome email, intake questionnaire, kickoff checklist
- [x] Edit request workflow, turnaround standards, message templates; `clients.csv` + `edit-log.csv` + `allowance.py` (allowance, missed turnarounds, £10 credits)
- [x] Monthly maintenance checklist, seasonal nudges, and report templates (Core one-liner; Plus and Group report)
- [x] Offboarding process (free site files, domain handover, data deletion)
- [x] `CLAUDE.md` operating rules for the agent
- [ ] Backlog: template v2 with separate /menu, /events, /private-hire pages (the plans promise "pages"; v1 is one page with sections)

## Phase 6: Go-to-market (`docs/06-acquisition.md`, `/ops/outreach`)
- [x] 90-day plan with weekly targets (16 Nov 2026 to 14 Feb 2027; about 16 clients)
- [x] Lead sources, lead-scoring rubric, `ops/crm.csv`, `score_leads.py` (tested), `fsa_leads.py` (untested: FSA API blocked here)
- [x] Walk-in, phone, letter, email (limited companies only) and DM scripts; 4-touch follow-up; PECR/GDPR channel rules; suppression list
- [x] Free health check and homepage mockup lead magnet (process + template)
- [x] 30-day short-form content calendar
- [x] Referrals ("buy a round": a month free each) and partner list
- [x] Sales call script, objections, close and payment flow
- [x] Own Google Business Profile and local SEO
- [ ] Founder: run `fsa_leads.py` on your laptop, or build the first 40 leads by walking the area

## Phase 7: Launch, metrics & scaling (`docs/07-scale.md`)
- [ ] Launch checklist and first-5-clients sprint
- [ ] KPI spec and calculator script in `/ops`
- [ ] Retention playbook
- [ ] Scaling path and contractor SOPs

## Definition of done
- [ ] Every phase complete
- [ ] Site builds and runs with one command; deploy documented
- [ ] A weekly Monday action list to land the first paying subscriber
