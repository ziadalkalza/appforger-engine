#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['workflows/operations/source-pipelines/README.md', 'templates/engine/project-control-template/pipelines/scripts/run_source_pipeline.py', 'skills/operations/source_pipeline_skills/run_source_pipeline/SKILL.md']
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
print("validate_source_pipeline_orchestrator: OK")
