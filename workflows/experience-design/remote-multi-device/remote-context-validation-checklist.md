# Remote Context Validation Checklist

Use this before any cross-device or remote-repo dependent task.

## Project-control

- [ ] `project-control/` exists locally or remote URL is known.
- [ ] Latest project-control changes are pulled or imported.
- [ ] `APPFORGER_PROJECT_STATUS.md` and `APPFORGER_PROJECT.yaml` exist.
- [ ] Relevant registries exist.

## Target repo

- [ ] Target repo is local or remote access mode is defined.
- [ ] Branch/commit/PR is identified.
- [ ] Repo-specific `AGENTS.md` or `APPFORGER_POINTER.md` exists or is generated.
- [ ] Files to inspect are listed in the work packet or code map.

## Cross-component dependencies

- [ ] Required design baseline exists and is current.
- [ ] Required API/backend baseline exists and is current.
- [ ] Any open change requests are reviewed.
- [ ] No dependent repo is ahead of project-control without an import/handoff.

## Decision

- [ ] Proceed.
- [ ] Proceed with explicit mock-only/placeholder exception.
- [ ] Block and repair project-control/context first.
