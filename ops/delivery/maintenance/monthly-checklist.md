# Monthly maintenance checklist

Do this in the first week of each month for every live client. The agent runs it and the founder skims the summary, about 10 minutes in total for all clients.

## For every client (🤖)
- [ ] **Uptime:** check UptimeRobot for any downtime last month. Note the uptime percentage for the report.
- [ ] **Build and dependencies:** run `npm outdated` in the client repo, and apply minor or patch updates for Astro and fonts on a branch. If the build passes and the preview looks right, merge. Leave major version upgrades for a quarterly batch (👤 approves).
- [ ] **Template sync:** if `site/src/templates/venue/VenueSite.astro` has changed, copy it into the client repo on a branch, check the preview, and merge.
- [ ] **Backups:** each client's repo is its backup, so check that the last push went through. Download a fresh `dist/` zip from Cloudflare (or run a local build) and store it in the client's folder in your backup drive.
- [ ] **Speed and accessibility:** run PageSpeed Insights on mobile. Fix anything below 90, usually an oversized photo.
- [ ] **Links:** click every phone, email, booking and map link. Booking systems change their URLs.
- [ ] **Hours:** compare the site with Google Business Profile, and fix whichever is wrong (ask the client if unsure).
- [ ] **Out-of-date content:** check for past events, expired notice banners and last season's menu still showing. Ask the client: "Should I take down X?"
- [ ] **Domain and SSL:** check the expiry date of the domain if we manage it (Plus and Group) and renew it at least 30 days before. SSL renews automatically on Cloudflare, so just confirm the padlock.
- [ ] **Small SEO improvement (Plus and Group):** one small thing a month, such as a better page description, a new FAQ answer from questions they often get, a seasonal line ("Now taking Christmas bookings"), or alt text on new photos.
- [ ] **Google Business Profile (Plus and Group):** one post a month (a special, an event or the season), plus any holiday hours coming up in the next 6 weeks.
- [ ] **Allowance report:** run `python3 ops/delivery/scripts/allowance.py <last month>` and apply any £10 credits in Stripe.
- [ ] **Billing:** look for failed payments in Stripe and follow the non-payment steps in `docs/02-offer.md` §3.
- [ ] **Report:** draft each client's monthly report from `report-template.md`.

## Seasonal reminders (send the client a nudge 4–6 weeks ahead)
| When | Nudge |
|---|---|
| Early Oct | Christmas menu, party bookings and holiday hours |
| Early Jan | January hours, Dry January drinks, Valentine's |
| Late Feb | Mother's Day (UK), Easter hours |
| Late Apr | Summer terrace and garden, bank holidays |
| Late Jul | Back-to-school and term-time hours (very relevant in Cambridge) |

## Every quarter (👤 + 🤖)
- Group clients: a 20-minute call.
- Everyone else: one personal "how's it going?" message, sent by the founder.
- Apply major dependency upgrades in a batch, then check every client's preview.
- Review the template backlog in `ops/delivery/README.md`.
