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
    "START_HERE/STAGE_WORKFLOW.md",
    "START_HERE/ENGINE_VS_APP_WORKSPACE_BOUNDARIES.md",
    "REGISTRIES/REPO_REGISTRY.md",
    "REGISTRIES/FEATURE_REGISTRY.md",
    "REGISTRIES/API_REGISTRY.md",
    "REGISTRIES/DESIGN_BASELINE_REGISTRY.md",
    "ARTIFACT_PACKETS/FIGMA_BASELINE_PACKET_TEMPLATE.md",
]

missing = [p for p in REQUIRED if not (ROOT / p).exists()]
if missing:
    print("Missing required AppForge files:")
    for p in missing:
        print(f"- {p}")
    sys.exit(1)

print("OK: required AppForge files exist.")
