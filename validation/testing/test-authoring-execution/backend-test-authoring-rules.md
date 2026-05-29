# Backend Test Authoring Rules

Backend tests should cover:

- service/business logic
- request validation
- authentication
- authorization/roles
- database constraints
- migrations
- external service failures
- rate-limit/retry behavior where relevant
- no secret leakage
- API contract compatibility

Codex must not mark backend tasks as verified unless the required backend tests were run or an explicit manual override is recorded.
