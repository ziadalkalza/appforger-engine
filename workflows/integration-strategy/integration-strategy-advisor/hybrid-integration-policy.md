# Hybrid Integration Policy

Use hybrid integration when one approach cannot satisfy all goals safely.

Examples:

- Confluence: official connector/MCP for live exploration, Appforger fetch/index pipeline for selected pages that require persistent Qdrant/Neo4j/project-control context.
- Git providers: official Git connector/MCP for live repo inspection, Appforger Git provider + code context pipeline for persistent code maps, RAG summaries, and graph relationships.

Hybrid decisions must clearly define:

- which part is handled by connector/MCP;
- which part is handled by Appforger API/pipeline;
- which data is duplicated or indexed;
- which system remains source of truth;
- credential placement;
- approval requirements.
