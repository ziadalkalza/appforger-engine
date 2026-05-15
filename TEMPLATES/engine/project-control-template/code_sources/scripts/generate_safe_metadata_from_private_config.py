#!/usr/bin/env python3
"""Generate safe AppForge code/access metadata from local-only/.env.local.

This script intentionally writes metadata and references only. It must not print or persist secret values.
Requires PyYAML: pip install pyyaml
"""
from __future__ import annotations
from pathlib import Path
import sys

try:
    import yaml
except Exception as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required for this helper: pip install pyyaml") from exc

PROJECT_CONTROL = Path.cwd()
WORKSPACE = PROJECT_CONTROL.parent
PRIVATE_CONFIG = WORKSPACE / "local-only" / ".env.local"

if not PRIVATE_CONFIG.exists():
    raise SystemExit(f"Missing private config: {PRIVATE_CONFIG}")

cfg = yaml.safe_load(PRIVATE_CONFIG.read_text(encoding="utf-8")) or {}
if cfg.get("rules", {}).get("appforge_can_index_this_file") is True:
    raise SystemExit("Private config must not be indexable. Set appforge_can_index_this_file: false")

out_code = PROJECT_CONTROL / "code_sources"
out_secrets = PROJECT_CONTROL / "access_and_secrets"
out_code.mkdir(parents=True, exist_ok=True)
out_secrets.mkdir(parents=True, exist_ok=True)

code_sources = []
for sid, src in (cfg.get("code_sources") or {}).items():
    code_sources.append({
        "id": sid,
        "role": src.get("role"),
        "canonical": bool(src.get("canonical", False)),
        "location": {
            "mode": src.get("location_mode"),
            "provider": src.get("provider"),
            "repo_url": src.get("repo_url"),
            "branch": src.get("branch"),
            "local_path": src.get("local_path"),
        },
        "access": {
            "auth_reference": src.get("auth_reference"),
            "secrets_stored_here": False,
            "current_user_access": src.get("access_level_for_current_user"),
        },
        "indexing": {
            "summary_indexing": True,
            "raw_code_indexing": bool(src.get("raw_code_indexing", False)),
            "requires_raw_code_indexing_approval": True,
        },
        "sync": {
            "mode": src.get("sync_mode", "manual"),
            "last_indexed_at": None,
        },
    })

(out_code / "code-source-registry.yaml").write_text(
    yaml.safe_dump({"code_sources": code_sources}, sort_keys=False), encoding="utf-8"
)

secrets = []
for area, env in (cfg.get("runtime_env") or {}).items():
    for name, meta in (env.get("variables") or {}).items():
        secrets.append({
            "id": f"{area}_{name}",
            "display_name": name,
            "type": "runtime_env",
            "required_for": [f"{area}_runtime"],
            "stored_in": {
                "location_type": "local_env_file",
                "location_name": env.get("local_env_file"),
                "value_stored_in_appforge": False,
            },
            "owner_role": "admin" if area == "backend" else "frontend_mobile_developer",
            "status": "configured_locally" if meta.get("value") else "not_configured",
        })

(out_secrets / "secret-metadata.yaml").write_text(
    yaml.safe_dump({"secrets": secrets}, sort_keys=False), encoding="utf-8"
)

print("Generated safe metadata only. Secret values were not written to project-control.")
