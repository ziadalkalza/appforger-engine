# How To Use Appforger

## For a new app

1. Copy this Appforger folder into a new workspace or create a new repo from it.
2. Fill `APPFORGER_PROJECT_STATUS.md`.
3. Choose the app creation mode in `docs/project-onboarding/start-here/project-creation-modes.md`.
4. Fill `templates/specifications/product-brief-template.md` into the active product brief.
5. Run the workflow in `docs/project-onboarding/start-here/stage-workflow.md`.
6. Use agents from `workflows/operations/agents/`.
7. Use skills from `skills/`.
8. Keep all registries updated.


## One-time Codex setup

Appforger includes root `AGENTS.md`. This is the global instruction file that tells Codex what Appforger is, where work belongs, and which rules apply automatically.

For separate code repositories, copy the relevant template from `docs/ai-clients/providers/codex/`:

- `BACKEND_REPO_AGENTS_TEMPLATE.md` ? backend repo `AGENTS.md`
- `IOS_REPO_AGENTS_TEMPLATE.md` ? iOS repo `AGENTS.md`
- `ANDROID_REPO_AGENTS_TEMPLATE.md` ? Android repo `AGENTS.md`
- `APPFORGER_POINTER_TEMPLATE.md` ? each code repo `APPFORGER_POINTER.md`

After this setup, your normal prompts should focus on the actual app task. You should not need to repeat global rules like approval gates, registry updates, or skill usage.

## Conversation starter prompt

Use this prompt in ChatGPT or Codex when starting a new app if the session has not loaded `AGENTS.md` yet:

```text
You are operating inside the Appforger engine. Read README.md, APPFORGER_PROJECT_STATUS.md, DECISION_LOG.md, ASSUMPTION_LOG.md, PENDING_QUESTIONS.md, docs/project-onboarding/start-here/stage-workflow.md, and the relevant registries before acting.

Do not generate app code yet. First create or update the product brief, choose the app mode, identify required external tools, and list the next approval gates.
```

## Main principle

Every artifact must be traceable:

```text
decision ? spec ? design/API/backend/frontend task ? implementation ? test ? registry update
```

## Do not do this

- Do not let Codex invent aesthetic UI.
- Do not skip Figma approval before native frontend implementation.
- Do not add unsupported stacks without engine upgrade.
- Do not hardcode secrets into docs or code.
- Do not automate paid/cloud resources without explicit approval.

## Template default rule

Appforger outputs are template-first by default.

Precedence order:

1. Use a relevant template override from `project-control` when present.
2. Otherwise use the matching template in `appforger-engine/templates/`.
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

- `docs/project-onboarding/operator-guides/README.md`
- `docs/project-onboarding/operator-guides/setup-and-first-run.md`
- `docs/project-onboarding/operator-guides/features-and-activities.md`
- `docs/getting-started/operator-guides/FEATURE_GUIDES/`

Use those files as the main operator guide for Appforger features and activities.
