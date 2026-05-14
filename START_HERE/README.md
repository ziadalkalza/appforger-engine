# AppForger v1

Start here:
- `START_HERE/START_HERE_FOR_AGENTS.md` for first-time agent setup.
- `START_HERE/SETUP_AND_FIRST_RUN_GUIDE.md` for manual setup.
- `NEW_APP_INITIALIZER/setup_appforge_project.py` for the easy workspace initializer.

This engine is distributed engine-only. The zip root must contain only `appforge-engine/`.


# AppForger v1 Engine

AppForger v1 is distributed as an **engine-only package**.

The zip contains only the reusable `appforge-engine/` folder. It does not contain live app code, a real `project-control/`, or generated workspace folders at the package root.

## Package structure

```text
AppForger_v1/
  appforge-engine/
```

Inside the engine are reusable rules, Markdown blueprints, skills, validators, initializer logic, examples, and templates.

Templates for generated project folders live inside:

```text
appforge-engine/ENGINE_TEMPLATES/
  project-control-template/
  workspace-template/
```

## Generated workspace structure

During onboarding/setup, AppForger creates project-specific folders outside the engine in the real workspace.

Example:

```text
my-app-workspace/
  appforge-engine/       # reusable engine copy/submodule
  project-control/       # generated from project-control-template
  docs/                  # shared project documents or links
  design-assets/         # approved/pending visual assets
  exports/               # generated evidence/reports/handoffs
  local-only/            # scratch/drafts/debug, normally not committed
  backend/               # only if backend is selected/needed
  web/                   # only for web projects
  mobile/                # generic mobile/Flutter/React Native track
  ios/                   # native iOS track only
  android/               # native Android track only
```

Implementation folders are conditional. For example, a web-only project gets `web/` but not `ios/` or `android/`; a generic mobile project gets `mobile/`; a native iOS+Android project gets `ios/` and `android/`.

## Source-of-truth boundaries

```text
appforge-engine/ = reusable engine logic and templates
project-control/ = project state, decisions, registries, baselines, packets
docs/ = shared project documents
design-assets/ = reusable visual assets
exports/ = generated evidence and reports
local-only/ = temporary private scratch work
backend/web/mobile/ios/android/ = real implementation code
```

The engine should not absorb app-specific code or live project state. Project-specific scripts/configs/integration instances are generated into `project-control/`, not stored as active runtime files in the engine.

## Start here

1. Read `AGENTS.md`.
2. Run or follow `PROJECT_ONBOARDING_AND_INITIALIZATION/` to answer setup questions.
3. Use `NEW_APP_INITIALIZER/` to create the external workspace folders.
4. Continue through the workflow selected by onboarding.


## Code Context Sources update

AppForger v1 now includes Code Context Sources under `CONTEXT_SYNC_AND_RETRIEVAL/code_context_sources/`.

For ongoing projects, onboarding asks whether the project is active. If yes, AppForger requires an initial code context bootstrap before code-aware implementation. Code sources may be local, remote Git, uploaded snapshot, CI-generated context, or summary-only.

Users fill sensitive/access/runtime variables in one private local file:

```text
local-only/.env.local
```

Project-control stores only generated metadata and references. Secret values and repo credentials stay outside project-control and context indexes.

## Feature completeness and validation

This engine includes a feature manifest at `REGISTRIES/APPFORGE_FEATURE_MANIFEST.json` and an audit note at `FEATURE_STATUS_AUDIT.md`. Some operational integrations are runnable scaffolds rather than production-complete cloud/provider SDKs. Run `python VALIDATION/validate_all.py --deep` from inside `appforge-engine/` or `python appforge-engine/VALIDATION/validate_all.py --deep` from the workspace root to verify the package structure.

## AppForger operator documentation

For the complete feature/activity index and practical how-to guides, read:

- `HOW_TO_USE_APPFORGE/README.md`
- `HOW_TO_USE_APPFORGE/SETUP_AND_FIRST_RUN.md`
- `HOW_TO_USE_APPFORGE/FEATURES_AND_ACTIVITIES.md`
