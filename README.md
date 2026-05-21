# Appforger Engine

Appforger is a guide-first project-control, workflow, and MCP engine for AI-assisted app development.

This package has been reorganized so files are easier to find by artifact type first, then by feature or platform. AI-client/model-specific files now live under `ai-models/`; non-AI third-party integrations now live under the integration area where they are used; and the `mcp/` folder is reserved for running Appforger as an MCP server.

## Top-level folders

```text
appforger-engine/
  ai-models/       # AI clients/models that use the engine: ChatGPT, Claude, Codex, Cursor, Copilot, Gemini
  docs/            # Human/operator documentation by feature
  workflows/       # Stage workflows, orchestration flows, and command scripts
  policies/        # Governance, security, release, design, and source-control policies
  skills/          # Reusable skills organized by engine feature
  templates/       # Project-control, workspace, prompt, packet, specification, and job templates
  integrations/    # Non-AI third-party app/platform integrations and integration policies
  runtime/         # Operational runtime setup for databases, context backends, and backend platforms
  mcp/             # Files needed to run Appforger as an MCP server
  validation/      # Validation scripts, testing guidance, QA, and audits
  registries/      # Engine and project-control registries
  examples/        # Runnable/example structures split out from templates
  tools/           # User-facing helper utilities
```

## Most important anchors

```text
mcp/server/                         # MCP server implementation
mcp/deployment/                     # Docker, env, and hosting deployment assets
mcp/clients/examples/               # Client configuration examples for connecting to the MCP
mcp/docs/                           # MCP install/use/security/hosting docs

ai-models/codex/                    # Codex-specific docs, policies, runtime, templates, and skills
ai-models/claude/                   # Claude-specific docs, policies, runtime, templates, and skills
ai-models/chatgpt/                  # ChatGPT-specific docs, policies, runtime, templates, and skills

templates/project-control/          # Canonical project-control template
templates/workspace/                # Canonical workspace template
templates/execution-packets/        # Generic, artifact, code-agent, and team handoff packets
templates/ai-prompts/generic/       # Model-agnostic AI prompts

integrations/design/figma/          # Figma design integration materials
integrations/source-control/github/ # GitHub source-control integration materials
integrations/source-control/bitbucket/
integrations/document-sources/confluence/
integrations/mcp-catalog/           # External MCP connector/config catalog

runtime/context-backend/qdrant/     # Qdrant runtime setup and guidance
runtime/context-backend/neo4j/      # Neo4j runtime setup and guidance
runtime/databases/postgres/         # Postgres runtime setup
runtime/backend-platforms/supabase/ # Supabase runtime setup
```

## Running the MCP locally

From inside this repository root:

```bash
python mcp/server/appforge_mcp_server.py --engine-root . --transport stdio
```

HTTP mode:

```bash
python mcp/server/appforge_mcp_server.py --engine-root . --transport http --host 0.0.0.0 --port 8080
```

Health check in HTTP mode:

```text
GET /health
```

## Notes about this restructure

- `.git/` and `desktop.ini` were intentionally preserved.
- Repeated folders such as `templates/templates/`, `validation/validation/`, and `docs/*/*` duplicates were flattened.
- Duplicate files were removed only when the contents were identical or merged when the intent was obvious, such as `README-2.md` into the folder `README.md`.
- Some Python filenames still contain `appforge` because they are import-safe runtime identifiers. The product name in docs is standardized as **Appforger**.
- Git metadata was preserved, but because files were moved, review `git status` after extraction before committing.

See `STRUCTURE_NOTES.md` for the detailed cleanup summary.
