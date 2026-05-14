#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    'CONTEXT_SYNC_AND_RETRIEVAL/code_context_sources/README.md',
    'CONTEXT_SYNC_AND_RETRIEVAL/code_context_sources/CODE_CONTEXT_SOURCE_POLICY.md',
    'CONTEXT_SYNC_AND_RETRIEVAL/code_context_sources/INITIAL_CODE_CONTEXT_BOOTSTRAP_POLICY.md',
    'CONTEXT_SYNC_AND_RETRIEVAL/code_context_sources/SINGLE_PRIVATE_CONFIG_POLICY.md',
    'ENGINE_TEMPLATES/project-control-template/code_sources/code-source-registry.yaml',
    'ENGINE_TEMPLATES/project-control-template/code_sources/code-access-policy.yaml',
    'ENGINE_TEMPLATES/project-control-template/code_sources/code-source-of-truth-map.yaml',
    'ENGINE_TEMPLATES/project-control-template/access_and_secrets/secret-metadata.yaml',
    'ENGINE_TEMPLATES/workspace-template/local-only/.env.local.example',
    'ENGINE_TEMPLATES/project-control-template/REGISTRIES/CODE_SOURCE_REGISTRY.md',
    'ENGINE_TEMPLATES/project-control-template/REGISTRIES/CODE_ACCESS_REGISTRY.md',
    'PROJECT_ONBOARDING_AND_INITIALIZATION/questionnaire_schema.yaml',
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('Missing Code Context Sources files:')
    for p in missing:
        print('-', p)
    sys.exit(1)

schema = (ROOT/'PROJECT_ONBOARDING_AND_INITIALIZATION/questionnaire_schema.yaml').read_text(encoding='utf-8', errors='ignore')
if 'ongoing_project' not in schema:
    print('Missing mandatory ongoing_project onboarding field')
    sys.exit(1)

private_template = (ROOT/'ENGINE_TEMPLATES/workspace-template/local-only/.env.local.example').read_text(encoding='utf-8', errors='ignore')
required_phrases = ['DO NOT COMMIT', 'appforge_can_index_this_file: false', 'code_sources:', 'runtime_env:']
for phrase in required_phrases:
    if phrase not in private_template:
        print(f'Missing phrase in private config template: {phrase}')
        sys.exit(1)

print('validate_code_context_sources: OK')
