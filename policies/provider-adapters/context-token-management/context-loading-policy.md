# Context Loading Policy

Appforger uses progressive context loading.

## Session start

For ordinary continuation work, load:

```text
AGENTS.md
APPFORGER_PROJECT_STATUS.md
APPFORGER_PROJECT.yaml
DECISION_LOG.md
PENDING_QUESTIONS.md
registries/project-control/decision-snapshots/project-memory-compaction.md
```

Do not load all folders.

## Stage start

When starting a stage, additionally load:

```text
workflows/operations/stage-contracts/<stage>_CONTRACT.md
workflows/experience-design/task-runner/task-routing-rules.md
relevant SKILL.md
relevant registry files only
```

## Task start

When starting a specific task, additionally load:

```text
templates/packets/code-agent-packets/providers/codex/<task>.md, if development work
templates/packets/artifact-packets/<packet>.md, if handoff/import work
registries/baselines/<current baseline>.md, if implementation depends on approved work
```

## Codex task start

Codex should not receive the whole engine. Provide:

```text
repo AGENTS.md
APPFORGER_POINTER.md
one Codex work packet
active baseline or contract needed for the task
relevant source files in the target repo
```

## Figma import start

For importing Figma work, load:

```text
integrations/design/figma/roundtrip/figma-import-back-to-appforge.md
workflows/artifact-lifecycle/artifact-imports/import-review-protocol.md
registries/project-control/baselines/baseline-versioning-rules.md
integrations/design/apps/figma/to-native/* only if implementation mapping is needed
```

## Avoid these prompts

Do not ask agents:

```text
Read the whole Appforger folder.
Read every registry.
Review all repos.
Use all previous context.
```

Use focused tasks instead.
