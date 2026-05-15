# Generic Vector DB Profile

A generic vector DB provider may be added later if it supports:
- upsert with metadata payloads
- filtering by project, artifact type, feature, approval status, and current/superseded state
- deletion or deactivation of stale records
- retrieval with scores and source metadata
- health checks

Provider-specific integration packs must define setup, auth, cost, security, indexing, and validation rules.
