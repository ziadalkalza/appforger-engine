# Index Project Documents

Purpose: Index allowed document summaries/extractions through the configured context backend.

Rules:
- Do not store full document bodies in project-control.
- Never overwrite original imported documents.
- Sensitive documents are excluded from indexing by default.
- Register source path/URL, summary path, lifecycle status, and indexing permission.
- Retrieval must point back to canonical docs storage.
