# Context Backend Sync Job Policy

Context sync may run through:

- manual command
- Codex-requested job
- local Git hook
- GitHub Action
- future server/MCP job

Before indexing, the job must apply exclusion rules for secrets, local-only debug files, build artifacts, and unapproved drafts.

After indexing, the job must run freshness validation and record a sync report.
