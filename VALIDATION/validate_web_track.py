from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'workflows/web-implementation/web-frontend/README.md',
    'workflows/backend-implementation/web-frontend/web-stack-selection.md',
    'integrations/design/figma/to-web/figma-to-react-mapping.md',
    'workflows/release-delivery/delivery/web-deployment/README.md',
    'validation/quality-assurance/web-qa/playwright-workflow.md',
    'skills/web-implementation/select-web-stack/SKILL.md',
    'ai-models/codex/templates/code-agent-packets/codex-web-packet-template.md',
    'registries/project-control/web-route-registry.md',
]
missing = [p for p in REQUIRED if not (ROOT / p).exists()]
if missing:
    print('Missing web track files:')
    for p in missing:
        print('-', p)
    raise SystemExit(1)
print('AppForge web track validation passed.')
