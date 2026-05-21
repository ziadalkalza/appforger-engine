from __future__ import annotations
from pathlib import Path
from typing import Iterable
from manifest_loader import load_resource_map


class ResourceProvider:
    def __init__(self, engine_root: Path):
        self.engine_root = engine_root
        self.map = load_resource_map(engine_root)

    def list_resources(self) -> list[dict]:
        out = []
        for r in self.map.get("resources", []):
            p = self.engine_root / r["path"]
            if p.exists() or r.get("optional"):
                out.append({
                    "uri": r["uri"],
                    "name": r.get("id", r["uri"]),
                    "mimeType": r.get("mime_type", "text/plain"),
                    "description": r.get("description", r.get("path", ""))
                })
        return out

    def read_resource(self, uri: str) -> dict:
        for r in self.map.get("resources", []):
            if r["uri"] == uri:
                p = self.engine_root / r["path"]
                if not p.exists():
                    raise FileNotFoundError(f"Resource path missing: {r['path']}")
                return {"uri": uri, "mimeType": r.get("mime_type", "text/plain"), "text": p.read_text(encoding="utf-8", errors="replace")}
        raise KeyError(f"Unknown AppForger resource URI: {uri}")

    def search(self, query: str, limit: int = 20) -> list[dict]:
        q = (query or "").lower().strip()
        results = []
        if not q:
            return results
        for r in self.map.get("resources", []):
            p = self.engine_root / r["path"]
            if not p.exists():
                continue
            text = p.read_text(encoding="utf-8", errors="replace")
            hay = (r.get("id", "") + " " + r.get("uri", "") + " " + text[:20000]).lower()
            if q in hay:
                results.append({"uri": r["uri"], "name": r.get("id", r["uri"]), "path": r["path"]})
            if len(results) >= limit:
                break
        return results
