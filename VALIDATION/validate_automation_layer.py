#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    root/'policies/release-delivery/automation-jobs/README.md',
    root/'policies/security-and-privacy/automation-jobs/automation-levels.md',
    root/'templates/jobs/automation/job-definition-template.md',
    root/'skills/automation/create-automation-job/SKILL.md',
]
missing = [str(p.relative_to(root)) for p in required if not p.exists()]
if missing:
    print('Missing automation layer files:')
    print('\n'.join(missing))
    sys.exit(1)
print('Automation layer validation passed.')
