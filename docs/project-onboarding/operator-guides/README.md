# How to Use Appforger

This folder is the operator-facing documentation set for using Appforger. It is different from `docs/generated-app/app-usage-templates/`, which contains templates for documentation that may be generated for the app being built.

Start here:

1. Read `SETUP_AND_FIRST_RUN.md`.
2. Read `FEATURES_AND_ACTIVITIES.md` for the full feature/activity index.
3. Use `ACTIVITY_INDEX.md` to find the correct guide for a task.
4. Use `COMMANDS_CHEATSHEET.md` for common commands.
5. Use `TROUBLESHOOTING_AND_VALIDATION.md` when something fails or when validating a package/workspace.

## Documentation map

- `SETUP_AND_FIRST_RUN.md` — how to set up Appforger in a new or existing workspace.
- `FEATURES_AND_ACTIVITIES.md` — complete overview of features and activities.
- `ACTIVITY_INDEX.md` — task-to-guide index.
- `COMMANDS_CHEATSHEET.md` — common commands and what they do.
- `TROUBLESHOOTING_AND_VALIDATION.md` — validation, smoke tests, and troubleshooting.
- `FEATURE_GUIDES/` — focused guides for major feature areas.

## Key boundaries

- `appforger-engine/` is the reusable engine.
- `project-control/` is generated project state and registries.
- `docs/` stores project documents when the user chooses local docs storage.
- `local-only/` stores private local config and must not be committed.
- Code lives in app repos/folders or registered remote repos.
- RAG, graph, and SQL storage are derived/operational systems, not replacements for source truth.


## Integration Strategy Advisor

Before adding an integration, Appforger can compare official connectors/plugins/MCPs, existing Appforger integrations, direct APIs, custom Python, and hybrid approaches. See `mcp/docs/feature-guides/integration-strategy-advisor.md`.
