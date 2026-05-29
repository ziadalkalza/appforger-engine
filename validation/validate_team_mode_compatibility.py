#!/usr/bin/env python3
from pathlib import Path
import sys
engine=Path(__file__).resolve().parents[1]
text=(engine/'validation/operational-audits/operational-audit/team-mode-audit.md').read_text(encoding='utf-8').lower()
for term in ['inactive until team members are added','single-user','named approvers','project-control changes should go through prs']:
 if term not in text:
  print(f'Missing team mode term: {term}')
  sys.exit(1)
print('Team mode compatibility validation passed.')
