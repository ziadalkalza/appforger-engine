# Safe Automation Rules

Low-risk automation may run with minimal friction:

- validate registries
- validate required files
- generate draft context packs
- run local tests
- detect stale context
- generate draft Trello export packets
- check package decision records
- create draft next-step packets if enabled

Medium-risk automation requires awareness or packet approval:

- updating project-control registries
- creating active GitHub Action workflows
- importing Figma packets as candidate baselines
- preparing commits

High-risk automation requires explicit approval:

- approving baselines
- activating integrations
- adding packages
- modifying production env configuration
- creating cloud resources
- pushing commits
- deploying staging

Critical automation is not allowed without high-risk override and human confirmation:

- production publishing
- app store submission
- production data deletion
- production secret rotation
- live payment activation
- release blocker waiver
