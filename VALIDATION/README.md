# AppForge v1 Validation

Use the current v1 validators for day-to-day checks. Legacy construction-stage validator names, if present, are internal compatibility checks and are not public release labels.

Recommended final consistency checks:

```bash
python appforge-engine/VALIDATION/validate_engine_structure.py
python appforge-engine/VALIDATION/validate_source_of_truth_rules.py
python appforge-engine/VALIDATION/validate_workflow_compatibility.py
python appforge-engine/VALIDATION/validate_automation_safety.py
python appforge-engine/VALIDATION/validate_context_backend_safety.py
python appforge-engine/VALIDATION/validate_team_mode_compatibility.py
python appforge-engine/VALIDATION/validate_provider_layer.py
python appforge-engine/VALIDATION/validate_agent_orchestration_layer.py
python appforge-engine/VALIDATION/validate_team_operations_backend_layer.py
python appforge-engine/VALIDATION/validate_project_docs_library.py
python appforge-engine/VALIDATION/validate_stronger_context_backend.py
python appforge-engine/VALIDATION/validate_project_onboarding_layer.py
```
