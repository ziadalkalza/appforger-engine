# Context and Token Management

This folder defines how Appforger keeps ChatGPT/Codex sessions efficient as an app grows.

Core rule:

```text
Do not load the whole engine or all app artifacts for normal work.
Load the operating context, current stage context, and the smallest task-specific packet needed.
```

Use these files:

- `TOKEN_MANAGEMENT_RULES.md` — rules agents must follow to reduce token use.
- `CONTEXT_LOADING_POLICY.md` — what to read at session start, stage start, and task start.
- `MEMORY_SAVE_PROTOCOL.md` — what to update after sessions, stages, Codex work, Figma imports, and GitHub commits.
- `SESSION_START_PROTOCOL.md` — how to start ChatGPT/Codex sessions without uploading everything.
- `CONTEXT_PACK_TEMPLATE.md` — compact task context packet for large projects.
- `CONTEXT_BUDGET_CHECKLIST.md` — quick checklist before asking an agent to read files.
