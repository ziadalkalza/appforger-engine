# Plan Mode Policy

Plan mode is a low-token, no-implementation mode used to align with the user before real work.

## Enter plan mode when

- the task affects architecture,
- the task adds a new integration,
- the task changes approved baselines,
- the user asks for a big new feature,
- requirements are unclear,
- work may be expensive/destructive,
- Codex would need to inspect many files,
- there is a risk of UI drift,
- online research is required before safe action.

## Plan mode output

In plan mode, produce:

```text
Goal:
Current known context:
Missing information:
Assumptions:
Options:
Risks:
Recommended path:
Questions for user:
Files/stages likely affected:
What will happen after approval:
```

Do not write production code, activate integrations, create cloud resources, approve baselines, or make commits in plan mode.
