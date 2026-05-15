# Context Backend Architecture

Recommended layers:

1. source-control app/project-control â€” canonical approved project truth.
2. Code repos â€” live implementation truth.
3. design tool â€” approved design source, recorded as baselines in project-control.
4. SQL context store â€” structured operational state and metadata.
5. Vector/RAG store â€” semantic retrieval over summaries and approved artifacts.
6. Object/document storage â€” screenshots, exports, reports, and larger artifacts.

The retrieval layer must always return source metadata and point back to canonical files.
