# Integration Pack Schema

Every AppForge third-party integration pack must follow this schema. The schema tells AppForge what information to collect; the specific values must come from official docs, project constraints, and user answers.

## Required top-level fields

```yaml
integration_name: ""
integration_type: ""
status: draft | reviewed | approved | active | deprecated
supported_project_tracks: [mobile, web, backend, design, qa]
intended_use_cases: []
unsupported_use_cases: []
risk_level: low | medium | high | critical
requires_user_approval: true
requires_official_docs_review: true
requires_secrets: false
requires_paid_account_or_billing: false
requires_backend: false
requires_frontend: false
requires_mobile_platform_setup: false
requires_webhooks: false
requires_storage: false
requires_permissions: []
```

## Required sections

Each integration pack must include:

1. `README.md` — what the integration is for and how AppForge uses it.
2. `BOUNDARY.md` — what the third-party tool does and does not own.
3. `CLARIFICATION_QUESTIONS.md` — questions AppForge must ask before using the service.
4. `OFFICIAL_DOCS_RESEARCH.md` — official sources consulted, dates, and unresolved items.
5. `SETUP_CHECKLIST.md` — manual setup actions.
6. `SECRETS_POLICY.md` — required secrets and where they must live.
7. `COST_AND_RISK_REVIEW.md` — cost, quota, vendor lock-in, and risk review.
8. `SECURITY_PRIVACY_REVIEW.md` — security/privacy rules and forbidden patterns.
9. `BACKEND_RUNBOOK.md` — backend responsibilities, if applicable.
10. `FRONTEND_RUNBOOK.md` — web/mobile frontend responsibilities, if applicable.
11. `PLATFORM_SPECIFIC_RUNBOOKS.md` — iOS/Android/Web differences, if applicable.
12. `TEST_CHECKLIST.md` — tests that prove the integration works.
13. `FAILURE_RECOVERY.md` — what to do when setup, auth, webhooks, SDKs, or APIs fail.
14. `CODEX_PACKET_TEMPLATE.md` — focused implementation packet for Codex.
15. `REGISTRY_UPDATES.md` — AppForge/project-control files that must be updated.

## Optional sections

Add these when relevant:

- `WEBHOOK_POLICY.md`
- `PERMISSIONS_POLICY.md`
- `MIGRATION_POLICY.md`
- `DATA_RETENTION_POLICY.md`
- `RATE_LIMIT_POLICY.md`
- `SANDBOX_TEST_MODE.md`
- `APP_STORE_REVIEW_NOTES.md`
- `FIGMA_OR_DESIGN_HANDOFF.md`
- `MCP_OR_CONNECTOR_SETUP.md`

## Completion criteria

An integration pack is ready only when:

- required clarification answers are recorded,
- official documentation sources are recorded,
- unknowns are marked,
- setup and secrets are clear,
- tests are defined,
- risks/costs are reviewed,
- registry updates are prepared,
- user approval is captured.
