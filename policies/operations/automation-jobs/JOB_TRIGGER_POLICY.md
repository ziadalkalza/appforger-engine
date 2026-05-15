# Job Trigger Policy

Supported triggers:

- `manual`: user runs command or asks AppForge/Codex to run job.
- `codex_requested`: Codex runs job as part of an approved packet.
- `local_git_hook`: local post-commit/post-merge/pre-push hook.
- `github_action`: triggered by push/PR/tag/workflow dispatch.
- `scheduled`: GitHub cron or future scheduler.
- `future_mcp_server`: reserved for server-backed AppForge.

Every trigger must record a job run. Local hooks are only active on machines where the user installs them.
