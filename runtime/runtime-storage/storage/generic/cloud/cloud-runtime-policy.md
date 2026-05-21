# Cloud Runtime Policy

Appforger storage units may run locally through Docker or connect to cloud services. Cloud mode is for Appforger-specific operational storage: SQL state, vector/RAG storage, and graph relationships.

Supported cloud target categories in v1:
- SQL database service for operational state and optional graph tables.
- Vector database service for vector/RAG storage.
- Graph database service for graph storage.

Service-specific setup belongs under `runtime/platform/storage/apps/`.

Rules:
- Cloud connection values live in `local-only/.env.local` or a real secret manager.
- `project-control/runtime/runtime-selection.yaml` stores provider/mode/references only.
- Appforger may validate cloud endpoints and initialize schemas/collections/constraints after approval.
- Appforger must not create paid cloud resources unless a future explicit provisioning workflow is approved.
- Cloud setup is high-risk because it involves credentials, billing, persistent storage, access control, and project data.
