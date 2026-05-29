from __future__ import annotations
from pathlib import Path
from manifest_loader import load_feature_manifest
from appforge_risk_classifier import classify_action


def _quote(value: str) -> str:
    return '"' + value.replace('"', '\\"') + '"'


def tool_schemas() -> list[dict]:
    return [
        {"name":"list_features","description":"List AppForger feature manifest entries.","inputSchema":{"type":"object","properties":{}}},
        {"name":"list_skills","description":"List AppForger SKILL.md resources.","inputSchema":{"type":"object","properties":{}}},
        {"name":"search_appforge_resources","description":"Keyword search manifest-selected resources.","inputSchema":{"type":"object","properties":{"query":{"type":"string"},"limit":{"type":"integer"}},"required":["query"]}},
        {"name":"get_resource","description":"Read a manifest-selected AppForger resource by URI.","inputSchema":{"type":"object","properties":{"uri":{"type":"string"}},"required":["uri"]}},
        {"name":"create_setup_plan","description":"Return setup command and approval notes. Does not execute.","inputSchema":{"type":"object","properties":{"project_name":{"type":"string"},"adapter":{"type":"string"},"target":{"type":"string","description":"Project root selected by the user or AI client. Defaults to the MCP workspace root if configured, otherwise current directory."},"assets":{"type":"boolean","description":"Compatibility flag; generic assets/ is created by default."},"design_assets":{"type":"boolean","description":"Create assets/design/."},"include_local_only":{"type":"boolean","description":"Create local-only/ and local private config files."}}}},
        {"name":"create_adoption_plan","description":"Return adoption planning guidance. Does not move files.","inputSchema":{"type":"object","properties":{"source_hint":{"type":"string"},"target":{"type":"string","description":"Project root selected by the user or AI client. Defaults to the MCP workspace root if configured, otherwise current directory."}}}},
        {"name":"create_cleanup_plan","description":"Return cleanup command reference and risk metadata. Does not delete.","inputSchema":{"type":"object","properties":{"mode":{"type":"string"},"target":{"type":"string","description":"Project root selected by the user or AI client. Defaults to the MCP workspace root if configured, otherwise current directory."}}}},
        {"name":"create_project_control_module_plan","description":"Return a command to add optional project-control modules after onboarding changes. Does not execute.","inputSchema":{"type":"object","properties":{"modules":{"type":"array","items":{"type":"string"}},"target":{"type":"string","description":"Project root selected by the user or AI client. Defaults to the MCP workspace root if configured, otherwise current directory."}},"required":["modules"]}},
        {"name":"create_context_sync_plan","description":"Return source pipeline/code/docs sync command reference. Does not run.","inputSchema":{"type":"object","properties":{"source_id":{"type":"string"},"storage_mode":{"type":"string"}}}},
        {"name":"classify_action_risk","description":"Classify workflow or command risk.","inputSchema":{"type":"object","properties":{"text":{"type":"string"}},"required":["text"]}},
        {"name":"create_business_requirements_plan","description":"Return a BRD creation/import plan. Does not write project files.","inputSchema":{"type":"object","properties":{"project_name":{"type":"string"},"has_user_template":{"type":"boolean"},"template_source":{"type":"string"},"target":{"type":"string","description":"Project root selected by the user or AI client. Defaults to the MCP workspace root if configured, otherwise current directory."}}}},
        {"name":"create_integration_strategy_plan","description":"Return an integration strategy advisor plan. Does not create integration code or execute actions.","inputSchema":{"type":"object","properties":{"integration":{"type":"string"},"goal":{"type":"string"},"needs_persistent_rag":{"type":"boolean"},"needs_graph":{"type":"boolean"}}}},
        {"name":"create_feature_request_issue_plan","description":"Create an issue request plan for a new global AppForger MCP/engine feature. Does not modify project files.","inputSchema":{"type":"object","properties":{"feature":{"type":"string"},"goal":{"type":"string"},"requested_surface":{"type":"string"}},"required":["feature"]}}
    ]


class ToolProvider:
    def __init__(self, engine_root: Path, resource_provider, workspace_root: Path | None = None):
        self.engine_root = engine_root
        self.resources = resource_provider
        self.workspace_root = workspace_root

    def _target(self, args: dict) -> str:
        return str(args.get("target") or self.workspace_root or ".")

    def _engine_script(self, *parts: str) -> str:
        return str(self.engine_root.joinpath(*parts))

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
            target = self._target(args)
            script = self._engine_script("workflows", "operations", "new-app-initializer", "setup_appforge_project.py")
            cmd = f"python {_quote(script)} --target {_quote(target)} --name {_quote(project)}"
            if adapter != "ask":
                cmd += f" --agent-adapters {_quote(adapter)}"
            if args.get("assets"):
                cmd += " --assets"
            if args.get("design_assets"):
                cmd += " --design-assets"
            if args.get("include_local_only"):
                cmd += " --include-local-only"
            risk = classify_action(cmd)
            risk["risk"] = "medium"
            risk["requires_user_approval"] = True
            return {"workflow":"setup_appforge_project", "engine_root": str(self.engine_root), "target": target, "recommended_command": cmd, **risk}
        if name == "create_adoption_plan":
            target = self._target(args)
            script = self._engine_script("workflows", "operations", "project-adoption-git-boundaries", "scripts", "appforge_adopt.py")
            cmd = f"python {_quote(script)} --target {_quote(target)} scan"
            return {"workflow":"adopt_existing_project", "engine_root": str(self.engine_root), "target": target, "recommended_command": cmd, **classify_action("adopt existing project scan")}
        if name == "create_cleanup_plan":
            mode = args.get("mode", "remove-engine")
            target = self._target(args)
            script = self._engine_script("workflows", "operations", "workspace-artifact-lifecycle", "scripts", "appforge_clean.py")
            cmd = f"python {_quote(script)} --target {_quote(target)} --mode {_quote(mode)}"
            risk = classify_action(cmd)
            risk["risk"] = "high"
            risk["requires_user_approval"] = True
            return {"workflow":"clean_appforge_project", "engine_root": str(self.engine_root), "target": target, "recommended_command": cmd, **risk}
        if name == "create_project_control_module_plan":
            modules = args.get("modules") or []
            if isinstance(modules, str):
                modules = [m.strip() for m in modules.split(",") if m.strip()]
            target = self._target(args)
            script = self._engine_script("workflows", "operations", "project-control-modules", "appforge_project_control_module.py")
            module_flags = " ".join(f"--module {_quote(str(m))}" for m in modules)
            cmd = f"python {_quote(script)} --target {_quote(target)} enable {module_flags}".strip()
            risk = classify_action(cmd)
            risk["risk"] = "medium"
            risk["requires_user_approval"] = True
            return {"workflow":"enable_project_control_modules", "engine_root": str(self.engine_root), "target": target, "modules": modules, "recommended_command": cmd, **risk}
        if name == "create_context_sync_plan":
            source = args.get("source_id", "<source_id>")
            storage = args.get("storage_mode")
            cmd = f"python project-control/pipelines/scripts/run_source_pipeline.py --source {source}"
            if storage:
                cmd += f" --storage-mode {storage}"
            return {"workflow":"run_source_pipeline", "recommended_command": cmd, **classify_action(cmd)}
        if name == "classify_action_risk":
            return classify_action(args.get("text", ""))

        if name == "create_business_requirements_plan":
            target = self._target(args)
            project = args.get("project_name", "<project name>")
            has_template = bool(args.get("has_user_template", False))
            template_source = args.get("template_source") or ("user_provided_template" if has_template else "templates/specifications/business-requirements-document-template.md")
            return {
                "workflow": "create_business_requirements_document",
                "project": project,
                "target": target,
                "mcp_executes": False,
                "mandatory": True,
                "template_source": template_source,
                "project_brd_path": "project-control/requirements/business-requirements-document.md",
                "registry_path": "project-control/registries/requirements-document-registry.md",
                "skill": "skills/product-management/create-business-requirements-document/SKILL.md",
                "workflow_policy": "workflows/product/business-requirements/business-requirements-workflow.md",
                "requires_user_approval": True,
                "next_steps": [
                    "Read current project-control status, decisions, assumptions, pending questions, and requirements registry.",
                    "If the user supplied a template, store the project-specific copy under project-control/requirements and register it.",
                    "If no user template exists, use the engine BRD template.",
                    "Create or update the BRD before product brief, UX/design, backend/API, frontend, QA, or release work.",
                    "Record open questions, assumptions, requirement IDs, and approval state."
                ],
                **classify_action("create business requirements document plan")
            }

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
                "decision_packet_template": "templates/project-control/integrations/integration-decision-packet.template.md",
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
                "issue_template": "mcp/docs/feature-requests-and-issues.md",
                "requires_user_approval": False,
                "next_steps": [
                    "Classify whether this is project-local or a global MCP/engine feature.",
                    "If global, open an issue on the AppForger MCP repository using the issue template.",
                    "Include acceptance criteria, risk classification, and required validators/smoke tests."
                ],
                **classify_action("feature request issue")
            }
        raise KeyError(f"Unknown tool: {name}")
