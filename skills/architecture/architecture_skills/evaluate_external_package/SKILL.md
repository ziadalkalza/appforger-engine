# Skill: evaluate_external_package/SKILL

## Purpose

Evaluate whether to use an external package or build manually. Research current package docs/registry data, ask user, and record the decision.

## Required context

- External `project-control/APPFORGE_PROJECT_STATUS.md`
- External `project-control/APPFORGE_PROJECT.yaml`
- Relevant registry files
- Relevant stage/feature/story packet

## Rules

- Enter plan mode when scope is broad or unclear.
- Ask when not sure.
- Do not write live project outputs inside `appforge-engine/`.
- Update external project-control only after approval where required.
- Record post-actions and evidence when the task is complete.

## Output

A focused artifact, registry update plan, and next recommended action.
