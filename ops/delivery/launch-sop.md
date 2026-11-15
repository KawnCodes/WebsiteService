# Launch a client site in 5 working days

The clock starts when the client has **returned the intake questionnaire and sent their content**. If content is late, so is the launch. Tell the client that up front.

👤 = founder · 🤖 = agent

## Day 0: Signed
- [ ] 👤 The client has agreed to the plan in writing (email or WhatsApp is fine) **or** signed up through the Stripe link, which comes with a 14-day trial.
- [ ] 👤 Send the welcome email (`onboarding/welcome-email.md`) with the intake questionnaire.
- [ ] 🤖 Add a row to `ops/clients.csv` with `status=onboarding`.
- [ ] 👤 Book a 20-minute kickoff, in person at the venue if possible, to get photos and logins at the same time.

## Day 1: Kickoff and setup
- [ ] 👤 Go through `onboarding/kickoff-checklist.md` with the owner.
- [ ] 🤖 Run `ops/delivery/scripts/new-client.sh <slug>`. Create a private GitHub repo `client-<slug>` and push to it.
- [ ] 🤖 Fill in `venue.json` from the intake answers: name, type, address, phone, hours, booking link.
- [ ] 🤖 Type up the menu from their photo or PDF into `venue.json`. Mark dietary tags **only where the client has confirmed them**.
- [ ] 🤖 Choose theme colours from their logo or signage. Check the contrast: text on background must be at least 4.5:1.
- [ ] 🤖 Create a Cloudflare Pages project (root `/`, build `npm run build`, output `dist`) so they have a `*.pages.dev` preview.

## Day 2: Full draft
- [ ] 🤖 Write the About, events and private-hire text from the intake answers in the venue's own voice. Keep it short.
- [ ] 🤖 Add photos to the gallery. Compress them, and add alt text.
- [ ] 🤖 Run the QA checklist below on the preview.
- [ ] 👤 Review the preview on your phone (about 15 minutes), and fix anything that reads as "AI-ish" or generic.

## Day 3: Client review
- [ ] 👤 Send the preview link: *"Here's your site. Have a look on your phone. Reply with any changes in one message, ideally by tomorrow."*
- [ ] 🤖 Make the requested changes the same day. **Changes before launch don't count toward the monthly allowance.**

## Day 4: Domain and final checks
- [ ] 👤 **Domain.** Either:
  - they have one: get registrar access, or have them add the DNS records while you're on the phone together; or
  - they don't (Plus and Group): register it **in the client's name** and add it to Cloudflare.
- [ ] 🤖 Add the custom domain in Cloudflare Pages. Redirect `www` to the bare domain, or the other way round.
- [ ] 🤖 Set `siteUrl` in `venue.json` to the real domain and rebuild.
- [ ] 🤖 Run the QA checklist again on the real domain.
- [ ] 👤 The client approves by replying "approved" in writing, which you keep for the records.

## Day 5: Live
- [ ] 🤖 Point the domain at the site and confirm HTTPS works.
- [ ] 👤 **Google Business Profile:** make the hours, website link and menu link match the new site. (On Plus and Group you'll be a manager on the profile. On Core, sit with the owner and do it together.)
- [ ] 🤖 Add an UptimeRobot monitor for the domain, with alerts going to the founder.
- [ ] 🤖 Submit the sitemap in Google Search Console, if the client gives access.
- [ ] 👤 **Billing:** in Stripe, end the trial today so billing starts from launch. If they haven't signed up yet, send their plan's Payment Link.
- [ ] 🤖 Update `ops/clients.csv`: `status=live`, `launch_date`, `min_term_end` (launch + 3 months, or + 6 for founding venues).
- [ ] 👤 Send the "You're live" message, below.
- [ ] 👤 Put reminders in your calendar:
  - day 25: the end of the 30-day guarantee window, so check they're happy;
  - month 6 for founding venues: switch them to Core at £49.

## QA checklist (run on Day 2 and again on Day 4)
- [ ] `npm run build` finishes with no errors.
- [ ] Phone (390px wide): nothing scrolls sideways, buttons are easy to tap, and the menu is readable.
- [ ] Every link, phone number (`tel:`) and email works. The booking link opens the right system.
- [ ] Opening hours match what the client said **and** their Google Business Profile.
- [ ] The "Open now" badge is right, checked at a time when they're open.
- [ ] Prices and dietary tags match the client's menu exactly, and the allergen note is there.
- [ ] The private-hire form sends a test enquiry that reaches the **client's** inbox.
- [ ] Mobile score in PageSpeed Insights is at least 90 for Performance and Accessibility.
- [ ] Google's Rich Results Test recognises the venue: Restaurant, CafeOrCoffeeShop or BarOrPub.
- [ ] There's no "demo" banner, `"demo": false` is set, and there's no `noindex`.
- [ ] There's no placeholder text left: search the page for `[`, `CLIENT`, `example`.

## "You're live" message (WhatsApp or email)
> Hi {first name}, {venue} is live at {domain} 🎉
>
> From now on, just message me here with any changes: new menu, hours, closures, events. On your {plan} plan you get {allowance} changes a month, done {turnaround}.
>
> Your first payment of £{price} goes out today. You can manage your card or billing any time here: {portal link}.
>
> Thanks for trusting me with it. {founder first name}
