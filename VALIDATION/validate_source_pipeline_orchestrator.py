#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['SOURCE_PIPELINES/README.md', 'ENGINE_TEMPLATES/project-control-template/pipelines/scripts/run_source_pipeline.py', 'SKILLS/source_pipeline_skills/run_source_pipeline/SKILL.md']
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
print("validate_source_pipeline_orchestrator: OK")
