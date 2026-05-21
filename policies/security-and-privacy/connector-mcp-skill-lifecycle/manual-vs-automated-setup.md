# Manual vs Automated Setup

Appforger can generate setup instructions, config templates, skills, and task packets. It cannot assume manual setup has been done.

## Usually manual

- account creation,
- OAuth authorization,
- billing approval,
- production secrets,
- cloud project creation,
- App Store / Play Store accounts,
- DNS/certificates,
- MCP server installation when not available in the environment.

## Automatable when tools allow

- creating files,
- updating registries,
- generating config templates,
- preparing commits,
- running local validation scripts,
- generating execution packets,
- testing local repo builds.

## Approval rule

Ask before actions that spend money, expose accounts, grant permissions, change production, push code, merge PRs, or alter security posture.
