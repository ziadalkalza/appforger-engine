# Engine, Project-Control, and Code Separation

## Engine folder

`appforger-engine/` contains reusable rules, skills, prompts, protocols, validators, and templates.

It must not contain generated app-specific state or production app code.

## Project-control folder

`project-control/` contains the app-specific operating state:

- `APPFORGER_PROJECT_STATUS.md`
- `APPFORGER_PROJECT.yaml`
- `DECISION_LOG.md`
- `PENDING_QUESTIONS.md`
- `registries/`
- `workflows/operations/artifact-imports/`
- `registries/baselines/`
- `templates/packets/code-agent-packets/providers/codex/`
- `registries/decision-snapshots/`
- `CONTEXT_PACKS/`

## Code repos

Live code belongs only in:

- `backend/`
- `ios/`
- `android/`
- `web/`

## Rule

Appforger may reference commits, PRs, branch names, screenshots, test reports, and done reports. It must not absorb production source files into the engine.
