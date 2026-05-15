# Codex Setup

## In AppForge repo

Use Codex to edit:
- Markdown engine files
- project state
- registries
- packets
- skills
- templates

Do not use the AppForge repo for production app code.

## In implementation repos

Each implementation repo must contain:
- `AGENTS.md`
- `APPFORGE_POINTER.md`
- normal source code
- normal test/build tools

Codex should read the repo `AGENTS.md`, the AppForge pointer, and the current implementation packet before editing code.
