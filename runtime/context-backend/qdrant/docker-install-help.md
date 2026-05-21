# Docker Install Help

Qdrant local mode requires Docker.

General steps:

1. Install Docker Desktop on Windows/macOS, or Docker Engine on Linux.
2. Confirm Docker is running:

```bash
docker --version
docker ps
```

3. If Docker is unavailable, use Qdrant Cloud or skip local Qdrant setup.

Appforger should not assume Docker exists. It must validate before using local Qdrant.
