# Role Permissions

Permissions are project-control governance rules. They do not automatically grant access in GitHub/Figma/Supabase/Trello.

## Product Owner
Can approve product scope, epics, user stories, acceptance criteria, release scope, and high-risk overrides.

## UI/UX Designer
Can approve candidate visual baselines, design tokens, assets, and Figma handoff packets.

## Backend Developer / Lead
Can propose and approve backend implementation readiness, API contracts, data model changes, migrations, and backend handoff packets.

## Frontend/Mobile/Web Developer
Can implement approved packets and propose frontend readiness, but cannot approve design/API changes alone.

## QA Tester
Can approve test evidence, bug verification, and QA release readiness.

## Release Manager
Can coordinate release candidates, store/web publishing readiness, rollout plans, hotfixes, and rollback records.

## Admin/DevOps
Can configure infrastructure, production environments, and secrets when authorized.

## Code source access defaults

For Code Context Sources:

- Admin/DevOps can configure code sources, repo access metadata, indexing, sync, and approvals when authorized.
- Backend developers can write authorized backend code sources.
- Frontend/mobile developers can write authorized web/mobile/iOS/Android frontend sources.
- Product, design, QA, and other roles are read-only by default.
- Read-only may mean metadata-only, summaries-only, maps-only, or raw files if explicitly allowed.

If a role lacks required access, Appforger must generate an access request or blocked execution packet instead of guessing.
