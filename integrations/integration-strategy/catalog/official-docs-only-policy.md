# Official Docs Only Policy

Integration packs that affect security, money, user data, deployment, app-store behavior, or production infrastructure must be based on official documentation.

## Required citation record

The pack must record:

- official docs consulted,
- date checked,
- sections relevant to setup/security/testing,
- assumptions and unknowns,
- user-provided constraints.

## Forbidden behavior

Do not:

- infer current API setup from memory,
- copy undocumented secrets or config names from examples without verification,
- treat blog posts as production truth,
- activate an integration when required official documentation is unavailable,
- generate production implementation code for an unverified integration.

## Draft-only exception

Appforger may create a draft integration pack without browsing only if it is clearly marked:

```text
Status: draft_only_unverified
Not approved for implementation.
Requires official documentation review before activation.
```
