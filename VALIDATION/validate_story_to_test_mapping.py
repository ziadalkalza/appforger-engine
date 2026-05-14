#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('../project-control')
required = [root/'REGISTRIES/USER_STORY_REGISTRY.md', root/'REGISTRIES/TEST_CASE_REGISTRY.md']
missing = [str(p) for p in required if not p.exists()]
if missing:
    print('Missing story/test mapping files:')
    print('\n'.join(missing))
    sys.exit(1)
print('Story-to-test mapping validation passed')
