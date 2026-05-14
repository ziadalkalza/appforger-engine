# Auth Decision Rules

Auth is required only if the app requires accounts, protected data, roles, payments, personalization, or ownership.

## Auth decision must happen early

Before backend implementation, decide:

- Does the app need user accounts?
- Are guest users allowed?
- What roles exist?
- What data is private?
- What permissions are needed?
- What auth providers are needed?

## Options

- No auth.
- Supabase auth.
- Custom JWT auth through FastAPI.
- Third-party auth provider through engine upgrade if unsupported.

## Approval

Auth/security design requires approval before implementation.
