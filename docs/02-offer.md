# 02: Offer, Pricing & Unit Economics

_Status: draft v1, 15 Nov 2026. The numbers come from `ops/pricing-model.csv`. Change the inputs there, not here._

## 1. The three plans

There's **no setup fee** and **no VAT** on any plan. Every plan has a **3-month minimum**, then it's monthly with 30 days' notice. If a venue pays for a year upfront, it gets **2 months free**.

| | **Core: £49/mo** | **Plus: £79/mo** | **Group: £129/mo** |
|---|---|---|---|
| Best for | A single café, pub or restaurant that just needs it right | Busy venues with events, private hire and changing menus | Owners with 2–3 venues, or very events-heavy places |
| Pages | Up to 5 (Home, Menu, About, Book/Contact, Gallery) | Up to 10, adding Events, Private hire with an enquiry form, Gift vouchers, Careers | Up to 3 venues, 20 pages in total |
| Menu | A real web page (not a PDF), with allergen key | Same, plus seasonal and set menus | Same, for each venue |
| Edit requests per month | 5 | 15 | Unlimited small edits (fair use, about 40) |
| Edit turnaround | Within 1 working day | Same day for menu, hours and closure changes sent before 3pm, **7 days a week**; anything else within 1 working day | Same as Plus, with priority (about 4 working hours) |
| Hosting, SSL, backups, uptime monitoring | ✓ | ✓ | ✓ |
| Domain | Stays in your name and you pay for it (about £10/yr). We set it up. | We register it **in your name** and pay for it | Same as Plus, for each venue |
| Booking | Link or widget from your existing booking provider | Same, plus private-hire enquiry form | Same |
| Google Business Profile | Monthly check that your hours match | We manage it: hours, holiday closures, a monthly post and photos | Same, for each venue |
| SEO | Basic setup: titles, descriptions, structured data for menu and opening hours, sitemap | Same, plus a small monthly improvement | Same, plus a local SEO review each quarter |
| Report | One-line monthly email ("all fine, here's what changed") | Monthly report: visits, enquiries and changes made | Same, plus a quarterly 20-minute call |
| Support | Email or WhatsApp | Same | Same, plus a phone call when needed |

**Founding venues** (the first 5): build free, **£29/month for 6 months**, then Core at £49. The minimum term is 6 months. In return they give a testimonial, a case study and permission to film.

**Why there's no plan cheaper than £49:**
- A £29 plan would pull most clients down to it, and the model in §6 would need about 75 clients to hit the 6-month goal.
- £49 is already at the bottom of the full-service hospitality market (see `docs/01-concept.md` §4).
- The founding offer gives us a low price that's limited in time, without anchoring the whole business to it.

## 2. Scope rules

### What counts as one edit request
One message about content on an **existing page**, which the agent and a quick human check can finish in under about 30 minutes. Examples:
- Swap the whole menu for a new one (yes, the whole menu counts as **one** edit).
- Change prices, dishes, hours or holiday closures.
- Add an event to the Events page.
- Swap photos, up to 10 per request.
- Add or remove a banner ("Closed Boxing Day", "Now taking Christmas bookings").
- Change text, up to about 300 words.

Several changes in one message count as one request if they fit in that 30 minutes. Unused edits don't carry over to the next month. If a venue regularly goes over its allowance, we suggest the next plan up and don't charge per edit.

### Out of scope (offered as an add-on or a referral)
- New pages, new features or integrations, and redesigns. A **free refresh** is included every 24 months on Plus and Group.
- Online ordering systems, ecommerce, online shops.
- Writing more than about 300 words of copy from scratch, logos and branding, and photography.
- Email accounts, social media management, paid ads.
- Fixing problems inside third-party platforms such as their booking system, ordering app or POS.

### Add-ons (one-off unless stated)
| Add-on | Price |
|---|---|
| Extra page | £39 |
| Seasonal or campaign landing page (Christmas, Valentine's, Mother's Day) | £39 |
| Extra pack of 5 edit requests | £15 |
| Google Business Profile setup and clean-up (included in Plus and Group) | £49 |
| Connecting an ordering, booking or gift-voucher widget from their provider | £49 |
| QR menu and review table-card design (printing at cost) | £25 |
| Copywriting (menu descriptions, About page), per page | £39 |
| Brand tidy-up (logo clean-up, colours, fonts) | £99 |
| Professional email setup (Google Workspace or Microsoft billed to them) | £29 |
| Photography | Referral to a local photographer; we pass on the partner rate |

Moving content over from their old website is **free** as part of the build.

## 3. Term, cancellation, ownership, non-payment

- **Minimum term:** 3 months, or 6 months for founding venues. If a venue cancels during it, the remaining months are still due. **This sets up the 30-day exception in §4:** in the first 30 days after launch they can leave and get month 1 refunded.
- **After the minimum term:** monthly, with 30 days' notice by email or WhatsApp.
- **Always the client's:** their domain, which is always registered in their name, plus their text, menus, photos and logo. They can take these with them at any time.
- **The site itself (design and code):** we license it to them while they subscribe. When they leave after the minimum term, **they take a free copy of their full site files**, ready to host anywhere, and we help point their domain wherever they want within 5 working days. _Decided 15 Nov 2026: free at any point, to build trust and make "you're never locked in" part of the sales pitch._
- **Non-payment:** Stripe retries automatically.
  - At 7 days late we send a friendly reminder.
  - At 21 days late, edits pause.
  - At 45 days late, after written notice, the site is taken offline. Their domain stays theirs.
  - _The suspension terms need checking by a professional before you use the contract (Phase 3)._
- **Price lock:** the price a client starts on is fixed for 12 months. Any increase after that comes with 60 days' notice.

## 4. Guarantee (limited risk to us)

1. **Pay nothing until you love it.** No payment until you've approved the finished site and it's live.
2. **First 30 days on us.** If you're not happy within 30 days of launch, cancel and we refund month 1 and waive the minimum term.
3. **Turnaround promise.** If we miss a turnaround time, the next month is £10 cheaper. That's capped at £10 a month.

**Our maximum loss per client:** about 3 hours of your time, plus the agent's work, plus £49. That's affordable. The guarantee matters because a venue owner's main fear is being locked into something that doesn't work.

## 5. Where the money goes (costs we know about)

| Cost | Per month | Type |
|---|---|---|
| Client site hosting (Cloudflare Pages free tier) | £0 | Per client |
| Stripe: 1.5% + 20p card fee + about 0.7% Billing fee | £1.28 per £49 | Per client |
| Domain (Plus and Group only) | about £1 | Per client |
| Contingency (forms, image tools, odd costs) | £1 to £2 | Per client |
| AI agent: Claude Pro | about £18 | Fixed, until about 25 clients |
| AI agent: Claude Max 5x | about £90 | Fixed, from about 25 clients |
| Insurance (professional indemnity) | about £15 | Fixed, from the first client |
| Agency domain, printing, marketing | about £11 | Fixed |
| ICO data protection fee (about £52 a year) | about £4.33 | Fixed |

**Total fixed costs at the start: about £48 a month**, just inside the £50 budget. The upfront spend is about £10 for the agency domain, £10 for printing and £52 for the ICO fee, about £72 of the £100.

## 6. Unit economics (from `ops/pricing-model.csv`)

| | Core £49 | Plus £79 | Group £129 |
|---|---|---|---|
| Variable cost per client | £2.28 | £3.94 | £7.04 |
| Gross margin | £46.72 (95%) | £75.06 (95%) | £121.96 (95%) |
| Human hours per month | 0.5 | 0.75 | 1.5 |
| Margin per human hour | £93 | £100 | £81 |

**Assumed mix:** 70% Core, 25% Plus, 5% Group, plus about £4 per client per month from add-ons. That gives an average of **£64.50 revenue per client**.

| Goal | Clients needed | Profit before tax and NI | Human hours a week to look after them |
|---|---|---|---|
| £2,250 MRR (May 2027) | **35** | about £2,035 | about 5 |
| £3,750 MRR (Nov 2027) | **59** | about £3,512 | about 8 (plus sales time) |

**Sample 12-month plan** (in the CSV; change the "New clients" column to your actual numbers):

| | Dec | Jan | Feb | Mar | Apr | **May** | Jun–Nov |
|---|---|---|---|---|---|---|---|
| New clients | 2 | 5 | 7 | 8 | 9 | 9 | 5/month |
| Active (after 3% monthly churn) | 2 | 7 | 14 | 21 | 30 | **38** | → **59** by Nov |
| MRR | £58 | £270 | £708 | £1,198 | £1,737 | **£2,260 ✓** | → **£3,826 ✓** |

**Honest read:**
- **This plan only works if you sell steadily from January to May: about 8–9 new venues a month.** After that, about 5 a month holds the line.
- **The 70/25/5 mix is a guess.** If everyone picks Core, the average falls to about £53 and you need about 43 clients for May. Plus is the plan to steer busy venues towards. Its events and private-hire page with an enquiry form is the easiest upsell to justify: one private-hire booking pays for the year.
- **3% monthly churn is optimistic for hospitality.** The minimum term and the monthly report help keep clients. Free site files when a client leaves make leaving easier, but make the sale easier too. Replace it with real numbers after 6 months.

## 7. Things to verify

- Stripe fees in the UK: the card rate and the Billing percentage. Sources give 0.5% to 0.7% for Billing.
- Claude plan prices in GBP. Anthropic bills in USD, so card foreign-exchange fees may apply.
- Professional indemnity insurance quotes.
- The VAT registration threshold (currently £90,000 a year according to the sources I found). We're nowhere near it, but confirm with HMRC.
- Whether Cloudflare's free tiers (Pages, Email Routing, Web Analytics) still cover this use.

## 8. Decisions (15 Nov 2026)

- Plans approved: Core £49, Plus £79, Group £129. We'll revisit after validation.
- Site files are free whenever a client leaves after the minimum term.
- Plus includes same-day changes, 7 days a week, for menu, hours and closures sent before 3pm.
