# Troubleshooting and Validation

## Validate the engine

```bash
cd appforger-engine
python validation/validate_all.py --deep
```

## Common checks

- Confirm the zip root contains only `appforger-engine/`.
- Confirm there are no stale placeholder files such as old placeholder question files, version notes, or old manifest files.
- Confirm there are no `__pycache__` or `.pyc` files.
- Confirm `local-only/.env.local` is not committed or indexed.
- Confirm dangerous actions are approval-gated.
- Confirm selected provider adapters are the only generated workspace adapters.

## If setup fails

1. Confirm Python is available.
2. Confirm you are running the setup command from the workspace root.
3. Confirm `appforger-engine/` is next to, not inside, `backend/` or `web/`.
4. Run the validation command above.
5. Check `docs/project-onboarding/start-here/setup-and-first-run-guide.md` and this documentation folder.

## If runtime services fail

1. Confirm Docker is installed and running.
2. Confirm `local-only/.env.local` exists.
3. Run runtime health checks.
4. Check `runtime/runtime-storage/storage/README.md`.

## If source pipelines fail

1. Check the source registry for the source ID.
2. Check the relevant skill under `skills/operations/source_pipeline_skills/`.
3. Run the source pipeline in mock/dry-run mode where supported.
4. Confirm credentials are referenced in `local-only/.env.local`, not stored in project-control.

## If MCP integration fails

1. Run the MCP server locally first with stdio.
2. Check `mcp/docs/install-and-use.md`.
3. Check client example configuration.
4. Confirm the remote MCP is guide-only and not expected to access local project files.
