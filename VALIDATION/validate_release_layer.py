from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'workflows/release-delivery/delivery/release-operations/release-readiness-policy.md',
    'workflows/release-delivery/delivery/release-operations/release-candidate-policy.md',
    'workflows/release-delivery/delivery/mobile-release/ios-app-store-release.md',
    'workflows/release-delivery/delivery/web-publishing/web-production-deployment.md',
    'policies/release-delivery/release-evidence-approvals/release-evidence-matrix.md',
    'skills/release-delivery/prepare-release-candidate/SKILL.md',
]
missing = [p for p in required if not (ROOT/p).exists()]
if missing:
    raise SystemExit('Missing release layer files: ' + ', '.join(missing))
print('Release layer validation passed.')
