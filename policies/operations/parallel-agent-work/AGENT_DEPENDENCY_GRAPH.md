# Agent Dependency Graph

Every parallel plan must include dependencies.

Dependency types:
- hard dependency: agent cannot start until resolved
- soft dependency: agent can start in draft/mock mode
- output dependency: downstream agent waits for done report or baseline approval
- conflict dependency: agents can run only if paths/branches do not overlap

Example:
- iOS Login Agent depends softly on `MOCK_API_CONTRACT_V1`.
- Real API integration depends hard on `API_BASELINE_V1` approval.
- QA Agent can create draft tests from user stories before implementation is complete.
