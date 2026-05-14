# Auth and Permission Model

This layer provides policy, schema, and starter guidance. It is not a production-ready identity system by itself.

Roles should map to permissions such as:
- view_task_state
- update_own_task_status
- approve_product_scope
- approve_design_baseline
- approve_api_baseline
- approve_qa_evidence
- approve_release_candidate
- manage_secret_metadata
- manage_team_members
- run_sync_jobs

Implementations may use Supabase Auth/RLS, FastAPI RBAC, or SQLite/local-only access controls.
