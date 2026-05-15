from __future__ import annotations
from pathlib import Path
import json


def load_feature_manifest(engine_root: Path) -> dict:
    path = engine_root / "registries" / "APPFORGE_FEATURE_MANIFEST.json"
    if not path.exists():
        return {"features": [], "error": f"missing {path}"}
    return json.loads(path.read_text(encoding="utf-8"))


def load_resource_map(engine_root: Path) -> dict:
    path = engine_root / "mcp" / "MCP_RESOURCE_MAP.json"
    if not path.exists():
        return {"resources": []}
    return json.loads(path.read_text(encoding="utf-8"))
