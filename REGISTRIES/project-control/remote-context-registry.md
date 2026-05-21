# Remote Context Registry

Track context fetched or imported from remote repos, Figma, Supabase/Postgres, PRs, branches, uploads, or external devices.

## Entry template

```yaml
context_id: REMOTE-CONTEXT-001
source_system: github | figma | supabase | postgres | uploaded_file | manual_summary
source_repo_or_file:
source_ref:
branch_or_commit:
retrieved_at:
retrieved_by:
used_for_task:
related_feature:
related_baseline:
status: candidate | approved | superseded | rejected
staleness_risk: low | medium | high
summary:
```
