# Token Management Rules

AppForge must minimize token usage by loading context progressively.

## Non-negotiable rules

1. Do not read the entire AppForge folder for normal app work.
2. Do not read all registries unless the task is global planning, project audit, or engine upgrade.
3. Do not read all backend, iOS, Android, and design files together unless performing cross-system integration review.
4. Prefer current baseline packets and stage summaries over raw history.
5. Prefer focused Codex work packets over long conversational context.
6. If a task needs more context, ask for or load only the next smallest relevant file.
7. Summarize completed work into stage/task summaries so future sessions do not need to reload full history.
8. The user-facing operator manual marked `DO_NOT_LOAD` is not execution context and should not be read unless the user explicitly asks how to use AppForge.

## Default context layers

### Always-read operating context

Read only these at the start of a normal AppForge session:

```text
AGENTS.md
APPFORGE_PROJECT_STATUS.md
APPFORGE_PROJECT.yaml
DECISION_LOG.md
PENDING_QUESTIONS.md
registries/decision-snapshots/PROJECT_MEMORY_COMPACTION.md
```

If the project is new and these files are empty, run the new app initializer workflow.

### Stage context

Read only the current stage contract and matching skill:

```text
workflows/operations/stage-contracts/<current_stage>_CONTRACT.md
skills/<relevant_skill>/SKILL.md
```

### Task context

Read only the artifact packet and registry entries required for the current task:

```text
templates/packets/code-agent-packets/providers/codex/<task_packet>.md
registries/baselines/<active_baseline>.md
registries/<affected_registry>.md
```

## When broader context is allowed

Broader context is allowed only for:

- engine upgrade
- architecture review
- full app audit
- release readiness review
- integration failure triage
- major refactor planning

Even then, prefer summaries and registries before raw files.

## Required output behavior

At the end of a meaningful task, report:

```text
Files read:
Files changed / should be changed:
Stage status:
Memory/state updates needed:
Next recommended task:
```
