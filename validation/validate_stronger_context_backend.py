#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[1]
engine=root/'appforger-engine'
checks=[
 engine/'runtime/context/context-backend'/'LOCAL_JSONL_CONTEXT_PROFILE.md',
 engine/'runtime/context/context-backend'/'CONTEXT_METADATA_SCHEMA.md',
 engine/'runtime/context/context-backend'/'CODE_CONTEXT_INDEXING_POLICY.md',
 engine/'runtime/context/context-backend'/'TREE_SITTER_CODE_INDEXING_GUIDE.md',
 engine/'templates'/'project-control'/'context-backend'/'scripts'/'build_local_jsonl_index.py',
 engine/'templates'/'project-control'/'context-backend'/'scripts'/'retrieve_local_jsonl_context.py',
]
missing=[str(p) for p in checks if not p.exists()]
if missing:
    print('Missing stronger context backend files:', *missing, sep='\n- '); sys.exit(1)
print('Stronger context backend validation passed')
