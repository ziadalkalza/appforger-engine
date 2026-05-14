# Agent Conflict Resolution

Agent conflicts must not be resolved silently.

Common conflicts:
- two agents edit the same file/path
- two agents change the same baseline
- one agent depends on a superseded API/design baseline
- a frontend agent expects fields the backend agent did not implement
- QA detects a blocker while release work continues

Resolution options:
- pause one or more agents
- reissue packets with updated baselines
- continue with mock/draft mode
- freeze a baseline
- open a change request
- reconcile outputs
- cancel/supersede a packet

All conflicts are recorded in `AGENT_CONFLICT_REGISTRY.md`.
