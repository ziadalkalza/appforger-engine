# Codex Task Packet Template

## Packet ID

## Target repo
backend / ios / android / design-assets

## Repo path

## Repo access mode
local_clone / remote_github / artifact_packet / not_available

## Remote context fallback
If the target repo or dependency repo is not local, use `REMOTE_AND_MULTI_DEVICE_WORKFLOWS/GITHUB_CONTEXT_FETCH_PROTOCOL.md` and register fetched/imported context in `REGISTRIES/REMOTE_CONTEXT_REGISTRY.md`.


## Goal

## Read first
- Repo `AGENTS.md`
- `APPFORGE_POINTER.md`
- Relevant AppForge registries
- Relevant source-of-truth baseline

## Source-of-truth artifacts

## Constraints
- Do not edit AppForge engine files from the code repo unless explicitly asked.
- Do not change approved API/design baseline without a change request.
- Do not commit secrets.

## Files/directories to inspect first

## Files likely to edit

## Acceptance criteria

## Tests to run

## Done report format
- Summary
- Files changed
- Tests run/results
- Registry updates needed
- Risks/open questions
## Completion Handling

This packet must declare whether the final commit is a checkpoint or completion claim.

Required completion section:

```yaml
completion_type: checkpoint | completion_claim
required_evidence:
  build:
  tests:
  visual_qa:
  registry_updates:
  done_report:
allowed_incomplete_statuses:
  - in_progress_committed
  - implemented_unverified
  - completed_with_warnings
  - user_marked_done_needs_evidence
```

Codex must not mark the task `completed_verified` unless the evidence requirements are satisfied or explicitly waived by the user.


## v13 Story/Docs/Test Links

Each generated Codex packet should include:

- Related epic/user story IDs
- Acceptance criteria
- Related test cases
- Documentation impact
- Package/library decisions if dependencies are added
- Required registry updates in external `project-control/`
