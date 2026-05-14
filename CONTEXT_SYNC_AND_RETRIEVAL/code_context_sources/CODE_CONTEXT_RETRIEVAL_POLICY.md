# Code Context Retrieval Policy

Docs and code context should be retrieved together only when the task requires both.

For example, a login-flow task may retrieve:

- product authentication requirements from docs
- backend auth route map
- frontend login component map
- API contract baseline

## Retrieval process

1. Identify task type.
2. Resolve relevant code sources from `code-source-registry.yaml`.
3. Check current role/access policy.
4. Retrieve allowed context: metadata, summaries, maps, task-scoped files, or raw files.
5. If implementation is requested, inspect actual files or require a fresh execution packet generated from actual files.
6. Log retrieval source ids and freshness.

## Source display behavior

Normal user-facing answers may use context naturally without showing source metadata every time.

Implementation packets, audit logs, and source-review requests must include exact source ids, file paths, and commit/snapshot metadata when available.
