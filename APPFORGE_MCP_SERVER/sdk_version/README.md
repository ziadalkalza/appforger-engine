# SDK-based MCP Version

The default AppForger MCP server is minimal and uses only the Python standard library. Future deployments can replace the transport layer with an official MCP SDK while preserving the same resource, prompt, and tool providers.

Keep the same safety rule: hosted remote MCP returns plans and command references, not direct project execution.
