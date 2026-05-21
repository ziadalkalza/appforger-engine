#!/usr/bin/env python3
"""Create an AppForger project workspace from engine templates.

The distributed AppForger zip is engine-only. This initializer expands the
engine templates into project-specific workspace folders outside appforger-engine.

Examples:
  # Web app with backend
  python appforger-engine/workflows/operations/new-app-initializer/create_new_app.py \
    --name "My Web App" --target ./my-app-workspace --app-type web --backend supabase

  # Generic mobile / Flutter app
  python appforger-engine/workflows/operations/new-app-initializer/create_new_app.py \
    --name "My Mobile App" --target ./my-app-workspace --app-type mobile --mobile-strategy generic --backend none

  # Native iOS + Android app with backend
  python appforger-engine/workflows/operations/new-app-initializer/create_new_app.py \
    --name "My Native App" --target ./my-app-workspace --app-type mobile --mobile-strategy native_both --backend fastapi_postgres

  # Backend-only project
  python appforger-engine/workflows/operations/new-app-initializer/create_new_app.py \
    --name "My API" --target ./my-api-workspace --app-type backend_only --backend fastapi_postgres
"""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "app"


def copytree_contents(src: Path, dst: Path) -> None:
    if not src.exists():
        raise FileNotFoundError(f"Template folder not found: {src}")
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        target = dst / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)


def add_common_workspace_dirs(target: Path, include_design_assets: bool, include_local_only: bool) -> None:
    common_dirs = [
        "docs/meeting-notes",
        "docs/product",
        "docs/design",
        "docs/backend",
        "docs/frontend",
        "docs/qa",
        "docs/release",
        "docs/legal-privacy",
        "docs/research",
        "docs/external",
        "docs/imports",
        "docs/summaries",
        "docs/archive",
        "assets",
        "exports/figma",
        "exports/screenshots",
        "exports/qa",
        "exports/reports",
        "exports/sandbox-reports",
    ]
    if include_design_assets:
        common_dirs.extend([
            "assets/design/approved",
            "assets/design/pending",
            "assets/design/archived",
        ])
    if include_local_only:
        common_dirs.append("local-only")
    for d in common_dirs:
        (target / d).mkdir(parents=True, exist_ok=True)
    if include_local_only:
        (target / "local-only/.appforge-created").write_text("Created by AppForger setup.\n", encoding="utf-8")


def resolve_implementation_dirs(app_type: str, mobile_strategy: str, backend: str, include_web: bool, include_ios: bool, include_android: bool, include_mobile: bool) -> set[str]:
    """Return implementation folders that should exist for this project.

    Shared folders are created separately. This function only controls actual
    implementation tracks: backend, web, mobile, ios, android.
    """
    dirs: set[str] = set()

    # Backend exists only when explicitly needed/selected or when app_type is backend_only.
    if app_type == "backend_only" or backend not in {"none", "no", "backendless"}:
        dirs.add("backend")

    if app_type in {"web", "both", "multi"} or include_web:
        dirs.add("web")

    if app_type in {"mobile", "both", "multi"} or include_mobile or include_ios or include_android:
        if mobile_strategy in {"generic", "flutter", "react_native", "cross_platform"} or include_mobile:
            dirs.add("mobile")
        elif mobile_strategy == "ios" or include_ios:
            dirs.add("ios")
        elif mobile_strategy == "android" or include_android:
            dirs.add("android")
        elif mobile_strategy in {"native_both", "separate_native", "parallel_native"}:
            dirs.update({"ios", "android"})
        elif mobile_strategy == "none":
            pass
        else:
            # Safe generic mobile default when app_type says mobile but strategy is undecided.
            dirs.add("mobile")

    # Direct flags always add their track.
    if include_ios:
        dirs.add("ios")
    if include_android:
        dirs.add("android")
    if include_web:
        dirs.add("web")
    if include_mobile:
        dirs.add("mobile")

    return dirs


def patch_yaml(path: Path, replacements: dict[str, str]) -> None:
    text = path.read_text(encoding="utf-8")
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--target", required=True)
    ap.add_argument("--app-type", default="unknown", choices=["web", "mobile", "both", "multi", "backend_only", "unknown"])
    ap.add_argument("--mobile-strategy", default="generic", choices=["generic", "flutter", "react_native", "cross_platform", "ios", "android", "native_both", "separate_native", "parallel_native", "none"])
    ap.add_argument("--backend", default="undecided", help="none | supabase | fastapi_postgres | existing | undecided")
    # Backward-compatible optional flags.
    ap.add_argument("--mode", default="standard")
    ap.add_argument("--include-web", action="store_true")
    ap.add_argument("--include-ios", action="store_true")
    ap.add_argument("--include-android", action="store_true")
    ap.add_argument("--include-mobile", action="store_true")
    ap.add_argument("--include-assets", action="store_true")
    ap.add_argument("--include-design-assets", action="store_true")
    ap.add_argument("--include-local-only", action="store_true")
    args = ap.parse_args()

    engine = Path(__file__).resolve().parents[3]
    target = Path(args.target).resolve()
    target.mkdir(parents=True, exist_ok=True)

    templates = engine / "templates"
    copytree_contents(templates / "project-control", target / "project-control")
    add_common_workspace_dirs(target, args.include_design_assets, args.include_local_only)

    impl_dirs = resolve_implementation_dirs(
        args.app_type,
        args.mobile_strategy,
        args.backend,
        args.include_web,
        args.include_ios,
        args.include_android,
        args.include_mobile,
    )
    for d in sorted(impl_dirs):
        (target / d).mkdir(parents=True, exist_ok=True)

    slug = slugify(args.name)
    pc = target / "project-control"
    (pc / "APPFORGE_PROJECT_STATUS.md").write_text(
        f"# APPFORGE_PROJECT_STATUS\n\n"
        f"Project name: {args.name}\n"
        f"Slug: {slug}\n"
        f"Current stage: onboarding\n"
        f"App type: {args.app_type}\n"
        f"Mobile strategy: {args.mobile_strategy}\n"
        f"Backend: {args.backend}\n"
        f"Generated implementation folders: {', '.join(sorted(impl_dirs)) or 'none'}\n"
        f"Next recommended action: Complete AppForger onboarding and generate active project rules.\n",
        encoding="utf-8",
    )

    y = pc / "APPFORGE_PROJECT.yaml"
    if y.exists():
        patch_yaml(
            y,
            {
                "project_name: TBD": f"project_name: {args.name}",
                "app_mode: TBD": f"app_mode: {args.mode}",
                "  mobile: false": f"  mobile: {str(any(x in impl_dirs for x in ['mobile','ios','android'])).lower()}",
                "  web: false": f"  web: {str('web' in impl_dirs).lower()}",
                "  backend: false": f"  backend: {str('backend' in impl_dirs).lower()}",
                "  app_type: TBD": f"  app_type: {args.app_type}",
                "  backend_needed: TBD": f"  backend_needed: {'no' if 'backend' not in impl_dirs else 'yes'}",
            },
        )

    (target / "README.md").write_text(
        f"# {args.name} Workspace\n\n"
        f"Created from the AppForger v1 engine-only package.\n\n"
        f"The reusable engine lives in `appforger-engine/`. Project-specific state lives in `project-control/`.\n\n"
        f"Generated implementation folders: `{', '.join(sorted(impl_dirs)) or 'none'}`.\n\n"
        f"Shared folders: `docs/`, `exports/`"
        f", `assets/`"
        f"{', `assets/design/`' if args.include_design_assets else ''}"
        f"{', `local-only/`' if args.include_local_only else ''}.\n",
        encoding="utf-8",
    )

    print(f"Created AppForger workspace at {target}")
    print("Implementation folders:", ", ".join(sorted(impl_dirs)) or "none")


if __name__ == "__main__":
    main()
