#!/usr/bin/env python3
from pathlib import Path
import json, sys
root = Path(__file__).resolve().parents[1]
required = [
    'workflows/strategy/integration-strategy-advisor/README.md',
    'workflows/strategy/integration-strategy-advisor/INTEGRATION_STRATEGY_POLICY.md',
    'workflows/strategy/integration-strategy-advisor/CONNECTOR_FIRST_POLICY.md',
    'workflows/strategy/integration-strategy-advisor/CONNECTOR_VS_API_DECISION_TREE.md',
    'workflows/strategy/integration-strategy-advisor/OFFICIAL_CONNECTOR_RESEARCH_POLICY.md',
    'workflows/strategy/integration-strategy-advisor/HYBRID_INTEGRATION_POLICY.md',
    'workflows/strategy/integration-strategy-advisor/CUSTOM_CODE_ITERATION_POLICY.md',
    'skills/integrations/generic/strategy/choose_integration_approach/SKILL.md',
    'skills/integrations/generic/strategy/research_official_connectors/SKILL.md',
    'skills/integrations/generic/strategy/plan_hybrid_integration/SKILL.md',
    'templates/engine/project-control-template/integrations/integration-strategy-registry.yaml',
    'templates/engine/project-control-template/integrations/integration-decision-log.md',
    'templates/engine/project-control-template/integrations/connector-catalog.yaml',
    'templates/engine/project-control-template/integrations/integration-decision-packet.template.md',
    'docs/getting-started/operator-guides/FEATURE_GUIDES/INTEGRATION_STRATEGY_ADVISOR.md',
    'mcp/interface/prompts/choose_integration_approach.md',
]
missing = [p for p in required if not (root/p).exists()]
if missing:
    print('Missing Integration Strategy Advisor paths:')
    for p in missing: print('-', p)
    sys.exit(1)
policy=(root/'workflows/strategy/integration-strategy-advisor/INTEGRATION_STRATEGY_POLICY.md').read_text(encoding='utf-8')
needles=['official connector','custom API/Python','decision packet']
for n in needles:
    if n.lower() not in policy.lower():
        print('Policy missing wording:', n)
        sys.exit(1)
# MCP resource check
m=root/'mcp/MCP_RESOURCE_MAP.json'
if m.exists():
    data=json.loads(m.read_text(encoding='utf-8'))
    ids={r.get('id') for r in data.get('resources',[])}
    for rid in ['integration-strategy-policy','integration-strategy-skill','connector-catalog-template']:
        if rid not in ids:
            print('MCP resource map missing', rid)
            sys.exit(1)
print('validate_integration_strategy_advisor: OK')
