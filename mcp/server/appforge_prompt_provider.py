from __future__ import annotations

PROMPTS = {

    "choose_integration_approach": """Use AppForger's Integration Strategy Advisor. Compare official connector/MCP, existing AppForger integration, direct API, custom Python, and hybrid. Research current official options before recommending custom code. Return decision packet sections and approval requirements.""",
    "research_official_connectors": """Research current official/trusted connectors, plugins, and MCP servers for the requested service. If browsing is unavailable, mark verification as required. Summarize read/write capability, auth, scopes, cost, and fit for the user's goal.""",
    "create_integration_strategy_plan": """Create an integration strategy plan. Do not execute actions. Return connector/API/custom/hybrid recommendation, risk classification, cost/hosting notes, setup steps, and decision packet path.""",
    "setup_appforge_project": """Use AppForger to set up a project. Inspect whether this is new/existing/ongoing. Use the setup command reference. Do not generate provider adapters unless requested. Create optional workspace folders such as assets/design or local-only only when onboarding answers require them.""",
    "adopt_existing_project": """Create an adoption plan for an existing project. Default to register-only. Do not move/copy/symlink unless an approval file and CLI flags are present.""",
    "configure_runtime_storage": """Guide the user to choose local Docker or cloud storage for Postgres, Qdrant, and Neo4j/Postgres graph tables. Return commands and required .env variables.""",
    "configure_cloud_runtime": """Create a cloud runtime setup plan. Do not provision cloud resources. Return provider-specific setup steps and risk flags.""",
    "import_repo_and_bootstrap_code_context": """Guide repo import and code context bootstrap. Respect source registry, access policy, raw-code indexing approval, and stale-context gates.""",
    "fetch_confluence_context": """Guide Confluence fetch-only context. Use storage modes docs_mirror, exports_snapshot, local_only_mirror, rag_only, or metadata_only. Do not write to Confluence.""",
    "run_source_pipeline": """Run the source pipeline workflow. Identify source type, storage mode, indexing, graph settings, and return local command with risk metadata.""",
    "clean_appforge_project": """Create a cleanup plan. Cleanup is risky. Return command references only and require user approval before local execution.""",
    "diagnose_appforge_project": """Inspect AppForger structure using safe validation commands. Report missing layers, stale files, and next actions.""",
    "create_execution_packet": """Create an execution packet that references project-control truth, source registries, constraints, risks, and approval requirements.""",
    "create_business_requirements_document": """Create or import the mandatory Business Requirements Document before real app-building work. If the user has a template, store the project-specific copy under project-control/requirements and register it. Otherwise use the engine BRD template. The BRD sits above the product brief and must be referenced by UX, design, backend/API, frontend, QA, and release work.""",
    "request_mcp_feature_issue": """Create an issue request plan for a new global AppForger MCP feature. Do not implement in the user project. Tell the user to open the issue on the AppForger MCP repository."""
}


def list_prompts() -> list[dict]:
    return [{"name": k, "description": v[:140]} for k, v in PROMPTS.items()]


def get_prompt(name: str, arguments: dict | None = None) -> dict:
    if name not in PROMPTS:
        raise KeyError(f"Unknown prompt: {name}")
    args = arguments or {}
    body = PROMPTS[name]
    if args:
        body += "\n\nArguments:\n" + "\n".join(f"- {k}: {v}" for k, v in args.items())
    return {"description": name, "messages": [{"role": "user", "content": {"type": "text", "text": body}}]}
