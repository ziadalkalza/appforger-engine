# Runtime Storage: Local and Cloud

AppForger runtime storage can run locally through Docker or connect to cloud services.

Local units:

- Postgres for operational state;
- Qdrant for vector/RAG storage;
- Neo4j for graph relationships.

Cloud modes use endpoint references in `local-only/.env.local` and runtime selection in `project-control/runtime/runtime-selection.yaml`.
