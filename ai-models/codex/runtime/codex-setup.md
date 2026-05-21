# Codex Setup

## In Appforger repo

Use Codex to edit:
- Markdown engine files
- project state
- registries
- packets
- skills
- templates

Do not use the Appforger repo for production app code.

## In implementation repos

Each implementation repo must contain:
- `AGENTS.md`
- `APPFORGER_POINTER.md`
- normal source code
- normal test/build tools

Codex should read the repo `AGENTS.md`, the Appforger pointer, and the current implementation packet before editing code.
