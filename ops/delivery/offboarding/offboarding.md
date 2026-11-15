# Offboarding: when a client cancels

**Principle:** make leaving easy and friendly. Being "never locked in" is part of what we sell, ex-clients refer people, and venues sometimes come back after a sale or a refit.

## 1. Notice received (👤, same day)
- [ ] Acknowledge it warmly (template below). Confirm the **final billing date**: 30 days' notice, or the end of the minimum term if that's later. The 30-day guarantee is the exception: if they cancel within 30 days of launch, refund month 1 and they can leave straight away.
- [ ] Ask **one** question: "Can I ask what made you decide? It helps me get better." Log the answer in `ops/clients.csv` notes. **This is our churn data.**
- [ ] If the reason can be fixed (price, too many changes needed, a missed turnaround), offer **one** fix, such as moving down to Core or a month free. Don't push.

## 2. Before the final date (🤖, with 👤 approval)
- [ ] Ask where the site is going:
  - (a) they'll host the site files themselves or with a new provider,
  - (b) they're moving to another platform, or
  - (c) they're closing the venue.
- [ ] **Hand over (free, after the minimum term):**
  - [ ] A zip of the full built site (`dist/`) **and** the source repo: either transfer the GitHub repo to their account, or include a zip of it.
  - [ ] `venue.json` and all their photos in a separate folder, so they can rebuild anywhere.
  - [ ] A one-page "how to host this" note: drag `dist/` onto Netlify Drop or Cloudflare Pages, which is free.
- [ ] **Domain:**
  - [ ] If it's registered in their name with us as a delegate, remove our access and give them the registrar login details.
  - [ ] If DNS is on our Cloudflare account, help them repoint it **on the day**, or move the zone to their own Cloudflare account. Never let the site go dark before the date they've agreed.
- [ ] **Google Business Profile:** remove ourselves as Manager after updating the website link if it's changing.
- [ ] **Forms:** if the Web3Forms key is ours, switch it off after the move. If it's theirs, it's simply theirs.

## 3. On the final date (🤖)
- [ ] Cancel the subscription in Stripe so it ends at the period end, with no proration unless that was agreed.
- [ ] Delete the Cloudflare Pages project, **only after** the domain has moved, or the venue has confirmed it's closing.
- [ ] Remove the UptimeRobot monitor.
- [ ] Archive the client repo (don't delete it) for 12 months. Then delete it, in line with the privacy policy.
- [ ] Delete any form submissions or personal data we still hold for them (we're their processor).
- [ ] Update `ops/clients.csv`: `status=cancelled`, plus the reason in notes.

## 4. Afterwards (👤)
- [ ] One week later: "Hope the move went smoothly, anything you need?" Then put a reminder in for **6 months** to check in.
- [ ] If they were happy and are only closing or selling: ask for a Google review and whether they know other owners who might want a site.

## Template: notice received
> Hi {first name}, thanks for letting me know. Sorry to see you go, but no problem at all.
>
> Your last payment will be on {date} and the site stays live until {final date}. Before then I'll send you everything you need to keep it: the full site files, your photos and menu, and your domain details. It's all yours.
>
> Can I ask what made you decide? Totally fine if you'd rather not say. It just helps me improve.
>
> {founder first name}
