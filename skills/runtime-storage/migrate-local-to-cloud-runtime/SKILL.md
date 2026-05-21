# Migrate Local Runtime to Cloud Runtime Skill

Use when the user wants to move Appforger storage from local Docker to cloud services.

Procedure:
1. Identify current local services and whether they contain important data.
2. Ask the user which data should be migrated: SQL state, vector collections, graph relationships.
3. Generate a migration plan before any export/import.
4. Validate cloud endpoints first.
5. Export local data only after approval.
6. Import into cloud only after approval.
7. Update `runtime-selection.yaml` and write a migration report.

Runtime volume deletion is separate and must follow cleanup safety rules.
