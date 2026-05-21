# Appforger Active Rules

Generated from onboarding answers. Do not manually invent active rules without updating onboarding answers and `APPFORGER_PROJECT.yaml`.

## Current status

- Active rules generated: false
- Last generated: TBD

## Active project rules

- TBD

## Default safe rules until initialized

- Help/explanation questions are allowed.
- Real project work is blocked until minimal onboarding is complete.
- Unknown non-critical answers are allowed.
- Critical unknowns must be answered before affected workflows proceed.

## Code context defaults until initialized

- Code-aware implementation is blocked until relevant code sources are registered and fresh enough for the requested work.
- Ongoing projects require initial code context bootstrap.
- Raw code indexing is disabled unless explicitly approved.
- Secret values must come from `local-only/.env.local` or approved external secret stores, never project-control.
