# GitHub Repo Mapping

Recommended repos:

```text
appforger-engine          # reusable Appforger engine
appname-project-control  # app-specific memory, registries, baselines, packets
appname-backend          # backend source code
appname-ios              # iOS source code
appname-android          # Android source code
appname-web              # web source code, if used
appname-design-assets    # approved exported assets, optional
```

Each implementation repo must contain:

- `AGENTS.md` copied from the appropriate Appforger bootstrap template.
- `APPFORGER_POINTER.md` pointing to `project-control/` and `appforger-engine/`.

The project-control repo must track repo names, local paths, remotes, branches, and status in `REGISTRIES/REPO_REGISTRY.md`.
