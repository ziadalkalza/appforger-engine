#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['workflows/operations/workspace-artifact-lifecycle/scripts/appforge_clean.py', 'docs/getting-started/start-here/CLEANUP_GUIDE.md', 'skills/operations/cleanup_skills/clean_appforge_from_project/SKILL.md']
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
print("validate_cleanup_command: OK")
