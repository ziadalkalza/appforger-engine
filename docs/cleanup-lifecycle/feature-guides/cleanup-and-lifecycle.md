# Cleanup and Lifecycle

Cleanup can remove Appforger files, remove marked `local-only/`, restore move-adopted sources, or remove runtime containers/volumes. Destructive actions require approval and volume deletion requires strong confirmation. Cleanup must be allowlist-based and must not delete generic project folders such as `docs/`, `assets/`, `exports/`, or implementation source folders.
