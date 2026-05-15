# Context Freshness Policy

A context index is stale if project-control contains newer canonical state than the context backend.

Examples:

- project-control says API_BASELINE_V3 is current, the context index returns V2 as current.
- a story is superseded in USER_STORY_REGISTRY but still retrieved as active.
- source commit in payload does not match latest indexed project-control commit.

When stale, AppForge must warn and reindex before relying on retrieved content.
