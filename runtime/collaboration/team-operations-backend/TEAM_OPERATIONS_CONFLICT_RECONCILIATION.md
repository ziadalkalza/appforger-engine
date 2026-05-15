# Conflict Reconciliation

Conflicts can occur when backend state and project-control disagree.

Examples:
- backend says task is approved, project-control has no approval record
- backend says handoff complete, project-control packet is still pending
- backend says release blocker resolved, QA registry still marks blocker open

Resolution options:
1. Treat project-control as truth and overwrite backend state on next sync.
2. Generate project-control sync PR from backend state.
3. Create conflict record and require owner decision.
4. Mark accepted risk if allowed by policy.
