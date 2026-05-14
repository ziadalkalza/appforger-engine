FROM python:3.11-slim
WORKDIR /app
COPY appforge-engine /app/appforge-engine
ENV APPFORGE_MCP_TRANSPORT=http
ENV APPFORGE_MCP_HOST=0.0.0.0
ENV APPFORGE_MCP_PORT=8080
EXPOSE 8080
CMD ["python", "appforge-engine/APPFORGE_MCP_SERVER/server/appforge_mcp_server.py", "--engine-root", "appforge-engine", "--transport", "http", "--host", "0.0.0.0", "--port", "8080"]
