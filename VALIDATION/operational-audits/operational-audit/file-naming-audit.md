# File Naming Audit

This audit reviews whether repository file names explain what the files do without relying too much on hidden context.

## Summary

The repository is mostly well named at the domain level: folders such as `mcp`, `workflows/product/project-onboarding`, `runtime/context/context-backend`, `workflows/implementation/web-frontend`, and `workflows/delivery/release-operations` clearly describe ownership and purpose.

The main naming weakness is inconsistent specificity:

- Many Markdown policy/template files are explicit and self-describing.
- `README.md` and `SKILL.md` are intentionally conventional, but ambiguous when viewed outside their folder path.
- Some Python modules use generic names that are only clear after reading imports.
- A few adjacent folders overlap semantically and should be disambiguated in documentation or future renames.

## Naming Standard

Use these rules for future files and rename migrations:

- Prefer `domain_action_object.ext` for executable scripts, for example `initialize_appforge_workspace.py`.
- Prefer `DOMAIN_OBJECT_PURPOSE.md` for policies and guides, for example `MCP_REMOTE_HOSTING_GUIDE.md`.
- Keep `README.md` only when the file is a folder landing page.
- Keep `SKILL.md` only inside a named skill directory where the directory name is the skill identity.
- Avoid generic names such as `auth.py`, `config.py`, `setup.py`, `guide.md`, or `template.md` unless the parent folder makes the purpose unambiguous.
- Do not rename manifest-listed files without updating validators, registries, MCP resource maps, and documentation references in the same change.

## Keep As-Is

These names are sufficiently clear because the filename itself describes the artifact:

- `templates/specifications/feature-spec-template.md`
- `templates/specifications/api-contract-template.md`
- `templates/specifications/screen-spec-template.md`
- `registries/APPFORGE_FEATURE_MANIFEST.json`
- `mcp/MCP_RESOURCE_MAP.json`
- `mcp/docs/mcp-prompt-catalog.md`
- `mcp/docs/mcp-tool-catalog.md`
- `validation/validate_all.py`
- `validation/validate_feature_manifest.py`
- `tools/workspace/collect_repo_status.py`

## Keep Conventional Names

These look vague in isolation but are correct because their parent folders provide the missing context and tooling expects the convention:

- `README.md` files throughout the repo.
- `skills/**/SKILL.md` files.
- `Dockerfile`.
- `.env.local.example` and other environment examples.

Do not rename these unless the repository first adopts a different discovery convention.

## Rename Candidates

These files would be clearer with more explicit names. Rename only in a coordinated migration.

| Current file | Suggested name | Reason |
| --- | --- | --- |
| `mcp/server/auth.py` | `http_authorization.py` | The file checks HTTP authorization headers, not general auth. |
| `mcp/server/manifest_loader.py` | `appforge_manifest_loader.py` | It loads Appforger feature/resource manifests, not arbitrary manifests. |
| `integrations/source-control/generic/python/git_providers/base_provider.py` | `git_provider_base.py` | More searchable and explicit outside package context. |
| `workflows/operations/new-app-initializer/setup_appforge_project.py` | `initialize_appforge_workspace.py` | The script prepares a workspace; "setup project" is broad. |
| `workflows/operations/new-app-initializer/create_new_app.py` | `create_app_workspace_from_config.py` | The script name should distinguish app workspace creation from app code generation. |
| `workflows/operations/workspace-scaffold/create_app_workspace.py` | `scaffold_app_workspace.py` | More action-specific and avoids overlap with `create_new_app.py`. |
| `workflows/operations/workspace-artifact-lifecycle/scripts/appforge_clean.py` | `clean_appforge_workspace_artifacts.py` | Clarifies scope and avoids sounding like a generic cleaner. |
| `mcp/docs/install-and-use.md` | `MCP_INSTALL_AND_USE.md` | Clearer when linked outside the MCP folder. |
| `mcp/docs/remote-hosting-guide.md` | `MCP_REMOTE_HOSTING_GUIDE.md` | Clearer when surfaced through search results or MCP resources. |
| `docs/generated-app-documentation/app-usage-templates/user-operator-manual-do-not-load.md` | `APP_USAGE_DOCS_OPERATOR_MANUAL_EXCLUDE_FROM_CONTEXT.md` | The current name says what not to do but not what the file is for. |

## Overlapping Areas To Clarify

These folder names are understandable, but their boundaries should be documented because they can look similar:

- `workflows/delivery/web-deployment` vs `workflows/delivery/web-publishing`: deployment should mean hosting setup; publishing should mean release workflow and production readiness.
- `docs/document-management/documentation-system`, `docs/document-management/project-docs-library`, and `docs/generated-app/app-usage-templates`: distinguish engine documentation rules, project document storage, and generated end-user documentation templates.
- `runtime/context/context-backend` vs `workflows/operations/context-sync-retrieval`: distinguish storage/index architecture from source sync and retrieval workflows.
- `policies/providers/model-tool-routing` vs `policies/providers/provider-layer`: distinguish task routing policy from provider abstraction/profile definitions.

## Required Migration Updates

Any rename of manifest-listed or validator-required files must update:

- `registries/APPFORGE_FEATURE_MANIFEST.json`
- `mcp/MCP_RESOURCE_MAP.json`
- `validation/*.py`
- `README.md`
- `docs/getting-started/start-here/*.md`
- `docs/getting-started/operator-guides/**/*.md`
- `registries/project-control/skill-registry.md` when skill paths change
- imports inside Python modules

## Recommendation

Do not bulk-rename the repository in one pass. The current path-based naming model is mostly coherent, and large renames would create high link and validator churn.

Recommended sequence:

1. Rename the small Python modules with generic names first.
2. Update imports, validators, feature manifest entries, and MCP resource maps in the same commit.
3. Add alias notes in README files where external users may have copied old command paths.
4. Leave `README.md` and `SKILL.md` conventions intact.
5. Re-run `validation/validate_all.py` after Python is available.
