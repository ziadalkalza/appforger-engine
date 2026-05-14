# Run Security Review

## Purpose
Apply AppForge security/privacy checklists to a feature, backend, or release.

## Inputs
- APPFORGE_PROJECT_STATUS.md
- APPFORGE_PROJECT.yaml
- Relevant registry files

## Outputs
- Security checklist result
- Risks
- Required fixes

## Steps
1. Read the current AppForge state.
2. Confirm engine/app-code separation.
3. Perform the workflow described by this skill.
4. Update affected registries.
5. Produce a done report and next-step recommendation.

## Approval gates
Do not promote outputs to an approved baseline without explicit user approval.

## Failure handling
If required inputs are missing, create an open question or task packet instead of guessing.
