# AppForger Setup and First Run Guide

## Where to extract the zip

Extract the zip so the workspace contains:

```text
my-workspace/
  appforge-engine/
```

Do not place `appforge-engine/` inside `backend/` or `web/`.

## Easy setup

```bash
python appforge-engine/NEW_APP_INITIALIZER/setup_appforge_project.py --target . --name "My Product"
```

The setup creates:

```text
project-control/
docs/
design-assets/
exports/
local-only/
```

Then copy/fill:

```text
local-only/.env.local
```

## Runtime storage

Choose local Docker or cloud services during onboarding. Local mode can run Postgres, Qdrant, and Neo4j.

## Existing/ongoing projects

For ongoing projects, run adoption scan and code/doc context bootstrap before implementation.

## Cloud storage units

If you choose cloud storage instead of local Docker, fill the cloud endpoint references in `local-only/.env.local`, then run:

```bash
python project-control/runtime/scripts/appforge_runtime.py validate-cloud --profiles postgres,qdrant,neo4j
```

Only run cloud schema/collection/constraint initialization after approval:

```bash
python project-control/runtime/scripts/appforge_runtime.py init-cloud-schema --profiles postgres,qdrant,neo4j --approved
```
