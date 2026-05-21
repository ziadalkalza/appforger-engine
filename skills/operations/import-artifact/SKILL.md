# Import Artifact

## Purpose
Review and register artifacts returned from Figma, image generation, GitHub, backend, iOS, Android, or user uploads.

## Inputs
- APPFORGER_PROJECT_STATUS.md
- APPFORGER_PROJECT.yaml
- Relevant registry files

## Outputs
- Import inbox entry
- Review result
- Registry/baseline updates needed

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
