# Context Backend Enablement Policy

Context backend is optional and disabled by default.

Enable only after:

- User approves the backend profile: Qdrant, Supabase, or Hybrid
- Indexing scope is approved
- Cost/security review is completed
- Secrets policy is confirmed
- Exclusion rules are active
- Validation script passes

Supported sync modes:

- Manual command
- Codex-run sync task
- Local Git hook
- Optional GitHub Action
- Future MCP/server sync
