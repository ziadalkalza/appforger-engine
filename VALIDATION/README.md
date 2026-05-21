# Appforger v1 Validation

Use the current v1 validators for day-to-day checks. Legacy construction-stage validator names, if present, are internal compatibility checks and are not public release labels.

Recommended final consistency checks:

```bash
python appforger-engine/validation/validate_engine_structure.py
python appforger-engine/validation/validate_source_of_truth_rules.py
python appforger-engine/validation/validate_workflow_compatibility.py
python appforger-engine/validation/validate_automation_safety.py
python appforger-engine/validation/validate_context_backend_safety.py
python appforger-engine/validation/validate_team_mode_compatibility.py
python appforger-engine/validation/validate_provider_layer.py
python appforger-engine/validation/validate_agent_orchestration_layer.py
python appforger-engine/validation/validate_team_operations_backend_layer.py
python appforger-engine/validation/validate_project_docs_library.py
python appforger-engine/validation/validate_stronger_context_backend.py
python appforger-engine/validation/validate_project_onboarding_layer.py
```
