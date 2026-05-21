# External Content Validation

Before Appforger starts a stage that depends on external folders or services, it must validate that the external content exists and follows Appforger rules.

Validate:

- `project-control/` exists and contains required state files.
- selected implementation repos exist locally.
- selected implementation repos contain `AGENTS.md` and `APPFORGER_POINTER.md`.
- selected implementation repos are Git repos when persistence is required.
- `design-assets/`, `exports/`, and `local-only/` exist.
- Figma links are registered before design baseline approval.
- GitHub remote URLs are registered before team/collaboration workflows.
- backend environment placeholders exist before backend work starts.
- Codex work packets point to valid target repos.

External validation must run during:

1. New app initialization.
2. Stage start.
3. Before Codex work packet execution.
4. Before approving a baseline.
5. Before committing or recording done reports.
