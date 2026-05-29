#!/usr/bin/env python3
"""AppForger runtime manager.

Supports local Docker services and cloud endpoint validation for AppForger-specific storage units:
Postgres/SQL, Qdrant/vector, and Neo4j/graph.
"""
import argparse
import os
import socket
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path


def load_env(path: Path):
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip())


def env_file(target):
    return Path(target) / "local-only/.env.local"


def compose_file(target):
    return Path(target) / "project-control/runtime/docker/docker-compose.appforge-runtime.yml"


def runtime_report(target, name):
    p = Path(target) / "project-control/runtime/cloud" / name
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def init_local_env(target):
    local = Path(target) / "local-only"
    local.mkdir(parents=True, exist_ok=True)
    dst = local / ".env.local"
    if dst.exists():
        print(f"exists: {dst}")
        return
    example = local / ".env.local.example"
    if example.exists():
        dst.write_text(example.read_text(encoding="utf-8"), encoding="utf-8")
    else:
        dst.write_text("POSTGRES_URL=\nQDRANT_URL=http://localhost:6333\nQDRANT_API_KEY=\nNEO4J_URI=bolt://localhost:7687\n", encoding="utf-8")
    print(f"created: {dst}")


def run_compose(target, args):
    load_env(env_file(target))
    cf = compose_file(target)
    if not cf.exists():
        raise SystemExit(f"Missing compose file: {cf}")
    cmd = ["docker", "compose", "-f", str(cf)]
    for p in args.profiles.split(","):
        if p.strip():
            cmd += ["--profile", p.strip()]
    cmd += [args.action]
    if args.action == "up":
        cmd += ["-d"]
    print(" ".join(cmd))
    if not args.dry_run:
        raise SystemExit(subprocess.call(cmd))


def check_socket(name, host, port, timeout=2.0):
    s = socket.socket()
    s.settimeout(timeout)
    try:
        s.connect((host, int(port)))
        return True, f"{name}: OK {host}:{port}"
    except Exception as e:
        return False, f"{name}: FAIL {host}:{port} ({e})"
    finally:
        s.close()


def local_health(target, profiles):
    load_env(env_file(target))
    checks = []
    if "postgres" in profiles:
        checks.append(("postgres", "127.0.0.1", os.getenv("APPFORGE_POSTGRES_PORT", "55432")))
    if "qdrant" in profiles:
        checks.append(("qdrant", "127.0.0.1", os.getenv("APPFORGE_QDRANT_PORT", "6333")))
    if "neo4j" in profiles:
        checks.append(("neo4j", "127.0.0.1", os.getenv("APPFORGE_NEO4J_BOLT_PORT", "7687")))
    ok = True
    lines = []
    for name, host, port in checks:
        passed, msg = check_socket(name, host, port)
        ok = ok and passed
        print(msg)
        lines.append(msg)
    (Path(target) / "project-control/runtime/runtime-status.md").parent.mkdir(parents=True, exist_ok=True)
    (Path(target) / "project-control/runtime/runtime-status.md").write_text("# Runtime Status\n\n" + "\n".join(lines) + "\n", encoding="utf-8")
    raise SystemExit(0 if ok else 1)


def validate_cloud(target, profiles):
    load_env(env_file(target))
    ok = True
    lines = ["# Cloud Runtime Health Report", ""]
    profiles = set(profiles)
    if "postgres" in profiles:
        url = os.getenv("POSTGRES_URL", "")
        if url:
            parsed = urllib.parse.urlparse(url)
            status = "OK parseable" if parsed.scheme and parsed.hostname else "FAIL unparseable"
            if "FAIL" in status: ok = False
            lines.append(f"- postgres: {status} host={parsed.hostname or '?'}")
        else:
            ok = False; lines.append("- postgres: FAIL missing POSTGRES_URL")
    if "qdrant" in profiles:
        url = os.getenv("QDRANT_URL", "")
        if not url:
            ok = False; lines.append("- qdrant: FAIL missing QDRANT_URL")
        else:
            try:
                req = urllib.request.Request(url.rstrip("/") + "/collections", headers={"api-key": os.getenv("QDRANT_API_KEY", "")})
                with urllib.request.urlopen(req, timeout=4) as r:
                    lines.append(f"- qdrant: OK HTTP {r.status}")
            except Exception as e:
                ok = False; lines.append(f"- qdrant: FAIL {e}")
    if "neo4j" in profiles:
        uri = os.getenv("NEO4J_URI", "")
        if not uri:
            ok = False; lines.append("- neo4j: FAIL missing NEO4J_URI")
        else:
            parsed = urllib.parse.urlparse(uri)
            host = parsed.hostname or "localhost"
            port = parsed.port or (7687 if parsed.scheme.startswith("bolt") else 7474)
            passed, msg = check_socket("neo4j", host, port)
            ok = ok and passed
            lines.append("- " + msg)
    out = runtime_report(target, "cloud-runtime-health-report.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    raise SystemExit(0 if ok else 1)


def init_cloud_schema(target, profiles, approved=False):
    if not approved:
        raise SystemExit("Refusing cloud initialization without --approved. This may create schemas/collections/constraints.")
    load_env(env_file(target))
    lines = ["# Cloud Runtime Initialization Report", "", "This command records the intended initialization steps."]
    profiles = set(profiles)
    if "postgres" in profiles:
        lines.append("- postgres: apply project-control/runtime/sql/*.sql using the configured POSTGRES_URL.")
    if "qdrant" in profiles:
        lines.append("- qdrant: ensure collections appforge_docs, appforge_code, appforge_confluence, appforge_mixed_context exist.")
    if "neo4j" in profiles:
        lines.append("- neo4j: apply project-control/runtime/cloud/neo4j-constraints.cypher.")
    out = runtime_report(target, "cloud-runtime-init-report.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--target", default=".")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init-local-env")
    for c in ["up", "down", "ps"]:
        sp = sub.add_parser(c)
        sp.set_defaults(action=c)
        sp.add_argument("--profiles", default="postgres,qdrant")
        sp.add_argument("--dry-run", action="store_true")
    hp = sub.add_parser("health")
    hp.add_argument("--profiles", default="postgres,qdrant")
    vc = sub.add_parser("validate-cloud")
    vc.add_argument("--profiles", default="postgres,qdrant,neo4j")
    ic = sub.add_parser("init-cloud-schema")
    ic.add_argument("--profiles", default="postgres,qdrant,neo4j")
    ic.add_argument("--approved", action="store_true")
    args = ap.parse_args()
    if args.cmd == "init-local-env": init_local_env(args.target)
    elif args.cmd == "health": local_health(args.target, set(args.profiles.split(",")))
    elif args.cmd == "validate-cloud": validate_cloud(args.target, set(args.profiles.split(",")))
    elif args.cmd == "init-cloud-schema": init_cloud_schema(args.target, set(args.profiles.split(",")), args.approved)
    else: run_compose(args.target, args)


if __name__ == "__main__":
    main()
