"""Embedding adapter examples for AppForge context backend.

Default `hash_dev` is deterministic and dependency-free. It is useful only for
pipeline validation, not high-quality semantic retrieval.
"""
from __future__ import annotations
import hashlib, math, os
from typing import List


def _normalize(vec: List[float]) -> List[float]:
    norm = math.sqrt(sum(x*x for x in vec)) or 1.0
    return [x/norm for x in vec]


def hash_dev_embed(text: str, dim: int = 384) -> List[float]:
    vec = [0.0] * dim
    for token in text.lower().split():
        h = hashlib.sha256(token.encode('utf-8')).digest()
        idx = int.from_bytes(h[:4], 'little') % dim
        sign = 1.0 if h[4] % 2 == 0 else -1.0
        vec[idx] += sign
    return _normalize(vec)


def openai_embed(text: str, model: str = "text-embedding-3-small") -> List[float]:
    from openai import OpenAI
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    resp = client.embeddings.create(model=model, input=text)
    return resp.data[0].embedding


def local_sentence_transformer_embed(text: str, model_name: str) -> List[float]:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(model_name)
    return model.encode([text], normalize_embeddings=True)[0].tolist()


def embed_text(text: str, provider: str = "hash_dev", dim: int = 384, model: str | None = None) -> List[float]:
    if provider == "hash_dev":
        return hash_dev_embed(text, dim=dim)
    if provider == "openai":
        return openai_embed(text, model=model or "text-embedding-3-small")
    if provider == "local":
        if not model:
            raise ValueError("local embedding provider requires a model name")
        return local_sentence_transformer_embed(text, model_name=model)
    raise ValueError(f"Unsupported embedding provider: {provider}")
