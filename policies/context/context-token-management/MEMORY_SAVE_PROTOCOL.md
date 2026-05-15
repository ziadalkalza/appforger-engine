# Memory Save Protocol

AppForge memory is file-based. ChatGPT/Codex memory is not enough.

## When to save memory

Save/update AppForge memory after:

- completing a stage
- approving a design/API/backend/frontend baseline
- importing Figma or image artifacts
- generating a Codex work packet
- finishing a Codex task
- committing or merging to GitHub
- resolving a change request
- discovering a new constraint, risk, or decision
- changing backend/API/frontend architecture

## Minimum memory update set

For most tasks, update or propose updates to:

```text
APPFORGE_PROJECT_STATUS.md
DECISION_LOG.md
PENDING_QUESTIONS.md
registries/TASK_STATUS_REGISTRY.md
registries/decision-snapshots/STAGE_SUMMARY_TEMPLATE.md or a filled stage summary
```

## Design memory update

After Figma/design work, update:

```text
registries/SCREEN_REGISTRY.md
registries/DESIGN_ASSET_REGISTRY.md
registries/DESIGN_BASELINE_REGISTRY.md
registries/baselines/DESIGN_BASELINE_REGISTRY.md
registries/decision-snapshots/STAGE_SUMMARY_TEMPLATE.md
```

## Backend/API memory update

After backend/API work, update:

```text
registries/API_REGISTRY.md
registries/DATA_MODEL_REGISTRY.md
registries/baselines/API_BASELINE_REGISTRY.md
registries/baselines/BACKEND_BASELINE_REGISTRY.md
```

## Frontend memory update

After native frontend work, update:

```text
registries/FEATURE_REGISTRY.md
registries/SCREEN_REGISTRY.md
registries/TEST_REGISTRY.md
registries/baselines/FRONTEND_BASELINE_REGISTRY.md, if applicable
templates/packets/code-agent-packets/providers/codex/CODEX_DONE_REPORT_TEMPLATE.md or a filled done report
```

## GitHub memory update

After a commit/PR/merge, record:

```text
repo name
branch
commit/PR reference
summary of changed files
tests run
registry/baseline impact
remaining issues
```

Do not store secrets in AppForge memory.

## End-of-session summary

At the end of a working session, create or update a short summary:

```text
What changed
What was approved
What remains open
What files/repos were touched
What should happen next
What context should the next session read
```

Store this in the relevant stage summary and, for large projects, compact it into:

```text
registries/decision-snapshots/PROJECT_MEMORY_COMPACTION.md
```
## Completion Memory Save

When saving memory after a task, record whether the update is:

- checkpoint progress,
- completion claim,
- verified completion,
- manual override,
- reopened work.

Do not summarize checkpoint commits as completed tasks.
