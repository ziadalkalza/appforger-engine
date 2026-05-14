# Validate Cloud Runtime Skill

Use this when the user wants to connect AppForger to cloud Postgres/Qdrant/Neo4j services. Read `project-control/runtime/runtime-selection.yaml`, load only references from `local-only/.env.local`, run runtime health checks, and report missing credentials or failed endpoints. Do not create paid resources without explicit approval.
