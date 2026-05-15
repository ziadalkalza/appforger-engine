# Web Stack Selection

Use this file before any web implementation work begins.

## Default decision order

1. Does the project need SEO, routing, server rendering, auth middleware, or production web app behavior? Prefer Next.js + React + TypeScript.
2. Is it a lightweight SPA/admin tool with separate backend APIs? Prefer React + Vite + TypeScript.
3. Is it static content only? Use static HTML/CSS/JS.
4. Is another framework requested? Run `ENGINE_UPGRADE_PROTOCOL.md` before using it.

## Required output

- Selected web stack
- Repo mode: `web-only`, `web-plus-backend`, `fullstack-web`, or `shared-backend-web-mobile`
- Hosting target
- Auth/session strategy
- Styling/token strategy
- Test strategy
- Reasoning and tradeoffs
