# Source of Truth Policy

`project-control/` remains canonical for decisions, baselines, registries, packet records, approvals, and durable project memory.

The Team Operations Backend is a queryable operational mirror/control layer. When it disagrees with project-control, Appforger must flag a sync conflict and reconcile before using the backend state as current.

Default conflict resolution order:
1. Project-control approved files.
2. Approved GitHub PR/commit references.
3. Operations backend state if backed by a valid sync record.
4. Draft/unreviewed backend state.
