from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    'RELEASE_OPERATIONS/RELEASE_READINESS_POLICY.md',
    'RELEASE_OPERATIONS/RELEASE_CANDIDATE_POLICY.md',
    'MOBILE_RELEASE/IOS_APP_STORE_RELEASE.md',
    'WEB_PUBLISHING/WEB_PRODUCTION_DEPLOYMENT.md',
    'RELEASE_EVIDENCE_AND_APPROVALS/RELEASE_EVIDENCE_MATRIX.md',
    'SKILLS/release_skills/prepare_release_candidate/SKILL.md',
]
missing = [p for p in required if not (ROOT/p).exists()]
if missing:
    raise SystemExit('Missing release layer files: ' + ', '.join(missing))
print('Release layer validation passed.')
