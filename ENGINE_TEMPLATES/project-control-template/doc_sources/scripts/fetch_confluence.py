#!/usr/bin/env python3
import argparse, json, os, re
from pathlib import Path


def load_env(target):
    env = Path(target) / "local-only/.env.local"
    if env.exists():
        for line in env.read_text(encoding="utf-8", errors="ignore").splitlines():
            s = line.strip()
            if not s or s.startswith("#") or "=" not in s:
                continue
            k, v = s.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


def _safe_filename(title):
    return re.sub(r"[^A-Za-z0-9._-]+", "-", str(title)).strip("-") or "confluence-page"


def _pages_from_mock(mock_json, page_id=None):
    raw = json.loads(Path(mock_json).read_text(encoding="utf-8"))
    if isinstance(raw, dict) and "pages" in raw:
        raw = raw["pages"]
    if isinstance(raw, dict):
        raw = [raw]
    pages = []
    for i, item in enumerate(raw or []):
        if not isinstance(item, dict):
            continue
        pid = str(item.get("id") or item.get("page_id") or page_id or i)
        pages.append({
            "id": pid,
            "title": item.get("title") or f"confluence-page-{pid}",
            "body": item.get("body") or item.get("text") or item.get("content") or "",
            "labels": item.get("labels") or [],
            "version": item.get("version"),
            "updated": item.get("updated") or item.get("updated_at"),
            "parent_id": item.get("parent_id"),
        })
    return pages


def _pages_from_live_placeholder(page_id=None, space_key=None):
    # Fetch-only live provider calls are intentionally routed through the provider layer.
    # This command remains safe offline and returns a metadata placeholder when no mock is supplied.
    pid = str(page_id or space_key or "unknown")
    return [{"id": pid, "title": f"confluence-page-{pid}", "body": "", "labels": [], "version": None, "updated": None, "parent_id": None}]


def write_outputs(target, source, page_id, storage_mode, mock_json=None, graph=False, space_key=None):
    target = Path(target)
    pages = _pages_from_mock(mock_json, page_id) if mock_json else _pages_from_live_placeholder(page_id, space_key)
    index_path = target / "project-control/context-backend/local-jsonl/source_index.jsonl"
    log_path = target / "project-control/doc_sources/confluence-fetch-log.md"
    graph_path = target / "project-control/runtime/graph/graph_nodes.jsonl"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    for data in pages:
        pid = str(data.get("id") or page_id or "unknown")
        title = data.get("title") or f"confluence-page-{pid}"
        body = data.get("body") or ""
        md = f"# {title}\n\n{body}\n"
        fname = f"{_safe_filename(title)}__{pid}.md"
        if storage_mode == "docs_mirror":
            out = target / "docs/confluence" / source / fname
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(md, encoding="utf-8")
        elif storage_mode == "exports_snapshot":
            out = target / "exports/confluence" / source / fname
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(md, encoding="utf-8")
        elif storage_mode == "local_only_mirror":
            out = target / "local-only/doc_sources/confluence" / source / fname
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(md, encoding="utf-8")
        if storage_mode != "metadata_only":
            index_path.parent.mkdir(parents=True, exist_ok=True)
            with index_path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps({
                    "source_id": source,
                    "source_type": "confluence",
                    "page_id": pid,
                    "title": title,
                    "labels": data.get("labels", []),
                    "version": data.get("version"),
                    "updated": data.get("updated"),
                    "text": md[:2000],
                    "storage_mode": storage_mode,
                }) + "\n")
        with log_path.open("a", encoding="utf-8") as fh:
            fh.write(f"- fetched {source} page={pid} mode={storage_mode} title={title}\n")
        if graph:
            graph_path.parent.mkdir(parents=True, exist_ok=True)
            with graph_path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps({
                    "id": f"confluence:{source}:{pid}",
                    "type": "ConfluencePage",
                    "title": title,
                    "source_id": source,
                    "parent_id": data.get("parent_id"),
                }) + "\n")
        count += 1
    print(f"fetched {source} pages={count} storage={storage_mode}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", default=".")
    ap.add_argument("--source", required=True)
    ap.add_argument("--page-id")
    ap.add_argument("--include-children", action="store_true")
    ap.add_argument("--space-key")
    ap.add_argument("--storage-mode", default="rag_only", choices=["docs_mirror", "exports_snapshot", "local_only_mirror", "rag_only", "metadata_only"])
    ap.add_argument("--fetch-only", action="store_true")
    ap.add_argument("--mock-json")
    ap.add_argument("--graph", action="store_true")
    args = ap.parse_args()
    load_env(args.target)
    write_outputs(args.target, args.source, args.page_id, args.storage_mode, args.mock_json, args.graph, args.space_key)


if __name__ == "__main__":
    main()
