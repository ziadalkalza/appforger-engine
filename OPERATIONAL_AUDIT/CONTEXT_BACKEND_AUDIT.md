# Context Backend Audit

Checks v16 context backend behavior.

## Rules

- Context backend is optional.
- Project-control/GitHub remains canonical in v16-v20.
- RAG/Qdrant retrieval must include source metadata.
- Stale indexes must be detected.
- Secrets, env files, build artifacts, debug logs, and unapproved drafts are excluded by default.
- Retrieval packs must cite source paths, artifact IDs, versions, and approval status.
