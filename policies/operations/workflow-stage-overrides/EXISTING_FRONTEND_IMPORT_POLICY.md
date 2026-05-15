# Existing Frontend Import Policy

An existing frontend may be imported as a starting point.

Required steps:
1. identify repo/path/source;
2. inspect routes/screens/components if tooling allows;
3. create frontend inventory;
4. map screens to product goals/user stories;
5. compare with desired app scope;
6. detect backend/API/data needs;
7. create gap analysis;
8. record imported frontend baseline as pending_review;
9. approve, refactor, or replace.

Imported frontend does not bypass testing, documentation, package review, security, or release readiness.

## Code Context Sources update

Existing frontend/mobile import must register the source as a Code Context Source when code or code-derived context is available.

Required additions:
1. record whether the frontend/mobile source is canonical;
2. record local/remote/snapshot/CI-generated/summary-only fetch mode;
3. validate role access and credential references;
4. run initial code context bootstrap for ongoing projects;
5. generate frontend maps: routes/screens, components, state management, API clients, theme/design system, navigation flow, dependencies, risky files;
6. mark context as fresh, stale, partial, summary-only, blocked, or not_started.

Imported frontend/mobile code is not modified during bootstrap.
