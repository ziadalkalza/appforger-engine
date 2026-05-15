#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=[
"runtime/platform/storage/README.md",
"workflows/operations/project-adoption-git-boundaries/README.md",
"integrations/source-control/generic/README.md",
"integrations/document-sources/confluence/README.md",
"workflows/operations/source-pipelines/README.md",
"workflows/operations/new-app-initializer/setup_appforge_project.py",
"workflows/operations/workspace-artifact-lifecycle/scripts/appforge_clean.py",
"workflows/operations/project-adoption-git-boundaries/scripts/appforge_adopt.py",
"docs/getting-started/start-here/START_HERE_FOR_AGENTS.md",
"templates/engine/workspace-template/local-only/.env.local.example",
"templates/engine/project-control-template/pipelines/scripts/run_source_pipeline.py",
"templates/engine/project-control-template/code_sources/scripts/bootstrap_code_context.py",
"templates/engine/project-control-template/doc_sources/scripts/fetch_confluence.py",
]
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
print("validate_operational_layers: OK")
