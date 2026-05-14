#!/usr/bin/env python3
from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
required = [
    "CONTEXT_BACKEND/README.md",
    "QDRANT_CONTEXT_PROFILE/QDRANT_SETUP_CHECKLIST.md",
    "SUPABASE_CONTEXT_PROFILE/SUPABASE_CONTEXT_BACKEND_SETUP.md",
    "CONTEXT_SYNC_AND_RETRIEVAL/RETRIEVE_CONTEXT_PACK.md",
    "ENGINE_TEMPLATES/project-control-template/context-backend/scripts/index_project_control.py",
    "ENGINE_TEMPLATES/project-control-template/context-backend/schemas/supabase_context_schema.sql",
    "SKILLS/context_backend_skills/setup_context_backend/SKILL.md",
]
missing = [p for p in required if not (root/p).exists()]
if missing:
    print("Missing context backend layer files:")
    for p in missing: print("-", p)
    sys.exit(1)
print("Context backend layer validation passed.")
