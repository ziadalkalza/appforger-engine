from pathlib import Path
import sys
root = Path(__file__).resolve().parents[2]
engine = root / 'appforge-engine'
required = [
    engine/'TEAM_OPERATIONS_BACKEND'/'README.md',
    engine/'TEAM_OPERATIONS_BACKEND'/'TEAM_OPERATIONS_BACKEND_POLICY.md',
    engine/'TEAM_OPERATIONS_BACKEND'/'TEAM_OPERATIONS_SOURCE_OF_TRUTH_POLICY.md',
    engine/'TEAM_OPERATIONS_BACKEND'/'TEAM_OPERATIONS_SECRET_METADATA_POLICY.md',
    engine/'ENGINE_TEMPLATES'/'project-control-template'/'team-operations-backend'/'schemas'/'postgres_team_operations_schema.sql',
    engine/'ENGINE_TEMPLATES'/'project-control-template'/'REGISTRIES'/'TEAM_OPERATIONS_BACKEND_REGISTRY.md',
]
missing=[str(p.relative_to(root)) for p in required if not p.exists()]
if missing:
    print('Missing required Team Operations Backend files:')
    print('\n'.join(missing))
    sys.exit(1)
print('Team Operations Backend layer validation passed.')
