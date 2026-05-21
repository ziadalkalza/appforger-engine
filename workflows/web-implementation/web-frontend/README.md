# Web Frontend Track

The Web Frontend Track is optional. Activate it only when the project includes a browser-based app, admin dashboard, SaaS portal, marketing site, or fullstack web app.

Appforger still keeps the same engine boundary: production web code belongs in a sibling repo such as `web/` or `web-app/`, not inside the Appforger engine folder.

## Supported default stack profiles

- Next.js + React + TypeScript for full web apps, SaaS apps, dashboards, authenticated portals, and production-grade web products.
- React + Vite + TypeScript for lighter SPAs, prototypes, dashboards, and embedded web apps.
- Static HTML/CSS/JS only for very small static sites or temporary demos.

Any unsupported stack, such as Angular, Astro, Remix, Rails, Laravel, Django templates, Nuxt, SvelteKit, or custom enterprise frameworks, requires the Engine Upgrade Protocol before use.
