# Deployment Rules

## Generic rule

Deployment target selection belongs to the selected backend stack or app profile.

Generic backend work should record:

- runtime environment;
- hosting target;
- secrets placement;
- migration strategy;
- rollback expectations;
- validation/smoke-test commands.

## Unsupported deployment

Targets without an active stack/app profile require an engine upgrade or an explicit draft-only plan before production use.

## Production guardrails

- No secrets in Markdown.
- No production destructive migrations without approval.
- Backups must be documented.
- Environment variables must be documented but not exposed.
