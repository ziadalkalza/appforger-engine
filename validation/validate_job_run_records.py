#!/usr/bin/env python3
from pathlib import Path
import sys
pc = Path.cwd()/'project-control'
registry = pc/'REGISTRIES/JOB_RUN_REGISTRY.md'
if not registry.exists():
    print('JOB_RUN_REGISTRY.md not found; skipping project-level validation.')
    sys.exit(0)
text = registry.read_text(encoding='utf-8')
if 'Run ID' not in text or 'Status' not in text:
    print('JOB_RUN_REGISTRY.md is missing required headings.')
    sys.exit(1)
print('Job run registry validation passed.')
