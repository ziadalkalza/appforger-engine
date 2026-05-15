#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
engine = root / 'appforge-engine'
checks = [
    engine/'docs/document-management/project-docs-library'/'README.md',
    engine/'templates/engine'/'workspace-template'/'docs'/'README.md',
    engine/'templates/engine'/'project-control-template'/'registries'/'DOCUMENT_LIBRARY_REGISTRY.md',
]
missing=[str(p) for p in checks if not p.exists()]
if missing:
    print('Missing docs library files:', *missing, sep='\n- '); sys.exit(1)
print('Project docs library validation passed')
