# Example Job: Context Reindex

```yaml
job_id: JOB-CONTEXT-REINDEX-001
name: Reindex project-control context
job_type: context_sync
trigger: manual | local_git_hook | github_action
risk_level: low
requires_approval: false
inputs:
  - project-control/
allowed_outputs:
  - project-control/context-backend/index-reports/
  - project-control/REGISTRIES/CONTEXT_SYNC_REGISTRY.md
forbidden_actions:
  - read .env files
  - index local-only/debug
  - approve baselines
failure_behavior: retry_once_then_report
```
