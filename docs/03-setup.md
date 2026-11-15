# 03: Brand & Business Setup

_Status: draft v1, 15 Nov 2026. UK sole trader, based in Cambridge. **This is not legal or tax advice.** Items marked ⚖️ need a professional to check them or need confirming on the official GOV.UK, HMRC or ICO page._

## 1. Business name: final 3 (revised 15 Nov 2026)

I brainstormed about 30 names and ran a quick web search on the strongest. Each name had to:
- be easy to say once over the noise of a busy bar and still be remembered,
- mean something to hospitality people,
- not clash with an existing web or hospitality brand.

| | **Running Tab** | **Housemade** | **Walk-In** |
|---|---|---|---|
| The idea | Your website on a running tab: a small monthly amount, no big bill | "House-made", as on a menu: made here, made properly | Walk-ins welcome: no booking, no contract, no fuss. It also brings customers through the door. |
| Tagline | "Put your website on the tab." | "Websites for independent venues. Made in Cambridge." | "Websites for venues. Walk-ins welcome." |
| How it sounds in the pitch | "We're Running Tab: your website on a monthly tab, £49." It explains the business model in two words. | "I'm from Housemade. We build and run websites for independents like you." | "I'm from Walk-In. Funny, because I literally just walked in." A built-in opener for door-to-door sales. |
| Strengths | Very memorable, slightly cheeky, says it's a subscription without the word "subscription" | Warm, a bit premium, works beyond food (guesthouses, bakeries) and outside Cambridge | Fits how you'll sell, friendly, short |
| Risks | "Tab" can suggest a bill that keeps growing. Copy needs to keep it positive: "small, fixed, cancel any time." | Safer but less distinctive, and it doesn't hint at the monthly model | Spelling: walk-in, walkin or walk in? Walk-in fridge jokes. A common word, so harder to rank for on Google. |
| Quick conflict search | No web or hospitality brand found | No web or hospitality brand found | No web or hospitality brand found |
| Domains to try | `runningtab.co.uk`, `runningtab.studio`, `runningtabsites.co.uk` | `housemade.studio`, `housemadesites.co.uk`, `gethousemade.co.uk` | `walkin.studio`, `walkinsites.co.uk`, `walkinwebsites.co.uk` |
| **Score** (memorable, meaning, low risk; out of 15) | **13** | **12** | **10** |

**Recommendation: Running Tab.** With no marketing budget and no audience, being remembered after a 2-minute chat counts most, and Running Tab explains the offer before you do. Housemade is the safe runner-up.

**Rejected after searching:**
- **Yes Chef**: a website agency called Yes Chef Studio already exists.
- **Covers**: a hospitality branding and web studio called Covers already exists.
- **Mise**: "Mise Studio" already builds restaurant websites, and there's restaurant software called Mise.
- **Open Tab**: too close to OpenTable, which risks confusion or a complaint.
- **The Pass, Corner Table, Open Today, Front Door, Chalkboard**: too generic, or already used by many restaurants.

_These were quick web searches, not legal clearance. Run the checks below before buying anything._

### Checks to run before committing

Do these yourself. It takes about 30 minutes.

1. **Domain:** search a registrar such as Cloudflare, Porkbun or Namecheap. Note the *renewal* price, not just the first-year price.
2. **Companies House:** search the name on GOV.UK ("Find and update company information"). You don't need a company as a sole trader, but avoid names that match an existing company in a similar trade, because of passing off.
3. **Trademarks:** search on GOV.UK ("Search for a trade mark") for classes **35** (advertising and business) and **42** (web design and hosting). If someone has an identical or close mark in these classes, drop the name. ⚖️ Registering your own trademark costs about £170 or more online. That's not needed now, so revisit it in year 2.
4. **Social handles:** check Instagram, TikTok, YouTube, Facebook and LinkedIn for `@housemade`, `@housemade.studio` or `@housemadecambridge`. Claim them all on the same day.
5. **Google:** search "Housemade Cambridge" and "Housemade web design" and make sure nobody nearby is already using it.
6. **The say-it test:** say it to 3 people from hospitality and ask them to spell it back a day later.

**Trading-name rules for sole traders:** you can trade under a name other than your own, but your **own name and an address must appear** on invoices, contracts and your website. ⚖️ Confirm this on the GOV.UK page about naming a business.

## 2. UK legal and admin checklist (sole trader)

### This week (before the first client)
- [ ] **Register as self-employed with HMRC for Self Assessment.**
  - The legal deadline is 5 October after the end of the tax year you start trading in. For the 2026/27 tax year that's 5 Oct 2027.
  - Do it now anyway, because the UTR (tax reference) arrives by post and takes time.
- [ ] **Open a separate business bank account.** Free business accounts are available (Starling, Monzo, Tide and others; compare their current fees). Keep every penny of the business going through it.
- [ ] **Keep records from day one** in a simple spreadsheet: income, expenses and receipts. HMRC expects records to be kept for at least 5 years after the 31 January filing deadline.
- [ ] **ICO data protection fee.** Do the ICO's "do I need to pay?" self-assessment. Most businesses that hold customer and prospect data electronically must pay. Tier 1 is about £52 a year. ⚖️
- [ ] **Insurance:** get quotes for **professional indemnity** (in case a client claims your work cost them money) and **public liability** (because you're walking into venues). These are often bundled for about £10–£20 a month. ⚖️ Have them in place before the first paid client.

### Before you take payments
- [ ] **Stripe account** in your name as a sole trader, linked to the business bank account. Stripe will ask for ID (KYC). Turn on the **Customer Portal** so clients can update their card or cancel themselves.
- [ ] **Client terms of service, with a data processing agreement (DPA) built in.** I'll draft these in Phase 4 as `site` Terms plus `ops/contracts/`. They should cover:
  - Service scope, edits and turnaround (from `docs/02-offer.md`).
  - Minimum term, notice, the guarantee, and payment and suspension.
  - Ownership: the client owns their domain and content, and gets free site files when they leave.
  - Limitation of liability, capped at, say, 3 months' fees.
  - **UK GDPR Article 28 processor terms.** We process the personal data that comes through each client's enquiry and private-hire forms, so we're their *processor*.
  - A list of **sub-processors**: Cloudflare (hosting), Stripe (billing), Anthropic (the AI agent), our email provider, and the form provider.
  - ⚖️ **Have a solicitor review the terms once** before you've signed about 5 clients. Expect a few hundred pounds, and ask local firms for a fixed-fee review. That's the one professional cost worth budgeting for from early revenue.
- [ ] **Privacy policy** for the agency site: what we collect (lead forms, emails), why, how long we keep it, and people's rights. Name the AI tools that process client data. Draft in Phase 4. ⚖️
- [ ] **Cookies:** use **cookieless analytics** (Cloudflare Web Analytics) and no tracking pixels, so the agency site needs no cookie banner. ⚖️ The rules changed under the Data (Use and Access) Act 2025, so confirm the current position with the ICO.

### Later (keep an eye on these)
- [ ] **VAT:** you must register once taxable turnover goes over **£90,000** in any rolling 12 months. We forecast about £45k a year by Nov 2027, so this isn't close, but check every quarter. ⚖️
- [ ] **Making Tax Digital for Income Tax:** sole traders over certain income levels must keep digital records and send quarterly updates.
  - The thresholds are being phased in: £50k from April 2026, £30k from April 2027, £20k from April 2028. They're based on income from earlier tax years.
  - At our forecast you're likely to come in from **April 2028 or 2029**. Use MTD-compatible software from year 2 so it's painless. ⚖️
- [ ] **Accessibility:** build every client site to **WCAG 2.2 AA** as standard. It's good practice, reduces risk under the Equality Act, and is a selling point.
- [ ] **Email outreach rules (PECR):** covered fully in Phase 6, before any cold email goes out.
- [ ] **Limited company:** think about switching once profit reaches about £30–£50k, for tax efficiency and limited liability. ⚖️ Ask an accountant then, not now.

### What to get a professional to check
1. The client terms and DPA (solicitor), once, before about 5 clients.
2. Your first Self Assessment return (an accountant, or use HMRC's free guidance). Optional in year 1.
3. Whether your insurance covers your actual work.
4. Whether to switch to a limited company, when profit grows.

## 3. Tool stack (free first)

The rule is that the agent must be able to read and write every tool, so we prefer files in the repo and tools with APIs.

| Job | Tool | Cost | Why |
|---|---|---|---|
| Agency site and client sites hosting | **Cloudflare Pages** | £0 | Free tier with no bandwidth limits, fast in the UK, deploys from GitHub |
| DNS, email forwarding, analytics | **Cloudflare** (DNS, Email Routing, Web Analytics) | £0 | All in one dashboard. Analytics are cookieless. |
| Code, sites, edit tracking | **GitHub** (you have it) + **GitHub Issues** | £0 | Each edit request becomes an issue the agent picks up, so there's a built-in audit trail |
| AI agent | **Claude Pro** (includes Claude Code), then Max at about 25 clients | about £18, then about £90 a month | Does the builds, edits, research and drafts |
| Billing | **Stripe Billing** via Payment Links + Customer Portal | Fees only | Subscriptions with no code. Payment Links can require ticking the terms. |
| CRM | **`ops/crm.csv`** in the repo (Phase 6) | £0 | The agent can read and update it directly. Move to HubSpot free only if it gets too big. |
| Client messages | **WhatsApp Business** on your phone + email | £0 | Venue owners message on WhatsApp. That's where edit requests will come in. |
| Business email (sending) | **Zoho Mail free plan** on your domain, or Gmail with forwarding at first | £0 | Sending from `hello@yourdomain` builds trust. Upgrade to Google Workspace (about £7 a month) only when needed. Check that Zoho's free plan still allows a custom domain. |
| Booking calls | **Cal.com** free | £0 | 15-minute "website chat" link for the site and follow-ups |
| Contracts and e-sign | Terms accepted at Stripe checkout, plus an order-form PDF sent by email | £0 | Enough for small B2B deals. ⚖️ Ask the solicitor to confirm. Add a free e-sign tool later if a client wants one. |
| Lead forms | Cloudflare Pages Functions or a free form service (decided in Phase 4) | £0 | |
| Uptime monitoring | **UptimeRobot** free | £0 | 50 monitors, enough for year 1 |
| Design | **Figma** or **Canva** free | £0 | Mockups and social graphics |
| Bookkeeping | Spreadsheet + bank app, then MTD software in year 2 | £0 | |

**Recurring costs I'm adding:** Claude Pro at about £18 a month. Everything else stays on free tiers until there's revenue. Insurance (about £15 a month) and the ICO fee (about £52 a year) are business costs rather than tools. All of these are in `ops/pricing-model.csv`. **Total: about £48 a month.**

## 4. Brand kit (works for any of the 3 names; logo direction written for Housemade, adjust once chosen)

### Personality
Like a good front-of-house manager: **warm, quick, plain-spoken and reliable**. It knows the trade, never shows off, and has a touch of kitchen humour.

### Colours
Every text and background pair below passes WCAG AA contrast (4.5:1 or higher).

| Token | Hex | Use | Contrast |
|---|---|---|---|
| `ink` | `#1F1B16` | Body text, logo | 15.9:1 on cream |
| `cream` | `#FAF6EF` | Page background | — |
| `tomato` | `#B83A1E` | Buttons and calls to action, links, accents | White text 5.7:1; on cream 5.3:1 |
| `sage` | `#4F6F55` | Secondary buttons, tags | White text 5.6:1; on cream 5.2:1 |
| `butter` | `#F2C14E` | Highlights, "specials" badges (ink text only) | Ink text 10.2:1 |
| `stone` | `#6B635A` | Muted text, captions | 5.5:1 on cream |

### Fonts (free, from Google Fonts)
- **Headings: Fraunces**, a soft serif that feels like a menu or a chalkboard. Use weights 600–700.
- **Body: Inter**, clear on phones. Use 400 and 600.
- Sizes: body 17–18px on mobile, headings in a 1.25 ratio scale.

### Logo direction
- **A lowercase wordmark, "housemade."**, in Fraunces 700, in ink, ending in a small tomato-coloured full stop.
- **Mark and favicon:** a rounded tomato square with a cream lowercase "h". The arch of the "h" hints at a roof or a serving hatch.
- Don't use a stock "web design" cursor, or a chef's hat clip-art. The agent will produce SVG versions in Phase 4. Get a designer to polish it later if you want.

### Tone of voice

| Do | Don't |
|---|---|
| "Text us your new menu. It's live tonight." | "We leverage cutting-edge AI solutions to optimise your digital presence." |
| Say "show up on Google" | Say "SEO-driven organic visibility" |
| Use short sentences and real venue words: covers, specials, private hire, service | Use agency jargon: synergy, holistic, bespoke digital journey |
| Give a straight price: "£49 a month, no VAT, no contract after 3 months" | Say "Contact us for a quote" |
| Mention AI honestly in the FAQ: "We use modern tools, including AI, so changes are fast. A real person checks everything." | Put "AI-powered" in headlines |

### Photography and visuals
- Real Cambridge venues: natural light, hands, plates, chalkboards, busy service.
- Phone screenshots of real client sites, before and after.
- No stock photos of smiling office workers.

## 5. Setup order (about 2–3 hours, spread over the first week)

1. Run the name checks in §1. Then buy the domain (about £10–£30) and claim the social handles.
2. Register as self-employed with HMRC.
3. Open the business bank account.
4. Do the ICO self-assessment and pay the fee if it applies (about £52).
5. Set up Cloudflare (DNS, email forwarding) and Zoho or Gmail for `hello@`.
6. Sign up for Claude Pro if you haven't already.
7. Create the Stripe account (payment links come after the Phase 4 site).
8. Get insurance quotes, and buy the policy when the first client is about to sign.

**Upfront total:** domain about £10–£30, printing about £10, ICO about £52, which comes to about £72–£92. That's within the £100.
