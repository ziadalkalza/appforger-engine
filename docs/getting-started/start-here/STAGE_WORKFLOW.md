# Stage Workflow

AppForge is stage-gated but iterative.

## Default stages

```text
S0 Engine setup
S1 Ideation
S2 Product requirements
S3 App mode selection
S4 UX flows
S5 Visual direction
S6 Figma UI/prototype/assets/animations
S7 Design approval
S8 Backend stack selection
S9 Backend implementation/testing
S10 API contract approval
S11 Native frontend implementation
S12 Integration
S13 QA
S14 Release documentation
```

## Stage outputs

### S1 Ideation

- Product concept.
- Target user.
- Problem/value.
- Success criteria.

### S2 Product requirements

- Product brief.
- MVP scope.
- Feature registry.
- Non-goals.

### S3 App mode selection

- One selected app creation mode.
- Platform strategy.
- Repo strategy.

### S4 UX flows

- User journeys.
- Screen map.
- Navigation model.
- Edge cases.

### S5 Visual direction

- Brand direction.
- Asset needs.
- Image-generation prompts.
- Design references.

### S6 Figma work

- Figma file.
- Prototype.
- Components.
- Animation notes.
- Exportable assets.

### S7 Design approval

- Approved design baseline.
- Screen registry updated.
- Design asset registry updated.

### S8 Backend stack selection

- Supabase or FastAPI + PostgreSQL.
- Auth decision.
- Deployment path.

### S9 Backend implementation/testing

- Database schema.
- Auth setup if needed.
- Backend endpoints/functions.
- Local/free-cloud test.

### S10 API contract approval

- Approved API contract.
- Data models.
- Error states.
- Integration rules.

### S11 Native frontend implementation

- SwiftUI app/code if selected.
- Kotlin Compose app/code if selected.
- Screen-by-screen implementation from approved Figma.

### S12 Integration

- App-to-backend wiring.
- Environment configs.
- Auth/session handling.
- Error handling.

### S13 QA

- Unit tests.
- Integration tests.
- API tests.
- UI tests.
- Manual QA.
- Accessibility.
- Performance.
- Security review.

### S14 Release documentation

- App store docs.
- Play Store docs.
- Backend production checklist.
- Privacy/permissions checklist.
- Release notes.

## Iteration

If a later stage exposes a problem, use `docs/getting-started/start-here/ITERATION_AND_CHANGE_REQUESTS.md`. Do not restart the whole project.
