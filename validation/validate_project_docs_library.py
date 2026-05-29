#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
engine = root / 'appforger-engine'
checks = [
    engine/'docs/document-management/project-docs-library'/'README.md',
    engine/'templates'/'workspace'/'docs'/'README.md',
    engine/'templates'/'project-control'/'registries'/'document-library-registry.md',
]
missing=[str(p) for p in checks if not p.exists()]
if missing:
    print('Missing docs library files:', *missing, sep='\n- '); sys.exit(1)
print('Project docs library validation passed')
