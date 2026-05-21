# Project Adoption and Git Boundaries

Existing projects are registered by default. Appforger must not move/copy/symlink source folders unless an adoption plan is generated, approved, and applied explicitly.

The engine is not committed with project code. `local-only/` is private. A shared project-control repo may include `project-control/`, docs, design assets, and selected exports.
