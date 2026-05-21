# Flexible Workflow and Stage Overrides

Appforger workflows are recommended paths, not rigid waterfalls.

A project may skip, substitute, reorder, import, or draft stages when that better fits the project, team, or available artifacts. The flexibility is allowed only when Appforger records the reason, runs impact analysis, preserves source-of-truth boundaries, and keeps non-negotiable rules active.

This layer supports cases such as:
- skipping Figma and using a high-fidelity HTML sandbox as the visual baseline
- injecting an existing frontend or backend
- building a backendless/static web app
- starting with mock APIs before backend exists
- changing workflow after requirements reveal a backend is needed or not needed
- importing existing designs, codebases, or external artifacts
- using draft branches or local-only experiments before promotion
