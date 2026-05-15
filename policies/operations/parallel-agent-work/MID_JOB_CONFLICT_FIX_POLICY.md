# Mid-Job Conflict Fix Policy

If a conflict is detected while an agent is still working:
1. Pause the affected agent(s).
2. Create a mid-job conflict report.
3. Identify whether the conflict is file, baseline, API, design, security, release, or provider/brand related.
4. Select a resolution: rebase, reissue packet, switch to mock mode, freeze baseline, create change request, cancel/supersede packet, or reconcile outputs.
5. Update the affected packets.
6. Continue only after the conflict record is resolved or accepted as risk.

Agents must not keep working on known conflicting instructions.

If the mid-job conflict invalidates the original parallel work plan, update or replace that plan before any affected agent resumes.
