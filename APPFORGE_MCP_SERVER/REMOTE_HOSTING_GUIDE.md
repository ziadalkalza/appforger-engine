# Remote Hosting Guide

AppForger can be hosted as a remote MCP logic server. In remote mode, it does not access user local files or execute project actions. It exposes manifest-selected AppForger resources, workflow prompts, and plan/search tools.

## Recommended deployment options

- Docker on a VPS
- DigitalOcean App Platform

## Remote behavior

Remote MCP returns:

- AppForger skills and policies
- workflow prompts
- command references
- risk flags
- approval requirements

Remote MCP must not directly:

- move/delete files
- push Git changes
- start local Docker services
- fetch private Confluence/Bitbucket content
- index private repos
- provision paid cloud resources

## Environment

Use `deployment/env/mcp.env.example` as the starting point.



Safety invariant: remote hosted AppForger MCP does not execute project actions; it returns command references with `mcp_executes: false` and approval requirements.
