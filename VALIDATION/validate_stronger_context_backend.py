#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[2]
engine=root/'appforge-engine'
checks=[
 engine/'CONTEXT_BACKEND'/'LOCAL_JSONL_CONTEXT_PROFILE.md',
 engine/'CONTEXT_BACKEND'/'CONTEXT_METADATA_SCHEMA.md',
 engine/'CONTEXT_BACKEND'/'CODE_CONTEXT_INDEXING_POLICY.md',
 engine/'CONTEXT_BACKEND'/'TREE_SITTER_CODE_INDEXING_GUIDE.md',
 engine/'ENGINE_TEMPLATES'/'project-control-template'/'context-backend'/'scripts'/'build_local_jsonl_index.py',
 engine/'ENGINE_TEMPLATES'/'project-control-template'/'context-backend'/'scripts'/'retrieve_local_jsonl_context.py',
]
missing=[str(p) for p in checks if not p.exists()]
if missing:
    print('Missing stronger context backend files:', *missing, sep='\n- '); sys.exit(1)
print('Stronger context backend validation passed')
