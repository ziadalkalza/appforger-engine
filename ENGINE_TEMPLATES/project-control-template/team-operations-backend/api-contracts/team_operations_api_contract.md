# Team Operations API Contract

This file defines API shapes for implementations such as Supabase, FastAPI/Postgres, or SQLite-backed local APIs.

Suggested endpoints:
- GET /ops/tasks
- GET /ops/tasks/{id}
- POST /ops/tasks/{id}/status-change-request
- GET /ops/approvals
- POST /ops/approvals/{id}/decision
- GET /ops/handoffs
- POST /ops/handoffs/{id}/complete
- GET /ops/conflicts
- POST /ops/conflicts/{id}/resolution
- GET /ops/agent-runs
- GET /ops/job-runs
- GET /ops/release-blockers
- GET /ops/audit-events

Write endpoints must create audit events and, where canonical project-control changes are needed, generate a sync packet/PR rather than silently modifying canonical files.
