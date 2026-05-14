# Manual Actions Policy

## Rule

AppForge must explicitly separate automated work from human/manual work.

## Manual actions include

- Creating cloud accounts.
- Creating Supabase projects.
- Creating DigitalOcean droplets.
- Creating Render services.
- Creating app store records.
- Creating bundle IDs.
- Creating certificates/profiles.
- Creating keystores.
- Setting billing.
- Setting DNS.
- Copying secrets into secure environment stores.
- Approving designs.
- Approving API contracts.
- Approving paid model/tool usage.

## Checklist format

Every manual action checklist must include:

- Why this action is needed.
- Who performs it.
- Step-by-step instructions.
- What output must be returned to AppForge.
- Where the output is stored.
- Security warning if secrets are involved.

## Secret handling

Never paste secrets into Markdown files intended for Git.

Use placeholders:

```text
SUPABASE_URL=<store in .env>
SUPABASE_ANON_KEY=<store in .env>
DATABASE_URL=<store in secret manager>
```
