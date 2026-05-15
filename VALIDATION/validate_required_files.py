#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "AGENTS.md",
    "APPFORGE_PROJECT_STATUS.md",
    "DECISION_LOG.md",
    "PENDING_QUESTIONS.md",
    "docs/getting-started/start-here/STAGE_WORKFLOW.md",
    "docs/getting-started/start-here/ENGINE_VS_APP_WORKSPACE_BOUNDARIES.md",
    "registries/REPO_REGISTRY.md",
    "registries/FEATURE_REGISTRY.md",
    "registries/API_REGISTRY.md",
    "registries/DESIGN_BASELINE_REGISTRY.md",
    "templates/packets/artifact-packets/FIGMA_BASELINE_PACKET_TEMPLATE.md",
]

missing = [p for p in REQUIRED if not (ROOT / p).exists()]
if missing:
    print("Missing required AppForge files:")
    for p in missing:
        print(f"- {p}")
    sys.exit(1)

print("OK: required AppForge files exist.")
