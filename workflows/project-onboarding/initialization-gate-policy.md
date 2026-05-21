# Initialization Gate Policy

## Purpose

The initialization gate prevents Appforger from making incorrect workflow assumptions when first added to a project.

When a project has no saved onboarding profile, Appforger must automatically trigger onboarding on the first project-work request, pause high-impact work, ask the minimal required setup questions, save the answers, generate active rules, then resume the original user task.

## Gate states

```yaml
initialization_status: not_started | in_progress | complete_minimal | complete_full | needs_update
```

## What is blocked until minimal onboarding is complete

- Implementation planning that depends on platform/backend/provider choices.
- Execution packet generation.
- Figma/design workflow activation.
- Backend/frontend setup.
- Context backend indexing.
- Team operations backend activation.
- Automation job creation or execution.
- Package/integration activation.

## What is allowed before onboarding

- Conceptual questions about Appforger.
- Help using the engine.
- Explanation of folders, stages, packets, providers, context, docs, team mode, or automation.

## Auto-trigger rule

Onboarding must not wait for a user to explicitly say "start onboarding".
If the user asks for real project work and initialization is incomplete, Appforger must immediately start the onboarding gate flow and preserve the original request for automatic resume.

## Critical vs non-critical unknowns

Non-critical questions may be stored as `unknown_pending`.

Critical questions cannot remain unknown if they block the requested workflow. Appforger must explain why the answer is needed and provide recommended choices.
