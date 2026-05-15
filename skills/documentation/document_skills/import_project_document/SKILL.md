# Import Project Document

Purpose: Import a document into docs/ or an external docs provider and create a document import packet.

Rules:
- Do not store full document bodies in project-control.
- Never overwrite original imported documents.
- Sensitive documents are excluded from indexing by default.
- Register source path/URL, summary path, lifecycle status, and indexing permission.
- Retrieval must point back to canonical docs storage.
