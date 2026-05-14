# Cloud Provider Setup Guide

Use this when the user chooses cloud runtime instead of local Docker.

1. Create or select cloud services:
   - Postgres/Supabase for operational SQL.
   - Qdrant Cloud for vector context.
   - Neo4j Aura for graph relationships.
2. Store connection values in `local-only/.env.local` or a secret manager.
3. Set `project-control/runtime/runtime-selection.yaml` to cloud modes.
4. Run validation:

```bash
python project-control/runtime/scripts/appforge_runtime.py validate-cloud --profiles postgres,qdrant,neo4j
```

5. Initialize schemas/collections/constraints after approval:

```bash
python project-control/runtime/scripts/appforge_runtime.py init-cloud-schema --profiles postgres,qdrant,neo4j
```

This guide does not create paid cloud resources automatically.
