# Environments and Secrets

Defines local/dev/staging/production environment strategy. Never store secrets in AppForge Markdown.

## Single private local configuration

The user-facing file for sensitive/access/runtime values is:

```text
local-only/.env.local
```

Users should fill this one file rather than spreading repo tokens, URLs, env values, and access variables across many files. AppForge derives safe metadata and templates from it, but never stores actual values in project-control.
