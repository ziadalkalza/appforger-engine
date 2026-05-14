#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=[
"RUNTIME_INFRASTRUCTURE/README.md",
"PROJECT_ADOPTION_AND_GIT_BOUNDARIES/README.md",
"GIT_PROVIDER_INTEGRATIONS/README.md",
"DOC_SOURCE_INTEGRATIONS/README.md",
"SOURCE_PIPELINES/README.md",
"NEW_APP_INITIALIZER/setup_appforge_project.py",
"WORKSPACE_AND_ARTIFACT_LIFECYCLE/scripts/appforge_clean.py",
"PROJECT_ADOPTION_AND_GIT_BOUNDARIES/scripts/appforge_adopt.py",
"START_HERE/START_HERE_FOR_AGENTS.md",
"ENGINE_TEMPLATES/workspace-template/local-only/.env.local.example",
"ENGINE_TEMPLATES/project-control-template/pipelines/scripts/run_source_pipeline.py",
"ENGINE_TEMPLATES/project-control-template/code_sources/scripts/bootstrap_code_context.py",
"ENGINE_TEMPLATES/project-control-template/doc_sources/scripts/fetch_confluence.py",
]
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
print("validate_operational_layers: OK")
