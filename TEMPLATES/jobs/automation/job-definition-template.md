# Job Definition Template

```yaml
job_id: JOB-000
name: ""
job_type: validation | context_sync | test | codex_execution | figma_import | trello_export | release_check
trigger: manual | codex_requested | local_git_hook | github_action | scheduled | future_mcp_server
risk_level: low | medium | high | critical
automation_level_required: 2
requires_approval: false
approval_mode: local | github_pr | hybrid | future_server
owner_role: Appforger Operator
inputs: []
allowed_outputs: []
forbidden_actions: []
preconditions: []
post_actions: []
failure_behavior: write_report_and_stop
parallel_policy:
  can_run_parallel: false
  conflicts_with: []
```
