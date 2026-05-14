# Existing Backend Import Policy

An existing backend may be imported as a project input.

Required steps:
1. identify backend repo/API docs/deployment;
2. inspect API routes and data model if tooling allows;
3. create API inventory;
4. map API capabilities to user stories/screens;
5. detect missing endpoints and security risks;
6. create backend gap analysis;
7. create or update API baseline candidate;
8. approve before production frontend integration.

## Code Context Sources update

Existing backend import must register the backend as a Code Context Source when code or code-derived context is available.

Required additions:
1. record whether the backend source is canonical;
2. record local/remote/snapshot/CI-generated/summary-only fetch mode;
3. validate role access and credential references;
4. run initial code context bootstrap for ongoing projects;
5. generate backend maps: API routes, auth/security, database models, migrations, integrations, dependencies, risky files;
6. mark context as fresh, stale, partial, summary-only, blocked, or not_started.

Imported backend code is not modified during bootstrap.
