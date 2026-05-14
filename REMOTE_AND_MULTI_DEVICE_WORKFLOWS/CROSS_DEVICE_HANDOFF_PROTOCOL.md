# Cross-Device Handoff Protocol

## Purpose

When different devices or team members work on different parts of the app, all handoffs must pass through project-control.

## Backend → Frontend handoff

Backend developer must provide:

- backend repo/branch/commit/PR,
- updated API registry entry,
- updated API baseline if contract changed,
- migration notes if data model changed,
- test results,
- known limitations.

Frontend developer reads:

- latest API baseline,
- backend handoff summary,
- Figma/design baseline,
- frontend execution packet.

## Frontend → Backend handoff

Frontend developer must provide:

- missing API/data requirements,
- integration errors,
- request/response examples,
- screenshots/logs,
- change request if API behavior must change.

## Designer → Frontend handoff

Designer must provide:

- Figma baseline packet,
- frame/component names,
- exported assets if needed,
- token/component mapping,
- interaction and motion notes.

## QA → Dev handoff

QA must provide:

- test case ID,
- environment/device/browser,
- expected vs actual,
- evidence path/link,
- affected baseline/feature/API.

## Required storage

Cross-device handoffs are persistent project memory. Store them in:

```text
project-control/DECISION_SNAPSHOTS/
project-control/ARTIFACT_IMPORTS/
project-control/REGISTRIES/TEAM_HANDOFF_REGISTRY.md
```
