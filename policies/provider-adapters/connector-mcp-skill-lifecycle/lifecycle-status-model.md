# Lifecycle Status Model

Use these statuses for connectors, MCPs, skills, and integration packs.

```text
requested
planned
generated
installed
authorized
configured
validated
active
failed
blocked
revoked
deprecated
not_required
```

## Meaning

- `requested`: user/project asked for it.
- `planned`: Appforger has a plan but no files/config yet.
- `generated`: definitions/config/templates exist.
- `installed`: package/server/skill files placed where needed.
- `authorized`: user granted account/API/OAuth access.
- `configured`: settings/env/config are present.
- `validated`: connection or invocation test passed.
- `active`: allowed for current project tasks.
- `failed`: validation or setup failed.
- `blocked`: missing user action, account, docs, secrets, or permission.
- `revoked`: access removed.
- `deprecated`: no longer preferred.
- `not_required`: intentionally unused for this project.
```

Do not treat `generated` as `active`.
