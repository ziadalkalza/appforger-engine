#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=[
"runtime/runtime-storage/storage/README.md",
"workflows/operations/project-adoption-git-boundaries/README.md",
"integrations/source-control/bitbucket/docs/README-2.md",
"integrations/document-sources/confluence/docs/README.md",
"workflows/source-pipeline/source-pipelines/README.md",
"workflows/operations/new-app-initializer/setup_appforge_project.py",
"workflows/operations/workspace-artifact-lifecycle/scripts/appforge_clean.py",
"workflows/operations/project-adoption-git-boundaries/scripts/appforge_adopt.py",
"docs/project-onboarding/start-here/start-here-for-agents.md",
"templates/workspace/local-only/.env.local.example",
"templates/project-control/pipelines/scripts/run_source_pipeline.py",
"templates/project-control/code-sources/scripts/bootstrap_code_context.py",
"templates/project-control/doc-sources/scripts/fetch_confluence.py",
]
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
print("validate_operational_layers: OK")
