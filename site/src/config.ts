// Business settings for the agency site. Edit text here; links come from .env.
const env = import.meta.env;

export const business = {
  name: 'Running Tab',
  tagline: 'Put your website on the tab.',
  description:
    'Websites for independent cafés, pubs and restaurants in Cambridge. We build, host and look after your site for £49 a month. No upfront cost, no VAT, and menu changes go live the same day.',
  // Legal identity: a sole trader must show their own name and an address on the site.
  ownerName: '[Your full name]',
  legalLine: '[Your full name] trading as Running Tab',
  address: '[Business address for correspondence], Cambridge',
  area: 'Cambridge and nearby villages',
  email: env.PUBLIC_CONTACT_EMAIL || 'hello@runningtab.co.uk',
  whatsapp: env.PUBLIC_WHATSAPP_NUMBER || '',
  bookingUrl: env.PUBLIC_BOOKING_URL || '/contact',
  portalUrl: env.PUBLIC_STRIPE_PORTAL_URL || '',
  formAccessKey: env.PUBLIC_FORM_ACCESS_KEY || '',
  analyticsToken: env.PUBLIC_CF_ANALYTICS_TOKEN || '',
};

export type Plan = {
  id: 'core' | 'plus' | 'group';
  name: string;
  price: number;
  blurb: string;
  features: string[];
  stripeLink: string;
  featured?: boolean;
};

export const plans: Plan[] = [
  {
    id: 'core',
    name: 'Core',
    price: 49,
    blurb: 'For a single café, pub or restaurant that just needs it right.',
    features: [
      'Up to 5 pages: home, menu, about, book/contact, gallery',
      'Your menu as a proper web page, not a PDF',
      '5 change requests a month, done within 1 working day',
      'Hosting, security, backups and uptime monitoring',
      'Link or widget for your existing booking system',
      'Monthly check that your Google hours match',
    ],
    stripeLink: env.PUBLIC_STRIPE_LINK_CORE || '',
  },
  {
    id: 'plus',
    name: 'Plus',
    price: 79,
    blurb: 'For busy venues with events, private hire and changing menus.',
    features: [
      'Everything in Core, up to 10 pages',
      'Events, private hire with an enquiry form, gift vouchers',
      '15 change requests a month',
      'Same-day changes to menus, hours and closures, 7 days a week (sent before 3pm)',
      'We look after your Google Business Profile',
      'Domain included, registered in your name',
      'Monthly report: visits, enquiries and changes',
    ],
    stripeLink: env.PUBLIC_STRIPE_LINK_PLUS || '',
    featured: true,
  },
  {
    id: 'group',
    name: 'Group',
    price: 129,
    blurb: 'For owners with 2–3 venues, or very events-heavy places.',
    features: [
      'Everything in Plus, for up to 3 venues',
      'Unlimited small changes (fair use)',
      'Priority turnaround, about 4 working hours',
      'A local Google check-up for each venue every quarter',
      'A 20-minute call every quarter',
    ],
    stripeLink: env.PUBLIC_STRIPE_LINK_GROUP || '',
  },
];

export const founding = {
  price: 29,
  months: 6,
  spots: 5,
  stripeLink: env.PUBLIC_STRIPE_LINK_FOUNDING || '',
};

export const addons: [string, string][] = [
  ['Extra page', '£39'],
  ['Seasonal or campaign page (Christmas, Valentine’s, Mother’s Day)', '£39'],
  ['Extra pack of 5 change requests', '£15'],
  ['Google Business Profile setup and clean-up (included in Plus and Group)', '£49'],
  ['Connect an ordering, booking or gift-voucher widget', '£49'],
  ['QR menu and review table-card design (printing at cost)', '£25'],
  ['Copywriting, per page (menu descriptions, About page)', '£39'],
  ['Brand tidy-up (logo, colours, fonts)', '£99'],
  ['Professional email setup', '£29'],
];

export const nav = [
  { href: '/how-it-works', label: 'How it works' },
  { href: '/pricing', label: 'Pricing' },
  { href: '/portfolio', label: 'Work' },
  { href: '/faq', label: 'FAQ' },
];

export const whatsappLink = (text = 'Hi Running Tab, I’d like to chat about a website for my venue.') =>
  business.whatsapp ? `https://wa.me/${business.whatsapp}?text=${encodeURIComponent(text)}` : '';
