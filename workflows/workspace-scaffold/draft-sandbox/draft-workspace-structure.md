# Draft Workspace Structure

Real project workspaces should include draft/sandbox folders outside `appforger-engine/`.

```text
my-app-workspace/
  local-only/
    drafts/
      html-prototypes/
      figma-notes/
      image-generations/
      codex-experiments/
      backend-experiments/
      package-experiments/
    sandbox/
      web-preview/
      api-mock/
      ui-mock/
      package-tests/
      backend-experiments/
  exports/
    drafts/
    sandbox-reports/
```

`local-only/` content is not committed by default.

`project-control/REGISTRIES/DRAFT_REGISTRY.md` can record the draft metadata without storing raw draft files.
