# Start Here for Agents

This file exists before workspace setup. Codex, Claude Code, Cursor, Copilot agents, and other coding assistants should read this file when the user asks to set up AppForger.

## First setup rule

Do not guess the workspace layout. Inspect the current folder, then run the setup wrapper.

If the user selected a provider, generate only that provider's adapter:
- Codex/OpenAI: `--agent-adapters codex`
- Claude Code: `--agent-adapters claude`
- Cursor: `--agent-adapters cursor`
- Copilot: `--agent-adapters copilot`

If provider is unclear, ask which adapter to generate. Do not generate all adapters by default.

## Command

```bash
python appforge-engine/NEW_APP_INITIALIZER/setup_appforge_project.py --target . --name "<project name>"
```

## After setup

Point the user to:
- `local-only/.env.local`
- `project-control/`
- selected adapter file, such as `AGENTS.md` or `CLAUDE.md`
- onboarding and source pipeline next steps
