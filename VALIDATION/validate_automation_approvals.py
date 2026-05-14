#!/usr/bin/env python3
from pathlib import Path
import sys
pc = Path.cwd()/'project-control'
registry = pc/'REGISTRIES/AUTOMATION_APPROVAL_REGISTRY.md'
if not registry.exists():
    print('AUTOMATION_APPROVAL_REGISTRY.md not found; skipping project-level validation.')
    sys.exit(0)
text = registry.read_text(encoding='utf-8')
if 'Approval ID' not in text:
    print('AUTOMATION_APPROVAL_REGISTRY.md is missing expected headings.')
    sys.exit(1)
print('Automation approval registry validation passed.')
