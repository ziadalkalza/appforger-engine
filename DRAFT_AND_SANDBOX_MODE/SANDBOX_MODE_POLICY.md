# Sandbox Mode Policy

Sandbox mode is a stronger form of draft mode where the user intentionally runs or previews an experiment.

## Sandbox locations

Preferred local locations:

```text
local-only/sandbox/web-preview/
local-only/sandbox/api-mock/
local-only/sandbox/ui-mock/
local-only/sandbox/package-tests/
local-only/sandbox/backend-experiments/
```

## Sandbox truth boundary

A sandbox can prove that an idea works, but it does not become project truth until promoted.

## Sandbox outputs

A sandbox may produce:

- screenshots;
- notes;
- prototype URLs;
- short code snippets;
- package evaluation results;
- mock API examples;
- recommendations.

These should be reviewed before being promoted into `project-control/`, design baselines, API contracts, package decisions, or Codex implementation packets.
