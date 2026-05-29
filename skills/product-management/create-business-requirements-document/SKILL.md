# Create Business Requirements Document

## Purpose

Create or import the mandatory Business Requirements Document (BRD) that sits above the product brief and drives design, build, QA, and release decisions.

## When to use

Use this skill during the Product requirements stage before creating or approving the product brief, UX flows, Figma work, backend/API contracts, frontend implementation packets, or QA plans.

## Inputs

- Existing user BRD or BRD template, if provided.
- Raw app idea, product brief draft, stakeholder notes, source documents, or onboarding answers.
- Business constraints, platform goals, integrations, compliance/security/privacy needs, timeline and release expectations.

## Outputs

- Business Requirements Document.
- Requirements document registry entry.
- Open questions and assumptions.
- BRD-to-product-brief alignment notes.
- Traceability seeds for features, screens, APIs/data, and tests.

## Required context files

- `APPFORGER_PROJECT_STATUS.md`
- `DECISION_LOG.md`
- `ASSUMPTION_LOG.md`
- `PENDING_QUESTIONS.md`
- `templates/specifications/business-requirements-document-template.md`
- `project-control/requirements/business-requirements-document.md`
- `project-control/registries/requirements-document-registry.md`
- `workflows/product/business-requirements/business-requirements-workflow.md`

## Rules

- The BRD is mandatory for real app-building work.
- If the user provides a template, use it for the project-specific BRD and store it under `project-control/requirements/`.
- Do not add a user-provided template to the reusable engine unless the user explicitly approves an engine upgrade.
- If no user template exists, use the engine BRD template.
- The BRD sits above the product brief. Product brief content must be derived from or reconciled with the BRD.
- Do not proceed to UX/design/build stages unless the BRD is approved, explicitly draft-only, or waived with risks recorded.
- Give every business requirement a stable ID and preserve traceability into features, screens, APIs/data, and tests.
- Record missing information in `PENDING_QUESTIONS.md` and reversible assumptions in `ASSUMPTION_LOG.md`.

## Steps

1. Read current project state and requirements registry.
2. Determine whether the user supplied an existing BRD or template.
3. If a user template exists, copy its structure into the project-specific BRD without promoting it into the engine.
4. If no template exists, use `templates/specifications/business-requirements-document-template.md`.
5. Populate business context, objectives, stakeholders, scope, requirements, constraints, risks, open questions, and traceability.
6. Generate or update the product brief only after BRD alignment is clear.
7. Update the requirements document registry.
8. Update downstream registries with requirement IDs where applicable.
9. Request approval before allowing Product requirements to close.

## Approval gates

User approval is required before app mode selection, UX/design work, backend/API work, or implementation work begins.

## Failure handling

If the BRD cannot be completed, keep the Product requirements stage open, document blockers, and allow only explicitly marked exploration or draft work.

## Handoffs

Every design, backend, API, frontend, QA, or release packet created after this skill must reference the active BRD path and relevant requirement IDs.
