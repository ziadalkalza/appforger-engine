# API Contract Rules

## Purpose

API contracts protect native frontends from backend ambiguity.

## Required sections

- Version.
- Base URL/environment.
- Auth/session model.
- Endpoints/functions.
- Request schemas.
- Response schemas.
- Error codes.
- Pagination.
- Upload/download behavior.
- Loading/empty/error state mapping.
- Mock data.
- Breaking-change policy.

## Approval

Do not start native frontend implementation against real backend unless API contract is approved or the frontend task explicitly uses approved mock data.

## Change after approval

Open an API change request.

Classify:

- non-breaking
- breaking
- backend-only
- frontend-impacting
- data-model-impacting
