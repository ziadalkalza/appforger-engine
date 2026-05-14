#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[2]
engine = root / 'appforge-engine'
checks = [
    engine/'PROJECT_DOCS_LIBRARY'/'README.md',
    engine/'ENGINE_TEMPLATES'/'workspace-template'/'docs'/'README.md',
    engine/'ENGINE_TEMPLATES'/'project-control-template'/'REGISTRIES'/'DOCUMENT_LIBRARY_REGISTRY.md',
]
missing=[str(p) for p in checks if not p.exists()]
if missing:
    print('Missing docs library files:', *missing, sep='\n- '); sys.exit(1)
print('Project docs library validation passed')
