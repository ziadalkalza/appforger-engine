# 88 Operational Audit

This layer defines how to audit Appforger as a complete file/GitHub-based app-building engine.

The audit checks the whole accumulated engine, not just the most recent feature layer. It verifies structure, source-of-truth boundaries, workflow compatibility, flexible overrides, draft/sandbox isolation, context backend safety, team mode, automation safety, release readiness, and end-to-end scenario readiness.

Operational audit mode should be used when:

- releasing a new Appforger engine version;
- adding a major capability such as context backend, team mode, automation, flexible workflows, or release operations;
- preparing a real project to rely on the engine;
- checking whether older rules conflict with newer capabilities.
