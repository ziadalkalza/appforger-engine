# Prepare Hotfix Plan

## Purpose

Prepare a focused hotfix/rollback plan for a released or release-candidate build.

## Required inputs

- APPFORGER_PROJECT_STATUS.md
- APPFORGER_PROJECT.yaml
- RELEASE_REGISTRY.md
- RELEASE_CANDIDATE_REGISTRY.md when applicable
- TEST_REGISTRY.md and TASK_COMPLETION_REGISTRY.md
- relevant platform registries and release docs

## Outputs

- release packet or updated release docs
- registry updates
- evidence checklist
- approval or blocker status

## Rules

- Do not publish or submit automatically.
- Ask before creating a release candidate or final release approval.
- Critical blockers require fix or high-risk user override.
- Non-critical missing evidence may be waived only with user approval.
