# Agent Audit Log Policy

Every sub-agent run requires an audit record.

Record:
- agent ID
- provider/human executor
- brand family
- packet ID
- start/end status
- source baselines used
- branches/paths touched
- outputs created
- tests/checks run
- conflicts detected
- handoffs created
- reconciliation records required/completed

In team mode, audit updates to project-control should go through PRs.
