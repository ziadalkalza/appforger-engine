# Promotion Policy

Promotion means moving an artifact from temporary/candidate status into persistent project memory, source code, assets, or reports.

## Promotion triggers

- User says it is approved.
- It is used by production code.
- It is referenced by an approved baseline.
- It supports a release/QA decision.
- It is part of a merged PR.

## Required steps

1. Classify the artifact lifecycle.
2. Move it to the correct folder.
3. Register it in the relevant registry.
4. Link it to a stage, feature, baseline, or task.
5. Commit it to the correct repo if persistent.
6. Update `APPFORGE_PROJECT_STATUS.md` if the project status changed.
