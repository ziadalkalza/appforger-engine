# Memory Save Protocol

Appforger memory is file-based. ChatGPT/Codex memory is not enough.

## When to save memory

Save/update Appforger memory after:

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
APPFORGER_PROJECT_STATUS.md
DECISION_LOG.md
PENDING_QUESTIONS.md
registries/TASK_STATUS_REGISTRY.md
registries/project-control/decision-snapshots/stage-summary-template.md or a filled stage summary
```

## Design memory update

After Figma/design work, update:

```text
registries/project-control/screen-registry.md
registries/project-control/design-asset-registry.md
registries/project-control/design-baseline-registry.md
registries/project-control/baselines/design-baseline-registry.md
registries/project-control/decision-snapshots/stage-summary-template.md
```

## Backend/API memory update

After backend/API work, update:

```text
registries/project-control/api-registry.md
registries/project-control/data-model-registry.md
registries/project-control/baselines/api-baseline-registry.md
registries/project-control/baselines/backend-baseline-registry.md
```

## Frontend memory update

After native frontend work, update:

```text
registries/project-control/feature-registry.md
registries/project-control/screen-registry.md
registries/project-control/test-registry.md
registries/project-control/baselines/frontend-baseline-registry.md, if applicable
ai-models/codex/templates/code-agent-packets/codex-done-report-template.md or a filled done report
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

Do not store secrets in Appforger memory.

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
registries/project-control/decision-snapshots/project-memory-compaction.md
```
## Completion Memory Save

When saving memory after a task, record whether the update is:

- checkpoint progress,
- completion claim,
- verified completion,
- manual override,
- reopened work.

Do not summarize checkpoint commits as completed tasks.
