# Codex Draft Workflow

Codex may create draft code in two approved ways:

## Option A: Local-only draft

```text
local-only/drafts/codex-experiments/<draft-id>/
```

Use this for throwaway components, layout tests, proof-of-concepts, or package experiments.

## Option B: Draft branch

Use a branch such as:

```text
draft/<feature-or-idea>
```

Rules:

- A draft branch may compile or run, but it is not approved implementation.
- It must not merge until promoted.
- It must not mark task completion unless converted into a real task packet and reviewed.
- It must be recorded in `DRAFT_REGISTRY.md`.
