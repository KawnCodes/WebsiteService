# Client website (built and run by Running Tab)

This repo is one venue's website. Almost everything lives in **`venue.json`**: menu, hours, notices, events, colours and contact details.

- Run it locally: `npm install && npm run dev`
- Build it: `npm run build` (the output goes in `dist/`)
- Hosting: Cloudflare Pages (root `/`, build `npm run build`, output `dist`)
- To make an edit: open an issue using the **Edit request** template, change `venue.json` on a branch, check the preview URL, merge.

Template version: copied from `WebsiteService/site/src/templates/venue/VenueSite.astro` when this site was created. To pick up template improvements, copy the newer file over and check the preview.

If the client leaves, this repo, `venue.json` and the `dist/` folder are what they take with them, for free.
