# Code Context Sources Review Report

Status: added to Appforger v1.

## Verified additions

- Code Context Sources policy files live under `workflows/operations/context-sync-retrieval/code_context_sources/`.
- Mandatory ongoing project onboarding question added.
- Initial code context bootstrap policy added.
- Role-aware backend/frontend_mobile/admin/read-only access model added.
- CI-generated context added as first-class fetch mode.
- Single private config file template added at `local-only/.env.local.example`.
- Project-control templates added for code source registries, access policies, staleness logs, bootstrap reports, and access/secret metadata.
- Secret values remain outside project-control and context indexes.

## Root package rule

Final package must contain only `appforger-engine/` at zip root.
