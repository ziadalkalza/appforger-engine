# Team Operations Backend Overview

This layer adds a future-ready operational state backend for team workflows, automation, and sub-agent orchestration.

It stores live state such as task status, approval queues, blocker status, handoff status, conflict status, agent run status, automation job run status, current stage state, and secret metadata. It stores source links to canonical files rather than copying those files.

Recommended profiles:
- Supabase: easiest hosted option.
- FastAPI + Postgres: custom backend option.
- SQLite: supported local or hosted lightweight option, suitable for small teams, prototypes, and local/offline operation.
