from __future__ import annotations
import os


def auth_config() -> dict:
    return {
        "api_key_configured": bool(os.environ.get("APPFORGE_MCP_API_KEY")),
        "oidc_issuer": os.environ.get("APPFORGE_MCP_OIDC_ISSUER", ""),
        "oidc_audience": os.environ.get("APPFORGE_MCP_OIDC_AUDIENCE", ""),
        "auth_mode": os.environ.get("APPFORGE_MCP_AUTH_MODE", "api_key_or_oidc_template"),
    }


def check_http_authorization(headers) -> tuple[bool, str]:
    """Minimal HTTP auth scaffold.

    If APPFORGE_MCP_API_KEY is set, require Authorization: Bearer <key> or X-API-Key.
    OIDC validation is intentionally a deployment scaffold here; configure it in the
    reverse proxy / platform or replace this function with proper JWT validation.
    """
    expected = os.environ.get("APPFORGE_MCP_API_KEY")
    if not expected:
        return True, "no API key configured"
    auth = headers.get("Authorization", "")
    xkey = headers.get("X-API-Key", "")
    if auth == f"Bearer {expected}" or xkey == expected:
        return True, "api key accepted"
    return False, "missing or invalid API key"
