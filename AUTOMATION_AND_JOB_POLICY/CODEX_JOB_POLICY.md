# Codex Job Policy

Codex jobs must be driven by packets. A Codex job packet must specify:

- target repo
- target branch
- files to inspect
- files allowed to edit
- source baselines
- tests to run
- registry updates allowed
- done report destination
- commit/push policy

Codex may update registries only if the packet explicitly permits it. In team mode, such updates should be proposed through a PR.
