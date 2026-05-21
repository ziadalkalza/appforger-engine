# Connector Lifecycle Policy

Connectors such as GitHub, Figma, Google Drive, Supabase, or others must be tracked by availability, permission, and validation status.

## Connector readiness checklist

- Connector requested.
- User/platform supports it.
- Access authorized.
- Scope/permissions understood.
- Test read operation completed.
- Test write operation completed if write access is required.
- Project registry updated.

## If connector is unavailable

Use one of:

- user-provided file upload/export,
- manual link + summary,
- GitHub PR/commit link,
- artifact packet,
- mock-only exception.

Do not pretend connector access exists.
