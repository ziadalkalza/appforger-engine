# Parallel Work Plan Template

```yaml
parallel_plan_id: PWP-0001
feature: example
status: draft | active | paused | completed | cancelled
agents:
  - agent_id: AGENT-BACKEND-001
    packet: PACKET-BACKEND-001
    owns: backend API
  - agent_id: AGENT-QA-001
    packet: PACKET-QA-001
    owns: draft test cases
shared_dependencies:
  - USER_STORY_001
  - DESIGN_BASELINE_V1
fixed_baselines:
  - DESIGN_BASELINE_V1
mock_contracts:
  - MOCK_API_CONTRACT_V1
conflict_risk: low | medium | high | critical
reconciliation_required: true | false
```
