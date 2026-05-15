from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'workflows/delivery/release-operations/RELEASE_READINESS_POLICY.md',
    'workflows/delivery/release-operations/RELEASE_CANDIDATE_POLICY.md',
    'workflows/delivery/mobile-release/IOS_APP_STORE_RELEASE.md',
    'workflows/delivery/web-publishing/WEB_PRODUCTION_DEPLOYMENT.md',
    'policies/delivery/release-evidence-approvals/RELEASE_EVIDENCE_MATRIX.md',
    'skills/delivery/release_skills/prepare_release_candidate/SKILL.md',
]
missing = [p for p in required if not (ROOT/p).exists()]
if missing:
    raise SystemExit('Missing release layer files: ' + ', '.join(missing))
print('Release layer validation passed.')
