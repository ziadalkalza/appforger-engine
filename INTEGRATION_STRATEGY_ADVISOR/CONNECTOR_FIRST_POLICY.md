# Connector-First Policy

AppForger should prefer official secure connectors, plugins, or MCP servers when the user only needs live access, search, summarization, or model-assisted interaction with an external service.

Use connector/plugin/MCP first when:

- an official provider connector exists;
- access should remain permissioned by the provider;
- the user does not need persistent AppForger-owned storage;
- the user does not need AppForger Qdrant/Neo4j indexing;
- the integration is common SaaS such as Confluence, Jira, GitHub, GitLab, Bitbucket, Google Drive, Slack, Notion, Linear, Trello, etc.

Do not assume the starter catalog is current. The acting model should research official connector availability before use, especially for SaaS/MCP ecosystems.
