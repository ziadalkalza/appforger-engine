# AppForger Engine

AppForger is a guide-first, project-control and workflow engine for AI-assisted app development.

This repository hosts the reusable AppForger engine and its MCP interface layer. The MCP server exposes AppForger logic (skills, templates, policies, prompts, tools, and command references) to AI clients so they can guide work in a user project safely and consistently.

## What AppForger Is

AppForger is a reusable engine for:

- project setup and onboarding
- project-control and workflow orchestration
- code and documentation context handling
- integration strategy and provider guidance
- runtime storage guidance and infrastructure policies
- source pipeline orchestration
- cleanup and lifecycle controls

It is designed to guide AI tools such as Codex, Claude, Cursor, Copilot, ChatGPT-compatible MCP clients, and Gemini.

The engine includes:

- skills (`SKILLS/`)
- policies and guidance docs
- templates (`TEMPLATES/`)
- validators (`VALIDATION/`)
- Python command references and automation logic
- MCP resources, prompts, and tools (`APPFORGE_MCP_SERVER/`)

## What the MCP Does

The MCP server lives in `APPFORGE_MCP_SERVER/` and uses the rest of this repository as its logic library.

It exposes:

- manifest-selected resources
- reusable prompts
- planning and search tools
- risk classification metadata
- command references and approval requirements

Hosted/remote safety boundary:

- The MCP does **not** execute user project actions in remote mode.
- It returns plans and command references for the user’s AI client/model to run locally after user approval.
- Risky operations must be marked approval-required (for example: cleanup/delete/move actions, runtime volume deletion, Git push, raw code indexing, cloud provisioning, write-enabled integrations).

## What This Repository Provides

- Project onboarding and setup workflows
- Provider-specific AI adapters and routing guidance
- Project-control templates
- Code source import and code context sync guidance
- Runtime storage support guidance for Postgres, Qdrant, and Neo4j
- Local/cloud runtime guidance
- Confluence fetch-only integration boundaries
- Git provider integration guidance for Bitbucket, GitHub, and GitLab
- Source pipeline orchestration policies
- Integration Strategy Advisor
- Project adoption and Git boundary management
- Cleanup workflows
- Skills and execution packet workflows
- MCP server exposure of AppForger logic

## Repository Structure

Main folders in this repository:

- `START_HERE/` - onboarding and first-run guidance
- `HOW_TO_USE_APPFORGE/` - practical usage docs and command references
- `SKILLS/` - AppForger skill library
- `TEMPLATES/` - reusable templates for specs, QA, releases, and routes
- `REGISTRIES/` - engine registries and manifest/state catalogs
- `APPFORGE_MCP_SERVER/` - MCP interface layer and deployment assets
- `RUNTIME_INFRASTRUCTURE/` - runtime/storage policies and scripts
- `DOC_SOURCE_INTEGRATIONS/` - documentation source integration policies
- `GIT_PROVIDER_INTEGRATIONS/` - git provider integration boundaries/policies
- `SOURCE_PIPELINES/` - source pipeline policies and orchestration
- `INTEGRATION_STRATEGY_ADVISOR/` - integration decision/risk guidance
- `VALIDATION/` - validation scripts and safety checks

Note on naming:

- In some docs/examples you may see `appforge-engine/` as a parent folder name. In this repository, the current root **is** the engine root.

## Run the MCP Locally

From the parent directory that contains this repository folder:

```bash
python appforge-engine/APPFORGE_MCP_SERVER/server/appforge_mcp_server.py --engine-root appforge-engine --transport stdio
```

From inside this repository root:

```bash
python APPFORGE_MCP_SERVER/server/appforge_mcp_server.py --engine-root . --transport stdio
```

HTTP mode:

```bash
python APPFORGE_MCP_SERVER/server/appforge_mcp_server.py --engine-root . --transport http --host 0.0.0.0 --port 8080
```

Health check (HTTP mode):

- `GET /health`

## Deploy Remotely

Deploy the **entire repository**, not only `APPFORGE_MCP_SERVER/`.

- `APPFORGE_MCP_SERVER/` is the server layer.
- The rest of the repository is the logic library it serves.

For hosted deployments, run in HTTP mode and use the provided deployment assets:

- `APPFORGE_MCP_SERVER/deployment/docker/`
- `APPFORGE_MCP_SERVER/deployment/digitalocean/`
- `APPFORGE_MCP_SERVER/deployment/env/mcp.env.example`
- `APPFORGE_MCP_SERVER/REMOTE_HOSTING_GUIDE.md`

Render-style hosting can use the same HTTP entrypoint pattern (container/web service running `appforge_mcp_server.py --transport http`).

## Connect an AI Client

Add your hosted MCP endpoint to an MCP-compatible client configuration.

```json
{
  "mcpServers": {
    "appforger": {
      "url": "https://your-domain.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

Use your client’s exact MCP config format if it differs.

## Use AppForger in a Project

High-level flow:

1. Install this engine locally, or connect your AI client to a hosted AppForger MCP.
2. Ask your AI model to use AppForger workflows/resources for the task.
3. AppForger returns setup plans, skills, templates, and command references.
4. The user/model runs approved commands locally in the target project workspace.

Operational boundaries:

- `local-only/.env.local` is for local/private credentials when running engine-local workflows (store outside version control).
- `project-control/` is where project state/metadata should live in user projects.
- Project docs, code repositories, runtime DB/vector/graph stores, and RAG artifacts stay in their own project locations under AppForger rules.

## Contributing

Contributions are welcome via issues and pull requests in your Git provider workflow (for example, GitHub).

### Requesting New Features or Fixes

For new AppForger/MCP capabilities, open an issue in this repository.

- Do not implement global AppForger engine behavior only inside one user project.
- Include: feature goal, expected workflow, affected folders, risk level, examples, and whether MCP resources/prompts/tools are impacted.
- For bugs, include reproduction steps, expected behavior, actual behavior, logs, and package/version details.

### Suggested Issue Formats

Feature request:

- Summary
- Problem
- Proposed behavior
- Example workflow
- Affected area
- Risk/safety concerns
- MCP exposure needed?
- Validation/testing expectations

Bug report:

- Summary
- Steps to reproduce
- Expected behavior
- Actual behavior
- Logs/screenshots
- Environment
- AppForger version/package

### Contribution Rules

- Keep engine root clean.
- Never commit secrets.
- Do not add local-only runtime files.
- Keep risky actions approval-gated.
- Add/update `SKILL.md` when adding a workflow.
- Add/update related policies/templates when behavior changes.
- Add/update validators when new features are added.
- Update `HOW_TO_USE_APPFORGE/` docs for user-facing behavior changes.
- Run validation before opening a PR.

## Validation

Run the validation suite before PR submission (from repo root):

```bash
python VALIDATION/validate_all.py
```

If your change touches a specific subsystem, also run targeted validators in `VALIDATION/`.

## Operational vs Guidance Scope

- Operational components: MCP server runtime, validators, deployment files, and executable scripts.
- Guidance/scaffolding components: skills, policies, templates, playbooks, and command references used by AI clients for safe execution planning.
