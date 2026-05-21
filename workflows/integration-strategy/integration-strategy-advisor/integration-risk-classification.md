# Integration Risk Classification

Classify each integration option:

- `official_provider_connector`
- `official_mcp_server`
- `trusted_marketplace_connector`
- `community_mcp_server`
- `internal_company_connector`
- `direct_api`
- `custom_python`
- `manual_export_import`
- `hybrid`

Security dimensions:

- read-only vs write-capable;
- scope breadth;
- credential placement;
- secret storage;
- data duplication;
- sensitive data indexing;
- auditability;
- enterprise/admin controls;
- hosting/cost implications;
- rate limits and quotas;
- maintenance ownership.

Write-capable connectors must default to read-only usage unless the user explicitly enables write actions per integration. Any write action requires explicit approval.
