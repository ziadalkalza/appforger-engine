# Local Qdrant Docker Setup

Start Qdrant locally:

```bash
docker run -p 6333:6333 -p 6334:6334   -v "$(pwd)/qdrant_storage:/qdrant/storage"   qdrant/qdrant
```

Health check:

```bash
curl http://localhost:6333/healthz
```

Default local URL:

```text
http://localhost:6333
```
