# Engine Overview

## What AppForger is

AppForger is a reusable app-building engine for planning, designing, implementing, testing, and releasing apps through controlled workflows, execution packets, registries, validators, and project-specific rules.

## Engine-only distribution

The distributed zip contains only:

```text
AppForger_v1/appforge-engine/
```

All real project folders are generated later by onboarding/setup from templates inside the engine.

## What AppForger is not

- It is not a one-click app generator.
- It is not a place to store live app code.
- It is not the canonical storage for project documents.
- It does not silently create cloud accounts, paid resources, production secrets, releases, or deployments.
- It does not run background jobs unless a model/tool/runner with execution access is used.

## Core boundaries

```text
appforge-engine/ = reusable logic, policies, blueprints, templates, validators
project-control/ = app-specific memory, decisions, baselines, execution packets
docs/ = shared project documents outside project-control
exports/ = generated reports/evidence
local-only/ = temporary drafts/debug
implementation folders = backend/web/mobile/ios/android as selected
```

## Core v1 capabilities

- onboarding questionnaire and active project rules
- conditional workspace generation
- provider/model/tool routing
- provider-agnostic execution packets
- parallel work and sub-agent orchestration
- team operations backend planning/state model
- project docs library and stronger context backend
- script and integration blueprints
- project engine overrides
- draft/sandbox mode
- flexible workflows and stage overrides
- testing/QA and release preparation
- automation job policy/templates

## Context and truth rule

RAG/context backends retrieve relevant context and source references. They do not replace canonical project-control, docs, Figma/design baselines, or implementation repos.
