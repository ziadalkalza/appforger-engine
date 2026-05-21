#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['workflows/source-pipeline/source-pipelines/README.md', 'templates/project-control/pipelines/scripts/run_source_pipeline.py', 'skills/source-pipeline/run-source-pipeline/SKILL.md']
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
print("validate_source_pipeline_orchestrator: OK")
