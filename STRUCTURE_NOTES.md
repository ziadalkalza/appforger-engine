# Appforger Structure Notes

## Decisions applied

- Added `ai-models/`, `examples/`, and `tools/` as top-level artifact folders.
- Kept `.git/` and `desktop.ini` exactly as requested.
- Flattened repeated same-name folders where safe.
- Merged the two project-control template locations into `templates/project-control/`.
- Moved workspace template content into `templates/workspace/`.
- Moved examples from `templates/templates/*-example/` and `templates/examples/*-example/` into `examples/`.
- Moved AI-client/model-specific files into `ai-models/{model}/`.
- Moved non-AI third-party app/platform materials out of `external-platforms/` into functional integration folders.
- Kept the `mcp/` folder focused on running Appforger as an MCP server. External MCP catalogs/config templates moved under `integrations/mcp-catalog/`; MCP prompt templates moved under `templates/integration-strategy/mcp-prompts/`.
- Normalized most folder and markdown/config filenames to lowercase kebab-case while preserving runtime-sensitive Python/import filenames and conventional files like `README.md`, `SKILL.md`, `Dockerfile`, `MCP_RESOURCE_MAP.json`, and `APPFORGE_FEATURE_MANIFEST.json`.

## Cleanup stats

- Files copied: 4709
- Files moved or renamed: 1529
- Exact duplicate files skipped: 2
- Collisions kept with a meaningful suffix: 0
- README-style files merged: 2
- Text files updated for path references/naming: 580

## Important resulting paths

```text
ai-models/
examples/
tools/
templates/project-control/
templates/workspace/
mcp/server/
mcp/deployment/
mcp/docs/
integrations/design/figma/
integrations/source-control/github/
integrations/source-control/bitbucket/
integrations/document-sources/confluence/
integrations/mcp-catalog/
runtime/context-backend/qdrant/
runtime/backend-platforms/supabase/
```

## Validation

After restructuring, the main deep validation command passed:

```bash
python validation/validate_all.py --deep
```

The MCP server help command also ran successfully from the new path:

```bash
python mcp/server/appforge_mcp_server.py --help
```

## Duplicate handling

Exact duplicates were skipped. Where `README-2.md` existed beside `README.md`, it was merged into `README.md` when the content was distinct.

## Git note

The `.git/` folder is preserved. Since the working tree was reorganized outside Git, run:

```bash
git status
```

after extracting the ZIP and review the path changes before committing.
