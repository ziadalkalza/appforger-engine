# Clean Appforge From Project Skill

Use when cleaning Appforger-created artifacts from a project.

Rules:
- Dry-run first.
- Require confirmation for destructive modes and runtime volume deletion.
- Use an explicit allowlist only.
- Do not delete generic project folders such as `docs/`, `assets/`, `exports/`, `backend/`, `web/`, `mobile/`, `ios/`, or `android/`.
- Remove `project-control/` only when it contains AppForger marker files.
- Remove generated AI adapter files only when they contain the AppForger marker.
- Remove `local-only/` only when it is empty or contains `.appforge-created`.
- If ownership is unclear, skip and report the path.
