# Codex MCP Config Template

Use this as a planning template. Never commit secrets.

```json
{
  "mcpServers": {
    "github": {
      "command": "[github-mcp-command]",
      "args": [],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "figma": {
      "command": "[figma-mcp-command]",
      "args": [],
      "env": {
        "FIGMA_ACCESS_TOKEN": "${FIGMA_ACCESS_TOKEN}"
      }
    },
    "supabase": {
      "command": "[supabase-mcp-command]",
      "args": [],
      "env": {
        "SUPABASE_ACCESS_TOKEN": "${SUPABASE_ACCESS_TOKEN}"
      }
    }
  }
}
```

Store real tokens in local environment variables or a secure secret manager.
