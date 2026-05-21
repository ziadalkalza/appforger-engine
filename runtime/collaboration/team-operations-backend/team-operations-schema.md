# Team Operations Schema

Core entities:
- team_members
- role_assignments
- operational_tasks
- approvals
- handoffs
- conflicts
- reviews
- release_blockers
- agent_runs
- job_runs
- workflow_stage_state
- secret_metadata
- audit_events
- sync_events

Each row should include source metadata whenever it represents or mirrors a project-control artifact: `source_path`, `source_registry`, `source_commit`, `approval_status`, `last_synced_at`, and `is_current`.
