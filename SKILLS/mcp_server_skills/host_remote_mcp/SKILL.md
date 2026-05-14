# Host Remote AppForger MCP Skill

Use this skill when the user wants to deploy AppForger as a hosted MCP service.

Steps:

1. Use `APPFORGE_MCP_SERVER/REMOTE_HOSTING_GUIDE.md`.
2. Choose Docker or DigitalOcean deployment.
3. Keep execution mode `guide_only`.
4. Expose only manifest-selected resources.
5. Configure API key and OAuth/OIDC scaffolds as needed.
6. Verify `/health`.
7. Do not connect private projects or secrets unless a separate project-aware local/secure deployment is designed.
