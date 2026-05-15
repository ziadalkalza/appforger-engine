# Skill: Select Web Stack

## Purpose
Choose the supported web stack for a project or feature.

## Required inputs
- PRODUCT_OVERVIEW.md
- APPFORGE_PROJECT_STATUS.md
- APPFORGE_PROJECT.yaml
- target platforms
- backend choice if known

## Steps
1. Determine whether this is web-only, web+backend, fullstack web, admin dashboard, or shared backend with mobile.
2. Choose Next.js + React + TypeScript, React + Vite + TypeScript, or static HTML/CSS/JS.
3. If the requested stack is unsupported, run Engine Upgrade Protocol.
4. Update `workflows/implementation/web-frontend/web_stack_selection.md` and `APPFORGE_PROJECT.yaml`.
5. Create a decision entry.

## Output
A stack decision with tradeoffs, repo mode, hosting target, and next tasks.
