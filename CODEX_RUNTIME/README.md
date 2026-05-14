# Codex Runtime

This folder explains how to use Codex with AppForge and separate implementation repos.

## Default artifact format policy

Codex should generate AppForge artifacts using templates by default.

Precedence:

1. `project-control` template override (if present and relevant).
2. `appforge-engine/TEMPLATES/` matching template.
3. Freeform output only when explicitly requested by the user.

When generating docs outside `project-control`, default to typed docs folders:
`docs/product`, `requirements`, `ux_ui`, `api_backend`, `architecture`, `delivery`, `qa`, `operations`, `governance`, `assets_imports`.
