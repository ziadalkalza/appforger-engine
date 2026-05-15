from __future__ import annotations
from pathlib import Path
from manifest_loader import load_feature_manifest
from appforge_risk_classifier import classify_action


def tool_schemas() -> list[dict]:
    return [
        {"name":"list_features","description":"List AppForger feature manifest entries.","inputSchema":{"type":"object","properties":{}}},
        {"name":"list_skills","description":"List AppForger SKILL.md resources.","inputSchema":{"type":"object","properties":{}}},
        {"name":"search_appforge_resources","description":"Keyword search manifest-selected resources.","inputSchema":{"type":"object","properties":{"query":{"type":"string"},"limit":{"type":"integer"}},"required":["query"]}},
        {"name":"get_resource","description":"Read a manifest-selected AppForger resource by URI.","inputSchema":{"type":"object","properties":{"uri":{"type":"string"}},"required":["uri"]}},
        {"name":"create_setup_plan","description":"Return setup command and approval notes. Does not execute.","inputSchema":{"type":"object","properties":{"project_name":{"type":"string"},"adapter":{"type":"string"}}}},
        {"name":"create_adoption_plan","description":"Return adoption planning guidance. Does not move files.","inputSchema":{"type":"object","properties":{"source_hint":{"type":"string"}}}},
        {"name":"create_cleanup_plan","description":"Return cleanup command reference and risk metadata. Does not delete.","inputSchema":{"type":"object","properties":{"mode":{"type":"string"}}}},
        {"name":"create_context_sync_plan","description":"Return source pipeline/code/docs sync command reference. Does not run.","inputSchema":{"type":"object","properties":{"source_id":{"type":"string"},"storage_mode":{"type":"string"}}}},
        {"name":"classify_action_risk","description":"Classify workflow or command risk.","inputSchema":{"type":"object","properties":{"text":{"type":"string"}},"required":["text"]}},
        {"name":"create_integration_strategy_plan","description":"Return an integration strategy advisor plan. Does not create integration code or execute actions.","inputSchema":{"type":"object","properties":{"integration":{"type":"string"},"goal":{"type":"string"},"needs_persistent_rag":{"type":"boolean"},"needs_graph":{"type":"boolean"}}}},
        {"name":"create_feature_request_issue_plan","description":"Create an issue request plan for a new global AppForger MCP/engine feature. Does not modify project files.","inputSchema":{"type":"object","properties":{"feature":{"type":"string"},"goal":{"type":"string"},"requested_surface":{"type":"string"}},"required":["feature"]}}
    ]


class ToolProvider:
    def __init__(self, engine_root: Path, resource_provider):
        self.engine_root = engine_root
        self.resources = resource_provider

    def call(self, name: str, args: dict | None = None) -> dict:
        args = args or {}
        if name == "list_features":
            return load_feature_manifest(self.engine_root)
        if name == "list_skills":
            skills = []
            root = self.engine_root / "skills"
            for p in root.rglob("SKILL.md") if root.exists() else []:
                skills.append({"id": str(p.relative_to(root)).replace('/SKILL.md',''), "path": str(p.relative_to(self.engine_root))})
            return {"skills": skills}
        if name == "search_appforge_resources":
            return {"results": self.resources.search(args.get("query", ""), int(args.get("limit", 20)))}
        if name == "get_resource":
            return self.resources.read_resource(args["uri"])
        if name == "create_setup_plan":
            adapter = args.get("adapter", "ask")
            project = args.get("project_name", "<project name>")
            cmd = f"python appforge-engine/workflows/operations/new-app-initializer/setup_appforge_project.py --target . --name \"{project}\""
            if adapter != "ask":
                cmd += f" --agent-adapters {adapter}"
            risk = classify_action(cmd)
            risk["risk"] = "medium"
            risk["requires_user_approval"] = True
            return {"workflow":"setup_appforge_project", "recommended_command": cmd, **risk}
        if name == "create_adoption_plan":
            cmd = "python appforge-engine/workflows/operations/project-adoption-git-boundaries/scripts/appforge_adopt.py --target . scan"
            return {"workflow":"adopt_existing_project", "recommended_command": cmd, **classify_action("adopt existing project scan")}
        if name == "create_cleanup_plan":
            mode = args.get("mode", "remove-engine")
            cmd = f"python appforge-engine/workflows/operations/workspace-artifact-lifecycle/scripts/appforge_clean.py --target . --mode {mode}"
            risk = classify_action(cmd)
            risk["risk"] = "high"
            risk["requires_user_approval"] = True
            return {"workflow":"clean_appforge_project", "recommended_command": cmd, **risk}
        if name == "create_context_sync_plan":
            source = args.get("source_id", "<source_id>")
            storage = args.get("storage_mode")
            cmd = f"python project-control/pipelines/scripts/run_source_pipeline.py --source {source}"
            if storage:
                cmd += f" --storage-mode {storage}"
            return {"workflow":"run_source_pipeline", "recommended_command": cmd, **classify_action(cmd)}
        if name == "classify_action_risk":
            return classify_action(args.get("text", ""))

        if name == "create_integration_strategy_plan":
            integration = args.get("integration", "<integration>")
            goal = args.get("goal", "<goal>")
            needs_rag = bool(args.get("needs_persistent_rag", False))
            needs_graph = bool(args.get("needs_graph", False))
            approach = "hybrid" if (needs_rag or needs_graph) else "official_connector_or_mcp_first"
            return {
                "workflow": "choose_integration_approach",
                "integration": integration,
                "goal": goal,
                "recommended_approach": approach,
                "mcp_executes": False,
                "requires_user_approval": True,
                "research_required": True,
                "decision_packet_template": "templates/engine/project-control-template/integrations/integration-decision-packet.template.md",
                "next_steps": [
                    "Research current official connector/plugin/MCP options.",
                    "Check existing AppForger built-in integrations.",
                    "Compare connector/API/custom/hybrid approaches.",
                    "Create integration decision packet before custom code."
                ],
                **classify_action("integration strategy advisor")
            }

        if name == "create_feature_request_issue_plan":
            feature = args.get("feature", "<feature>")
            goal = args.get("goal", "<goal>")
            surface = args.get("requested_surface", "resource/prompt/tool/connector/template")
            return {
                "workflow": "request_appforge_mcp_feature",
                "feature": feature,
                "goal": goal,
                "requested_surface": surface,
                "mcp_executes": False,
                "recommended_action": "open_issue_on_appforge_mcp_repo",
                "issue_template": "mcp/FEATURE_REQUESTS_AND_ISSUES.md",
                "requires_user_approval": False,
                "next_steps": [
                    "Classify whether this is project-local or a global MCP/engine feature.",
                    "If global, open an issue on the AppForger MCP repository using the issue template.",
                    "Include acceptance criteria, risk classification, and required validators/smoke tests."
                ],
                **classify_action("feature request issue")
            }
        raise KeyError(f"Unknown tool: {name}")
