# Test Authoring and Execution

This layer defines how Appforger creates, evolves, writes, runs, and records tests. It complements `validation/domains/qa/` and `workflows/operations/task-completion-evidence/`.

Core rule: tests are living artifacts. Draft test cases are created when a feature spec is created, then refined after design approval, API approval, implementation discoveries, bug reports, and release preparation.

This layer does not store production test code. Test code belongs in the implementation repos:

- `backend/`
- `ios/`
- `android/`
- `web/`

Project-specific test plans, test cases, and evidence belong in `project-control/` and `exports/qa/`.
