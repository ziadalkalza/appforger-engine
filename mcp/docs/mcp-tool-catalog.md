# MCP Tool Catalog

The Appforger MCP exposes read/plan/search tools by default:

- `list_features`
- `list_skills`
- `search_appforge_resources`
- `get_resource`
- `create_setup_plan`
- `create_adoption_plan`
- `create_cleanup_plan`
- `create_project_control_module_plan`
- `create_context_sync_plan`
- `create_business_requirements_plan`
- `classify_action_risk`

Tools return plans, command references, risk flags, and approval requirements. They do not execute project actions in remote mode.

Setup, adoption, and cleanup plan tools separate the shared engine location from the selected project target:

- `engine_root` is where the reusable Appforger engine is installed.
- `target` is the project root selected by the user or AI client. It can be any local path, not a required folder layout. If omitted, tools use the configured `--workspace-root`; if that is also omitted, command plans use `.` for the AI client's current working directory.

## create_project_control_module_plan

Creates a command plan for adding optional `project-control/` sections after an onboarding answer or later project change requires them. Example: when a project changes from single-user to team mode, request the `team` module instead of copying the entire project-control template.

## create_feature_request_issue_plan

Creates an issue request plan for a new global Appforger MCP/engine feature. This tool does not modify project files. It returns the issue template path, risk notes, proposed MCP surface, and next steps for opening an issue on the Appforger MCP repository.

## create_business_requirements_plan

Creates a BRD creation/import plan. The tool does not write project files. It returns the mandatory BRD workflow, project-control BRD path, registry path, template source rule, required approval, and downstream design/build gate notes.
