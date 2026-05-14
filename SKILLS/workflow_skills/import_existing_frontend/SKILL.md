# Skill: Import Existing Frontend

Use when a frontend repo or artifact already exists.

Steps:
1. Identify source repo/path.
2. Inspect structure if available.
3. Create routes/screens/components inventory.
4. Map to product/user stories.
5. Create gap analysis.
6. Register imported artifact.
7. Create baseline candidate or refactor plan.

## Code Context Sources requirements

When importing an existing frontend/mobile codebase:

1. Register the source in `code-source-registry.yaml`.
2. Mark whether it is canonical.
3. Record fetch mode: local, remote Git, snapshot, CI-generated, or summary-only.
4. Validate role access and auth reference metadata.
5. Run initial code context bootstrap if the project is ongoing.
6. Generate route/screen, component, state, API-client, theme/design, navigation, dependency, and risky-file maps.
7. Do not modify frontend/mobile code during bootstrap.
