# Running Tab: agency website

This is the marketing site for Running Tab, plus the reusable venue template used for client sites and the 3 demo sites.

**Stack:** [Astro](https://astro.build) producing static HTML, plain CSS and self-hosted fonts.

**Why Astro:**
- It produces fast, plain static pages that score well on SEO and speed.
- Hosting on Cloudflare Pages is free.
- Each client site is just a JSON data file fed into one template, so an edit request is usually a one-line change the AI agent can make safely.
- No database, no CMS logins and no plugins to keep updated.

## Run it locally (one command)

You need Node.js 20 or newer.

```bash
cd site && npm install && npm run dev
```

Then open http://localhost:4321. To produce the files that get deployed (they go in `site/dist/`), run `npm run build`. To view that built version locally, run `npm run preview`.

## What's where

| Path | What it is |
|---|---|
| `src/config.ts` | Business details, plans, prices, add-ons. **Edit prices and copy here.** |
| `src/pages/` | Home, how it works, pricing, work (portfolio), FAQ, contact, terms, privacy, thanks, 404, plus `sitemap.xml` and `robots.txt` |
| `src/templates/venue/VenueSite.astro` | **The reusable client site template**: menu, live open/closed status, hours, events, private-hire form, and Google-readable data (schema.org) |
| `demos/*.json` | 3 fictional demo venues. Each is one data file. A new client = copy one and edit it. |
| `public/` | Favicon and the social share image (`og.png`) |
| `.env.example` | Every setting the site reads. Copy it to `.env`. |

## Settings (.env)

Copy `.env.example` to `.env` and fill it in.

- Every value in it ends up in the public page, so none of them are secrets.
- **Never put a Stripe secret key (`sk_...`) in this site.** It doesn't need one, because it only links to Stripe Payment Links.
- `.env` is gitignored, so it won't be committed.

| Variable | Where to get it |
|---|---|
| `PUBLIC_SITE_URL` | Your domain, e.g. `https://runningtab.co.uk` |
| `PUBLIC_STRIPE_LINK_CORE` / `_PLUS` / `_GROUP` / `_FOUNDING` | Stripe Payment Links (see below). Blank hides the "Sign up" buttons. |
| `PUBLIC_STRIPE_PORTAL_URL` | Stripe → Settings → Billing → Customer portal → "Login link" |
| `PUBLIC_FORM_ACCESS_KEY` | A free key from web3forms.com, sent to your business email. This key is designed to be public. |
| `PUBLIC_BOOKING_URL` | Your Cal.com link for 15-minute chats |
| `PUBLIC_CONTACT_EMAIL`, `PUBLIC_WHATSAPP_NUMBER` | Your details. Write the WhatsApp number as `447...`, with no + and no spaces. |
| `PUBLIC_CF_ANALYTICS_TOKEN` | Cloudflare → Analytics & Logs → Web Analytics. These analytics are cookieless, so no cookie banner is needed. Or leave this blank and turn analytics on in the Pages project settings instead. |

Also replace the placeholders in `src/config.ts` (`[Your full name]`, business address) and on the homepage (`[Your first name]`). As a sole trader you must show your name and an address.

## Stripe Payment Links (subscription mode)

1. In Stripe → Product catalogue, create one product per plan with a **recurring monthly price**: Core £49, Plus £79, Group £129. Also create Founding at £29.
   - For Founding, set the price, then after 6 months switch each customer to Core in the Stripe dashboard. This is a manual step: put a calendar reminder in.
2. Go to Payment Links → New and pick the plan's price. Then:
   - **Add a free trial** of 14 days. You only charge once the site is live and approved. If a build runs over, extend that customer's trial in the dashboard.
   - **Require customers to accept your terms of service.** Set the Terms URL (`/terms`) under Settings → Public details.
   - Collect the business name and phone number.
   - After payment, redirect to `https://yourdomain/thanks`.
3. Paste each link into `.env` and rebuild.
4. Turn on the **Customer portal** so clients can update their card or cancel. That matches the "never locked in" promise.

Check the details above against Stripe's current dashboard: option names move around.

## Deploy to Cloudflare Pages (free)

1. Push this repo to GitHub. It's already there.
2. In Cloudflare → Workers & Pages → Create → Pages → **Connect to Git**, choose `KawnCodes/WebsiteService`.
3. Build settings:
   - Framework preset: **Astro**
   - Root directory: `site`
   - Build command: `npm run build`
   - Build output directory: `dist`
4. Under **Environment variables**, add the same `PUBLIC_*` values as in your `.env`. Production builds read them from here.
5. Deploy. You'll get a `*.pages.dev` address straight away.
6. From now on, every push to the production branch redeploys automatically. Other branches get preview URLs, which are handy for showing a client a change before it goes live.

Netlify and Vercel work the same way (root `site`, build `npm run build`, output `dist`) if you'd rather use them.

## Connect your domain

1. Buy the domain at Cloudflare Registrar if it supports your extension, or at any registrar such as Porkbun or Namecheap.
2. If you bought it elsewhere, add the domain to Cloudflare as a site (free plan) and change the nameservers at your registrar to the two Cloudflare gives you. This can take up to 24 hours.
3. In the Pages project → **Custom domains**, add `runningtab.co.uk` and `www.runningtab.co.uk`. Cloudflare creates the DNS records and SSL certificate.
4. Redirect `www` to the bare domain, or the other way round: Cloudflare → Rules → Redirect Rules.
5. Email: Cloudflare → Email → **Email Routing**. Forward `hello@` to your inbox for free. To *send* from `hello@`, set up Zoho Mail free or Google Workspace and add the SPF/DKIM records they give you.
6. Submit `https://yourdomain/sitemap.xml` in Google Search Console.

## Making a client site from the template

For now, this is how a demo is made:

1. Copy `demos/larkspur.json` to `demos/<client-slug>.json`.
2. Fill in the real menu, hours, theme colours and so on.
3. Set `"demo": false`, and add their `formAccessKey` if they want enquiry forms.

Phase 5 (`ops/delivery/`) turns this into a standalone client-site repo and a 5-day launch process.

## Checks before going live

- Run `npm run build` and make sure it finishes with no errors.
- Check every page on a phone. Nothing should scroll sideways.
- Fill in every placeholder in `src/config.ts`.
- Have a solicitor review the Terms and Privacy pages; both are marked as drafts.
- Paste a page URL into Google's Rich Results Test to check the structured data.
