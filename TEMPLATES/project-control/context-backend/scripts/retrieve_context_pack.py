#!/usr/bin/env python3
"""Retrieve a lightweight context pack from the local JSONL index.

This starter retrieves from the dependency-free local index. Qdrant retrieval can
be added using the same metadata rules.
"""
from __future__ import annotations
import argparse, json, math, sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.append(str(SCRIPT_DIR))
from embedding_adapters import embed_text


def cosine(a, b):
    return sum(x*y for x,y in zip(a,b)) / ((math.sqrt(sum(x*x for x in a)) or 1) * (math.sqrt(sum(y*y for y in b)) or 1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--project-control", default=".")
    ap.add_argument("--index", default="context-backend/index-reports/local_index.jsonl")
    ap.add_argument("--out", default="context-backend/retrieval-packs/retrieval_pack.md")
    ap.add_argument("--top-k", type=int, default=8)
    ap.add_argument("--provider", default="hash_dev")
    ap.add_argument("--dim", type=int, default=384)
    args = ap.parse_args()
    root = Path(args.project_control).resolve()
    idx = root / args.index
    if not idx.exists():
        raise SystemExit(f"Index not found: {idx}. Run index_project_control.py first.")
    qv = embed_text(args.query, provider=args.provider, dim=args.dim)
    scored = []
    for line in idx.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        rec = json.loads(line)
        scored.append((cosine(qv, rec["vector"]), rec))
    scored.sort(reverse=True, key=lambda x: x[0])
    out = root / args.out
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"# Retrieval Pack", "", f"Query: `{args.query}`", "", "Retrieved items point back to project-control sources. Do not treat this pack as canonical without checking source files.", ""]
    for rank, (score, rec) in enumerate(scored[:args.top_k], 1):
        p = rec["payload"]
        lines += [f"## {rank}. {p.get('source_path')} (score {score:.3f})", "", f"- artifact_type: {p.get('artifact_type')}", f"- approval_status: {p.get('approval_status')}", f"- is_current: {p.get('is_current')}", f"- indexed_at: {p.get('indexed_at')}", "", rec["text"][:1000], ""]
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote retrieval pack to {out}")

if __name__ == "__main__":
    main()
