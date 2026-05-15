# Setup and First Run

Use this guide to apply AppForger to a new or existing project.

## 1. Extract the package

Extract the zip so the workspace contains:

```text
my-workspace/
  appforge-engine/
```

Do not place `appforge-engine/` inside `backend/` or `web/`. It should sit beside project folders.

## 2. Ask an AI model to set up AppForger, or run setup manually

Agent-assisted setup:

```text
Read appforge-engine/docs/getting-started/start-here/START_HERE_FOR_AGENTS.md and set up AppForger for this project.
```

Manual setup:

```bash
python appforge-engine/workflows/operations/new-app-initializer/setup_appforge_project.py --target . --name "My Product"
```

Choose provider adapters explicitly, for example:

```bash
python appforge-engine/workflows/operations/new-app-initializer/setup_appforge_project.py \
  --target . \
  --name "My Product" \
  --agent-adapters codex
```

## 3. Fill the local private env file

After setup, fill:

```text
local-only/.env.local
```

This is the single local/private configuration file for secrets, service URLs, Git provider tokens, Confluence tokens, runtime endpoints, and local-only settings.

Do not commit or index this file.

## 4. Complete onboarding

Answer onboarding questions about:

- new/existing/ongoing project;
- local or remote code sources;
- project runtime storage;
- docs and source integrations;
- provider adapters;
- Git/project-control boundaries.

If the project is ongoing, AppForger requires initial code context bootstrap before code-aware implementation.

## 5. Configure runtime storage

For local Docker storage, use Postgres, Qdrant, and optionally Neo4j:

```bash
python project-control/runtime/scripts/appforge_runtime.py init-local-env
python project-control/runtime/scripts/appforge_runtime.py up --profiles postgres,qdrant,neo4j
python project-control/runtime/scripts/appforge_runtime.py health --profiles postgres,qdrant,neo4j
```

For cloud storage, configure `project-control/runtime/runtime-selection.yaml` and place endpoint references in `local-only/.env.local`.

## 6. Register docs and code sources

Typical source registrations:

- backend repo;
- frontend/mobile repo;
- Confluence source;
- project docs folder;
- external docs snapshots.

Use `project-control/code_sources/` and `project-control/doc_sources/` registries generated from templates.

## 7. Bootstrap context

Code context:

```bash
python project-control/code_sources/scripts/bootstrap_code_context.py --source backend-main
```

Source pipeline:

```bash
python project-control/pipelines/scripts/run_source_pipeline.py --source backend-main
```

Confluence example:

```bash
python project-control/pipelines/scripts/run_source_pipeline.py \
  --source product-space \
  --storage-mode rag_only
```

## 8. Validate

From inside `appforge-engine/`:

```bash
python validation/validate_all.py --deep
```

Or ask the AI model to run the appropriate validators before changing project files.

## 9. Start normal work

After setup, use AppForger skills and execution packets to:

- plan features;
- assign work to AI coding tools;
- fetch and index sources;
- review code maps and graph relationships;
- run validation/domains/qa/release workflows;
- track approvals and evidence.
