# Team Mode Audit

Checks that team mode is safe but optional.

## Rules

- Team mode is available but inactive until team members are added.
- Single-user mode remains valid.
- Named approvers are required in team mode.
- Project-control changes should go through PRs in team mode.
- Role context packs reduce token usage and role confusion.
- Secret access is metadata-governed; Appforger must not store secret values.
- Meeting notes are stored as structured files and tracked by registry.
