// @ts-check
import { defineConfig } from 'astro/config';
import { loadEnv } from 'vite';

const env = loadEnv(process.env.NODE_ENV ?? 'production', process.cwd(), '');

export default defineConfig({
  site: env.PUBLIC_SITE_URL || 'https://runningtab.co.uk',
  trailingSlash: 'ignore',
  build: { format: 'directory' },
});
