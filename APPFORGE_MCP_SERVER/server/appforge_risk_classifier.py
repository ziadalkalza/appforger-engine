from __future__ import annotations

HIGH_RISK_WORDS = {
    "clean", "delete", "remove", "move", "push", "provision", "deploy", "secret",
    "raw code", "volume", "production", "migration", "auth", "payment"
}
MEDIUM_RISK_WORDS = {"fetch", "index", "sync", "bootstrap", "adopt", "runtime", "docker"}


def classify_action(text: str) -> dict:
    hay = (text or "").lower()
    risk = "low"
    reasons = []
    for word in sorted(HIGH_RISK_WORDS):
        if word in hay:
            risk = "high"
            reasons.append(f"contains high-risk term: {word}")
    if risk == "low":
        for word in sorted(MEDIUM_RISK_WORDS):
            if word in hay:
                risk = "medium"
                reasons.append(f"contains medium-risk term: {word}")
    requires = risk in {"medium", "high", "critical"}
    return {
        "risk": risk,
        "requires_user_approval": requires,
        "mcp_executes": False,
        "run_location": "user_local_workspace",
        "reasons": reasons or ["read-only guidance or lookup"]
    }
