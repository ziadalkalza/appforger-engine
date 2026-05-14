# Acceptance Criteria to Test Cases

For each acceptance criterion, AppForge should generate at least:

1. One positive-path test.
2. One negative or edge-case test where applicable.
3. One UI/behavior test if the criterion affects user interaction.
4. One backend/API test if the criterion depends on server state.
5. One security/privacy test if the criterion involves auth, permissions, payment, location, health, personal data, or secrets.

Example:

Acceptance criterion: user can log in with valid credentials.

Tests:
- TC-AUTH-001: valid login succeeds.
- TC-AUTH-002: invalid password returns error.
- TC-AUTH-003: empty fields are blocked before API call.
- TC-AUTH-004: network failure shows retry/error state.
- TC-AUTH-005: auth token is not logged or exposed.
