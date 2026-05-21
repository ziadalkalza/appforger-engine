# Skill: Retrieve Context Pack

## Purpose
Retrieve focused context for a task/role without loading the whole project.

## Steps
1. Identify task type and role.
2. Query context backend using source filters.
3. Return only current/approved context unless draft mode is requested.
4. Include source paths and metadata.
5. Verify canonical files where required.
6. Save retrieval pack under project-control/context-backend/retrieval-packs/.
