# Skill: Create Third-Party Integration Pack

## Purpose

Create a reusable AppForge integration pack for a third-party service before it is used in app code.

## Inputs

- requested integration name,
- intended use case,
- target project tracks: backend, web, iOS, Android, design, QA,
- user constraints,
- official documentation links or browsing permission,
- current project stack.

## Required context

Read:

- `INTEGRATIONS/INTEGRATION_PACK_SCHEMA.md`
- `INTEGRATIONS/INTEGRATION_RESEARCH_PROTOCOL.md`
- `INTEGRATIONS/INTEGRATION_TYPE_CLASSIFIER.md`
- `INTEGRATIONS/INTEGRATION_CLARIFICATION_QUESTIONS.md`
- `PLAN_MODE_AND_UNCERTAINTY/PLAN_MODE_POLICY.md`
- `CONNECTOR_MCP_SKILL_LIFECYCLE/LIFECYCLE_STATUS_MODEL.md`

## Steps

1. Enter plan mode.
2. Check whether the integration already exists in `REGISTRIES/INTEGRATION_PACK_REGISTRY.md`.
3. Classify integration type.
4. Ask required clarification questions.
5. Research official docs if current setup/security/API/pricing matters.
6. If official docs cannot be checked, create draft-only unverified pack and do not activate it.
7. Copy/fill `INTEGRATIONS/INTEGRATION_PACK_TEMPLATE/` into an approved integration folder or staging area.
8. Record assumptions, unknowns, docs, user answers, setup steps, secrets, tests, risks, and execution packet guidance.
9. Update lifecycle registries as `generated` or `reviewed`.
10. Ask user approval before activation.
11. After approval, update connector/dependency/environment registries and mark active for the project.

## Forbidden

- Do not create production code in app repos during this skill.
- Do not activate a high-risk integration without explicit approval.
- Do not place secrets in AppForge files.
- Do not rely on memory alone for production setup/security rules.

## Output

- integration pack files,
- registry updates,
- approval request,
- implementation readiness summary.
