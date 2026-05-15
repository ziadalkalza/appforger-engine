#!/usr/bin/env python3
from pathlib import Path
import json, sys
root = Path(__file__).resolve().parents[1]
manifest = json.loads((root/'registries/APPFORGE_FEATURE_MANIFEST.json').read_text(encoding='utf-8'))
missing=[]
for feature in manifest.get('features',[]):
    for rel in feature.get('required_paths',[]):
        if not (root/rel).exists():
            missing.append((feature.get('id'), rel))
if missing:
    print('Missing manifest-required files:')
    for fid, rel in missing:
        print(f'- {fid}: {rel}')
    sys.exit(1)
print('validate_feature_manifest: OK')
