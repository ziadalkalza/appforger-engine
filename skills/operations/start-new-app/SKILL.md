# Start New App

## Purpose
Create a clean app workspace and initial Appforger state without generating production app code.

## Inputs
- APPFORGER_PROJECT_STATUS.md
- APPFORGER_PROJECT.yaml
- Relevant registry files

## Outputs
- New app workspace checklist
- Initial app config
- Initial project registries

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
