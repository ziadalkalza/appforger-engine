# Code Access Registry

Tracks role-level code access. Do not store credentials or secret values here.

| Source ID | Role | Access Level | Read Scope | Write Scope | Auth Reference | Notes |
|---|---|---|---|---|---|---|
| backend-main | backend_developer | write | raw_files_if_allowed | owned_code_area, approved_task_branch | TBD | TBD |
| backend-main | frontend_mobile_developer | read_only | summaries, api_maps | none | TBD | TBD |
| frontend-main | frontend_mobile_developer | write | raw_files_if_allowed | owned_code_area, approved_task_branch | TBD | TBD |
| frontend-main | backend_developer | read_only | summaries, api_client_maps | none | TBD | TBD |
| all | admin | admin | all_allowed | all_allowed | TBD | TBD |
