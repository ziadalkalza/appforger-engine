# AppForger v1 Feature Status Audit

This report is generated to make the package state explicit after multiple feature additions.

## Status vocabulary

- `implemented`: implemented as stable policy/template behavior.
- `implemented_scaffold`: operational scaffold exists and can be run/smoke-tested, but it is not a production-grade provider/runtime implementation.
- `planned`: documented only and not executable.

## Current honesty statement

The package now contains the requested layers structurally and includes runnable scaffolds for setup, runtime, code context, Confluence fetch, Git provider integration, source pipelines, adoption, and cleanup. Some provider/runtime integrations are intentionally first-pass scaffolds and should not be described as production-complete cloud integrations without further hardening.

Run:

```bash
python appforge-engine/validation/validate_feature_manifest.py
python appforge-engine/validation/validate_all.py --deep
```

## Operator how-to documentation

Status: implemented.

The engine includes a dedicated `docs/getting-started/operator-guides/` documentation folder containing:

- setup and first-run guide;
- complete feature/activity index;
- activity-to-guide index;
- command cheatsheet;
- troubleshooting and validation guide;
- focused feature guides.


## Integration Strategy Advisor

Status: implemented scaffold. It provides connector-first decision policies, integration strategy skills, project-control templates, MCP prompt/resource exposure, and validation. It guides the acting model to research current official connectors/MCPs before generating custom API/Python integrations.
