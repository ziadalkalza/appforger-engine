# How To Use AppForge

## For a new app

1. Copy this AppForge folder into a new workspace or create a new repo from it.
2. Fill `APPFORGE_PROJECT_STATUS.md`.
3. Choose the app creation mode in `START_HERE/PROJECT_CREATION_MODES.md`.
4. Fill `TEMPLATES/product_brief_template.md` into the active product brief.
5. Run the workflow in `START_HERE/STAGE_WORKFLOW.md`.
6. Use agents from `AGENTS/`.
7. Use skills from `SKILLS/`.
8. Keep all registries updated.


## One-time Codex setup

AppForge includes root `AGENTS.md`. This is the global instruction file that tells Codex what AppForge is, where work belongs, and which rules apply automatically.

For separate code repositories, copy the relevant template from `CODEX_BOOTSTRAP/`:

- `BACKEND_REPO_AGENTS_TEMPLATE.md` → backend repo `AGENTS.md`
- `IOS_REPO_AGENTS_TEMPLATE.md` → iOS repo `AGENTS.md`
- `ANDROID_REPO_AGENTS_TEMPLATE.md` → Android repo `AGENTS.md`
- `APPFORGE_POINTER_TEMPLATE.md` → each code repo `APPFORGE_POINTER.md`

After this setup, your normal prompts should focus on the actual app task. You should not need to repeat global rules like approval gates, registry updates, or skill usage.

## Conversation starter prompt

Use this prompt in ChatGPT or Codex when starting a new app if the session has not loaded `AGENTS.md` yet:

```text
You are operating inside the AppForge engine. Read README.md, APPFORGE_PROJECT_STATUS.md, DECISION_LOG.md, ASSUMPTION_LOG.md, PENDING_QUESTIONS.md, START_HERE/STAGE_WORKFLOW.md, and the relevant registries before acting.

Do not generate app code yet. First create or update the product brief, choose the app mode, identify required external tools, and list the next approval gates.
```

## Main principle

Every artifact must be traceable:

```text
decision → spec → design/API/backend/frontend task → implementation → test → registry update
```

## Do not do this

- Do not let Codex invent aesthetic UI.
- Do not skip Figma approval before native frontend implementation.
- Do not add unsupported stacks without engine upgrade.
- Do not hardcode secrets into docs or code.
- Do not automate paid/cloud resources without explicit approval.

## Template default rule

AppForge outputs are template-first by default.

Precedence order:

1. Use a relevant template override from `project-control` when present.
2. Otherwise use the matching template in `appforge-engine/TEMPLATES/`.
3. Use freeform structure only when the user explicitly asks not to use templates.

## Docs classification default

When writing project docs outside `project-control`, classify artifacts by doc type:

1. `docs/product`
2. `docs/requirements`
3. `docs/ux_ui`
4. `docs/api_backend`
5. `docs/architecture`
6. `docs/delivery`
7. `docs/qa`
8. `docs/operations`
9. `docs/governance`
10. `docs/assets_imports`

Use this structure by default unless a project-specific docs convention overrides it.

## Full how-to documentation

The complete feature and activity documentation now lives in:

- `HOW_TO_USE_APPFORGE/README.md`
- `HOW_TO_USE_APPFORGE/SETUP_AND_FIRST_RUN.md`
- `HOW_TO_USE_APPFORGE/FEATURES_AND_ACTIVITIES.md`
- `HOW_TO_USE_APPFORGE/FEATURE_GUIDES/`

Use those files as the main operator guide for AppForger features and activities.
