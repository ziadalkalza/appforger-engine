# Setup Cloud Runtime Skill

Use when the user wants AppForger storage units to run in the cloud.

Procedure:
1. Read `project-control/runtime/runtime-selection.yaml`.
2. Confirm which storage units are cloud: SQL/Postgres, Qdrant/vector, Neo4j/graph.
3. Ensure the user has filled `local-only/.env.local` or configured an external secret manager.
4. Never ask the user to put secret values in `project-control`.
5. Run validation if execution is available:
   `python project-control/runtime/scripts/appforge_runtime.py validate-cloud --profiles postgres,qdrant,neo4j`
6. Only initialize schemas/collections/constraints after explicit approval:
   `python project-control/runtime/scripts/appforge_runtime.py init-cloud-schema --profiles postgres,qdrant,neo4j`
7. Report what was validated, what is missing, and what remains manual.

Do not create paid cloud resources automatically.
