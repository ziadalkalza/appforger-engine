# Connector vs API Decision Tree

## Step 1: Define the user's goal

- Live Q&A/search/summarization only?
- Persistent RAG/vector index required?
- Graph/impact relationships required?
- Repeatable scheduled pipeline required?
- Write-back/create/update/delete required?
- Custom transformation/business logic required?

## Step 2: Check official connectors/plugins/MCPs

If an official or trusted connector satisfies the goal, prefer it.

## Step 3: Check existing Appforger integrations

If Appforger already has a connector/runtime pipeline for the source, prefer it over custom code when persistent indexing is needed.

## Step 4: Choose hybrid when needed

Use hybrid when:

- connector is best for live exploration;
- Appforger pipeline is needed for approved persistent RAG/graph indexing;
- the connector does not expose enough data for project-control provenance;
- Confluence/Git sources need persistent relationships to code, docs, APIs, tests, or features.

## Step 5: Direct API or custom Python

Use direct API or custom Python only when connector and built-in integration paths are insufficient or the user explicitly approves custom work.
