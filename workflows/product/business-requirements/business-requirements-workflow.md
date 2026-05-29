# Business Requirements Workflow

The Business Requirements Document (BRD) is mandatory for real app-building work.

## Purpose

Create or import a BRD that becomes the business source of truth above the product brief, user stories, UX flows, design, backend/API, implementation, QA, and release work.

## Inputs

- User-provided BRD template or existing BRD, if available.
- Raw app idea, product brief, notes, stakeholder goals, or source documents.
- Known constraints, assumptions, integrations, budget/timeline limits, compliance needs, and launch expectations.

## Template rule

If the user provides a BRD template, store the project-specific copy under `project-control/requirements/` and record it in `project-control/registries/requirements-document-registry.md`.

Do not promote a user-provided template into the reusable engine unless the user explicitly approves it as an engine upgrade and any license/ownership concerns are resolved.

If the user does not provide a template, use `templates/specifications/business-requirements-document-template.md`.

## Required outputs

- `project-control/requirements/business-requirements-document.md`
- `project-control/registries/requirements-document-registry.md` entry
- Product brief alignment notes or generated product brief
- Open questions in `project-control/pending-questions.md`
- Assumptions in `project-control/assumption-log.md`
- Decisions in `project-control/decision-log.md`

## BRD content requirements

At minimum, the BRD must define:

- business context and objectives;
- stakeholders and target users;
- in-scope and out-of-scope work;
- business requirements with stable IDs;
- functional requirements and non-functional requirements;
- data, integration, security, privacy, accessibility, and operational requirements where relevant;
- design/UX implications;
- backend/API implications;
- risks, dependencies, and open questions;
- traceability from requirements to features, screens, APIs/data, and tests.

## Downstream use

The BRD sits above the product brief. Later artifacts must either reference the BRD or record a waiver:

- Product brief derives the concise product direction from the BRD.
- User stories and feature registry entries trace to BRD requirement IDs.
- UX flows and screen specs cover BRD user, scope, and edge-case requirements.
- Visual direction and Figma prompts respect BRD constraints and success criteria.
- Backend stack, data model, API contracts, and integrations cover BRD data, security, privacy, and operational requirements.
- Frontend/native/web implementation packets reference BRD-linked features and acceptance criteria.
- QA plans and test cases include BRD acceptance signals and non-functional requirements.

## Approval gate

Do not proceed past Product requirements into UX/design/build stages until:

- the BRD is approved, or
- the user explicitly approves a draft-only/mock-only exception, or
- an approved waiver is recorded with affected stages and risks.

## Failure handling

If the BRD cannot be completed because required information is missing, record blocking questions in `pending-questions.md`, record reversible assumptions in `assumption-log.md`, and keep downstream work blocked except for explicitly marked exploration.
