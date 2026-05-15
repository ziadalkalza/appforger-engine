# Database Rules

## General

- Database design follows product and UI data needs.
- Do not create tables before product requirements and major UX flows are clear.
- Do not use destructive migrations without approval.
- Keep data model registry updated.

## Stack/app-specific rules

Database enforcement details belong to the selected stack or app profile.

Each profile should define:

- migration approach;
- access-control model;
- server-only credential boundaries;
- seed/test data strategy;
- schema drift checks.

## Registry

Update `DATA_MODEL_REGISTRY.md` for each model/table.
