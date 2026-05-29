# Create Business Requirements Document

Use this prompt when a user needs to create or import the mandatory Business Requirements Document (BRD) for an Appforger project.

Return a plan only unless the user explicitly authorizes local file changes.

Required behavior:

- Treat the BRD as mandatory for real app-building work.
- If the user has a BRD template, store the project-specific copy under `project-control/requirements/` and register it in `project-control/registries/requirements-document-registry.md`.
- If the user does not have a template, use `templates/specifications/business-requirements-document-template.md`.
- Keep the BRD above the product brief.
- Block UX, design, backend/API, frontend, QA, and release work until the BRD is approved, draft-only, or waived with risk recorded.
- Preserve requirement IDs for traceability into features, screens, APIs/data, and tests.

Return:

- BRD source/template decision;
- target project-control paths;
- required questions;
- assumptions to record;
- approval gate;
- downstream artifacts that must reference the BRD.
