from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
engine = root / 'appforger-engine'
required = [
    engine/'runtime/collaboration/team-operations-backend'/'README.md',
    engine/'runtime/collaboration/team-operations-backend'/'TEAM_OPERATIONS_BACKEND_POLICY.md',
    engine/'runtime/collaboration/team-operations-backend'/'TEAM_OPERATIONS_SOURCE_OF_TRUTH_POLICY.md',
    engine/'runtime/collaboration/team-operations-backend'/'TEAM_OPERATIONS_SECRET_METADATA_POLICY.md',
    engine/'templates'/'project-control'/'team-operations-backend'/'schemas'/'postgres_team_operations_schema.sql',
    engine/'templates'/'project-control'/'registries'/'team-operations-backend-registry.md',
]
missing=[str(p.relative_to(root)) for p in required if not p.exists()]
if missing:
    print('Missing required Team Operations Backend files:')
    print('\n'.join(missing))
    sys.exit(1)
print('Team Operations Backend layer validation passed.')
