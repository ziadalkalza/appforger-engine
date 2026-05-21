#!/usr/bin/env python3
"""Bootstrap a project-control folder outside the AppForge engine.

This script creates app-specific state files and registries. It does not create production app code.
"""
from __future__ import annotations
import argparse, re, textwrap
from pathlib import Path

REGISTRIES = [
    "REPO_REGISTRY.md", "FEATURE_REGISTRY.md", "SCREEN_REGISTRY.md", "API_REGISTRY.md",
    "DATA_MODEL_REGISTRY.md", "CHANGE_REQUEST_REGISTRY.md", "GENERATED_ARTIFACT_REGISTRY.md",
    "EXTERNAL_DEPENDENCY_REGISTRY.md", "TASK_STATUS_REGISTRY.md", "TEST_REGISTRY.md",
]
BASELINES = ["DESIGN_BASELINE_REGISTRY.md", "API_BASELINE_REGISTRY.md", "BACKEND_BASELINE_REGISTRY.md", "FRONTEND_BASELINE_REGISTRY.md"]

def slugify(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "-", name.strip().lower()).strip("-") or "my-app"

def write_once(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(textwrap.dedent(text).strip()+"\n", encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", required=True, help="Workspace root containing project-control")
    ap.add_argument("--name", required=True, help="App/project name")
    ap.add_argument("--mode", default="undecided", help="AppForge mode")
    ap.add_argument("--targets", default="", help="Comma-separated targets: ios,android,web")
    ap.add_argument("--backend", default="undecided", help="supabase|fastapi_postgres|undecided")
    args = ap.parse_args()

    root = Path(args.workspace).resolve()
    pc = root / "project-control"
    slug = slugify(args.name)
    targets = [t.strip() for t in args.targets.split(',') if t.strip()]

    write_once(pc/"README.md", f"""
    # {args.name} Project Control

    This folder contains app-specific AppForge memory, registries, baselines, packets, and summaries.
    It is separate from the reusable AppForge engine and separate from production code repos.
    """)
    write_once(pc/"APPFORGE_PROJECT_STATUS.md", f"""
    # Project State

    Project: {args.name}
    Slug: {slug}
    Current stage: ideation
    Mode: {args.mode}
    Targets: {', '.join(targets) if targets else 'undecided'}
    Backend: {args.backend}

    ## Current status

    Not started.

    ## Next action

    Run the AppForge new app wizard and complete product requirements.
    """)
    write_once(pc/"PRODUCT_OVERVIEW.md", f"# Product Brief\n\nProject: {args.name}\n\n")
    write_once(pc/"DECISION_LOG.md", "# Decisions\n\n| ID | Decision | Status | Date | Notes |\n|---|---|---|---|---|\n")
    write_once(pc/"ASSUMPTION_LOG.md", "# Assumptions\n\n| ID | Assumption | Risk | Validation |\n|---|---|---|---|\n")
    write_once(pc/"PENDING_QUESTIONS.md", "# Open Questions\n\n| ID | Question | Owner | Status |\n|---|---|---|---|\n")
    yaml = f"""
    engine: AppForge
    project_name: {args.name!r}
    slug: {slug!r}
    current_stage: ideation
    app_mode: {args.mode!r}
    target_platforms:
      ios: {'ios' in targets}
      android: {'android' in targets}
      web: {'web' in targets}
    backend:
      selected_stack: {args.backend!r}
      status: not_started
    design:
      figma_file: ''
      approved_baseline: ''
    workspace:
      appforge_engine: ../appforger-engine
      project_control: .
      backend: ../backend
      ios: ../ios
      android: ../android
      web: ../web
      design_assets: ../design-assets
      exports: ../exports
      local_only: ../local-only
    """
    write_once(pc/"APPFORGE_PROJECT.yaml", yaml)

    for r in REGISTRIES:
        write_once(pc/"registries"/r, f"# {r.replace('_',' ').replace('.md','').title()}\n\n")
    for b in BASELINES:
        write_once(pc/"registries/baselines"/b, f"# {b.replace('_',' ').replace('.md','').title()}\n\n")
    write_once(pc/"workflows/operations/artifact-imports"/"IMPORT_INBOX.md", "# Import Inbox\n\nUse this to register incoming Figma, image, code, QA, and backend artifacts before approval.\n")
    write_once(pc/"templates/packets/code-agent-packets"/"README.md", "# Codex Work Packets\n\nGenerated Codex task packets for this app live here.\n")
    write_once(pc/"registries/decision-snapshots"/"STAGE_SUMMARY.md", "# Stage Summary\n\nKeep a compact summary of the current stage here.\n")
    write_once(pc/"CONTEXT_PACKS"/"README.md", "# Context Packs\n\nRole and task-specific context packs for token-efficient sessions live here.\n")
    print(f"Project-control bootstrapped at {pc}")

if __name__ == "__main__":
    main()
