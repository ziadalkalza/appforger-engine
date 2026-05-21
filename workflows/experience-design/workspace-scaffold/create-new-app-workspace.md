# Create New App Workspace

## Manual steps

1. Create parent folder:

```bash
mkdir my-app-workspace
cd my-app-workspace
```

2. Place Appforger inside:

```text
my-app-workspace/appforge/
```

3. Create sibling implementation folders:

```bash
mkdir backend ios android design-assets exports local-only
```

4. Initialize separate Git repos only inside implementation folders as needed:

```bash
cd backend && git init
cd ../ios && git init
cd ../android && git init
```

5. Copy repo instruction templates:

```text
appforge/ai-models/codex/docs/backend-repo-agents-template.md -> backend/AGENTS.md
appforge/ai-models/codex/docs/ios-repo-agents-template.md -> ios/AGENTS.md
appforge/ai-models/codex/docs/android-repo-agents-template.md -> android/AGENTS.md
appforge/ai-models/codex/docs/appforge-pointer-template.md -> each repo as APPFORGER_POINTER.md
```

6. Update `registries/project-control/repo-registry.md`.
