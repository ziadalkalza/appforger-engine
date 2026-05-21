# Generic HTTP MCP Example

```bash
python /absolute/path/to/appforger-engine/mcp/server/appforge_mcp_server.py \
  --engine-root /absolute/path/to/appforger-engine \
  --transport http \
  --host 0.0.0.0 \
  --port 8080
```

Health check:

```bash
curl http://localhost:8080/health
```
