#!/usr/bin/env python3
from pathlib import Path
root=Path(__file__).resolve().parents[1]
required=['integrations/source-control/generic/README.md', 'integrations/source-control/generic/python/git_providers/base_provider.py', 'integrations/source-control/bitbucket/python/git_providers/bitbucket_provider.py', 'integrations/source-control/generic/python/git_providers/url_normalizer.py', 'skills/integrations/apps/bitbucket/sync_code_source/SKILL.md']
missing=[r for r in required if not (root/r).exists()]
if missing:
    print("missing:", missing); raise SystemExit(1)
print("validate_git_provider_integrations: OK")
