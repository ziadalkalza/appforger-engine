# Draft and Sandbox Audit

Checks that draft experiments do not pollute project truth.

## Must pass

- Draft artifacts are local-only or explicitly marked as draft.
- Draft registry records may exist in project-control, but raw draft files are not approved truth.
- Draft branches are marked as draft/unapproved.
- Sandbox outputs cannot update registries or baselines automatically.
- Promotion requires review, classification, and approval.
- Draft indexing into context backend is disabled unless explicitly enabled.
