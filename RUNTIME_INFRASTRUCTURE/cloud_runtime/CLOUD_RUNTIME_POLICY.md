# Cloud Runtime Policy

AppForger storage units may run locally through Docker or connect to cloud services. Cloud mode is for AppForger-specific operational storage: SQL state, vector/RAG storage, and graph relationships.

Supported cloud targets in v1:
- Managed Postgres or Supabase Postgres for operational state and optional graph tables.
- Qdrant Cloud or compatible Qdrant endpoint for vector/RAG storage.
- Neo4j Aura or compatible Neo4j endpoint for graph storage.

Rules:
- Cloud connection values live in `local-only/.env.local` or a real secret manager.
- `project-control/runtime/runtime-selection.yaml` stores provider/mode/references only.
- AppForger may validate cloud endpoints and initialize schemas/collections/constraints after approval.
- AppForger must not create paid cloud resources unless a future explicit provisioning workflow is approved.
- Cloud setup is high-risk because it involves credentials, billing, persistent storage, access control, and project data.
