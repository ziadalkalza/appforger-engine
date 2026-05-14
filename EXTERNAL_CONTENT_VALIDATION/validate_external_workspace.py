#!/usr/bin/env python3
"""Validate an AppForge external workspace.

The validator checks that app-specific state and selected code folders exist outside the reusable engine.
It is intentionally conservative: it reports missing items and can be used before a stage starts.
"""
from __future__ import annotations
import argparse, json, os, sys
from pathlib import Path

REQUIRED_PROJECT_CONTROL_FILES = [
    "APPFORGE_PROJECT_STATUS.md", "PRODUCT_OVERVIEW.md", "DECISION_LOG.md", "ASSUMPTION_LOG.md", "PENDING_QUESTIONS.md", "APPFORGE_PROJECT.yaml",
    "REGISTRIES/REPO_REGISTRY.md", "REGISTRIES/FEATURE_REGISTRY.md", "REGISTRIES/SCREEN_REGISTRY.md",
    "REGISTRIES/API_REGISTRY.md", "REGISTRIES/DATA_MODEL_REGISTRY.md", "REGISTRIES/CHANGE_REQUEST_REGISTRY.md",
    "REGISTRIES/GENERATED_ARTIFACT_REGISTRY.md", "REGISTRIES/EXTERNAL_DEPENDENCY_REGISTRY.md",
    "ARTIFACT_IMPORTS/IMPORT_INBOX.md", "BASELINES/DESIGN_BASELINE_REGISTRY.md", "BASELINES/API_BASELINE_REGISTRY.md",
    "CODEX_WORK_PACKETS/README.md", "DECISION_SNAPSHOTS/STAGE_SUMMARY.md", "CONTEXT_PACKS/README.md",
]

ROOT_FOLDERS = ["project-control", "design-assets", "exports", "local-only"]
OPTIONAL_CODE_REPOS = ["backend", "ios", "android", "web"]

def check_file(base: Path, rel: str, errors: list[str]):
    if not (base / rel).exists():
        errors.append(f"missing required project-control file: {rel}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", required=True)
    ap.add_argument("--require", default="", help="Comma-separated required folders/repos: backend,ios,android,web")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    ws = Path(args.workspace).resolve()
    required = [x.strip() for x in args.require.split(',') if x.strip()]
    errors, warnings = [], []

    if not ws.exists():
        errors.append(f"workspace does not exist: {ws}")
    for folder in ROOT_FOLDERS:
        if not (ws/folder).exists():
            errors.append(f"missing required workspace folder: {folder}")
    pc = ws/"project-control"
    for rel in REQUIRED_PROJECT_CONTROL_FILES:
        check_file(pc, rel, errors)

    for repo in required:
        path = ws/repo
        if not path.exists():
            errors.append(f"required repo/folder missing: {repo}")
            continue
        if repo in OPTIONAL_CODE_REPOS:
            if not (path/"APPFORGE_POINTER.md").exists():
                errors.append(f"{repo} missing APPFORGE_POINTER.md")
            if not (path/"AGENTS.md").exists():
                warnings.append(f"{repo} missing AGENTS.md")
            if not (path/".git").exists():
                warnings.append(f"{repo} is not a git repo yet")

    result = "pass" if not errors else "fail"
    report = {"workspace": str(ws), "result": result, "errors": errors, "warnings": warnings}
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"External workspace validation: {result.upper()}")
        for e in errors:
            print(f"ERROR: {e}")
        for w in warnings:
            print(f"WARNING: {w}")
    return 0 if not errors else 2

if __name__ == "__main__":
    raise SystemExit(main())
