# Context Backend Architecture

Recommended layers:

1. GitHub/project-control — canonical approved project truth.
2. Code repos — live implementation truth.
3. Figma — approved design source, recorded as baselines in project-control.
4. SQL context store — structured operational state and metadata.
5. Vector/RAG store — semantic retrieval over summaries and approved artifacts.
6. Object/document storage — screenshots, exports, reports, and larger artifacts.

The retrieval layer must always return source metadata and point back to canonical files.
