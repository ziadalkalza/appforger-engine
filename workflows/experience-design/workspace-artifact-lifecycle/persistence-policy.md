# Persistence Policy

## Persist by default

- Approved decisions.
- Approved baselines.
- Registries.
- API contracts.
- Codex work packets.
- Done reports.
- Change requests.
- Test/QA reports that affect release readiness.
- Production source code.
- Approved design assets.

## Temporary by default

- Draft prompts.
- Failed image generations.
- Raw debug logs.
- Intermediate scratch JSON.
- Exploratory notes not accepted into a decision.
- Unapproved Figma exports.

## Promotion rule

Temporary content becomes persistent only after one of these events:

1. User approval.
2. Stage gate approval.
3. Accepted PR/commit.
4. Baseline creation.
5. Change request acceptance.
6. validation/domains/qa/release evidence requirement.
