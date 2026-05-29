# Project-Control Template

This template is copied outside the engine when a real app workspace is created.

Real location:

```text
my-app-workspace/project-control/
```

`project-control/` is the app-specific source of memory for decisions, stories, baselines, task packets, documentation state, and release notes. It should normally be committed to a dedicated GitHub repo such as `appname-project-control`.

The mandatory Business Requirements Document lives in `requirements/business-requirements-document.md` and is tracked in `registries/requirements-document-registry.md`. It sits above the product brief and must be referenced by design, build, QA, and release artifacts unless an approved waiver or draft-only exception is recorded.
