# Context Metadata Schema

Every indexed item must include metadata similar to:

```yaml
context_id: CTX-0001
project_id: my-app
source_type: project_control | docs | figma | repo_summary | qa_report | release_doc
source_path_or_url: project-control/REGISTRIES/API_REGISTRY.md
artifact_id: API-AUTH-LOGIN
artifact_type: api_contract
feature_id: AUTH
approval_status: approved
lifecycle_status: current
is_current: true
sensitivity: normal
indexing_allowed: true
source_commit: abc123
last_indexed: YYYY-MM-DD
summary_of: null
```

Retrieval output must include this metadata so Appforger can verify the canonical source.
