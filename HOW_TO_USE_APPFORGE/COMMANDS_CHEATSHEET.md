# Commands Cheatsheet

Commands are examples. Some paths exist after running setup because they are generated from engine templates.

## Setup

```bash
python appforge-engine/NEW_APP_INITIALIZER/setup_appforge_project.py --target . --name "My Product"
```

## Local runtime

```bash
python project-control/runtime/scripts/appforge_runtime.py init-local-env
python project-control/runtime/scripts/appforge_runtime.py up --profiles postgres,qdrant,neo4j
python project-control/runtime/scripts/appforge_runtime.py health --profiles postgres,qdrant,neo4j
```

## Code context

```bash
python project-control/code_sources/scripts/bootstrap_code_context.py --source backend-main
python project-control/code_sources/scripts/sync_code_context.py --source backend-main
python project-control/code_sources/scripts/validate_code_context_runtime.py
```

## Source pipeline

```bash
python project-control/pipelines/scripts/run_source_pipeline.py --source backend-main
python project-control/pipelines/scripts/run_source_pipeline.py --source product-space --storage-mode rag_only
python project-control/pipelines/scripts/run_source_pipeline.py --all
```

## Confluence

```bash
python project-control/doc_sources/scripts/fetch_confluence.py --source product-space --page-id 123456 --include-children --storage-mode rag_only
```

## Adoption and cleanup

```bash
python appforge-engine/PROJECT_ADOPTION_AND_GIT_BOUNDARIES/scripts/appforge_adopt.py --target . scan
python appforge-engine/WORKSPACE_AND_ARTIFACT_LIFECYCLE/scripts/appforge_clean.py --target . --mode remove-engine
```

## MCP

```bash
python appforge-engine/APPFORGE_MCP_SERVER/server/appforge_mcp_server.py --engine-root appforge-engine --transport stdio
python appforge-engine/APPFORGE_MCP_SERVER/server/appforge_mcp_server.py --engine-root appforge-engine --transport http --host 0.0.0.0 --port 8080
```

## Validation

```bash
cd appforge-engine
python VALIDATION/validate_all.py --deep
```
