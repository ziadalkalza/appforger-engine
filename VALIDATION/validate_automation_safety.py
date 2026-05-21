#!/usr/bin/env python3
from pathlib import Path
import sys
engine=Path(__file__).resolve().parents[1]
text=(engine/'validation/operational-audits/operational-audit/automation-safety-audit.md').read_text(encoding='utf-8').lower()
for term in ['approval required','forbidden silent automation','publish production','waive critical blockers','index secrets']:
 if term not in text:
  print(f'Missing automation safety term: {term}')
  sys.exit(1)
print('Automation safety validation passed.')
