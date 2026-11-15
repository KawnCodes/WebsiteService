# Sales call (15 minutes), objections, closing & payment

The aim is to understand their problem and show their mockup. Then make one clear ask. Let them do most of the talking.

## 1. Opening (1 minute)
> "Thanks for making time, I know how busy it gets. I'll keep it to 15 minutes. I'd like to ask a few questions, show you your mockup, and if it's not a fit, no problem. Sound OK?"

## 2. Questions (5–6 minutes; write the answers in the CRM)
1. "Who looks after the website at the moment? When did it last change?"
2. "How do people usually find you and book?"
3. "What do customers ask you over and over?"
4. "What happens with private-hire or event enquiries right now?"
5. "Have you tried to sort the website before? What happened?"
6. "What do you pay at the moment, for the domain, the builder or whoever looks after it?"
7. "If the website was just always right, without you thinking about it, what would that be worth to you?"

**Listen for the pain in their own words.** Repeat it back later: "You said the Christmas menu still isn't online…"

## 3. Show them (3–4 minutes)
- Open **their** mockup on your phone and hand it to them. Let them scroll.
- Point out 3 things that are tied to what they told you: the menu as a real page, the live "Open now" badge, and the booking or private-hire button.
- Then: "And when the menu changes, you just WhatsApp me a photo, and it's live {same day/within a day}."

## 4. Pricing (1 minute): recommend one plan
> "For you I'd suggest **{Core/Plus}**: £{price} a month, no VAT, nothing upfront. {Plus: because you do events and private hire, and your menu changes weekly.} It's a 3-month minimum, then monthly. And you don't pay a penny until you've seen the finished site and you're happy."

**Founding venues** (while there are still spots):
> "I'm taking 5 founding venues: £29 a month for six months and a free build, in exchange for an honest review and letting me share the before and after. You'd be one of them."

## 5. The close (one clear ask)
> "Shall we go for it? If you say yes today, I'll have your site ready to review by {date, about 5 working days after content}."

Then **stop talking.**

- **Yes:** go to the payment flow (§7).
- **"Let me think":** "Of course. What's the main thing you'd want to think through?" (That's usually the real objection; see below.) Then: "Shall I message you {Thursday}?"

## 6. Objections

| They say | You say |
|---|---|
| **"It's too expensive."** | "Totally fair. What do you pay now, all in? … Most venues spend more on {one keg / a staff shift} a month. And one private-hire booking or a few extra covers from Google pays for the year. There's no upfront cost, and you don't pay until you've seen it. If it's still not right, Core's the leanest option at £49." *(Don't discount Core. Offer a founding spot while one is open.)* |
| **"My nephew / a friend does websites."** | "That's great, and honestly, if they'll still be updating your menu at 4pm on a Friday in two years, stick with them. Most people come to me when that's stopped happening. The difference is I'm a fixed cost with set turnaround times, and you own everything if you leave." |
| **"I'll just use Wix / Squarespace."** | "You definitely can. It's about £10–£25 a month. The catch is you have to build it and keep it updated yourself. Would you rather spend your Sunday nights doing that, or send me a WhatsApp?" |
| **"Instagram is enough."** | "Instagram's brilliant, keep it! But when people search 'pub near me' or check your hours, Google sends them to a website, and Instagram doesn't show your menu or hours to Google properly. I link the two together." |
| **"We're too busy right now."** | "Which is exactly why you'd hand it to me. It's about 20 minutes of your time in total. Or let's pencil in the first week of January, when it's quieter, and I'll hold your founding price." |
| **"Send me some info."** | "Happy to. The mockup *is* the info: it's your actual homepage. Can I send it to your WhatsApp now and check back with you on Thursday?" |
| **"We got burned before by a web guy who vanished."** | "That's the most common story I hear. It's why your domain stays in your name, you can leave after 3 months and take the site with you free, and there's a 30-day money-back if you're not happy after launch." |
| **"I need to ask my partner / the owner."** | "Of course. Shall I send you the mockup and a one-line summary to forward? Or I'm happy to pop back when you're both in." |
| **"What if I want to leave?"** | "Give me 30 days' notice after the first 3 months. I hand over all your site files free, and help move your domain. No exit fees." |
| **"Is this AI?"** | "I use modern tools, including AI, to build fast. That's how it's £49 and not £149. But I check everything myself before it goes live, and you're dealing with me." |

## 7. Closing & payment flow

1. **A verbal yes** on the call. Then straight away send a WhatsApp or email confirming it:
   > "Brilliant, welcome aboard! Confirming: {plan}, £{price}/month, no VAT, a {3/6}-month minimum from launch. Nothing is charged until your site is live and you've approved it. Terms: runningtab.co.uk/terms. Can you reply 'confirmed'?"
2. **They reply "confirmed".** That's your written agreement. Store a screenshot in the client folder.
3. **Send the Stripe Payment Link** for their plan, with a **14-day trial**. They add their card, accept the terms, and they're charged nothing yet.
   - Or, if they'd rather, send the link only at launch.
4. **Same day:** send the welcome email and intake questionnaire (`ops/delivery/onboarding/`), and book the kickoff.
5. **Launch day:** end the trial in Stripe so billing starts. Send the "you're live" message with the billing-portal link.
6. **Update `crm.csv`:** `stage=won`, plus `plan` and `won_date`. Then add the venue to `clients.csv`.

## 8. After every call (2 minutes)
- Record a voice memo: the pain in their words, the objection, what happens next.
- 🤖 updates the CRM: `stage`, `notes`, `next_action`, `next_action_date`.
