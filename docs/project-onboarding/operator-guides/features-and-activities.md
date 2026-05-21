# Appforger Features and Activities

This file is the human-readable feature and activity index for Appforger. It explains what Appforger can do, where the related engine areas live, and which activities a user or AI coding model can perform with it.

Appforger is a project-control engine, workflow system, context/RAG/graph orchestration layer, and MCP-accessible skill library for AI-assisted app development.

## Core philosophy

- Skills and Markdown define the logic and workflows.
- YAML defines project choices and source registries.
- Python performs repeatable safe operations when execution is needed.
- Validators enforce structure and prevent drift.
- MCP exposes Appforger logic to whichever AI model or client the user uses.
- Risky actions are flagged and require user approval.

## 1. Core engine and project-control system

Appforger can create and manage a structured project workspace with `project-control/`, `docs/`, `design-assets/`, `exports/`, `local-only/`, and optional code folders such as `backend/`, `web/`, `mobile/`, `ios/`, and `android/`.

Activities:

- initialize a new project workspace;
- apply Appforger to an existing project;
- run mandatory onboarding;
- generate active project rules;
- track project state, decisions, approvals, baselines, handoffs, and release blockers;
- keep `project-control/` separate from app code;
- treat docs, code, and assets as their own source-of-truth areas.

Related areas:

- `docs/getting-started/start-here/`
- `workflows/operations/new-app-initializer/`
- `templates/engine/`
- `registries/`
- `runtime/context-backend/source-of-truth-policy.md`

## 2. Onboarding and setup

Appforger includes mandatory onboarding to decide project shape, source boundaries, runtime setup, and provider adapters.

Activities:

- classify the project as new, existing, ongoing, snapshot, or mixed;
- ask whether code sources already exist;
- ask whether runtime storage is local Docker or cloud;
- ask whether docs/context sources exist;
- select AI provider adapters;
- generate project profile and active rules;
- generate project-control templates;
- generate `local-only/.env.local`.

Related areas:

- `workflows/product/project-onboarding/`
- `docs/project-onboarding/start-here/setup-and-first-run-guide.md`
- `docs/project-onboarding/start-here/env-and-secrets-quickstart.md`
- `docs/project-onboarding/operator-guides/setup-and-first-run.md`

## 3. Provider and AI tool adapters

Appforger can generate adapter files for the selected AI coding tool.

Supported adapter targets:

- Codex / OpenAI coding agents: `AGENTS.md`
- Claude Code: `CLAUDE.md`
- Cursor: `.cursor/rules/appforge.mdc`
- GitHub Copilot / VS Code: `.github/copilot-instructions.md`

Activities:

- generate only the selected provider adapter;
- avoid creating unrelated adapter files;
- give coding agents Appforger-specific project instructions;
- route model behavior through skills and active project rules.

Related areas:

- `policies/providers/provider-layer/`
- `templates/packets/execution-packets/`
- `docs/project-onboarding/start-here/start-here-for-agents.md`
- `workflows/operations/new-app-initializer/setup_appforge_project.py`

## 4. Pre-setup agent bootstrap

Before workspace-level adapters exist, Appforger provides a pre-setup guide so the user can ask an AI model to initialize Appforger.

Activities:

- ask a model to read `docs/project-onboarding/start-here/start-here-for-agents.md`;
- let the model run the setup flow;
- generate the correct workspace-level adapter after setup.

Related areas:

- `docs/project-onboarding/start-here/start-here-for-agents.md`
- `docs/project-onboarding/start-here/agent-bootstrap-prompts.md`

## 5. Skills system

Appforger has a model-facing `skills/` layer. Skills describe repeatable workflows that AI models can follow.

Activities:

- guide models through onboarding, backend, frontend, design, documentation, testing, release, runtime, code context, Confluence, Git provider, source pipeline, adoption, cleanup, and MCP workflows;
- create and interpret execution packets;
- diagnose pipeline failures;
- apply adoption plans;
- configure runtime storage;
- sync context;
- enforce approval gates.

Related areas:

- `skills/`
- `templates/packets/execution-packets/`
- `templates/ai-prompts/`

## 6. Execution packets and provider routing

Appforger uses provider-agnostic execution packets so different AI tools can perform the right work with the right context.

Activities:

- generate work packets for Codex, Claude Code, and generic code agents;
- route tasks by capability;
- record provider choices;
- import provider done reports;
- reconcile outputs from multiple agents.

Related areas:

- `templates/packets/execution-packets/`
- `policies/providers/provider-layer/`
- `templates/packets/code-agent-packets/providers/codex/`
- `docs/collaboration/handoffs/`

## 7. Parallel work and sub-agent orchestration

Appforger supports parallel work planning and sub-agent role definitions.

Activities:

- create sub-agent roles;
- create parallel work plans;
- validate dependencies and conflict risk;
- dispatch work packets;
- pause, cancel, or supersede work;
- reconcile outputs;
- record done reports and handoffs.

Related areas:

- `policies/operations/parallel-agent-work/`
- `workflows/operations/agents/`
- `policies/collaboration/team-collaboration/`

## 8. Runtime infrastructure

Appforger can configure local or cloud storage units for its own operational features.

Local Docker storage units:

- Postgres for operational/team/runtime state;
- Qdrant for vector/RAG context storage;
- Neo4j for graph relationships and impact mapping.

Cloud/runtime scaffolds:

- managed Postgres;
- Supabase/Postgres;
- Qdrant Cloud;
- Neo4j Aura.

Activities:

- initialize local runtime env;
- start local Docker runtime;
- run health checks;
- configure `runtime-selection.yaml`;
- validate runtime infrastructure;
- document local/cloud runtime setup.

Related areas:

- `runtime/platform/storage/`
- `skills/runtime/runtime_skills/`
- `templates/project-control/runtime/`

## 9. Context backend and RAG

Appforger has a context backend for derived project knowledge.

Supported profiles:

- local JSONL;
- Qdrant;
- Supabase pgvector;
- generic vector database profile.

Activities:

- index project-control context;
- index docs;
- index code summaries;
- retrieve context packs;
- run context health checks;
- validate context freshness.

Boundary:

- RAG is derived context, not canonical truth.

Related areas:

- `runtime/context/context-backend/`
- `workflows/operations/context-sync-retrieval/`
- `skills/context/context-backend/`

## 10. Repo Import + Code Context Sync

This feature lets Appforger register local or remote code sources and build derived understanding from them.

Activities:

- register backend, web, mobile, iOS, and Android code sources;
- import existing backend and frontend repos;
- attach local code folders;
- register remote Git repos;
- support uploaded snapshots and CI-generated context;
- mark code sources canonical or non-canonical;
- bootstrap and sync code context;
- detect stale code context.

Generated maps include backend route/auth/database/migration/dependency maps and frontend route/component/API-client/state/theme/navigation maps.

Related areas:

- `workflows/operations/context-sync-retrieval/code_context_sources/`
- `templates/project-control/code_sources/`
- `skills/context/code-context/`
- `skills/workflow/workflow_skills/import_existing_backend/`
- `skills/workflow/workflow_skills/import_existing_frontend/`

## 11. Code graph and code tree runtime

Appforger can build code maps and relationships for backend and frontend/mobile sources.

Activities:

- scan backend/frontend/mobile repos;
- parse symbols;
- generate code maps;
- index code summaries into RAG;
- create graph nodes and edges;
- link frontend screens/components to backend APIs;
- link backend endpoints to services, models, tests, and requirements.

Planned/runtime language targets:

- Python;
- JavaScript;
- TypeScript;
- Dart;
- Swift;
- Kotlin.

Related areas:

- `templates/project-control/code_sources/scripts/`
- `runtime/platform/storage/graph/`
- `workflows/operations/source-pipelines/`

## 12. Source Pipeline Orchestrator

The source pipeline routes different source types into the correct fetch, indexing, and graph workflows.

Activities:

- run one command for source sync;
- route Confluence/doc sources through doc pipelines;
- route Git/code sources through code pipelines;
- index summaries into RAG;
- update graph relationships;
- update sync logs;
- diagnose source pipeline failures.

Related areas:

- `workflows/operations/source-pipelines/`
- `templates/project-control/pipelines/`
- `skills/operations/source_pipeline_skills/`

## 13. Confluence fetch-only integration

Appforger supports Confluence Cloud and Confluence Data Center as documentation sources.

Activities:

- fetch by space key;
- fetch by parent page/tree;
- fetch by page ID;
- fetch by page URL;
- fetch one page and all children;
- preserve hierarchy;
- fetch labels as metadata;
- compare versions/updated timestamps;
- run incremental sync;
- normalize pages to Markdown;
- index chunks/summaries into RAG;
- optionally create graph nodes.

Storage modes:

- `docs_mirror`: store full Markdown in `docs/confluence/`;
- `exports_snapshot`: store full Markdown in `exports/confluence/`;
- `local_only_mirror`: store full Markdown in `local-only/doc_sources/confluence/`;
- `rag_only`: index summaries/chunks without storing a full local copy;
- `metadata_only`: metadata only, no body chunks.

Boundary:

- fetch-only; no create/update/delete/write-back to Confluence.

Related areas:

- `integrations/document-sources/confluence/`
- `templates/project-control/doc_sources/`
- `skills/integrations/apps/confluence/`

## 14. Git provider integrations

Appforger supports a Git provider abstraction for GitHub, GitLab, and Bitbucket.

Bitbucket support includes:

- Bitbucket Cloud;
- Bitbucket Data Center configuration;
- API token metadata;
- URL normalization;
- remote file listing/fetching scaffolds;
- clone fallback;
- branch/PR command references;
- Bitbucket Pipelines context artifact templates.

Activities:

- configure Git provider;
- normalize repo URLs;
- register remote code sources;
- sync Bitbucket code source;
- create provider-aware command references;
- support shared project-control repo remotes.

Related areas:

- `integrations/source-control/generic/`
- `integrations/source-control/github/`
- `integrations/source-control/gitlab/`
- `integrations/source-control/bitbucket/`
- `skills/integrations/generic/source-control/ and app-specific source-control skills under skills/integrations/apps/`
- `templates/project-control/git_providers/`

## 15. Project Adoption & Git Boundaries

Appforger can safely adopt existing local projects.

Activities:

- scan an existing workspace;
- detect backend/web/mobile folders;
- detect Git layout;
- create an adoption plan;
- register sources without moving by default;
- move/copy/symlink only after approval;
- preserve existing `.git` folders;
- record original paths;
- restore move-adopted sources during cleanup;
- append Appforger-managed `features/miscellaneous/.gitignore` blocks.

Default:

- register only; do not move files automatically.

Related areas:

- `workflows/operations/project-adoption-git-boundaries/`
- `skills/onboarding/project_adoption_skills/`

## 16. Cleanup and lifecycle management

Appforger includes cleanup and lifecycle commands.

Activities:

- remove Appforger engine/control files while keeping project code;
- remove only local-only files;
- remove whole project while keeping engine;
- restore move-adopted sources;
- remove runtime containers;
- remove runtime volumes with confirmation;
- remove generated adapter files if Appforger-generated.

Safety:

- dry-run/planning first;
- destructive actions flagged;
- approval required;
- runtime volume deletion requires explicit confirmation.

Related areas:

- `workflows/operations/workspace-artifact-lifecycle/`
- `skills/operations/cleanup_skills/`

## 17. Git ignore and shared project-control repo

Appforger supports clean Git boundaries.

Activities:

- keep `appforger-engine/` out of app repos;
- keep `local-only/` out of Git;
- optionally create a separate project-control repo;
- include or exclude docs, design assets, exports, and code repos;
- ask before commit/push.

Related areas:

- `workflows/operations/project-adoption-git-boundaries/`
- `templates/project-control/git_boundaries/`

## 18. Secrets and environment management

Appforger uses a single local private env file:

```text
local-only/.env.local
```

Activities:

- keep secrets outside project-control;
- store only secret metadata in project-control;
- generate `.env.local.example`;
- document CI/CD and hosting secret names;
- avoid indexing secrets.

Related areas:

- `docs/project-onboarding/start-here/env-and-secrets-quickstart.md`
- `templates/workspace/local-only/.env.local.example`
- `policies/collaboration/team-secrets-access/`

## 19. MCP server

Appforger includes an MCP server that exposes engine logic to MCP-capable clients.

Activities:

- expose manifest-selected engine resources;
- expose skills and templates;
- expose prompts for setup, adoption, runtime, repo import, Confluence fetch, source pipelines, cleanup, diagnosis, and execution packet creation;
- return command references and risk flags;
- support local stdio and HTTP modes;
- support remote hosting via Docker or DigitalOcean templates.

Boundary:

- remote MCP does not execute project actions;
- it returns plans, workflows, command references, and risk flags;
- the user’s AI model runs approved commands locally.

Related areas:

- `mcp/`
- `skills/integrations/generic/mcp-server/`

## 20. Backend and API development

Activities:

- select backend stack;
- build FastAPI + Postgres backend;
- build Supabase backend;
- create API contracts;
- map backend routes;
- generate backend docs;
- review backend architecture.

Related areas:

- `workflows/implementation/backend/`
- `workflows/implementation/backend/`
- `skills/implementation/backend/`

## 21. Web frontend development

Activities:

- select web stack;
- create web architecture;
- implement React features;
- implement Next.js pages;
- deploy web preview;
- run web visual QA.

Related areas:

- `workflows/implementation/web-frontend/`
- `skills/implementation/web_skills/`

## 22. Native/mobile development

Activities:

- implement SwiftUI features;
- implement Jetpack Compose features;
- support mobile release preparation;
- map Figma to native iOS/Android;
- manage native repo scaffolds.

Related areas:

- `workflows/implementation/native-ios/`
- `workflows/implementation/native-android/`
- `workflows/delivery/store-assets/`

## 23. Design and Figma workflows

Activities:

- create UX flows;
- create visual direction;
- create Figma prompts;
- import design systems;
- approve design baselines;
- review image assets;
- map Figma to web or native;
- run visual QA.

Related areas:

- `workflows/experience-design/design-workflow/`
- `workflows/experience-design/design-workflow/`
- `integrations/design/apps/figma/roundtrip/`
- `integrations/design/image-generation/`

## 24. Documentation system

Activities:

- import project documents;
- classify documents;
- register documents;
- summarize documents;
- index documents;
- archive documents;
- generate developer/user docs;
- update changelog/release notes.

Related areas:

- `docs/document-management/documentation-system/`
- `docs/document-management/project-docs-library/`
- `integrations/document-sources/confluence/`

## 25. Product and backlog management

Activities:

- create product brief;
- create user stories;
- map stories to features;
- refine backlog;
- select project mode;
- export backlog to Trello.

Related areas:

- `workflows/product/user-stories-product-backlog/`
- `integrations/planning/trello/`
- `integrations/planning/task-management/`

## 26. QA and testing

Activities:

- create test plans;
- generate test cases;
- write automated tests;
- run and record tests;
- run QA review;
- close tasks with evidence;
- manage test data;
- run visual QA.

Related areas:

- `validation/domains/qa/`
- `validation/domains/test-authoring-execution/`
- `validation/domains/test-data/`

## 27. Release management

Activities:

- prepare release candidates;
- run release readiness reviews;
- record release approvals;
- generate release notes;
- create release docs;
- prepare hotfix plans;
- prepare mobile store submissions;
- prepare web publish plans;
- collect release evidence;
- manage release blockers.

Related areas:

- `workflows/delivery/release-docs/`
- `workflows/delivery/release-operations/`
- `policies/delivery/release-evidence-approvals/`
- `workflows/delivery/store-assets/`

## 28. Automation and jobs

Activities:

- create automation jobs;
- create GitHub Action jobs;
- disable jobs;
- handle failed jobs;
- record job runs;
- review automation risk;
- run local jobs.

Related areas:

- `policies/operations/automation-jobs/`
- `templates/jobs/automation-jobs/`
- `skills/operations/automation_skills/`

## 29. Team collaboration and governance

Activities:

- add team members;
- assign roles and permissions;
- create handoff packets;
- create role context packs;
- create team operating model;
- resolve team conflicts;
- review and approve artifacts;
- update team status;
- set up team operations backend.

Related areas:

- `policies/collaboration/team-collaboration/`
- `runtime/collaboration/team-operations-backend/`
- `policies/collaboration/team-collaboration/`

## 30. Security and privacy

Activities:

- run security review;
- classify high-risk actions;
- protect secrets;
- block raw code indexing unless approved;
- block sensitive Confluence indexing unless approved;
- label auth/security/payment/migration/API contract changes as high-risk.

Related areas:

- `policies/security/`
- `policies/collaboration/team-secrets-access/`
- `docs/project-onboarding/start-here/human-approval-gates.md`

## 31. Draft and sandbox mode

Activities:

- start draft experiments;
- create HTML sandboxes;
- review draft experiments;
- promote drafts to project truth;
- discard draft experiments.

Related areas:

- `workflows/operations/draft-sandbox/`

## 32. Flexible workflow and stage overrides

Activities:

- skip stages;
- substitute stages;
- reorder stages;
- import existing backend/frontend;
- promote sandbox to baseline;
- request project-specific workflow override;
- perform impact analysis.

Related areas:

- `policies/operations/workflow-stage-overrides/`
- `policies/operations/workflow-stage-overrides/`

## 33. Validation and audits

Activities:

- validate engine structure;
- validate feature manifest;
- validate skill layer;
- validate runtime infrastructure;
- validate code context sources;
- validate doc source integrations;
- validate Git provider integrations;
- validate source pipeline orchestrator;
- validate no stale placeholders;
- run operational audits.

Related areas:

- `validation/`
- `validation/audits/operational-audit/`

## 34. Feature manifest and status audit

Activities:

- list claimed features;
- verify required files exist;
- distinguish implemented, scaffold, and production-complete features;
- audit missing feature paths;
- prevent stale/redundant files from silently returning.

Related areas:

- `registries/APPFORGE_FEATURE_MANIFEST.json`
- `validation/operational-audits/operational-audit/feature-status-audit.md`
- `validation/validate_feature_manifest.py`

## 35. End-to-end uses

A user can use Appforger to:

- start a new app project;
- adopt an existing app project;
- connect backend/frontend/mobile repos;
- configure local/cloud Appforger runtime storage;
- index docs/code/Confluence into context;
- build code maps and code graphs;
- expose Appforger as an MCP to AI tools;
- generate execution packets for coding agents;
- manage parallel AI work;
- track approvals, handoffs, and evidence;
- create backend/API/frontend/mobile implementation plans;
- run QA and release workflows;
- keep project-control separate from code;
- cleanly remove Appforger from a project.


## Integration Strategy Advisor

Before adding an integration, Appforger can compare official connectors/plugins/MCPs, existing Appforger integrations, direct APIs, custom Python, and hybrid approaches. See `mcp/docs/feature-guides/integration-strategy-advisor.md`.
