# Classify Project Document

Purpose: Classify document type, sensitivity, lifecycle status, and related Appforger entities.

Rules:
- Do not store full document bodies in project-control.
- Never overwrite original imported documents.
- Sensitive documents are excluded from indexing by default.
- Register source path/URL, summary path, lifecycle status, and indexing permission.
- Retrieval must point back to canonical docs storage.
