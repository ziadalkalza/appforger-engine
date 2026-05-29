from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
reg = root/'templates/project-control/REGISTRIES'
required = ['MODEL_PROVIDER_REGISTRY.md','TOOL_PROVIDER_REGISTRY.md','ACTIVE_PROVIDER_REGISTRY.md','PROVIDER_DECISION_REGISTRY.md','PROVIDER_HANDOFF_REGISTRY.md']
missing=[p for p in required if not (reg/p).exists()]
if missing:
    print('Missing provider registries:')
    print('\n'.join(missing))
    sys.exit(1)
print('Provider registry validation passed.')
