# MCP Tool Catalog

The AppForger MCP exposes read/plan/search tools by default:

- `list_features`
- `list_skills`
- `search_appforge_resources`
- `get_resource`
- `create_setup_plan`
- `create_adoption_plan`
- `create_cleanup_plan`
- `create_context_sync_plan`
- `classify_action_risk`

Tools return plans, command references, risk flags, and approval requirements. They do not execute project actions in remote mode.

## create_feature_request_issue_plan

Creates an issue request plan for a new global AppForger MCP/engine feature. This tool does not modify project files. It returns the issue template path, risk notes, proposed MCP surface, and next steps for opening an issue on the AppForger MCP repository.
