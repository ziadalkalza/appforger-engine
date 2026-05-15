# GitHub Repo Mapping

Recommended repos:

```text
appforge-engine          # reusable AppForge engine
appname-project-control  # app-specific memory, registries, baselines, packets
appname-backend          # backend source code
appname-ios              # iOS source code
appname-android          # Android source code
appname-web              # web source code, if used
appname-design-assets    # approved exported assets, optional
```

Each implementation repo must contain:

- `AGENTS.md` copied from the appropriate AppForge bootstrap template.
- `APPFORGE_POINTER.md` pointing to `project-control/` and `appforge-engine/`.

The project-control repo must track repo names, local paths, remotes, branches, and status in `REGISTRIES/REPO_REGISTRY.md`.
