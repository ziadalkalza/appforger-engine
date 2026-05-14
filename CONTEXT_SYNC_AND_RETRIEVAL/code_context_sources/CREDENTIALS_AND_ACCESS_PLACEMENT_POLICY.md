# Credentials and Access Placement Policy

AppForge must never store actual secret values in engine files, project-control, docs, context indexes, execution packets, registries, or generated reports.

AppForge may store only metadata:

- secret name
- environment
- owning role
- allowed roles
- storage location type
- auth reference name
- status
- last rotation date if known
- whether the value is stored in AppForge, which must be false

Per-user credentials must live in user-controlled locations such as local Git credentials, OS keychains, local `.env.local` files, GitHub CLI auth, IDE secret stores, or approved enterprise secret managers.

Shared automation credentials must live in CI/CD secret stores, hosting environment variables, cloud secret managers, or Git provider app installations.

Remote repo credentials must be represented in AppForge by metadata references only, such as:

```yaml
auth_reference: github_app_backend_readonly
secrets_stored_here: false
```

If a task requires a secret value, AppForge must generate setup instructions or an access request. It must not ask the user to paste the secret into project-control or context files.
