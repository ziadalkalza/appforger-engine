# Runtime Infrastructure

AppForger can use local Docker or cloud services for runtime storage:
- Postgres for operational/team/runtime state
- Qdrant for RAG/vector storage
- Neo4j or Postgres graph tables for relationships

Runtime choices are stored in `project-control/runtime/runtime-selection.yaml`.

## Cloud runtime support

AppForger can use local Docker services or existing cloud services for its storage units. Use `cloud_runtime/` policies and `project-control/runtime/cloud/` templates when selecting Qdrant Cloud, Neo4j Aura, Supabase, or managed Postgres.
