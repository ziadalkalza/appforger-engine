# ChatGPT Connector Notes

Use this folder as the basis for a ChatGPT-compatible MCP/custom connector deployment when the product/client supports remote MCP or connector configuration.

Recommended mode:

- Host AppForger MCP using Docker/DigitalOcean.
- Expose only manifest-selected resources.
- Keep execution mode as `guide_only`.
- Return command references and risk metadata; do not execute user project actions remotely.
