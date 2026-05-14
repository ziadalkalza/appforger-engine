# Sub-Agent Execution Packet

```yaml
packet_id: PACKET-AGENT-0001
agent_id: AGENT-EXAMPLE-001
agent_role: Backend Agent
executor_type: provider | human | future_mcp_agent
brand_family: OpenAI | Anthropic | Google | Local | External | Mixed
recommended_providers:
  - Codex
  - Claude Code
risk_level: low | medium | high | critical
target_repo: ../backend
target_branch: feature/example
target_paths:
  - app/features/example/
allowed_actions:
  - inspect_repo
  - edit_allowed_paths
  - run_tests
forbidden_actions:
  - approve_baseline
  - edit_secrets
  - change_release_state
depends_on:
  - USER_STORY_EXAMPLE_001
  - API_BASELINE_V1
can_run_in_parallel_with:
  - PACKET-QA-0001
conflicts_with: []
requires_reconciliation: false
completion_evidence:
  - changed_files
  - test_results
  - done_report
```
