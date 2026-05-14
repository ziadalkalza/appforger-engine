# Integration Strategy Advisor

Use this guide when adding any external integration.

## Purpose

Before building custom integration code, AppForger asks whether the safest/easiest path is:

1. official connector/plugin/MCP;
2. existing AppForger built-in integration;
3. direct API;
4. custom Python;
5. hybrid.

## Recommended usage

Ask the model:

> Use AppForger's Integration Strategy Advisor to choose how to add `<service>` for `<goal>`. Research official secure connectors/MCPs first, compare against AppForger's built-in integrations and API/custom options, then create an integration decision packet.

## Confluence example

Default recommendation is hybrid:

- use official Atlassian/Confluence connector or MCP for live exploration/search;
- use AppForger's Confluence fetch/index pipeline only for selected pages requiring persistent Qdrant/Neo4j/project-control context.

## Git provider example

Default recommendation is hybrid:

- use official Git connector/MCP for live repo access when appropriate;
- use AppForger Git provider + code context pipeline for persistent code maps, RAG summaries, graph relationships, and staleness tracking.

## Custom Python warning

Custom Python should only be generated after approval. It may require testing and iteration to match authentication, pagination, API versions, schemas, rate limits, and edge cases.
