# Cross Model Consistency Policy

When multiple models/providers are used, AppForge must avoid divergent hidden assumptions.

Rules:

- Decisions must be stored in project-control.
- Provider-specific outputs must cite the packet/baseline they used.
- If two providers disagree, open a conflict or review record.
- Do not merge provider output into real project state until it is reviewed according to the artifact lifecycle.
