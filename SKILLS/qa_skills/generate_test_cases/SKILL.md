# Generate Test Cases Skill

## Purpose
Generate or update test cases as living artifacts.

## Rules
- Generate draft tests at feature-spec time.
- Expand after Figma/design approval.
- Expand after API/backend approval.
- Add regression tests for confirmed bugs.
- Do not invent implementation details not supported by baselines.

## Steps
1. Read acceptance criteria.
2. Convert criteria into product-level tests.
3. Add UI/API/backend/frontend/security/accessibility tests based on available baselines.
4. Mark unavailable tests as draft or blocked.
5. Update the test registry.
