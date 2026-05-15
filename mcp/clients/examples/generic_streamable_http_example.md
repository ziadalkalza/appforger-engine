# Generic HTTP MCP Example

```bash
python appforge-engine/mcp/interface/server/appforge_mcp_server.py \
  --engine-root appforge-engine \
  --transport http \
  --host 0.0.0.0 \
  --port 8080
```

Health check:

```bash
curl http://localhost:8080/health
```
