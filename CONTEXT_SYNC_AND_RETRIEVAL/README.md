# Context Sync and Retrieval

This folder defines how project-control content is indexed into optional context backends and retrieved as focused packs.

## Stronger Sync and Retrieval Rules

Sync pipelines must support:
- local JSONL default indexing
- Qdrant indexing when enabled
- source metadata on every record
- retrieval logs
- retrieval explanations
- stale context detection
- reindex/update task creation
- document summary indexing from `docs/summaries/`

## Code Context Sources

Code Context Sources live under `CONTEXT_SYNC_AND_RETRIEVAL/code_context_sources/`.

They add role-aware backend/frontend/mobile code context to the existing docs/context system. Registered code sources may be local, remote Git, uploaded snapshot, CI-generated, or summary-only.

For ongoing or existing projects, AppForge must run an initial code context bootstrap before code-aware implementation. Bootstrap creates safe summaries, maps, source metadata, freshness records, and context indexes without modifying source code.

The single user-facing sensitive configuration file is `local-only/.env.local`. Project-control stores only generated metadata and references.
