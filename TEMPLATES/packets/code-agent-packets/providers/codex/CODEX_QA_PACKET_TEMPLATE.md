# Codex QA Packet Template

## Packet ID

## Target repo
backend / ios / android / design-assets

## Repo path

## Repo access mode
local_clone / remote_github / artifact_packet / not_available

## Remote context fallback
If the target repo or dependency repo is not local, use `workflows/operations/remote-multi-device/GITHUB_CONTEXT_FETCH_PROTOCOL.md` and register fetched/imported context in `registries/REMOTE_CONTEXT_REGISTRY.md`.


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

## QA-specific checks
- Compare against baselines.
- Capture screenshots/results.
- Open change requests for failures.


## v13 Story/Docs/Test Links

Each generated Codex packet should include:

- Related epic/user story IDs
- Acceptance criteria
- Related test cases
- Documentation impact
- Package/library decisions if dependencies are added
- Required registry updates in external `project-control/`
