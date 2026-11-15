// @ts-check
import { defineConfig } from 'astro/config';
import venue from './venue.json' with { type: 'json' };

export default defineConfig({
  site: venue.siteUrl || 'https://example.com',
  build: { format: 'directory' },
});
