# Task Catalog

| Task ID | User intent | Required stage | Skill/packet |
|---|---|---|---|
| start_new_app | Start a new app | ideation | NEW_APP_INITIALIZER |
| create_product_brief | Define product | requirements | product brief skill |
| create_ux_flows | Define flows | ux_flow | skills/design/generic/create_ux_flows |
| create_figma_prompt | Prepare Figma work | figma_design | skills/design/apps/figma/create_prompt |
| import_figma_baseline | Bring Figma back | figma_design | ARTIFACT_IMPORTS + BASELINES |
| select_backend_stack | Choose backend | backend | skills/implementation/backend/generic/select_backend_stack |
| build_supabase_backend | Supabase backend | backend | code-agent backend packet |
| build_fastapi_backend | FastAPI/Postgres backend | backend | code-agent backend packet |
| create_api_contract | API baseline | api_contract | API packet |
| implement_ios_screen | SwiftUI implementation | native_frontend | code-agent iOS packet |
| implement_android_screen | Compose implementation | native_frontend | code-agent Android packet |
| run_visual_qa | Compare implementation to design | qa | visual QA packet |
| open_change_request | Modify approved artifact | any | change request packet |
| import_design_system | Add design rules | design | skills/design/generic/import_design_system |

## Web Track Tasks

- `select_web_stack`
- `create_web_architecture`
- `import_figma_web_baseline`
- `create_web_code_agent_packet`
- `implement_web_page`
- `run_web_visual_qa`
- `prepare_web_preview_deployment`



## v13 Tasks

- create_user_stories
- refine_product_backlog
- map_stories_to_features
- generate_user_docs
- generate_developer_docs
- update_changelog_and_release_notes
- export_backlog_to_trello
- evaluate_external_package

All v13 tasks must write project outputs to external `project-control/`, not to `appforge-engine/`.

## v14 draft/sandbox tasks

| Task ID | User intent | Required stage | Skill/packet |
|---|---|---|---|
| start_draft_experiment | Explore idea without changing project truth | any | draft_skills/start_draft_experiment |
| create_html_sandbox | Create quick HTML prototype | design/exploration | draft_skills/create_html_sandbox |
| review_draft_experiment | Decide if draft should be promoted/discarded | any | draft_skills/review_draft_experiment |
| promote_draft_to_project | Convert approved draft into real artifact | after review | draft_skills/promote_draft_to_project |
| discard_draft_experiment | Mark draft as discarded | any | draft_skills/discard_draft_experiment |

## v15 release and tool-routing tasks

- recommend_best_tool_for_task
- prepare_release_candidate
- generate_release_notes
- prepare_mobile_store_submission
- prepare_web_publish_plan
- run_release_readiness_review
- record_release_approval
- prepare_hotfix_plan

## Context backend tasks

- setup_context_backend
- index_project_context
- retrieve_context_pack
- validate_context_backend
- sync_project_control_to_context_backend

## Flexible Workflow Tasks

- request_stage_override
- perform_workflow_impact_analysis
- promote_sandbox_to_baseline
- import_existing_frontend
- import_existing_backend
- mark_stage_skipped
- create_workflow_variant
