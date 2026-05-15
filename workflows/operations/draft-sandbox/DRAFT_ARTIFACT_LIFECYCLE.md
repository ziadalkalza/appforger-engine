# Draft Artifact Lifecycle

Draft artifacts move through these statuses:

```text
draft_created
active
under_review
needs_revision
promoted
archived
discarded
expired_review_due
```

## Lifecycle

```text
create draft
→ optionally run/test/preview
→ record draft metadata
→ review
→ decide: promote, revise, archive, discard, or extend
```

## Expiry review

When a draft reaches its expiry review date, AppForge must ask the user what to do:

```text
This draft is due for review. Do you want to:
1. extend review date,
2. discard it,
3. archive it,
4. review/promote it now?
```

Do not delete draft files automatically.
