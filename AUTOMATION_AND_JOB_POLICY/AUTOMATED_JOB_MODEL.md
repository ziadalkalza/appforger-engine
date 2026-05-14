# Automated Job Model

A job definition says what is allowed. A job run record says what happened.

Minimum job fields:

```yaml
job_id: JOB-EXAMPLE-001
name: Example job
job_type: validation | context_sync | codex_execution | test | release_check | trello_export | figma_import
trigger: manual | local_git_hook | github_action | codex_requested | scheduled | future_mcp_server
risk_level: low | medium | high | critical
requires_approval: false
owner_role: AppForge Operator
inputs: []
allowed_outputs: []
forbidden_actions: []
failure_behavior: write_report_and_stop
```

A job may not modify files outside `allowed_outputs` unless the user explicitly approves and a new job definition is recorded.
