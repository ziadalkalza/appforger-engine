#!/usr/bin/env python3
from pathlib import Path
import sys
workspace = Path.cwd()
pc = workspace/'project-control'
registry = pc/'REGISTRIES/AUTOMATED_JOB_REGISTRY.md'
if not registry.exists():
    print('AUTOMATED_JOB_REGISTRY.md not found in project-control. If this is an engine-only validation, use validate_automation_layer.py instead.')
    sys.exit(0)
text = registry.read_text(encoding='utf-8')
if 'Job ID' not in text:
    print('AUTOMATED_JOB_REGISTRY.md does not include expected columns.')
    sys.exit(1)
print('Job registry validation passed.')
