# Integration Research Protocol

Use this protocol before generating or activating an integration pack.

## When research is required

Research is required when the integration involves any of:

- current SDK/API setup,
- auth/security,
- payments/subscriptions,
- maps/location,
- notifications/SMS/email,
- cloud deployment,
- storage/uploads,
- analytics/tracking,
- OAuth or external accounts,
- pricing/free-tier limits,
- app-store/platform restrictions,
- any service AppForge has not already approved.

## Allowed sources

Prefer:

1. official vendor documentation,
2. official SDK/API references,
3. official GitHub repos from the vendor,
4. official pricing/security pages,
5. platform documentation from Apple, Google, Figma, GitHub, Supabase, etc.

Use community posts only for troubleshooting notes, never as the primary source of truth for setup, security, or production rules.

## No-memory-only rule

```text
Do not create a production-ready integration pack from model memory alone.
If online research is unavailable and the user did not provide docs, mark the pack as draft-only or blocked.
```

## Research record

Every integration pack must include a research record:

```yaml
research_status: not_started | in_progress | complete | blocked
official_sources_consulted: []
source_dates_checked: []
unknowns: []
assumptions: []
requires_user_confirmation: []
```

## If research cannot be done

If the active environment cannot browse or access official docs:

1. say that official documentation access is required,
2. ask the user to provide docs/links or allow browsing,
3. create only a draft schema if useful,
4. do not activate the integration,
5. do not create implementation code that depends on unverified setup details.
