# Active Rules Generation Policy

After onboarding, AppForge generates `APPFORGE_ACTIVE_RULES.md` from the user's answers.

Examples:

- If `team_mode = inactive`, team PR requirements are inactive unless manually enabled.
- If `team_mode = active`, named approvers and project-control PR rules apply.
- If `design_workflow = html_sandbox_first`, HTML sandbox may substitute for Figma after promotion to visual baseline.
- If `backend_needed = no`, backendless workflow and waiver rules apply.
- If `preferred_backend = supabase`, Supabase backend workflows are preferred.
- If `brand_family_policy = high_risk_strict`, cross-brand high-risk dependent work requires reconciliation.
- If `context_backend = local_jsonl`, use local JSONL retrieval and source metadata.
- If `automation_level = local_validation`, automation may run validators/reports but not edit/push/merge without approval.

## Code Context Sources active rules

If `ongoing_project = yes_active_project`, generated active rules must include:

- initial code context bootstrap is required before code-aware implementation;
- stale/partial code context blocks implementation/refactor/release/high-risk work;
- code sources must be resolved from code-source-registry before packets use code context;
- the single private config file is the user-facing source for sensitive/access/runtime values;
- project-control may store only safe metadata and references.
