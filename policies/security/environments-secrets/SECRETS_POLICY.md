# Secrets Policy

- Never paste secrets into AppForge docs.
- Use placeholders only.
- Rotate exposed keys immediately.
- Track secret names, not values.

## Single private config rule

Use `local-only/.env.local` as the single user-filled local private configuration file.

Do not commit, index, cite, report, or copy this file into project-control. Generated project-control files may contain only metadata and references, never secret values.
