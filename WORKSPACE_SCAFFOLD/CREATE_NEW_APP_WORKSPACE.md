# Create New App Workspace

## Manual steps

1. Create parent folder:

```bash
mkdir my-app-workspace
cd my-app-workspace
```

2. Place AppForge inside:

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
appforge/CODEX_BOOTSTRAP/BACKEND_REPO_AGENTS_TEMPLATE.md -> backend/AGENTS.md
appforge/CODEX_BOOTSTRAP/IOS_REPO_AGENTS_TEMPLATE.md -> ios/AGENTS.md
appforge/CODEX_BOOTSTRAP/ANDROID_REPO_AGENTS_TEMPLATE.md -> android/AGENTS.md
appforge/CODEX_BOOTSTRAP/APPFORGE_POINTER_TEMPLATE.md -> each repo as APPFORGE_POINTER.md
```

6. Update `REGISTRIES/REPO_REGISTRY.md`.
