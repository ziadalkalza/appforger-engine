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
    "docs/project-onboarding/start-here/stage-workflow.md",
    "docs/project-onboarding/start-here/engine-vs-app-workspace-boundaries.md",
    "registries/project-control/repo-registry.md",
    "registries/project-control/feature-registry.md",
    "registries/project-control/api-registry.md",
    "registries/project-control/design-baseline-registry.md",
    "templates/execution-packets/artifact-packets/figma-baseline-packet-template.md",
]

missing = [p for p in REQUIRED if not (ROOT / p).exists()]
if missing:
    print("Missing required AppForge files:")
    for p in missing:
        print(f"- {p}")
    sys.exit(1)

print("OK: required AppForge files exist.")
