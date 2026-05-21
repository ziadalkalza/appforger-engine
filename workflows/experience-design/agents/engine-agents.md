# AGENTS.md — Appforger v1.0 Global Rules

You are operating inside **Appforger v1.0**.

## Non-negotiable folder boundary

`appforger-engine/` is reusable engine logic only. Do not write live app-specific project state, generated app code, generated assets, or task outputs inside the engine during normal app work.

Live project artifacts must go outside the engine, usually in sibling folders:

```text
../project-control/
../backend/
../ios/
../android/
../web/
../design-assets/
../exports/
../local-only/
```

All reusable templates/examples are stored inside the engine under `templates/engine/` and `templates/examples/`. The initializer copies/scaffolds from those templates into a real workspace.

## Context loading

For a real app project, read the external `../project-control/` files first. Use engine files only for rules, templates, skills, and validators.

Default always-read project files:

```text
../project-control/APPFORGER_PROJECT_STATUS.md
../project-control/APPFORGER_PROJECT.yaml
../project-control/DECISION_LOG.md
../project-control/PENDING_QUESTIONS.md
```

## Plan mode and uncertainty

If you are unsure, the request is broad, the stage is risky, the integration/package is unsupported, or current external facts are required, enter plan mode first. Ask targeted questions and do not implement until the user approves.

Do not speculate about third-party APIs, SDKs, pricing, licensing, package health, security behavior, cloud setup, or store/deployment rules. Research current official sources when needed, or mark the result draft-only if research is unavailable.


## Project onboarding and initialization gate

Before starting real project work in a project that has not completed onboarding, use `workflows/product/project-onboarding/`.

Allow general help/explanation questions before onboarding. Block high-impact project work until the minimal onboarding gate is complete.

High-impact work includes implementation packets, backend/frontend/design workflow activation, provider dispatch, integration/package activation, context backend indexing decisions, team operations backend activation, automation jobs, and release work.

When blocking for onboarding:
1. Save the original user request as pending.
2. Ask only critical minimal setup questions.
3. Allow `unknown_pending` only for non-critical questions.
4. If a critical answer is unknown, explain why it blocks the workflow and provide suggestions.
5. Save answers to Markdown and YAML.
6. Generate active project rules.
7. Resume the original user request.


## Model/tool agnostic provider routing

Before performing substantial work, identify the required capability and check whether the current provider/tool is suitable. Appforger routes by capability, not by brand.

If another provider is more suitable, recommend it and offer two paths:

1. Create an execution packet for the suitable provider.
2. Continue in the current tool as planning-only, draft-only, packet-generation-only, or an untested patch proposal.

High-risk tasks such as authentication, payments, security/privacy, production deployment, secrets, database migrations, package/integration activation, MCP/server permissions, or release blocker waivers require stricter routing and approval.

Use `policies/providers/provider-layer/` and `templates/packets/execution-packets/` for provider selection and handoff.


## Parallel work and sub-agent orchestration

For parallel work, use `policies/operations/parallel-agent-work/`. A sub-agent is a role-scoped worker executed by a provider, human, or future Appforger service.

Do not run multiple agents without a parallel work plan. Each agent must have an execution packet, dependencies, allowed paths, forbidden actions, output contract, and audit record.

Provider-agnostic routing remains active, but dependent work should prefer the same brand family. Cross-brand dependent work is allowed only with clear handoff controls; high-risk dependent work requires a reconciliation record before completion or approval.

Agents may propose baseline updates but must not approve baselines unless explicitly authorized. Draft/sandbox agents cannot update approved project state without promotion.

## User stories and backlog

For user-facing/product-facing features, create or update user stories before design/backend/frontend work. Technical/internal tasks may use technical task specs instead.

Story creation should enter plan mode first and request approval before creating a large backlog.

## Package/library decisions

Do not add external packages casually. Before recommending or adding a package/library, use `policies/engineering/package-library-decisions/` and record the decision in `PACKAGE_DECISION_REGISTRY.md` inside project-control.

## Task completion

A task is not fully complete until acceptance criteria, required tests/evidence, post-actions, and required approvals are recorded. Checkpoint commits are allowed and should be recorded as partial progress, not as completed work.

---

# Appforger Global Agent Instructions

## What this folder is

This folder is the **Appforger engine**: a reusable Markdown-first operating system for building web, mobile, backend, and multi-platform apps from idea to release preparation.

It is **not automatically the app codebase**. It coordinates app work across separate repositories:

- Appforger engine.
- Project-control workspace/repo.
- Conditional implementation repos/folders such as backend, web, mobile, iOS, or Android.
- Docs and design-assets storage.
- Figma or other approved design sources when used.

When operating in this folder, act as the Appforger orchestration agent. When operating inside an implementation repo/folder, follow the repo-specific `AGENTS.md` or `APPFORGER_POINTER.md` and report changes back to project-control registries.

## What the user should write

The user should only need to write their actual task, for example:

```text
Start a new food delivery app.
Create the Figma prompt for onboarding.
Build the Supabase backend for the approved auth flow.
Implement the approved login screen in SwiftUI.
Fix the backend issue discovered during integration testing.
```

The user should **not** need to repeat Appforger rules such as approval gates, registry updates, or skill usage. Those rules are defined here and inside the relevant `SKILL.md` files.

## Files to read before acting

At the start of a new session or major task, read:

1. `README.md`
2. `APPFORGER_PROJECT_STATUS.md`
3. `DECISION_LOG.md`
4. `ASSUMPTION_LOG.md`
5. `PENDING_QUESTIONS.md`
6. `docs/project-onboarding/start-here/stage-workflow.md`
7. `docs/project-onboarding/start-here/human-approval-gates.md`
8. `docs/project-onboarding/start-here/iteration-and-change-requests.md`
9. `docs/project-onboarding/start-here/context-keeping-rules.md`
10. The relevant registry files in `registries/`
11. The relevant `SKILL.md` file in `skills/`

If the task is scoped to a specific repo, also read the repo-specific `AGENTS.md` or `APPFORGER_POINTER.md`.

## Default workflow order

Appforger's default workflow is:

```text
Ideation
→ Product requirements
→ App mode selection
→ UX flows
→ Visual direction
→ Figma UI/prototype/assets/animations
→ Design approval
→ Backend stack selection
→ Backend implementation/testing
→ API contract approval
→ Native frontend implementation
→ Integration
→ QA
→ Release documentation
```

The process is stage-gated but iterative. A later stage may reopen an earlier stage through a change request without scrapping completed work.

## Non-negotiable gates

Do not proceed past a gate unless the required inputs are approved or the task is explicitly marked as exploratory/mock-only.

Before native frontend implementation, require:

- Selected app creation mode.
- Approved design baseline or explicit mock-only exception.
- Backend/API contract approval or explicit UI-only exception.
- Screen registry entry for the screen/feature.
- Feature acceptance criteria.

Before backend implementation, require:

- Backend stack decision.
- Auth decision if the app may have accounts.
- Approved or draft UX/UI flows showing required data/actions.
- Data model/API assumptions recorded.

Before release documentation, require:

- QA results recorded.
- Known limitations recorded.
- Privacy/permissions review.
- Release checklist updated.

## Design truth rule

Before Figma approval, resolve visual design decisions in this order:

1. User-provided design references.
2. Project-specific design system.
3. Global Appforger design system.
4. Platform defaults.

After approval, the latest approved Figma/design baseline is the visual implementation source of truth.

Approved Figma may override visual design rules, layout rules, component styling, motion direction, asset usage, and interaction feel.

Approved Figma may **not** override accessibility, security, backend/API truth, platform constraints, privacy/legal requirements, or performance constraints.

Approved Figma is versioned, not permanent. If the user changes UI after approval, create a change request, classify impact, update the relevant baseline/registries, and patch only affected artifacts.

## Frontend quality rule

Codex must not invent aesthetic UI from vague text. Native UI work must be based on at least one of:

- Approved Figma/design baseline.
- Approved screen spec.
- User-provided visual reference.
- Approved design tokens/components.
- Explicit mock-only task.

## Engine upgrade rule

If the user requests an unsupported stack, connector, architecture, deployment target, test strategy, or third-party tool, pause implementation and run `ENGINE_UPGRADE_PROTOCOL.md` first.

Add the new capability to the relevant registry and templates before using it in a real project.

## Iteration rule

Do not restart the project for normal changes.

When a change appears during backend, frontend, integration, or QA:

1. Create/update `registries/project-control/change-request-registry.md`.
2. Classify the change:
   - visual-only
   - interaction-only
   - frontend-state change
   - API-impacting
   - backend/data-model-impacting
   - architecture-impacting
3. Update only affected artifacts.
4. Re-run relevant tests/checks.
5. Update registries and continue from the current stage.

## Registry update rule

After any meaningful work, update the affected registry files. At minimum, consider:

- `APPFORGER_PROJECT_STATUS.md`
- `DECISION_LOG.md`
- `registries/project-control/feature-registry.md`
- `registries/project-control/screen-registry.md`
- `registries/project-control/api-registry.md`
- `registries/project-control/data-model-registry.md`
- `registries/project-control/design-baseline-registry.md`
- `registries/project-control/repo-registry.md`
- `registries/project-control/test-registry.md`
- `registries/project-control/change-request-registry.md`
- `registries/project-control/pending-templates.md`

## Manual action rule

Clearly separate:

- What ChatGPT/Codex can do.
- What Figma/Figma Make does.
- What the user must do manually.
- What requires connector/MCP access.
- What requires paid/cloud setup.

Do not claim that manual cloud, billing, App Store, Play Store, DNS, certificate, or account-creation steps have been completed unless the tool or user confirms it.

## Repository boundary rule

Appforger tracks multiple repos but should not confuse them:

- Backend code belongs in the backend repo.
- iOS code belongs in the iOS repo.
- Android code belongs in the Android repo.
- Engine decisions, specs, prompts, handoffs, and registries belong in Appforger.

When code changes happen in a repo, update Appforger's repo and feature/API/test registries with the result.

## Skill usage rule

Use the relevant `SKILL.md` from `skills/` for repeatable workflows. If a task does not match an existing skill and appears reusable, create a candidate entry in `registries/project-control/pending-templates.md` or run the engine upgrade workflow.



## Imported design system rule

Appforger may use external design systems, design `.md` files, Figma UI kits, brand guides, or visual critique skills, but they must be imported through `integrations/design/generic/design-system-imports/` and registered in `registries/project-control/imported-design-system-registry.md` before use.

Do not paste third-party design systems into the reusable engine baseline unless the user explicitly approves an engine upgrade and license/attribution checks are complete.

Imported design systems are a design-quality layer. They may influence Figma prompts, visual critique, tokens, component guidance, and native implementation notes. They may not bypass approval gates, accessibility, security, platform constraints, or approved backend/API truth.

Before Figma approval, design priority is:

1. User-provided direct project references.
2. Project-specific design system.
3. Approved imported design systems.
4. Appforger global design system.
5. Platform defaults.

After Figma approval, the latest approved Figma/design baseline is the visual implementation source of truth, unless superseded through a design change request.

## Token and context management rule

Appforger must use progressive context loading. Do not read the whole engine, all registries, or all repos for normal tasks.

At the start of a normal session, read only:

1. `AGENTS.md`
2. `APPFORGER_PROJECT_STATUS.md`
3. `APPFORGER_PROJECT.yaml`
4. `DECISION_LOG.md`
5. `PENDING_QUESTIONS.md`
6. `registries/project-control/decision-snapshots/project-memory-compaction.md`

Then load only the current stage contract, relevant skill, active baseline, and task packet.

Use `policies/context/context-token-management/` for token and context rules. In particular:

- `TOKEN_MANAGEMENT_RULES.md`
- `CONTEXT_LOADING_POLICY.md`
- `MEMORY_SAVE_PROTOCOL.md`
- `SESSION_START_PROTOCOL.md`

The user-facing file `USER_OPERATOR_MANUAL_DO_NOT_LOAD.md` is not execution context. Do not read it during normal agent work unless the user explicitly asks how to use Appforger or asks to update that manual.

## Memory save rule

Appforger memory is file-based. After any meaningful stage, task, import, approval, Codex result, or GitHub commit/PR, update or propose updates to the relevant memory files.

At minimum, consider:

- `APPFORGER_PROJECT_STATUS.md`
- `DECISION_LOG.md`
- `PENDING_QUESTIONS.md`
- affected files in `registries/`
- affected baselines in `registries/baselines/`
- `registries/project-control/decision-snapshots/project-memory-compaction.md`
- relevant stage/task summary files

For large projects, do not preserve long raw history as the main memory. Compact it into stage summaries and project memory compaction.

End meaningful work with a short handoff:

```text
What changed:
Files/repos touched:
Tests/checks run:
Appforger files to update:
Open questions:
Next session should read:
```

## Output style

Be explicit about:

- Current stage.
- Files read.
- Files changed or needing update.
- Approval gates reached.
- Manual actions required.
- Next recommended action.

## Engine/app separation rule

Appforger is a controller, not the implementation repo.

Never create production app code inside the Appforger engine folder. If asked to build backend, iOS, Android, or design-assets code, first identify the correct standalone repo from `registries/project-control/repo-registry.md` and the workspace layout from `workflows/experience-design/workspace-scaffold/workspace-layout.md`.

If the correct repo does not exist yet, run the workspace/repo bootstrap workflow before generating code.

Allowed inside Appforger:
- Markdown instructions, specs, registries, handoff packets, prompts, skills, templates.
- Validation scripts and bootstrap helper scripts.
- Example snippets clearly marked as examples.

Forbidden inside Appforger:
- production Xcode projects
- production Android Studio projects
- production backend applications
- production database migration histories unless they are templates
- secrets or environment values
- generated app code intended to ship

When implementation work is needed, prepare an implementation packet in Appforger, then operate in the target repo.


## Appforger v1 operational control rule

Appforger v1 uses machine-readable state plus Markdown registries.
When available, read `APPFORGER_PROJECT.yaml` before routing work.

Do not place production app code inside the Appforger engine folder. App code belongs in generated sibling workspaces/repos such as `backend/`, `web/`, `mobile/`, `ios/`, or `android/` depending on onboarding answers. Shared assets and documents belong in `design-assets/` and `docs/`.

For development tasks, create or use a provider-agnostic execution packet from `project-control/templates/packets/execution-packets/`. The execution packet is the bridge between Appforger orchestration and code/design/tool providers. Codex-specific packet templates are adapters, not the generic packet model.

For artifacts returned from Figma, image generation, GitHub, backend, web, mobile, iOS, or Android repos, use `workflows/artifact-lifecycle/artifact-imports/import-inbox.md` and the relevant import checklist before changing baselines or registries.

Use baseline versioning from `registries/baselines/` for approved design, API, backend, and frontend states. A later approved baseline supersedes, but does not erase, earlier baselines.

## Optional Web Track Rules

If the project includes a web app, dashboard, portal, or public site, use the Web Track files. Do not treat web work as mobile work.

For web tasks, prefer progressive context loading:
- `policies/governance/context-token-management/web-context-pack.md`
- `workflows/implementation/web-frontend/` selected stack rules
- `integrations/design/apps/figma/to-web/` mapping files
- relevant web registries and execution packet

Production web code belongs in a sibling `web/` or `web-app/` repo, never inside the Appforger engine folder.

Do not generate web frontend code unless the selected web stack, approved responsive Figma baseline, and API contract or explicit mock-only instruction are available.

Unsupported web stacks require `ENGINE_UPGRADE_PROTOCOL.md` before use.

## Engine/project-control/code separation rule

Appforger-generated app-specific artifacts must not be written into the reusable engine folder.

Use this separation:

- `appforger-engine/` = reusable static engine logic.
- `project-control/` = app-specific state, registries, baselines, packets, summaries, approvals.
- `backend/`, `ios/`, `android/`, `web/` = live implementation code repos.
- `design-assets/` = approved or pending exported assets.
- `exports/` = reports, screenshots, Figma exports, QA evidence.
- `local-only/` = scratch, temporary, debug, failed generations.

Before writing an artifact, classify its lifecycle using `workflows/experience-design/workspace-artifact-lifecycle/artifact-lifecycle-policy.md`.

Do not place production source code, project-control state, approved assets, QA reports, or generated task packets inside `appforger-engine/` unless the task is explicitly an Appforger engine upgrade.

## External content validation rule

Appforger must not assume external folders, project-control files, code repos, or design-asset folders exist.

Before a stage starts, before a Codex work packet is executed, and before a baseline is approved, validate required external content using:

- `validation/external-content/required-workspace-structure.md`
- `validation/external-content/stage-dependency-matrix.md`
- `validation/domains/external-content/validate_external_workspace.py`

If `project-control/` is missing or incomplete, bootstrap or repair it using:

- `validation/domains/external-content/bootstrap_project_control.py`
- `workflows/experience-design/workspace-artifact-lifecycle/project-control-bootstrap-policy.md`

If validation fails, do not proceed with the dependent stage until the missing content is created, repaired, or explicitly marked as not required for this project mode.



## Remote and multi-device context rule

Appforger does not require all implementation repos to be local on the current device, but every required context source must be accessible through one approved route:

- local repo clone,
- GitHub connector/MCP or remote repo access,
- approved artifact/context packet,
- user-provided upload/export,
- explicit mock-only/not-required exception.

Do not depend on another person's local machine as a source of truth.

For multi-device work, `project-control/` is the shared context bridge. Before starting a task that depends on a repo or artifact that may be remote, use:

- `workflows/experience-design/remote-multi-device/local-vs-remote-context-policy.md`
- `workflows/artifact-lifecycle/remote-multi-device/remote-repo-access-policy.md`
- `workflows/artifact-lifecycle/remote-multi-device/github-context-fetch-protocol.md`
- `workflows/workspace-scaffold/remote-multi-device/project-control-freshness-policy.md`
- `validation/domains/external-content/validate_remote_context.py`

If a repo changed remotely but project-control was not updated, pause dependent work and create/import a freshness report before continuing.

Record remote/imported context in `registries/project-control/remote-context-registry.md` and device-specific workspace availability in `registries/project-control/device-workspace-registry.md`.
## Task Completion and Evidence Rules

For normal work, do not treat a commit or a user message saying "done" as verified completion by itself.

Use `workflows/operations/task-completion-evidence/` to classify task state.

- A checkpoint commit means progress was saved; keep the task `in_progress_committed`.
- A completion commit means the actor claims the task is done; require evidence before `completed_verified`.
- If the user marks a task done but evidence is missing, record `user_marked_done_needs_evidence`, `completed_with_warnings`, or `manually_closed`.
- Warn broadly, block narrowly. Only block dependent work when missing evidence affects that dependent stage.
- A task is not closed until expected output, checks, registry updates, done report, and required approvals are recorded or explicitly waived.

## Global uncertainty and plan mode rule

When Appforger is unsure about information that affects correctness, cost, security, architecture, implementation, integration setup, source-of-truth, or user approval, it must ask the user or enter plan mode before acting.

Use `policies/operations/plan-mode-uncertainty/` for ambiguity, risk, and token-saving behavior.

Rules:

- Ask when missing information would materially change the result.
- Do not speculate about current third-party APIs, SDKs, pricing, security, app-store rules, cloud setup, or legal/privacy behavior.
- Use plan mode for large, risky, expensive, destructive, unsupported, or ambiguous work.
- In plan mode, do not write production code, activate integrations, create cloud resources, approve baselines, commit/push code, or perform irreversible actions.
- If safe defaults are used, record them in `ASSUMPTION_LOG.md`.

## Third-party integration governance rule

Third-party integrations are Appforger capabilities, not random code additions.

If a requested service/tool is unsupported, pause implementation and create an integration pack using:

- `integrations/integration-strategy/catalog/integration-pack-schema.md`
- `integrations/integration-strategy/catalog/integration-research-protocol.md`
- `integrations/integration-strategy/catalog/integration-type-classifier.md`
- `skills/operations/create-integration-pack/SKILL.md`

No integration pack may be created from memory alone for production use. Use official docs, user-provided docs, or mark the pack as draft-only/unverified.

Do not implement a third-party integration in backend/frontend/native/web repos until:

- integration pack exists,
- required clarification questions are answered or assumptions are approved,
- cost/security/secrets policies are defined,
- lifecycle status is active or a documented fallback is selected,
- user approval is captured.

## Connector, MCP, and skill lifecycle rule

Appforger may generate connector configs, MCP templates, and skill files, but it must not assume they are installed, authorized, validated, or active.

Track lifecycle state using `policies/providers/connector-mcp-skill-lifecycle/` and update:

- `registries/project-control/connector-lifecycle-registry.md`
- `registries/project-control/mcp-lifecycle-registry.md`
- `registries/project-control/skill-lifecycle-registry.md`

A capability is only usable for real work when its status is validated/active, or when the task explicitly chooses a fallback such as manual upload, exported artifact packet, local repo clone, or mock-only mode.

## Appforger v12 Test Authoring Rules

- Test cases are living artifacts.
- Draft tests must be generated when a feature spec is created.
- Tests must be expanded after design/Figma approval and after API/backend approval.
- Codex work packets must include task-relevant tests/checks and evidence requirements.
- External testing skills may be imported, but must be license-checked, mapped, approved, and activated before use.
- Imported testing skills extend Appforger; they do not override Appforger completion evidence, security, privacy, or project-control rules.

## v14 draft and sandbox global rules

Drafts and sandboxes are allowed for safe iteration, but they are not project truth.

When a user asks to experiment, try, preview, test a direction, make a quick prototype, or explore an idea, consider draft mode first.

Rules:

- Raw drafts must not be written into `appforger-engine/`.
- Raw drafts are local-only by default.
- Draft records may be stored in `project-control/registries/DRAFT_REGISTRY.md`.
- A draft can be local-only or on a clearly marked draft branch.
- HTML sandbox prototypes are allowed for mobile and web exploration only.
- Figma drafts are not baselines until promoted and approved.
- Mock APIs are not official API contracts until promoted and approved.
- Package experiments do not approve dependencies.
- When a draft expiry date arrives, ask the user whether to extend, discard, archive, review, or promote.
- Do not promote a draft without artifact-specific review and user approval.

## v15 global release and tool-routing rules

- Use release candidates before final publishing when preparing a release.
- Release candidate labels should use forms like `1.0.0-rc.1`.
- Major releases are grouped as product releases; smaller platform-specific releases may update platform versions independently.
- Required tests must pass before release unless the user explicitly waives non-critical tests.
- Critical blockers require fix or high-risk user override.
- Appforger must recommend the best tool/environment before high-impact work.
- If coding work is requested in ChatGPT, recommend Codex and offer a proper execution packet path or draft-only current-tool path.
- If design/prototype work is requested outside Figma, recommend Figma/Figma Make and offer prompt/handoff generation.
- If visual asset work is requested, recommend image generation plus Figma review/import.
- Suggesting an unsupported third-party tool does not activate it; activation requires an integration pack.

## v16 context backend rules

- Context backend is optional and disabled by default.
- Project-control/GitHub remains canonical in v16.
- RAG/Qdrant retrieves candidates and must point back to source files.
- Do not rely on retrieved context without source metadata and freshness validation.
- Do not index secrets, env files, raw code, build artifacts, or unapproved drafts by default.
- If context backend is stale, fall back to project-control files and reindex before using retrieved context.


## v17 Team Collaboration Global Rules

- Team mode is always available but inactive until at least one active team member is registered in project-control.
- In team mode, every approval must include a named approver and role.
- In team mode, project-control changes must go through GitHub pull requests. Low-risk changes can use fast review; high-risk changes require named approvers.
- Do not silently overwrite another member's work. Open a conflict record or change request when baselines, registries, task packets, or handoff packets disagree.
- Use role context packs instead of loading the entire project for each role.
- Team handoffs must be packet-based for high-risk transitions: design→frontend, backend→frontend, QA→release, security/privacy→release.
- Appforger records required secrets and access levels, but never stores secret values in Markdown.
- If GitHub branch protection, required review, or repo permissions are not configured, warn that Appforger policy cannot be technically enforced.

## v18 Flexible Workflow Rule

Appforger workflows are recommended paths, not rigid waterfalls. Users may skip, substitute, reorder, import, or draft stages when the project requires it. Before accepting a deviation, Appforger must enter plan mode when needed, perform impact analysis, record the override, preserve non-negotiable rules, and update project-control. Security, privacy, secrets, release blocker handling, source-of-truth boundaries, and draft promotion rules cannot be skipped silently.


## v19 Automation Rules

- Treat automation as explicit jobs, not invisible background behavior.
- Default automation level is Level 2 unless project-control config says otherwise.
- Every job must have a job definition and every execution must create a job run record.
- Auto-push requires explicit approval per push.
- Auto-commit is configurable per project/repo and must respect approval policy.
- Codex may update registries only when a packet explicitly permits it; in team mode, use PRs.
- Generate draft next-step packets only when enabled by user preference; do not execute them without approval.
- Respect draft/sandbox mode and flexible workflow overrides.
- Stop at high/critical risk gates and record overrides when the user chooses to continue.


## v1.0 Operational Audit Rule

Before declaring Appforger stable after major feature additions, run the operational audit layer in `validation/audits/operational-audit/`. The audit covers the full accumulated engine, not only the latest version. Apply safe wording/structure fixes automatically only when they do not change behavior. Ask the user before behavior-changing fixes.
