# Local-Only Policy

`local-only/` is for files that should not be committed by default.

Use it for:

- failed image generations
- scratch prompts
- raw debug logs
- temporary files
- local experiments
- one-off analysis files
- private environment notes

Never store secrets in AppForge, project-control, or local-only unless explicitly protected and excluded from version control.

If a local-only artifact becomes important, promote it through `PROMOTION_POLICY.md` and register it in `ARTIFACT_IMPORTS/IMPORTED_ARTIFACT_REGISTRY.md` or the relevant registry.
