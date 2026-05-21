# DigitalOcean Deployment Guide

This example deploys Appforger MCP as a guide-only remote HTTP MCP service.

1. Push the Appforger engine repository/package to a private deployment repo.
2. Create a DigitalOcean App Platform app using `digitalocean-app.yaml.example`.
3. Configure secrets in DigitalOcean, especially `APPFORGER_MCP_API_KEY` if you enable API-key auth.
4. Verify `/health` returns `{"status":"ok"}`.

The hosted MCP must not execute project actions. It returns plans, command references, risk flags, and approval requirements.
