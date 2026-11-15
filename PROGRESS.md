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
- [ ] Founder approves tier names and prices, ownership terms, and 7-day turnaround on Plus

## Phase 3: Brand & business setup
- [ ] `docs/03-setup.md`: 5 names and checks, UK legal and admin checklist, tool stack, brand kit

## Phase 4: Agency website (`/site`)
- [ ] Stack chosen and justified; runs with one command
- [ ] Pages: Home, How it works, Pricing, Portfolio, FAQ, Contact, Terms, Privacy
- [ ] Stripe Payment Links via `.env`; lead form; analytics; SEO, sitemap and robots.txt
- [ ] Deploy and domain guide
- [ ] 2–3 hospitality demo sites in `/site/demos`

## Phase 5: Delivery system (`/ops/delivery`)
- [ ] Client site template and 5-day launch process
- [ ] Onboarding: welcome email, intake questionnaire, kickoff checklist
- [ ] Edit request workflow and allowance tracking
- [ ] Monthly maintenance checklist and report template
- [ ] Offboarding process

## Phase 6: Go-to-market (`docs/06-acquisition.md`, `/ops/outreach`)
- [ ] 90-day plan with weekly targets
- [ ] Lead list method, scoring rubric, `ops/crm.csv`
- [ ] Email, DM and phone scripts and a 4-touch sequence (PECR-compliant)
- [ ] Free audit and mockup lead magnet
- [ ] 30-day short-form content plan
- [ ] Referrals and partnerships
- [ ] Sales call script, objections, close and payment flow
- [ ] Own Google Business Profile and local SEO

## Phase 7: Launch, metrics & scaling (`docs/07-scale.md`)
- [ ] Launch checklist and first-5-clients sprint
- [ ] KPI spec and calculator script in `/ops`
- [ ] Retention playbook
- [ ] Scaling path and contractor SOPs

## Definition of done
- [ ] Every phase complete
- [ ] Site builds and runs with one command; deploy documented
- [ ] A weekly Monday action list to land the first paying subscriber
