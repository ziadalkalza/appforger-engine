# Skill: Import Existing Backend

Use when an existing backend/API should be brought into Appforger.

Steps:
1. Identify repo/docs/deployment.
2. Inventory APIs/data models/auth/storage.
3. Compare to product needs.
4. Create API baseline candidate.
5. Identify security/env gaps.
6. Update imported artifact and API registries.

## Code Context Sources requirements

When importing an existing backend:

1. Register the backend in `code-source-registry.yaml`.
2. Mark whether it is canonical.
3. Record fetch mode: local, remote Git, snapshot, CI-generated, or summary-only.
4. Validate role access and auth reference metadata.
5. Run initial code context bootstrap if the project is ongoing.
6. Generate API route, auth/security, database model, migration, integration, dependency, and risky-file maps.
7. Do not modify backend code during bootstrap.
