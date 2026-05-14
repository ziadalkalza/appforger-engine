# Approval Required Actions

Approval is required before:

- committing or pushing changes, unless project/repo policy explicitly allows it
- merging PRs
- approving baselines
- activating integrations
- adding new external packages
- changing architecture
- changing production environment configuration
- creating cloud resources
- using paid services
- deploying staging or production
- publishing web/mobile apps
- waiving release blockers

## Approval modes

- **Local approval:** user confirms in ChatGPT/Codex/local terminal and the approval is recorded in `AUTOMATION_APPROVAL_REGISTRY.md`.
- **GitHub PR approval:** reviewer approves a PR. Required for team-mode project-control changes.
- **Hybrid approval:** user approves locally, then GitHub PR records final review.
- **Future server approval:** reserved for MCP/server mode.

For auto-push, approval is per push unless project policy explicitly says otherwise.
