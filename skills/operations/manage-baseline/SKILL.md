# Manage Baseline

## Purpose
Create, supersede, or diff approved baselines for design, API, backend, or frontend.

## Inputs
- APPFORGER_PROJECT_STATUS.md
- APPFORGER_PROJECT.yaml
- Relevant registry files

## Outputs
- Baseline entry
- Diff summary
- Impact classification

## Steps
1. Read the current Appforger state.
2. Confirm engine/app-code separation.
3. Perform the workflow described by this skill.
4. Update affected registries.
5. Produce a done report and next-step recommendation.

## Approval gates
Do not promote outputs to an approved baseline without explicit user approval.

## Failure handling
If required inputs are missing, create an open question or task packet instead of guessing.
