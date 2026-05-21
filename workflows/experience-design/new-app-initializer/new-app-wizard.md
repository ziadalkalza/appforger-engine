# New App Wizard

Ask only the critical setup questions needed to generate the correct workspace and active rules. Non-critical questions can remain `unknown_pending` until they block a workflow.

## Required workspace questions

1. Project name.
2. New project or existing/running project?
3. Single-user or team mode?
4. App type: web, mobile, both/multi-platform, backend-only, or unknown?
5. If mobile: generic/cross-platform mobile, native iOS, native Android, or separate native iOS + Android?
6. Backend: needed, not needed/backendless, existing backend, or not sure?
7. Starting point: scratch, existing code, existing design, existing docs, or mixed?
8. Design workflow: Figma first, HTML sandbox first, existing design/frontend, references, no UI yet, or not sure?
9. Preferred brand-family policy before choosing providers.
10. Preferred code/planning/design providers if known.
11. Docs storage location.
12. Context backend mode, if any.
13. Automation level.

## Output

- Generated workspace folders based on app type and mobile/backend answers.
- Filled `APPFORGER_PROJECT_STATUS.md`.
- Initial `APPFORGER_PROJECT.yaml`.
- Onboarding answers and active rules.
- Next-stage checklist.
