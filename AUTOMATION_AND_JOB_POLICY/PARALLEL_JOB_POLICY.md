# Parallel Job Policy

Parallel jobs are allowed only if dependencies and conflicts are declared.

Safe examples:

- backend tests and frontend visual QA
- Trello export packet generation and docs validation
- context reindex and test report generation

Unsafe examples:

- two jobs updating the same registry
- a baseline update while dependent implementation packet is running
- context reindex while project-control PR is half-merged

Conflicts must be recorded and resolved before merging outputs.
