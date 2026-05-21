# Context Sync Pipeline

Sync flow:

project-control update â†’ detect changed files â†’ chunk/summarize/index â†’ update SQL/vector metadata â†’ write sync report â†’ validate freshness.

Supported v16 triggers:

1. Manual command
2. code-agent sync
3. Local Git hook
4. source-control automation
5. Future MCP/server
