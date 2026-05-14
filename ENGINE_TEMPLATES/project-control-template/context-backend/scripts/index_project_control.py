#!/usr/bin/env python3
"""Index AppForge project-control Markdown into a local JSONL index and optionally Qdrant.

This is a starter script. It defaults to dependency-free local JSONL indexing
using hash_dev embeddings for pipeline validation. Use OpenAI/local/custom
embeddings for real semantic retrieval.
"""
from __future__ import annotations
import argparse, fnmatch, json, os, sys, time
from pathlib import Path
from typing import Dict, Iterable, List

try:
    import yaml
except Exception:
    yaml = None

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.append(str(SCRIPT_DIR))
from embedding_adapters import embed_text

DEFAULT_EXCLUDES = ["**/.env*", "**/*secret*", "**/*token*", "**/node_modules/**", "**/build/**", "**/dist/**", "**/local-only/debug/**"]
DEFAULT_INCLUDE_DIRS = ["."]


def load_config(path: Path) -> Dict:
    if yaml and path.exists():
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {}


def matches_any(path: str, patterns: List[str]) -> bool:
    return any(fnmatch.fnmatch(path, pat) for pat in patterns)


def iter_markdown_files(root: Path, excludes: List[str]) -> Iterable[Path]:
    for p in root.rglob("*.md"):
        rel = p.relative_to(root).as_posix()
        if matches_any(rel, excludes):
            continue
        if "/local-only/" in rel or rel.startswith("local-only/"):
            continue
        yield p


def chunk_text(text: str, max_chars: int = 1800) -> List[str]:
    parts, cur = [], []
    cur_len = 0
    for para in text.split("\n\n"):
        if cur_len + len(para) > max_chars and cur:
            parts.append("\n\n".join(cur))
            cur, cur_len = [], 0
        cur.append(para)
        cur_len += len(para)
    if cur:
        parts.append("\n\n".join(cur))
    return [p.strip() for p in parts if p.strip()]


def infer_artifact_type(path: Path) -> str:
    s = path.as_posix().lower()
    if "baseline" in s: return "baseline"
    if "registry" in s: return "registry"
    if "decision" in s: return "decision"
    if "test" in s: return "test_or_qa"
    if "release" in s: return "release"
    if "codex" in s or "packet" in s: return "packet"
    return "document"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project-control", default=".", help="Path to project-control folder")
    ap.add_argument("--config", default="context-backend/config/context_backend_config.yaml")
    ap.add_argument("--out", default="context-backend/index-reports/local_index.jsonl")
    ap.add_argument("--provider", default=None)
    ap.add_argument("--model", default=None)
    ap.add_argument("--dim", type=int, default=None)
    args = ap.parse_args()

    root = Path(args.project_control).resolve()
    config = load_config(root / args.config)
    cbcfg = config.get("context_backend", {})
    embcfg = config.get("embedding", {})
    idxcfg = config.get("indexing", {})
    provider = args.provider or embcfg.get("provider", "hash_dev")
    model = args.model or embcfg.get("model")
    dim = args.dim or int(embcfg.get("dimension", 384))
    excludes = list(DEFAULT_EXCLUDES) + list(idxcfg.get("excluded_globs", []) or [])

    records = []
    for md in iter_markdown_files(root, excludes):
        rel = md.relative_to(root).as_posix()
        text = md.read_text(encoding="utf-8", errors="ignore")
        for i, chunk in enumerate(chunk_text(text)):
            rec = {
                "id": hashlib_id(rel, i),
                "text": chunk,
                "vector": embed_text(chunk, provider=provider, dim=dim, model=model),
                "payload": {
                    "project_id": cbcfg.get("project_id", root.name),
                    "artifact_id": f"{rel}#chunk-{i}",
                    "artifact_type": infer_artifact_type(md),
                    "source_path": rel,
                    "approval_status": "unknown",
                    "baseline_version": "",
                    "is_current": True,
                    "indexed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "chunk_id": i,
                    "summary": chunk[:240].replace("\n", " ")
                }
            }
            records.append(rec)

    out = root / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"Indexed {len(records)} chunks to {out}")
    print("Note: local JSONL index is for validation. Configure Qdrant upsert separately for shared retrieval.")


def hashlib_id(source: str, chunk: int) -> str:
    import hashlib
    return hashlib.sha256(f"{source}:{chunk}".encode()).hexdigest()

if __name__ == "__main__":
    main()
