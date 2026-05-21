#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['workflows/operations/workspace-artifact-lifecycle/scripts/appforge_clean.py', 'docs/project-onboarding/start-here/cleanup-guide.md', 'skills/cleanup-lifecycle/clean-appforge-from-project/SKILL.md']
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
script=(root/'workflows/operations/workspace-artifact-lifecycle/scripts/appforge_clean.py').read_text(encoding='utf-8')
required_script_phrases=[
    'SAFE_ADAPTER_FILES',
    'rm_if_appforge_owned',
    'skip generic project folders',
    'not proven AppForger-created',
]
missing_phrases=[p for p in required_script_phrases if p not in script]
if missing_phrases:
    print('cleanup script missing safety phrases:', missing_phrases); raise SystemExit(1)
for forbidden in ['for p in target.iterdir():', 'rm(p,args.yes)']:
    if forbidden in script:
        print('cleanup script contains broad deletion pattern:', forbidden); raise SystemExit(1)
skill=(root/'skills/cleanup-lifecycle/clean-appforge-from-project/SKILL.md').read_text(encoding='utf-8')
if 'Do not delete generic project folders' not in skill:
    print('cleanup skill missing generic folder safety rule'); raise SystemExit(1)
print("validate_cleanup_command: OK")
