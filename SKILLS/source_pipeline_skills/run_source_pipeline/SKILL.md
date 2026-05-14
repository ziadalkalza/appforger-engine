# Run Source Pipeline Skill

Use this skill when the user asks to fetch, sync, index, or update project context from a registered source.

This skill is the model-facing orchestrator. The Python runner is the deterministic executor.

Procedure:
1. Read `project-control/pipelines/source-sync-pipeline.yaml`.
2. Resolve the source in doc source or code source registries.
3. Identify source type: Confluence/doc source, Git/code source, local docs, snapshot.
4. Check storage mode: docs mirror, exports snapshot, local-only mirror, RAG-only, metadata-only.
5. Check runtime mode: local Docker or cloud endpoints for SQL/Qdrant/Neo4j.
6. Check access/secrets policy; never expose secret values.
7. If execution is available, run:
   `python project-control/pipelines/scripts/run_source_pipeline.py --source <source_id>`
8. If execution is unavailable, create a manual execution packet with exact commands.
9. Report what was fetched, indexed, stored, graphed, skipped, stale, or blocked.

Do not bypass source registries or storage policies.
