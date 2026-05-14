#!/usr/bin/env python3
from pathlib import Path
import json, sys
root = Path(__file__).resolve().parents[1]
required = [
    'INTEGRATION_STRATEGY_ADVISOR/README.md',
    'INTEGRATION_STRATEGY_ADVISOR/INTEGRATION_STRATEGY_POLICY.md',
    'INTEGRATION_STRATEGY_ADVISOR/CONNECTOR_FIRST_POLICY.md',
    'INTEGRATION_STRATEGY_ADVISOR/CONNECTOR_VS_API_DECISION_TREE.md',
    'INTEGRATION_STRATEGY_ADVISOR/OFFICIAL_CONNECTOR_RESEARCH_POLICY.md',
    'INTEGRATION_STRATEGY_ADVISOR/HYBRID_INTEGRATION_POLICY.md',
    'INTEGRATION_STRATEGY_ADVISOR/CUSTOM_CODE_ITERATION_POLICY.md',
    'SKILLS/integration_strategy_skills/choose_integration_approach/SKILL.md',
    'SKILLS/integration_strategy_skills/research_official_connectors/SKILL.md',
    'SKILLS/integration_strategy_skills/plan_hybrid_integration/SKILL.md',
    'ENGINE_TEMPLATES/project-control-template/integrations/integration-strategy-registry.yaml',
    'ENGINE_TEMPLATES/project-control-template/integrations/integration-decision-log.md',
    'ENGINE_TEMPLATES/project-control-template/integrations/connector-catalog.yaml',
    'ENGINE_TEMPLATES/project-control-template/integrations/integration-decision-packet.template.md',
    'HOW_TO_USE_APPFORGE/FEATURE_GUIDES/INTEGRATION_STRATEGY_ADVISOR.md',
    'APPFORGE_MCP_SERVER/prompts/choose_integration_approach.md',
]
missing = [p for p in required if not (root/p).exists()]
if missing:
    print('Missing Integration Strategy Advisor paths:')
    for p in missing: print('-', p)
    sys.exit(1)
policy=(root/'INTEGRATION_STRATEGY_ADVISOR/INTEGRATION_STRATEGY_POLICY.md').read_text(encoding='utf-8')
needles=['official connector','custom API/Python','decision packet']
for n in needles:
    if n.lower() not in policy.lower():
        print('Policy missing wording:', n)
        sys.exit(1)
# MCP resource check
m=root/'APPFORGE_MCP_SERVER/MCP_RESOURCE_MAP.json'
if m.exists():
    data=json.loads(m.read_text(encoding='utf-8'))
    ids={r.get('id') for r in data.get('resources',[])}
    for rid in ['integration-strategy-policy','integration-strategy-skill','connector-catalog-template']:
        if rid not in ids:
            print('MCP resource map missing', rid)
            sys.exit(1)
print('validate_integration_strategy_advisor: OK')
