# Automation Levels

Default for new projects: **Level 2 — Local validation and reporting allowed**.

## Level 0 — Manual guidance only
AppForge gives instructions. User manually performs all work.

## Level 1 — Draft generation only
AppForge may generate draft stories, docs, tests, plans, and packets. No execution.

## Level 2 — Local validation and reporting
AppForge/Codex/scripts may run validators, generate reports, and create draft context packs. This is the default.

## Level 3 — Local execution with approval gates
Codex may edit local files, run tests, and prepare commits when a packet explicitly permits it.

## Level 4 — CI/GitHub Actions automation
GitHub Actions may run tests, validation, reindexing, and report generation. Production-affecting jobs still require approval.

## Level 5 — Future MCP/server automation
Reserved for AppForge server/MCP with auth, permissions, scheduling, audit logs, and secret management.

Automation level can be configured per project, stage, and repo.
