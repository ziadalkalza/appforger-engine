# Stage Reordering Policy

Stages may be reordered when the project needs discovery or iteration.

Examples:
- frontend sandbox before backend;
- requirements → UI exploration → requirements refinement;
- imported frontend first, backend/API later;
- backend spike before final UI when feasibility is uncertain.

Reordering must not hide dependency status. If frontend starts before API approval, packets must state mock/stub/pending API mode.
