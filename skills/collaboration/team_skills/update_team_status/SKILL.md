# update_team_status

## Purpose
Update team status, blockers, handoffs, and pending approvals.

## Required inputs
- Current APPFORGE_PROJECT_STATUS.md
- Relevant team registries
- Current task or artifact, if applicable

## Rules
- In team mode, approvals require named person and role.
- Do not store secret values.
- Use role context packs to reduce context.
- Update affected project-control registries after completion.

## Outputs
- Updated registry entries
- Handoff/approval/conflict/status file when relevant
- Follow-up actions and warnings
