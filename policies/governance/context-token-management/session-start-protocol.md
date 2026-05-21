# Session Start Protocol

Use this file to start new ChatGPT or Codex sessions without wasting tokens.

## ChatGPT continuation prompt

```text
You are operating inside Appforger.
Read only the operating context first:
- AGENTS.md
- APPFORGER_PROJECT_STATUS.md
- APPFORGER_PROJECT.yaml
- DECISION_LOG.md
- PENDING_QUESTIONS.md
- registries/project-control/decision-snapshots/project-memory-compaction.md

Do not read the whole engine.
Continue from the current stage and tell me the next best action.
```

## ChatGPT stage prompt

```text
Use Appforger.
We are starting the [stage name] stage.
Read the current project state, the matching stage contract, the relevant skill, and only the registries needed for this stage.
Create the stage plan, inputs needed, outputs expected, and approval gate.
```

## ChatGPT post-stage memory prompt

```text
Update Appforger memory for the completed stage.
Create a concise stage summary, update affected registries, update APPFORGER_PROJECT_STATUS.md, record decisions/open questions, and list the exact context the next session should read.
```

## Codex task prompt

```text
You are operating in the [backend/ios/android] repo under Appforger control.
Read this repo's AGENTS.md and APPFORGER_POINTER.md, then read the supplied Codex work packet only.
Do not read the whole Appforger engine.
Implement the task, run the required checks, and produce a done report with files changed, tests run, and Appforger registry updates needed.
```

## Figma import prompt

```text
Use Appforger to import this Figma work as a candidate design baseline.
Read only the Figma import protocol, artifact import protocol, baseline versioning rules, and relevant screen/design registries.
Classify what was imported, what is approved/pending, and what implementation packets can be created next.
```
