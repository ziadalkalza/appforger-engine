# Draft and Sandbox Mode

Draft and Sandbox Mode lets Appforger explore ideas without contaminating approved project truth, live implementation repos, or release-ready artifacts.

Use this layer when the user wants to try a visual direction, HTML prototype, Figma variation, mock API, package experiment, backend shape, or Codex code experiment before committing to the real workflow.

## Core rule

Draft output is not project truth.

Drafts may be recorded in `project-control/REGISTRIES/DRAFT_REGISTRY.md`, but raw draft files belong in `local-only/`, `exports/drafts/`, or a clearly marked draft branch until promoted.

## Default v14 behavior

- Draft records may be persisted in project-control.
- Raw draft files are local-only by default.
- HTML sandbox prototypes are allowed for mobile and web projects as exploration only.
- Codex may create draft code outside real repos or on a draft branch.
- Figma draft work is allowed but is not an approved baseline.
- Mock API sandboxes are allowed but are not official API contracts.
- Drafts should link to an epic/feature/story when known, but freeform exploration is allowed.
- Drafts have an expiry review; when due, Appforger asks whether to extend, discard, archive, review, or promote.
- Promotion requires artifact-specific review.
