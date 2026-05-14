# Integration Pack Generation Workflow

1. Receive integration request.
2. Enter plan mode if the integration is unsupported, risky, ambiguous, or likely to affect architecture.
3. Classify integration type using `INTEGRATION_TYPE_CLASSIFIER.md`.
4. Ask required clarification questions.
5. Research official documentation if current setup/security/API details matter.
6. Copy `INTEGRATION_PACK_TEMPLATE/` into `GENERATED_INTEGRATION_PACKS/<integration_name>/` or the approved engine integration folder.
7. Fill each required section.
8. Mark assumptions, unknowns, manual steps, secrets, costs, and security risks.
9. Update lifecycle registries as draft/reviewed.
10. Ask for user approval before activation.
11. After approval, register integration as active for the project and create project-specific execution packets.

## Output rule

Generating an integration pack does not mean production code should be written. It only makes the integration eligible for implementation tasks.
