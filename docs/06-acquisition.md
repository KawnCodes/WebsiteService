# 06: Go-to-market & client acquisition

_Status: draft v1, 15 Nov 2026. The main channel is **walking into venues**, backed up by phone, letters, compliant email to limited companies, short-form video, and referrals._

Scripts, the sales call, the content calendar and the tools are in [`ops/outreach/`](../ops/outreach/). The CRM is [`ops/crm.csv`](../ops/crm.csv).

## 1. The 90-day plan (Mon 16 Nov 2026 to Sun 14 Feb 2027)

**Funnel guesses to plan around** (these are guesses, not data; swap in your real numbers from week 3):

| Step | Assumed rate |
|---|---|
| Walk-in visit leads to a conversation with the owner or GM | ~35–40% |
| Conversation leads to them accepting a free mockup | ~50% |
| Mockup leads to a signed client | ~25% |

So about **40 visits → 15 conversations → 8 mockups → 2 clients a week**.

| Week (Mon) | Focus | Visits / touches | Owner conversations | Mockups sent | New clients | Notes |
|---|---|---|---|---|---|---|
| 1 · 16 Nov | Validation (`docs/01-concept.md` §6) | 25 | 6 | 2 | 0 | Build a list of 40 leads; print health checks |
| 2 · 23 Nov | Validation + founding offer | 25 | 6 | 4 | **2 founding** | Go or no-go on Sun 29 Nov |
| 3 · 30 Nov | Build founding sites #1–2 | 20 | 8 | 4 | 1 founding | First launch (5-day SOP) |
| 4 · 7 Dec | Founding spots 4–5 | 20 | 8 | 4 | 2 founding | Pitch: "set up in the quiet weeks of January" |
| 5 · 14 Dec | Book January chats | 15 | 6 | 3 | 0 | Venues are flat out, so book dates rather than push |
| 6 · 21 Dec | No visits | 0 | 0 | 0 | 0 | 🤖 builds and scores a list of 150 leads; film content |
| 7 · 28 Dec | Prepare | 0 | 0 | 8 prepared | 0 | 🤖 makes mockups for the top 20 leads ready for January |
| 8 · 4 Jan | **January push** | 40 | 15 | 8 | 1 | Founding case studies go up on the site |
| 9 · 11 Jan | Push | 40 | 15 | 8 | 2 | Start partner outreach (§6) |
| 10 · 18 Jan | Push + email to limited companies | 40 + 20 emails | 15 | 8 | 2 | Email sequence (§3) |
| 11 · 25 Jan | Push | 40 | 15 | 8 | 2 | Valentine's angle |
| 12 · 1 Feb | Push | 40 | 15 | 8 | 2 | Ask every client for referrals |
| 13 · 8 Feb | Push + **90-day review** | 40 | 15 | 8 | 2 | Compare real rates with these guesses and reset |
| **Total** | | **~385** | **~145** | **~83** | **~16** (5 founding + 11) | Pricing model needs 14 by end of Feb |

**Time:**
- About 5 walk-in sessions a week of 2–2.5 hours each, in quiet hours (Tue–Thu 2:30–5pm, and Mon/Fri 3–5pm).
- About 5 hours of calls and 3 hours of filming.
- That's **about 25 hours a week** of founder time while selling hard, inside your 30.
- The agent does the research, the mockups, the drafts and the CRM updates.

**Keep the weekly score** in `ops/crm.csv`, by filtering on the `stage` column. Every Monday, compare it with this table.

## 2. Building the lead list

**Sources, in order of how useful they are:**
1. **Walking the clusters.** Mill Road, Regent St / Hills Rd, King St / Burleigh St, the city centre lanes, Chesterton Rd / Mitcham's Corner, Histon Rd / Arbury, Cherry Hinton High St, Trumpington. Then the villages: Histon & Impington, Great Shelford, Sawston, Cottenham, plus Ely and St Ives as day trips.
2. **Google Maps.** Search "café", "pub", "restaurant" and "bakery" per cluster. Note the website link, the review count and the hours.
3. **FSA food hygiene open data.** Every food business registered with Cambridge City Council and South Cambridgeshire, with name and address. It's free under the Open Government Licence.
   - `ops/outreach/fsa_leads.py` imports it into `crm.csv`.
   - Run it on your own computer, because this cloud environment blocks that site.
   - A **recent rating date** for a business that isn't in the CRM yet usually means a new opening, which is a strong trigger.
4. **New-opening signals.** Cambridge City Council licensing applications, "coming soon" signs, local food Instagram accounts and Facebook groups, and the Cambridge Independent's food coverage.
5. **Companies House.** Check whether a venue is a **limited company**. That decides whether you can cold email it (§3).

**For each lead the agent records** (columns in `crm.csv`):
- website status: none, Linktree only, PDF menu, broken on mobile, out of date, or fine;
- whether the hours on the site match Google;
- whether there's a booking link;
- the review count;
- whether it's a limited company;
- any trigger;
- the best time to visit.

## 3. Outreach rules (UK: PECR and UK GDPR)

> ⚖️ **Summary, not legal advice. Check the ICO's direct marketing guidance before any email or DM campaign.**

| Channel | Who | Rule we follow |
|---|---|---|
| **Walk-in** (main channel) | Anyone | Fine. Be polite, leave if asked, and never return if they say no. |
| **Letter or postcard** | Anyone | Not covered by PECR's electronic rules. GDPR legitimate interests apply. Include an opt-out line. |
| **Phone (live calls)** | Anyone | **Screen against the TPS** (sole traders and partnerships) **and the CTPS** (companies) before calling. Say who you are and offer to remove them. |
| **Email** | **Limited companies and LLPs only** ("corporate subscribers") | Allowed without consent. Identify yourself, give a working opt-out, and keep it relevant to their business. |
| **Email** | Sole traders and partnerships ("individual subscribers") | **Not without prior consent.** So no cold email. Use walk-in, letter or phone instead. |
| **Social DMs** | Anyone | Treat these **like email**. Only send one after in-person contact, or when they've asked us to. |
| **WhatsApp or text** | Anyone | Only after they've given you their number and agreed to be contacted that way. |

- **Suppression list:** add anyone who says "no", "stop" or "not interested" to `ops/outreach/do-not-contact.csv` the same day, and check it before every touch.
- Keep a short record of the legitimate-interest basis for prospecting. It's already in the privacy policy, under "Prospective clients".
- Most independent venues are sole traders or partnerships. That's another reason **walking in is the main channel**.

## 4. Lead scoring (0–100)

Scored by `ops/outreach/score_leads.py` from the CRM columns:

| Factor | Points |
|---|---|
| **Website problem:** none or Linktree-only = 30 · PDF or image menu = 25 · broken on mobile = 25 · clearly out of date = 20 · fine = 0 | up to 30 |
| **Hours on the site don't match Google** | 10 |
| **No booking or enquiry route online** (if they take bookings) | 5 |
| **Independent** (not a chain or franchise) | 10. **Chains score 0 overall.** |
| **Busy:** review count of 150+ = 10 · 50–149 = 6 · under 50 = 2 | up to 10 |
| **Does events or private hire** (Plus upsell) | 10 |
| **Trigger:** new opening, new owner, refurb, hiring, or a bad review mentioning wrong info | 15 |
| **Reachable:** in an active cluster, with a known quiet time | 10 |

**A = 65+** (visit this week) · **B = 40–64** (this month) · **C = under 40** (nurture, or don't bother)

## 5. Lead magnet: free health check plus free homepage mockup

**What it is:**
1. The **Website Health Check** (`ops/outreach/health-check-template.md`): one printed page, left at the venue on the walk-in.
2. The **homepage mockup**: a real, clickable preview of their homepage on our template, using their name, menu and photos. It's offered in the conversation and sent within 2 working days.

**Making a mockup quickly** (🤖 about 30 minutes, 👤 5 minutes):
1. Run `ops/delivery/scripts/new-client.sh mockup-<slug> ../mockups/<slug>`.
2. Fill in `venue.json` from public information: Google listing, Instagram and their current site. Use **their hours, their menu (from a photo of the menu or their current site), and their colours**. Only use their photos from their public profiles for this private preview, and say so.
3. Deploy to a Cloudflare Pages preview. Because it's private, also set `"demo": true` so it carries the banner, and add `noindex`.
4. 👤 Check it on your phone, then send it by the channel they agreed (template in `scripts.md`, touch 2).
5. If they say no, **delete the preview within 30 days**, along with their content.

## 6. Content: 30-day short-form plan

**Platforms:** TikTok, Instagram Reels and YouTube Shorts. Film once and post on all three.

**Goal:**
- *Proof and familiarity*, so that when you walk in, an owner has maybe seen your face before.
- This is not the main lead source in the first 90 days. Treat followers as a bonus.

**Formats:**
- **Before → after redesigns:** use demo venues, or real clients with written permission.
- **Build timelapses:** screen-recording the menu going from a photo to a live page.
- **Website teardowns, done kindly:** use made-up or anonymised examples, or venues that have asked for one. **Never mock a real local business.** Cambridge is small and owners talk.
- **Behind the bar:** your hospitality stories, which tie the brand to you.
- **Quick tips for owners:** "3 things Google needs from your website".

The full 30-day calendar, with hooks, is in [`ops/outreach/content-calendar.csv`](../ops/outreach/content-calendar.csv). Post once a day if you can, and at least 4 times a week. Batch-film on Mondays.

## 7. Referrals & partnerships

**Client referrals:**
- **"Buy a round":** when a venue you referred signs up and pays its first month, **you both get a month free**.
- That costs £49–£79 per new client: well under any ad cost, and they stay longer.
- Ask at the moments clients are happiest: launch day, after a fast edit, and in the month-3 report.

**Partners** (people who already talk to venue owners every week):

| Partner | Why | What we offer |
|---|---|---|
| Brewery and drinks reps, coffee roasters, wholesalers | They visit venues weekly and know who's opening | £50 per signed client (disclosed to the client) |
| Hospitality accountants and bookkeepers | Trusted advisers to owners | £50 per signed client, plus a free site for their own practice in exchange for a referral page |
| Local photographers | Venues need photos *and* a site to put them on | Mutual referrals: we recommend them in our photography add-on |
| Sign makers and printers (menus, A-boards) | Menus change at the same time as websites | Mutual referrals; QR table cards |
| Booking and POS system reps | Their customers need somewhere to put the widget | Mutual referrals |
| Cambridge BID, trader associations (Mill Road etc.), Cambridgeshire Chamber | Owner networks and events | Free "website clinic" talk; a members' offer of a free health check |

Partner fees and anything they're paid must be **told to the client**. Keep a partner tab in `crm.csv` using `source=partner:<name>`.

## 8. Sales call, objections, close & payment

See [`ops/outreach/sales-call.md`](../ops/outreach/sales-call.md). In short:
- **The call:** about 15 minutes. They do most of the talking, about 80%.
- **Showing them:** their own mockup on your phone, not slides.
- **Closing:** one clear ask.
- **Payment:** the Stripe link with a 14-day trial, so nothing is charged until the site is live.

## 9. Running Tab's own Google Business Profile & local SEO

1. **Create the profile** as a **service-area business**: hide your home address and set the service area to Cambridge plus nearby villages.
   - Primary category: **Website designer**. Secondary: **Internet marketing service**. Check what categories Google currently offers.
2. **Fill in everything:**
   - the description, using the same words as the homepage;
   - services with prices (Core £49 and so on);
   - hours, and the website link;
   - photos: your face, the demo sites on a phone, and you at a venue, with permission.
3. **Get reviews from founding venues.** It's part of their deal. Send the review link in the launch message and again at day 25.
   - **Never** offer anything in return for a *positive* review.
   - Don't write reviews yourself, or ask friends who aren't clients.
4. **Post weekly:** a new client launch, a seasonal tip for owners, or a before/after.
5. **List the business consistently** with the same name, area and URL everywhere: Bing Places, Apple Business Connect, Yell, and local directories. (A business listing on any of these is called a "citation".)
6. **On the site:**
   - add a "Websites for Cambridge pubs" page and a "…cafés" page only once you have real examples to show;
   - write a short case study for each launch;
   - avoid thin "web design Mill Road" pages that exist only to target a search term, which Google penalises;
   - submit the sitemap in Search Console.
7. **Footer link on every client site:** "Website by Running Tab". Clients can ask to remove it. These links are a steady local SEO signal.

## 10. Decisions taken by default (from Phase 5) — change any you disagree with

- **Edit requests by WhatsApp** as the main channel, with email as a backup.
- **Routine hours and closure changes go live without founder approval** after a client's first 2 weeks. Menus, prices and allergen information always get founder approval.
- **The multi-page template (v2) gets built after the founding venues**, during the quiet week of 28 Dec.
