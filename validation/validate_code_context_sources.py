#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    'workflows/operations/context-sync-retrieval/code-context-sources/README.md',
    'workflows/operations/context-sync-retrieval/code-context-sources/code-context-source-policy.md',
    'workflows/artifact-lifecycle/context-sync-retrieval/code-context-sources/initial-code-context-bootstrap-policy.md',
    'workflows/operations/context-sync-retrieval/code-context-sources/single-private-config-policy.md',
    'templates/project-control/code-sources/code-source-registry.yaml',
    'templates/project-control/code-sources/code-access-policy.yaml',
    'templates/project-control/code-sources/code-source-of-truth-map.yaml',
    'templates/project-control/access-and-secrets/secret-metadata.yaml',
    'templates/workspace/local-only/.env.local.example',
    'templates/project-control/registries/code-source-registry.md',
    'templates/project-control/registries/code-access-registry.md',
    'workflows/product/project-onboarding/questionnaire-schema.yaml',
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('Missing Code Context Sources files:')
    for p in missing:
        print('-', p)
    sys.exit(1)

schema = (ROOT/'workflows/product/project-onboarding/questionnaire-schema.yaml').read_text(encoding='utf-8', errors='ignore')
if 'ongoing_project' not in schema:
    print('Missing mandatory ongoing_project onboarding field')
    sys.exit(1)

private_template = (ROOT/'templates/workspace/local-only/.env.local.example').read_text(encoding='utf-8', errors='ignore')
required_phrases = ['DO NOT COMMIT', 'appforge_can_index_this_file: false', 'code_sources:', 'runtime_env:']
for phrase in required_phrases:
    if phrase not in private_template:
        print(f'Missing phrase in private config template: {phrase}')
        sys.exit(1)

print('validate_code_context_sources: OK')
