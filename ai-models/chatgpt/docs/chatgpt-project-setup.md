# ChatGPT Project Setup

Use this when creating a ChatGPT Project for an Appforger-powered app.

## Recommended setup

1. Create a ChatGPT Project named after the app.
2. Upload or attach the Appforger engine folder or the most important Appforger files.
3. Add the content of `CHATGPT_MASTER_INSTRUCTIONS.md` to the project instructions.
4. Upload project-specific files as they are created:
   - `APPFORGER_PROJECT_STATUS.md`
   - `PRODUCT_OVERVIEW.md`
   - `DECISION_LOG.md`
   - relevant registries
   - Figma export packets
   - API contract packets
   - screenshots or generated images for review
5. Keep implementation code in separate repos. Do not upload entire app repos unless review is needed.

## Files to keep current

```text
APPFORGER_PROJECT_STATUS.md
DECISION_LOG.md
PENDING_QUESTIONS.md
REGISTRIES/REPO_REGISTRY.md
REGISTRIES/FEATURE_REGISTRY.md
REGISTRIES/SCREEN_REGISTRY.md
REGISTRIES/API_REGISTRY.md
REGISTRIES/CHANGE_REQUEST_REGISTRY.md
```

## Session start

At the start of a session, tell ChatGPT:

```text
Use the Appforger engine rules. Read the current project state and continue from the current stage. Do not create implementation code inside Appforger. Prepare packets for the correct repo when development is needed.
```
