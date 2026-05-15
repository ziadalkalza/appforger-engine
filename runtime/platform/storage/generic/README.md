# Runtime Infrastructure

AppForger can use local Docker or cloud services for runtime storage:
- SQL storage for operational/team/runtime state
- vector storage for RAG/context retrieval
- graph or relational storage for relationships

Runtime choices are stored in `project-control/runtime/runtime-selection.yaml`.

## Cloud runtime support

AppForger can use local Docker services or existing cloud services for its storage units. Use `generic/cloud/` policies for selection rules and `apps/` for service-specific setup.
