# API Test Authoring Rules

For each API endpoint, define tests for:

- valid request
- missing/invalid auth
- invalid request body/query/path
- not found
- conflict/duplicate
- permission denied
- backend failure where relevant
- response schema matches API baseline
- no sensitive data leakage

API tests must reference the current API baseline version.
