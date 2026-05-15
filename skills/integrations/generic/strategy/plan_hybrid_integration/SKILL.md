# Plan Hybrid Integration Skill

Use this skill when live connector access and persistent AppForger storage/indexing are both useful.

Examples:
- Documentation-source connector for live exploration plus AppForger fetch/index for selected pages.
- Git connector for live repo interaction + AppForger code context sync for persistent maps/RAG/graph.

The plan must clearly separate:
- connector responsibilities;
- AppForger pipeline responsibilities;
- source-of-truth boundaries;
- duplicate storage/indexing rules;
- credentials and approvals.
