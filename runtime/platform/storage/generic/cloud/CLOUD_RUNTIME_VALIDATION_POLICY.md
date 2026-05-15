# Cloud Runtime Validation Policy

Cloud validation must check only connectivity and required configuration. It must not create, modify, or delete cloud resources unless the user explicitly runs an initialization/provisioning command.

Validation checks:
- Required environment references are present.
- Endpoint URLs are syntactically valid.
- Vector database health endpoint responds when reachable.
- Graph database socket or API endpoint is reachable when configured.
- Postgres URL is present and parseable; schema setup requires an approved init step.
