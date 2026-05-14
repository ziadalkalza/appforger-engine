#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    root/'AUTOMATION_AND_JOB_POLICY/README.md',
    root/'AUTOMATION_AND_JOB_POLICY/AUTOMATION_LEVELS.md',
    root/'AUTOMATION_JOB_TEMPLATES/JOB_DEFINITION_TEMPLATE.md',
    root/'SKILLS/automation_skills/create_automation_job/SKILL.md',
]
missing = [str(p.relative_to(root)) for p in required if not p.exists()]
if missing:
    print('Missing automation layer files:')
    print('\n'.join(missing))
    sys.exit(1)
print('Automation layer validation passed.')
