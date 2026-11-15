# Outreach toolkit

The strategy and the 90-day plan are in `docs/06-acquisition.md`.

| File | Use it for |
|---|---|
| `scripts.md` | Walk-in, phone, letter, the 4-touch follow-up, the cold email sequence (limited companies only), DMs |
| `sales-call.md` | The 15-minute call, objection handling, closing and payment |
| `health-check-template.md` | The free one-page Website Health Check you leave at a venue |
| `content-calendar.csv` | 30 days of short-form video ideas, with hooks |
| `do-not-contact.csv` | The suppression list. **Check it before every touch.** |
| `score_leads.py` | Score and tier the leads in `ops/crm.csv`, and print the A-list |
| `fsa_leads.py` | Import Cambridge food businesses from the FSA open data into the CRM. Run it on your own computer. |

The weekly routine:
1. Run `python3 ops/outreach/score_leads.py`.
2. Visit the A-list.
3. Log every touch in `ops/crm.csv`: `stage`, `last_touch_date`, `touch_count`, `next_action`, `next_action_date`.
