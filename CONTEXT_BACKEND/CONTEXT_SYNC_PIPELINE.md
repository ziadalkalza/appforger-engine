# Context Sync Pipeline

Sync flow:

project-control update → detect changed files → chunk/summarize/index → update SQL/vector metadata → write sync report → validate freshness.

Supported v16 triggers:

1. Manual command
2. Codex-run sync
3. Local Git hook
4. GitHub Action
5. Future MCP/server
