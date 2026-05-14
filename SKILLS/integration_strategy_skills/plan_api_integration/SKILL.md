# Plan API Integration Skill

Use this skill when a direct API integration is selected.

Steps:
1. Confirm no official connector/built-in integration satisfies the goal alone.
2. Identify auth method and secret placement.
3. Define endpoints and data scope.
4. Define storage mode: docs, exports, local-only, RAG-only, metadata-only, or custom.
5. Define normalization/chunking/indexing path if needed.
6. Define tests, dry-run, logs, retries, and validation.

API integration code should live under the relevant project-control integration or source folder, not the workspace root.
