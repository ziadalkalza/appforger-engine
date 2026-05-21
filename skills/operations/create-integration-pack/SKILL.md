# Skill: Create Third-Party Integration Pack

## Purpose

Create a reusable Appforger integration pack for a third-party service before it is used in app code.

## Inputs

- requested integration name,
- intended use case,
- target project tracks: backend, web, iOS, Android, design, QA,
- user constraints,
- official documentation links or browsing permission,
- current project stack.

## Required context

Read:

- `integrations/integration-strategy/catalog/integration-pack-schema.md`
- `integrations/integration-strategy/catalog/integration-research-protocol.md`
- `integrations/integration-strategy/catalog/integration-type-classifier.md`
- `integrations/integration-strategy/catalog/integration-clarification-questions.md`
- `policies/governance/plan-mode-uncertainty/plan-mode-policy.md`
- `policies/provider-adapters/connector-mcp-skill-lifecycle/lifecycle-status-model.md`

## Steps

1. Enter plan mode.
2. Check whether the integration already exists in `registries/project-control/integration-pack-registry.md`.
3. Classify integration type.
4. Ask required clarification questions.
5. Research official docs if current setup/security/API/pricing matters.
6. If official docs cannot be checked, create draft-only unverified pack and do not activate it.
7. Copy/fill `integrations/catalog/pack-template/` into an approved integration folder or staging area.
8. Record assumptions, unknowns, docs, user answers, setup steps, secrets, tests, risks, and execution packet guidance.
9. Update lifecycle registries as `generated` or `reviewed`.
10. Ask user approval before activation.
11. After approval, update connector/dependency/environment registries and mark active for the project.

## Forbidden

- Do not create production code in app repos during this skill.
- Do not activate a high-risk integration without explicit approval.
- Do not place secrets in Appforger files.
- Do not rely on memory alone for production setup/security rules.

## Output

- integration pack files,
- registry updates,
- approval request,
- implementation readiness summary.
