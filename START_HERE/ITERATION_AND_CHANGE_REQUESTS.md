# Iteration and Change Requests

AppForge is not waterfall. It is stage-gated and iterative.

## When to create a change request

Create a change request when:

- UI changes after design approval.
- Backend changes after API approval.
- Frontend implementation exposes a design issue.
- Integration exposes backend/API mismatch.
- QA finds a defect.
- The user changes scope.
- A new stack/tool/integration is requested.

## Change classification

Classify each request as one or more:

- `visual_only`
- `interaction_only`
- `frontend_state`
- `api_impacting`
- `backend_data_model_impacting`
- `security_impacting`
- `performance_impacting`
- `release_impacting`
- `engine_upgrade_required`

## Workflow

```text
Open change request
→ classify impact
→ identify affected files/repos
→ update relevant source of truth
→ approve if required
→ patch affected implementation
→ rerun relevant tests
→ update registries
→ close change request
```

## UI change after Figma approval

Approved Figma is current truth, not permanent truth.

If UI changes during frontend development:

```text
Create UI change request
→ update Figma or screen spec
→ approve new design baseline
→ check API/backend impact
→ patch SwiftUI/Compose
→ continue
```

## Backend change after frontend starts

If frontend testing reveals backend issue:

```text
Create backend change request
→ check whether API contract changes
→ patch backend
→ rerun backend/API tests
→ update API registry if needed
→ patch frontend integration if needed
→ continue
```

## Change request template

```md
### CR-0001: Title

- Date:
- Requested by:
- Current stage:
- Type:
- Reason:
- Affected artifacts:
- Affected repos:
- Impact:
- Requires approval: yes/no
- Required tests:
- Status: open | in_progress | approved | implemented | tested | closed
```
