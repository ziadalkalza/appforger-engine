#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['PROJECT_ADOPTION_AND_GIT_BOUNDARIES/README.md', 'PROJECT_ADOPTION_AND_GIT_BOUNDARIES/scripts/appforge_adopt.py', 'SKILLS/project_adoption_skills/create_adoption_plan/SKILL.md', 'ENGINE_TEMPLATES/project-control-template/adoption/adoption-manifest.yaml']
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
print("validate_project_adoption_and_git_boundaries: OK")
