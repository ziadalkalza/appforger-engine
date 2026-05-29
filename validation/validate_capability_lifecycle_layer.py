#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
required = [
 'policies/provider-adapters/connector-mcp-skill-lifecycle/lifecycle-status-model.md',
 'ai-models/chatgpt/policies/connector-mcp-skill-lifecycle/skill-lifecycle-policy.md',
 'policies/source-control/github/connector-mcp-skill-lifecycle/mcp-lifecycle-policy.md',
 'integrations/backend-platforms/supabase/policies/connector-mcp-skill-lifecycle/connector-lifecycle-policy.md',
 'registries/project-control/connector-lifecycle-registry.md',
 'registries/project-control/mcp-lifecycle-registry.md',
 'registries/project-control/skill-lifecycle-registry.md',
]
missing=[p for p in required if not (ROOT/p).exists()]
if missing:
 print('Capability lifecycle missing files:')
 for p in missing: print('-', p)
 sys.exit(1)
print('Capability lifecycle validation passed.')
