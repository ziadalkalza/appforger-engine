# Task Routing Rules

1. Identify the user's requested outcome.
2. Read `APPFORGE_PROJECT.yaml` and `APPFORGE_PROJECT_STATUS.md`.
3. Determine current stage and required stage.
4. Select output template policy before generating artifacts:
   - If `project-control` provides a task-relevant template, use it first.
   - Else use the matching template from `appforge-engine/templates/`.
   - Only produce freeform structure when the user explicitly asks not to use templates.
5. If generating docs outside `project-control`, place them in typed folders (`docs/product` ... `docs/assets_imports`) unless the project defines a different convention.
6. If requested work is blocked by a gate, either:
   - ask for approval/missing artifact, or
   - open a change request if this is an iteration.
7. Use a skill for planning/design/registry tasks.
8. Use a Codex work packet for code-editing tasks.
9. Import results back through `workflows/operations/artifact-imports/`.
10. Update `TASK_STATUS_REGISTRY.md`.
