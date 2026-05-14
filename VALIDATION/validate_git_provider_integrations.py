#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['GIT_PROVIDER_INTEGRATIONS/README.md', 'GIT_PROVIDER_INTEGRATIONS/python/git_providers/base_provider.py', 'GIT_PROVIDER_INTEGRATIONS/python/git_providers/bitbucket_provider.py', 'GIT_PROVIDER_INTEGRATIONS/python/git_providers/url_normalizer.py', 'SKILLS/git_provider_skills/sync_bitbucket_code_source/SKILL.md']
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
print("validate_git_provider_integrations: OK")
