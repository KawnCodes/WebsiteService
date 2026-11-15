# Outreach scripts and the 4-touch follow-up

Check `do-not-contact.csv` before every touch, and read the channel rules in `docs/06-acquisition.md` §3. Keep everything short, personal and specific to the venue. If a message could be sent to any business, rewrite it.

## Walk-in (the main channel)

**When:** Tue–Thu 2:30–5pm, or Mon/Fri 3–5pm. Never during service, and never on Friday or Saturday evenings.

**Bring:** a printed health check for this venue, your phone with a demo site open, and a business card.

**Opener** (about 20 seconds):
> "Hi! Is the owner or manager around? … I'm {name}, from Running Tab. I've worked in hospitality for years and now I do websites, just for Cambridge venues. I ran a quick check on yours." *(Hand over the health check.)* "Two things stood out: {e.g. your menu's a PDF from the summer, and Google has you closed on Mondays}. Have you got 5 minutes now, or is there a better time this week?"

**If the owner isn't there:**
> "No worries. Could you pass this to them? My number's on it. When are they usually in?" *(Write the answer in the CRM under `best_time`.)*

**If they're busy:**
> "Totally get it. I'll get out of your way. Can I come back {day} around 3?"

**If they say no:**
> "No problem at all, thanks for your time. Keep that, it's free." *(Leave. Add them to `do-not-contact.csv` if they said "don't come back".)*

**If they're interested** (the 5-minute version): ask questions 1–4 from `sales-call.md`, then:
> "Can I mock up your homepage? It's free, takes me a couple of days, and you'll see exactly what you'd get. What's the best way to send it: WhatsApp or email?"
*(Getting their number or email here is your **consent** for touch 2.)*

## Phone (screen against the TPS and CTPS first)

> "Hi, is that {owner name}? I'm {name} from Running Tab, a small Cambridge business. I do websites for independent venues. Is now a bad time? … I had a look at {venue}'s site and noticed {specific issue}. I'm offering local venues a free homepage mockup, no strings attached. Would you like me to do one for you? … Great, what's the best way to send it?"
> If they say no: "No problem, I won't call again. Have a good service."

## Letter or postcard (for venues you can't catch in person)

> Hi {owner name},
> I'm {name}. I've worked in Cambridge hospitality for years, and now I build and look after websites for independent venues like {venue}.
> I noticed {specific issue}. It's a quick fix, and I'd be glad to mock up your homepage for free so you can see the difference.
> Websites from £49/month: no upfront cost, no VAT, menu changes the same day.
> Text or call {number}, or scan the code to book a 15-minute chat.
> {name}, Running Tab · runningtab.co.uk
> *Don't want to hear from me again? Text STOP to {number} and I'll take you off my list.*

## The 4-touch follow-up (after an in-person or phone conversation)

These go by the channel they agreed to. Stop as soon as they reply, or say no.

**Touch 1, Day 0: the visit or call itself.** Leave the health check behind.

**Touch 2, Day 2: the mockup**
> Hi {first name}, it's {name} from Running Tab. Great chatting {yesterday/on Tuesday}. Here's the homepage mockup for {venue}: {link}
> It's got your {winter menu / hours} on it, and the "open now" badge updates itself. Have a look on your phone and tell me what you think, honestly.

**Touch 3, Day 7: a check-in with something useful**
> Hi {first name}, quick one: I noticed Google still shows {issue}. You can fix that yourself in your Business Profile under "Edit profile > Hours". It takes 2 minutes.
> The mockup's still here if you want another look: {link}. Happy to pop in for 10 minutes at a quiet time this week if that's easier?

**Touch 4, Day 14: the friendly last message**
> Hi {first name}, I won't keep chasing. I know how busy it gets. If the timing's not right, no worries at all. If January's quieter, I'd love to get {venue} sorted then. The founding price of £29/month is open until I've filled the last {n} spots. Cheers, {name}

After touch 4, set `stage=nurture` and `next_action_date` to 60 days later. In January, one seasonal nudge is fine.

## Cold email sequence (limited companies and LLPs only, ⚖️)

Send to the venue's **business** email address. Before sending, confirm on Companies House that the business is a limited company or LLP, and that they're not on the do-not-contact list. Plain text, no tracking pixels, and no more than 20 a day.

**Email 1, Day 0:** Subject: *{venue}'s menu on Google*
> Hi {first name or "there"},
>
> I'm {name}, and I build websites for independent venues in Cambridge. I had a quick look at {venue} online and spotted {specific issue, e.g. the menu on your site is the summer one, and Google shows different Sunday hours}.
>
> I'd be happy to mock up your homepage for free, so you can see how it could look. No catch, and no obligation.
>
> Worth a look?
>
> {name}
> Running Tab, {legal line}, {address} · runningtab.co.uk
> Not interested? Reply "no thanks" and I won't email again.

**Email 2, Day 3:** Subject: *Re: {venue}'s menu on Google*
> Quick follow-up. Here's an example of what I mean, built for a (fictional) Mill Road café: {demo link}. Your version would have your menu, hours and booking link. Shall I make one?

**Email 3, Day 8:** Subject: *Christmas / spring hours at {venue}*
> One tip either way: {seasonal tip}. If you'd like the website side handled for you, it's £49/month, with no upfront cost and changes done the same day. {Booking link} for a 15-minute chat.

**Email 4, Day 15:** Subject: *Closing the loop*
> I'll stop here. I don't want to clutter your inbox. If it's ever useful, reply any time. Good luck with the season! {name}

**Every email needs:** your name and business, a postal address, and a working opt-out. Honour any opt-out the same day by adding them to `do-not-contact.csv`.

## DM (only after contact, or when they've asked)

> Hi! It's {name} from Running Tab. We chatted at {venue} on {day}. Here's that homepage mockup I promised: {link} 🙂
