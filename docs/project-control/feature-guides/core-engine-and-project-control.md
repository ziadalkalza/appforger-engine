# Core Engine and Project-Control

Use Appforger as a sidecar control layer beside your app code. The engine contains reusable logic. The generated `project-control/` folder contains project-specific state, rules, registries, baselines, approvals, and handoffs.

Do not put actual app code inside `project-control/`. Code remains in local folders, remote repos, or registered snapshots.
