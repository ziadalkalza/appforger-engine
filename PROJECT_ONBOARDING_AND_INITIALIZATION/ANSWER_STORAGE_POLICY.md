# Answer Storage Policy

Onboarding answers must be stored in both human-readable Markdown and machine-readable YAML.

Files:

```text
project-control/APPFORGE_PROJECT_PROFILE.md
project-control/APPFORGE_ONBOARDING_ANSWERS.md
project-control/APPFORGE_ACTIVE_RULES.md
project-control/APPFORGE_SETUP_STATUS.md
project-control/APPFORGE_PROJECT.yaml
```

Registries:

```text
PROJECT_INITIALIZATION_REGISTRY.md
ACTIVE_FEATURES_REGISTRY.md
ACTIVE_WORKFLOW_RULES_REGISTRY.md
PROVIDER_PREFERENCE_REGISTRY.md
STORAGE_MODE_REGISTRY.md
PENDING_ONBOARDING_QUESTIONS_REGISTRY.md
```

Never store secrets in onboarding answers. Store only secret metadata and setup status in the relevant secret metadata registries.

## Code source onboarding answers

Onboarding answers must store `ongoing_project` and Code Context Source setup choices in Markdown and YAML.

Never store credential values or secret values in onboarding answers. Store only auth references, source ids, access levels, bootstrap status, and secret metadata status.
