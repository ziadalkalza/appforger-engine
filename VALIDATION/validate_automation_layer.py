#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    root/'policies/operations/automation-jobs/README.md',
    root/'policies/operations/automation-jobs/AUTOMATION_LEVELS.md',
    root/'templates/jobs/automation-jobs/JOB_DEFINITION_TEMPLATE.md',
    root/'skills/operations/automation_skills/create_automation_job/SKILL.md',
]
missing = [str(p.relative_to(root)) for p in required if not p.exists()]
if missing:
    print('Missing automation layer files:')
    print('\n'.join(missing))
    sys.exit(1)
print('Automation layer validation passed.')
