# Agent Dispatch Policy

Before dispatching any sub-agent:
1. Select the required capability.
2. Select provider or human executor.
3. Check brand-family consistency for dependent work.
4. Create or reference an execution packet.
5. Validate dependencies and source-of-truth baselines.
6. Classify conflict risk.
7. Confirm allowed repos/paths and forbidden actions.
8. Record the run in `AGENT_RUN_REGISTRY.md`.

Dispatch does not mean autonomous execution in the file-based engine. It means the packet is ready to be executed by the chosen provider/human.
