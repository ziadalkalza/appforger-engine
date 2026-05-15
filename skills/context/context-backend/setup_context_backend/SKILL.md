# Skill: Setup Context Backend

## Purpose
Configure optional context backend mode for a project.

## Steps
1. Confirm context backend is optional and project-control remains canonical.
2. Ask user to choose profile: vector, SQL/vector, or hybrid context storage.
3. Confirm indexing scope and exclusions.
4. Confirm cost/security approval.
5. Create/update `project-control/context-backend/config/context_backend_config.yaml`.
6. Validate required folders/scripts/schemas.
7. Record status in CONTEXT_BACKEND_REGISTRY.md.

## Do not
- Enable paid services without approval.
- Index secrets or drafts by default.
- Treat RAG as canonical truth.
