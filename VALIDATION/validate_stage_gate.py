#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
state = (ROOT / "APPFORGE_PROJECT_STATUS.md").read_text(encoding="utf-8", errors="ignore").lower()

def has_text(path, needles):
    p = ROOT / path
    if not p.exists():
        return False
    t = p.read_text(encoding="utf-8", errors="ignore").lower()
    return any(n.lower() in t for n in needles)

errors = []

if "frontend" in state or "native" in state:
    if not has_text("registries/DESIGN_BASELINE_REGISTRY.md", ["approved", "baseline"]):
        errors.append("Frontend stage requires an approved design baseline.")
    if not has_text("registries/API_REGISTRY.md", ["approved", "contract", "endpoint"]):
        errors.append("Frontend stage requires an API contract or an explicit UI-only exception.")

if "backend" in state:
    if not has_text("workflows/implementation/backend/generic/backend_stack_selection.md", ["supabase", "fastapi", "postgres"]):
        errors.append("Backend stage requires backend stack selection.")

if errors:
    print("Stage gate validation failed:")
    for e in errors:
        print("-", e)
    sys.exit(1)

print("OK: no obvious stage gate conflicts found.")
