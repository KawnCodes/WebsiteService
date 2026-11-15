# Your weekly action list: from Monday 16 November to your first paying subscriber

👤 = you · 🤖 = ask the agent (open a Claude Code session in this repo and paste the task)

**The goal:** your first founding venue **paying £29/month by about Monday 7 December 2026**. Then 5 founding venues by about 18 December.

---

## Week 1: Mon 16 to Sun 22 Nov · Get set up, start conversations

### Monday 16 (about 5 hours)
- [ ] 👤 **Morning (1 hour):** run the name checks in `docs/03-setup.md` §1: domain, Companies House, the UK trademark register (classes 35 and 42), social handles. **Buy the domain** and claim `@runningtab…` on Instagram and TikTok.
- [ ] 👤 Register for Self Assessment on GOV.UK. Start opening a free business bank account.
- [ ] 🤖 *"Build 40 leads in `ops/crm.csv` for Mill Road and Chesterton from public information, check each website, then run `score_leads.py`."*
  - The agent can't reach every site from here, so you may need to paste Google Maps links in. Or run `fsa_leads.py` on your laptop.
- [ ] 👤 **Afternoon (2.5 hours):** walk Mill Road. You're not selling yet; you're **listening**. Use the Phase 1 script (`docs/01-concept.md` §6) and aim for 3 conversations. Log each one in `ops/validation-log.csv`.

### Tuesday 17 (about 5 hours)
- [ ] 🤖 *"Put my name, address and domain into the site config, then walk me through deploying to Cloudflare Pages."* (`site/README.md`)
- [ ] 👤 Set up: a free Web3Forms key, a Cal.com link, and WhatsApp Business on your phone. Add them to `.env` and to Cloudflare.
- [ ] 🤖 *"Write health checks for the top 20 leads."* 👤 Print them (about £5).
- [ ] 👤 **2:30–5pm:** walk-ins with health checks, about 8 venues.

### Wednesday 18 (about 5 hours)
- [ ] 👤 Check the site is live on your domain. Send a test enquiry from your phone.
- [ ] 👤 **2:30–5pm:** walk-ins, about 8 venues (Chesterton / Mitcham's Corner).
- [ ] 🤖 *"Turn my voice-memo notes into rows in `validation-log.csv` and `crm.csv`, and draft follow-ups."* 👤 Approve and send them.

### Thursday 19 (about 5 hours)
- [ ] 👤 Set up Stripe: verify your account, create the 4 Payment Links (14-day trial, terms checkbox) and turn on the Customer Portal. Add the links to `.env`.
- [ ] 🤖 *"Make homepage mockups for the 2 warmest leads."* (`docs/06-acquisition.md` §5)
- [ ] 👤 **2:30–5pm:** walk-ins and return visits. Show mockups on your phone.

### Friday 20 (about 3 hours)
- [ ] 👤 **3–5pm:** quick return visits to anyone who said "come back Friday".
- [ ] 👤 Get insurance quotes (professional indemnity and public liability).
- [ ] 👤 Do the ICO self-assessment. Pay the fee if it applies (about £52).

### Weekend
- [ ] 👤 Film 2–3 videos from `ops/outreach/content-calendar.csv` (days 1–3) and post them.
- [ ] 👤 Rest. Hospitality burnout is real, and you're about to do it from the other side.

**End of week 1 target:** 6+ owner conversations · 2+ mockups sent · site live · Stripe ready

---

## Week 2: Mon 23 to Sun 29 Nov · Close founding venues

- [ ] 👤 **Monday:** run the Monday routine (below). 🤖 *"Make mockups for every lead who said yes to one."*
- [ ] 👤 **Tue–Thu, 2:30–5pm:** walk-ins (8 a day) plus mockup follow-ups in person. **Make the founding offer** to everyone who confirms the problem (`ops/outreach/sales-call.md`).
- [ ] 👤 **When someone says yes:** send the confirmation message, get "confirmed" back, send the Founding Stripe link (14-day trial), and send the welcome email and intake questionnaire. Book the kickoff.
- [ ] 🤖 *"Add the new client to `clients.csv` and create their site with `new-client.sh`."*
- [ ] 👤 **Sunday 29: the go / no-go review.** 🤖 *"Summarise `validation-log.csv` against the success criteria in `docs/01-concept.md` §6."* Then decide: carry on, adjust the price or offer, or switch to Plan B (guest accommodation).

**End of week 2 target:** 10+ conversations in total · 2 founding venues confirmed

---

## Week 3: Mon 30 Nov to Sun 6 Dec · Build and launch founding venue #1

- [ ] 👤 **Monday:** the kickoff visit for founding venue #1 (`ops/delivery/onboarding/kickoff-checklist.md`). Take the photos.
- [ ] 🤖 Days 1–2 of the launch SOP: fill in `venue.json`, type up the menu, set up the preview, run QA.
- [ ] 👤 **Wednesday:** send the client the preview. 🤖 Make their changes the same day.
- [ ] 👤 **Thursday:** connect their domain, check Google Business Profile, get their written approval.
- [ ] 👤 **Tue–Thu afternoons:** keep doing walk-ins (6 a day) to fill founding spots 3–5.
- [ ] 👤 **Friday 4 Dec, or Monday 7 Dec at the latest: GO LIVE.** End the Stripe trial so billing starts. Send the "you're live" message. **🎉 Your first paying subscriber.**
- [ ] 🤖 Update `clients.csv` and add the UptimeRobot monitor. 👤 Put a reminder in your calendar for day 25.

---

## Every Monday after that (about 45 minutes)

1. 🤖 *"Run `ops/kpi.py --md`, `ops/delivery/scripts/allowance.py` and `ops/outreach/score_leads.py`, and give me a 5-line summary."*
2. 👤 Read it. Answer 3 questions:
   - Am I on target for this week in `docs/06-acquisition.md` §1?
   - Is anything late, or any client showing a warning sign (`docs/07-scale.md` §4)?
   - What's the **one** weakest step in the funnel, and what am I changing this week to fix it?
3. 👤 Block your walk-in sessions in your calendar (Tue–Thu 2:30–5pm, and Mon/Fri 3–5pm).
4. 🤖 *"Prepare health checks for this week's A-list, and mockups for anyone waiting on one."*
5. 👤 Batch-film 3–4 videos for the week.
6. 👤 Log last week's hours and spending, if you haven't already.
7. 👤 Do one thing for a client: a review ask, a referral ask, a seasonal nudge or a check-in.
