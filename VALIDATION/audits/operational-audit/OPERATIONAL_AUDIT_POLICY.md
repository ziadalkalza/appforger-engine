# Operational Audit Policy

AppForge v1.0 treats operational audit as a stability gate for the engine itself.

## Scope

The audit applies to the full accumulated AppForge engine lineage, including:

- early engine rules, skills, prompts, registries, and templates;
- mobile/native workflows;
- web workflows;
- design, Figma, image, and visual QA workflows;
- backend and API workflows;
- user stories, docs, test authoring, and release docs;
- draft/sandbox mode;
- context backend mode;
- team collaboration;
- flexible workflow overrides;
- automation jobs and policy.

## Safe fixes

The audit may apply safe fixes automatically when they only clarify or align rules, for example:

- replacing hardcoded “Figma required” language with “approved visual baseline required”;
- clarifying that backend may be skipped only through an approved no-backend workflow;
- clarifying that RAG/Qdrant is retrieval/indexing, not canonical truth;
- clarifying that automation must respect approvals, job definitions, risk levels, and audit records.

## Unsafe fixes

The audit must ask the user before changes that alter behavior, delete content, change defaults, activate automations, change canonical truth, or rewrite project-control data.
