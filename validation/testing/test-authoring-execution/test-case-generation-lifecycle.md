# Test Case Generation Lifecycle

## Rule
Every feature gets draft test cases at feature-spec time. Tests are expanded as the project gains more detail.

## Lifecycle

1. Feature specification
   - Generate product-level tests from acceptance criteria.
   - Store draft tests in the project-control test registry.

2. UX/UI/Figma approval
   - Add UI, visual, interaction, accessibility, loading, empty, and error-state tests.
   - Link tests to design baseline version.

3. Backend/API approval
   - Add endpoint, auth, permission, validation, data-model, and contract tests.
   - Link tests to API baseline version.

4. Codex task packet creation
   - Include only task-relevant tests/checks in the packet.
   - Do not ask Codex to run the entire project test suite unless required.

5. Implementation
   - Add tests for edge cases discovered during coding.
   - Record warnings when tests are skipped.

6. Bug fixing
   - Every confirmed bug should create or update a regression test.

7. Release preparation
   - Promote critical feature tests into regression/release checklist.

## Statuses
- draft
- ready_to_automate
- automated
- manual_only
- blocked
- deprecated
- regression
- release_critical
