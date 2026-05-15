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

- skills (`skills/`)
- policies and guidance docs (`policies/`, `docs/`)
- templates (`templates/specs/`, `templates/packets/`, `templates/engine/`)
- validators (`validation/`)
- Python command references and automation logic
- MCP resources, prompts, tools, clients, and hosting assets (`mcp/`)

## What the MCP Does

The MCP server lives in `mcp/` and uses the rest of this repository as its logic library.

It exposes:

- manifest-selected resources
- reusable prompts
- planning and search tools
- risk classification metadata
- command references and approval requirements

Hosted/remote safety boundary:

- The MCP does **not** execute user project actions in remote mode.
- It returns plans and command references for the user's AI client/model to run locally after user approval.
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

Root folders are domain buckets. Detailed files live inside context-specific subfolders rather than directly beside unrelated domains.

When a feature area has both general rules and app/provider-specific variants, it uses `generic/` plus `apps/`, `providers/`, or another domain-specific variant folder. When an area only has generic files, those files live directly in the feature folder instead of inside a `generic/` wrapper.

```text
docs/
  getting-started/
    start-here/
    operator-guides/
  runbooks/
    backend/
    failure-playbooks/
  ai-clients/
    generic/
    providers/
  collaboration/
  document-management/
  generated-app/

integrations/
  source-control/
    generic/
    github/
      team-workflow/
    gitlab/
    bitbucket/
  document-sources/
    confluence/
    google-drive/
  design/
    generic/
    apps/
  planning/
  catalog/

mcp/
  interface/
    server/
    prompts/
  clients/
    examples/
    configs/
  hosting/
    deployment/
  sdk/
  catalog/

policies/
  operations/
  collaboration/
  context/
  delivery/
  engineering/
  providers/
    provider-layer/
      provider_profiles/
        generic/
        providers/
        apps/
  security/
    external-tool-boundaries/
      generic/
      providers/
      apps/

runtime/
  context/
    context-backend/
    apps/
  execution/
    generic/
    local-models/
    providers/
  platform/
    storage/
      generic/
      apps/
  collaboration/

skills/
  product/
  design/
  implementation/
    backend/
      generic/
      stacks/
      apps/
  quality/
  delivery/
  operations/
  runtime/
  context/
    code-context/
    context-backend/
  integrations/
    generic/
    apps/
  collaboration/
  documentation/
  onboarding/
  providers/
    generic/
    providers/
  governance/
  architecture/
  workflow/

templates/
  specs/
  packets/
  jobs/
  ai-prompts/
    generic/
    providers/
    apps/
  engine/
  examples/

workflows/
  product/
  experience-design/
  implementation/
    backend/
      generic/
      stacks/
      apps/
  strategy/
  delivery/
  operations/

validation/
  audits/
  domains/
```

Other root folders:

- `registries/` - engine registries, manifests, baselines, and decision snapshots.
- `scripts/` - standalone utility scripts.
- `validation/` root files - executable validators, including `validation/validate_all.py`.

Common path anchors:

- Feature specs: `templates/specs/feature_spec_template.md`
- Execution packets: `templates/packets/execution-packets/`
- Code-agent packets: `templates/packets/code-agent-packets/`
- Provider-specific code-agent packet adapters: `templates/packets/code-agent-packets/providers/`
- AI prompts: `templates/ai-prompts/generic/`, `templates/ai-prompts/providers/`, `templates/ai-prompts/apps/`
- MCP server: `mcp/interface/server/appforge_mcp_server.py`
- MCP client examples: `mcp/clients/examples/`
- MCP deployment assets: `mcp/hosting/deployment/`
- Runtime storage: `runtime/platform/storage/`
- Storage app setup: `runtime/platform/storage/apps/`
- Context backend: `runtime/context/context-backend/`
- Context storage app profiles: `runtime/context/apps/`
- Provider runtimes: `runtime/execution/providers/`
- Provider profiles: `policies/providers/provider-layer/provider_profiles/`
- External tool boundaries: `policies/security/external-tool-boundaries/`
- Source pipelines: `workflows/operations/source-pipelines/`
- Integration strategy: `workflows/strategy/integration-strategy-advisor/`

Note on naming:

- In some docs/examples you may see `appforge-engine/` as a parent folder name. In this repository, the current root **is** the engine root.

## Run the MCP Locally

From the parent directory that contains this repository folder:

```bash
python appforge-engine/mcp/interface/server/appforge_mcp_server.py --engine-root appforge-engine --transport stdio
```

From inside this repository root:

```bash
python mcp/interface/server/appforge_mcp_server.py --engine-root . --transport stdio
```

HTTP mode:

```bash
python mcp/interface/server/appforge_mcp_server.py --engine-root . --transport http --host 0.0.0.0 --port 8080
```

Health check (HTTP mode):

- `GET /health`

## Deploy Remotely

Deploy the **entire repository**, not only `mcp/`.

- `mcp/` is the server layer.
- The rest of the repository is the logic library it serves.

For hosted deployments, run in HTTP mode and use the provided deployment assets:

- `mcp/hosting/deployment/docker/`
- `mcp/hosting/deployment/digitalocean/`
- `mcp/hosting/deployment/env/mcp.env.example`
- `mcp/REMOTE_HOSTING_GUIDE.md`

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

Use your client's exact MCP config format if it differs.

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
- Update `docs/getting-started/operator-guides/` docs for user-facing behavior changes.
- Run validation before opening a PR.

## Validation

Run the validation suite before PR submission (from repo root):

```bash
python validation/validate_all.py
```

If your change touches a specific subsystem, also run targeted validators in `validation/`.

## Operational vs Guidance Scope

- Operational components: MCP server runtime, validators, deployment files, and executable scripts.
- Guidance/scaffolding components: skills, policies, templates, playbooks, and command references used by AI clients for safe execution planning.
