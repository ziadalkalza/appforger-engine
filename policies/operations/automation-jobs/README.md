# Automation and Job Policy

This layer defines how AppForge automation works without turning the engine into uncontrolled background agents.

Automation is expressed as jobs:

```text
trigger → load scoped context → run allowed workflow/skill/script → validate result → record evidence → stop or request approval
```

A job is not allowed to infer new authority. It may only do what its job definition permits.

## Key principles

1. Automation is opt-in and risk-classified.
2. Every job has an owner, trigger, inputs, allowed outputs, forbidden actions, and failure behavior.
3. Every job run is recorded in `JOB_RUN_REGISTRY.md`.
4. Approval can happen locally, through GitHub PRs, through Codex confirmation, or through future server workflows.
5. Production release, production secrets, destructive actions, paid services, and baseline approvals require explicit approval.
6. Draft/sandbox and flexible workflow rules still apply.
