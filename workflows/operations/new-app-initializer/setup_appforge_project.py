#!/usr/bin/env python3
import argparse, shutil, os, subprocess, sys
from pathlib import Path

CORE_PROJECT_CONTROL_PATHS = [
    "README.md",
    "appforge-active-rules.md",
    "appforge-onboarding-answers.md",
    "appforge-project-profile.md",
    "appforge-project-status.md",
    "appforge-project.yaml",
    "appforge-setup-status.md",
    "assumption-log.md",
    "decision-log.md",
    "pending-questions.md",
    "product-overview.md",
    "project-profile.md",
    "registries/active-features-registry.md",
    "registries/active-provider-registry.md",
    "registries/active-workflow-rules-registry.md",
    "registries/pending-onboarding-questions-registry.md",
    "registries/project-initialization-registry.md",
    "registries/provider-decision-registry.md",
    "registries/provider-preference-registry.md",
    "registries/stage-override-registry.md",
    "workflow-overrides/.gitkeep",
]

PROJECT_CONTROL_MODULES = {
    "access": [
        "access-and-secrets",
        "registries/code-access-registry.md",
        "registries/secret-access-registry.md",
        "registries/secret-metadata-registry.md",
    ],
    "adoption": [
        "adoption",
        "git-boundaries",
    ],
    "automation": [
        "automation",
        ".github/workflows",
        "registries/automated-job-registry.md",
        "registries/automation-approval-registry.md",
        "registries/automation-failure-registry.md",
        "registries/automation-schedule-registry.md",
        "registries/job-run-registry.md",
    ],
    "code": [
        "code-sources",
        "pipelines",
        "registries/code-context-risk-registry.md",
        "registries/code-context-staleness-registry.md",
        "registries/code-context-sync-registry.md",
        "registries/code-source-registry.md",
    ],
    "context": [
        "context-backend",
        "registries/context-backend-registry.md",
        "registries/context-index-registry.md",
        "registries/context-retrieval-registry.md",
        "registries/context-storage-registry.md",
        "registries/context-sync-registry.md",
    ],
    "docs": [
        "doc-sources",
        "registries/document-import-registry.md",
        "registries/document-indexing-registry.md",
        "registries/document-library-registry.md",
        "registries/document-sensitivity-registry.md",
        "registries/documentation-registry.md",
        "registries/meeting-notes-registry.md",
    ],
    "github": [
        ".github",
        "git-providers",
    ],
    "integrations": [
        "integrations",
        "registries/tool-provider-registry.md",
        "registries/tool-recommendation-registry.md",
    ],
    "runtime": [
        "runtime",
        "registries/deployment-registry.md",
        "registries/storage-mode-registry.md",
    ],
    "release": [
        "release-docs",
        "release-packets",
        "registries/post-release-registry.md",
        "registries/release-candidate-registry.md",
        "registries/release-evidence-registry.md",
        "registries/release-registry.md",
        "registries/store-asset-registry.md",
    ],
    "team": [
        "team",
        "registries/agent-conflict-registry.md",
        "registries/agent-dependency-registry.md",
        "registries/agent-handoff-registry.md",
        "registries/agent-output-registry.md",
        "registries/agent-run-registry.md",
        "registries/approval-registry.md",
        "registries/conflict-registry.md",
        "registries/parallel-work-registry.md",
        "registries/provider-handoff-registry.md",
        "registries/reconciliation-registry.md",
        "registries/review-registry.md",
        "registries/role-assignment-registry.md",
        "registries/sub-agent-registry.md",
        "registries/team-handoff-registry.md",
        "registries/team-member-registry.md",
        "registries/team-task-registry.md",
    ],
    "team-operations": [
        "team-operations-backend",
        "registries/team-operations-access-registry.md",
        "registries/team-operations-audit-registry.md",
        "registries/team-operations-backend-registry.md",
        "registries/team-operations-state-registry.md",
        "registries/team-operations-sync-registry.md",
    ],
}

WORKSPACE_MODULES = {"assets", "design-assets", "local-only"}

def copytree_merge(src, dst):
    if not src.exists(): return
    for p in src.rglob("*"):
        rel=p.relative_to(src)
        out=dst/rel
        if p.is_dir():
            out.mkdir(parents=True, exist_ok=True)
        else:
            out.parent.mkdir(parents=True, exist_ok=True)
            if not out.exists():
                shutil.copy2(p,out)

def copy_path(src_root, dst_root, rel):
    src=src_root/rel
    dst=dst_root/rel
    if not src.exists(): return
    if src.is_dir():
        copytree_merge(src,dst)
    else:
        dst.parent.mkdir(parents=True,exist_ok=True)
        if not dst.exists():
            shutil.copy2(src,dst)

def parse_modules(value):
    return {m.strip().lower() for m in (value or "").split(",") if m.strip()}

def modules_from_answers(args):
    modules=parse_modules(args.enable_modules)
    unknown=modules-set(PROJECT_CONTROL_MODULES)
    if unknown:
        known=", ".join(sorted(PROJECT_CONTROL_MODULES))
        raise SystemExit(f"Unknown project-control module(s): {', '.join(sorted(unknown))}. Known modules: {known}")
    project_state=(args.project_state or "ask").lower()
    app_type=(args.app_type or "ask").lower()
    backend=(args.backend or "ask").lower()
    team_mode=(args.team_mode or "ask").lower()
    context_backend=(args.context_backend or "ask").lower()
    automation_level=(args.automation_level or "ask").lower()
    public_release=(args.public_release or "ask").lower()

    if team_mode == "team":
        modules.add("team")
    if args.team_operations_backend:
        modules.update({"team", "team-operations"})
    if project_state in {"existing", "ongoing", "running", "import"}:
        modules.update({"adoption", "code"})
    if args.init_local_runtime_env or backend in {"yes", "true", "needed", "required"}:
        modules.add("runtime")
    if context_backend not in {"ask", "none", "off", "false", ""}:
        modules.add("context")
    if automation_level not in {"ask", "none", "off", "0", ""}:
        modules.add("automation")
    if public_release in {"yes", "true", "expected"} or app_type in {"mobile", "ios", "android"}:
        modules.add("release")
    return modules

def parse_workspace_modules(value):
    modules=parse_modules(value)
    unknown=modules-WORKSPACE_MODULES
    if unknown:
        known=", ".join(sorted(WORKSPACE_MODULES))
        raise SystemExit(f"Unknown workspace module(s): {', '.join(sorted(unknown))}. Known modules: {known}")
    return modules

def workspace_modules_from_answers(args):
    modules=parse_workspace_modules(args.enable_workspace_modules)
    design_workflow=(args.design_workflow or "ask").lower()
    if args.assets:
        modules.add("assets")
    if args.design_assets or design_workflow in {"figma", "existing-design", "existing_design", "design-assets", "assets"}:
        modules.update({"assets", "design-assets"})
    if args.include_local_only or args.init_local_runtime_env:
        modules.add("local-only")
    return modules

def copy_workspace(src, target, modules):
    copy_path(src,target,Path("docs"))
    (target/"exports").mkdir(parents=True,exist_ok=True)
    (target/"assets").mkdir(parents=True,exist_ok=True)
    if "design-assets" in modules:
        (target/"assets/design").mkdir(parents=True,exist_ok=True)
    if "local-only" in modules:
        (target/"local-only").mkdir(parents=True,exist_ok=True)
        for rel in ["local-only/.env.local.example", "local-only/README-start-here.md"]:
            copy_path(src,target,Path(rel))
        env_ex=target/"local-only/.env.local.example"
        env=target/"local-only/.env.local"
        if env_ex.exists() and not env.exists():
            shutil.copy2(env_ex, env)

def copy_project_control(src, dst, modules):
    dst.mkdir(parents=True, exist_ok=True)
    for rel in CORE_PROJECT_CONTROL_PATHS:
        copy_path(src,dst,Path(rel))
    for module in sorted(modules):
        for rel in PROJECT_CONTROL_MODULES.get(module, []):
            copy_path(src,dst,Path(rel))

def write_scaffold_summary(target, modules):
    active=", ".join(sorted(modules)) or "none"
    path=target/"project-control/appforge-scaffold-summary.md"
    if not path.exists():
        path.write_text(
            "# AppForger Scaffold Summary\n\n"
            "Project-control starts with core driver files only. Optional sections are added when onboarding answers or later changes activate them.\n\n"
            f"Active optional modules: {active}\n\n"
            "Use the project-control module command to add future modules such as `team`, `runtime`, `automation`, or `context`.\n",
            encoding="utf-8"
        )

def write_adapter(target, adapter):
    marker="<!-- AppForger generated adapter -->\n"
    content=marker+"# AppForger\n\nRead `project-control/APPFORGE_ACTIVE_RULES.md` and follow AppForger source-of-truth rules.\n"
    if adapter=="codex":
        (target/"AGENTS.md").write_text(content,encoding="utf-8")
    elif adapter=="claude":
        (target/"CLAUDE.md").write_text(content,encoding="utf-8")
    elif adapter=="cursor":
        p=target/".cursor/rules/appforge.mdc"; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(content,encoding="utf-8")
    elif adapter=="copilot":
        p=target/".github/copilot-instructions.md"; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(content,encoding="utf-8")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--target", default=".")
    ap.add_argument("--name", default="AppForger Project")
    ap.add_argument("--agent-adapters", default="")
    ap.add_argument("--project-state", default="ask")
    ap.add_argument("--app-type", default="ask")
    ap.add_argument("--backend", default="ask")
    ap.add_argument("--team-mode", choices=["ask","single","team"], default="ask")
    ap.add_argument("--context-backend", default="ask")
    ap.add_argument("--automation-level", default="ask")
    ap.add_argument("--public-release", default="ask")
    ap.add_argument("--design-workflow", default="ask")
    ap.add_argument("--enable-modules", default="", help="Comma-separated optional project-control modules to scaffold.")
    ap.add_argument("--enable-workspace-modules", default="", help="Comma-separated optional workspace modules: assets, design-assets, local-only.")
    ap.add_argument("--assets", action="store_true", help="Accepted for compatibility. Generic assets/ is created by default.")
    ap.add_argument("--design-assets", action="store_true", help="Create assets/design/ for design assets.")
    ap.add_argument("--include-local-only", action="store_true", help="Create local-only/ and local private config files.")
    ap.add_argument("--team-operations-backend", action="store_true")
    ap.add_argument("--init-local-runtime-env", action="store_true")
    args=ap.parse_args()
    target=Path(args.target).resolve()
    engine=Path(__file__).resolve().parents[3]
    tmpl=engine/"templates"
    modules=modules_from_answers(args)
    workspace_modules=workspace_modules_from_answers(args)
    copy_project_control(tmpl/"project-control", target/"project-control", modules)
    copy_workspace(tmpl/"workspace", target, workspace_modules)
    (target/"project-control/APPFORGE_ACTIVE_RULES.md").write_text("# AppForger Active Rules\n\nGenerated by setup.\n",encoding="utf-8")
    adapters=[a.strip() for a in args.agent_adapters.split(",") if a.strip()]
    if "all" in adapters:
        adapters=["codex","claude","cursor","copilot"]
    for a in adapters:
        write_adapter(target,a)
    write_scaffold_summary(target, modules)
    (target/"APPFORGE_INJECTION_SUMMARY.md").write_text(f"# AppForger Injection Summary\n\nProject: {args.name}\nAdapters: {', '.join(adapters) or 'none'}\n",encoding="utf-8")
    print(f"AppForger workspace prepared at {target}")
    print(f"Project-control optional modules: {', '.join(sorted(modules)) or 'none'}")
    print(f"Workspace optional modules: {', '.join(sorted(workspace_modules)) or 'none'}")
    if "local-only" in workspace_modules:
        print("Fill local-only/.env.local next.")
if __name__=="__main__": main()
