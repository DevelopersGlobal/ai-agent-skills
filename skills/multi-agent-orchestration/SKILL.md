---
name: multi-agent-orchestration
description: Designs and coordinates multi-agent pipelines where specialized agents collaborate to complete complex tasks. Includes communication protocols, failure handling, and state management.
category: plan
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Single agents are limited by context window, specialization depth, and parallelism. Multi-agent systems overcome these limits by routing subtasks to specialized agents. But multi-agent systems introduce new failure modes: lost context, conflicting decisions, infinite loops, and cascading failures.

This skill provides the architecture and coordination patterns to build multi-agent systems that are reliable, observable, and maintainable.

## When to Use

- The task requires more context than a single agent can handle
- Different subtasks require different specializations (research, coding, review, security)
- Subtasks can be parallelized for speed
- The workflow is long-running and requires checkpointing
- Different tasks require different levels of human oversight

## Process

### Step 1: Design the Agent Network

1. **Define agent responsibilities**: Each agent should have a single, well-defined job. Name them by role: `researcher`, `coder`, `reviewer`, `security-auditor`, `tester`.
2. **Define communication topology**: Who can talk to whom?
   - **Pipeline**: Agent A → Agent B → Agent C (sequential)
   - **Supervisor**: Orchestrator dispatches to specialists (hub-and-spoke)
   - **Peer**: Agents collaborate as equals (mesh)
3. **Define data contracts**: What does each agent receive? What does it output? Use structured formats (JSON schemas) for inter-agent communication.
4. **Define the orchestration logic**: Who decides which agent acts next?

**Verify:** You can draw the agent network on a whiteboard with clear roles and data flow.

### Step 2: Implement Context Management

5. Each agent should receive **only the context it needs** — not the full conversation history.
6. Use a shared state store (database, key-value store) for information that multiple agents need.
7. Pass **summaries**, not full transcripts, when context must traverse agent boundaries.
8. Include a **task ID** in every message for tracing.

**Verify:** No agent receives more context than it requires for its specific task.

### Step 3: Design for Failure

9. **Every agent call can fail** — plan for it:
   - Timeout with a defined maximum duration
   - Retry with exponential backoff (max 3 retries)
   - Fallback behavior when retries are exhausted
10. **Prevent infinite loops**: Track call depth. If depth > N (e.g., 10), surface to human review.
11. **Checkpointing**: For long workflows, save state after each major step so the workflow can be resumed after failure.
12. **Dead letter queue**: Failed tasks that exhaust retries go to a queue for human inspection.

**Verify:** Failure scenarios are defined for every agent-to-agent call.

### Step 4: Human-in-the-Loop Checkpoints

13. Define which decisions require human approval:
    - Irreversible actions (data deletion, financial transactions, external communications)
    - High-uncertainty states (agents disagree, confidence below threshold)
    - Sensitive operations (PII access, privileged system access)
14. Design the human review interface: What information does the reviewer need? What actions can they take?

**Verify:** At least one human-in-the-loop checkpoint exists for high-risk operations.

### Step 5: Observability

15. Log every agent invocation: inputs, outputs, duration, token usage, errors.
16. Implement distributed tracing across the agent network (trace ID propagated through all calls).
17. Dashboard: agent activity, success/failure rates, latency, token consumption.
18. Alerts: agent down, retry rate spike, context overflow, unexpected output patterns.

**Verify:** You can trace any specific task's full execution path across all agents from logs alone.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "One agent is simpler" | Until it hits context limits, fails silently, or produces wrong results. Multi-agent is the right tool for complex tasks. |
| "We'll add observability later" | Multi-agent systems without observability are black boxes. Debug them in production — I dare you. |
| "Agents are smart, they'll figure it out" | Agents are tools. They need clear roles, contracts, and failure boundaries. |
| "The happy path works fine" | Multi-agent systems fail in complex ways. Design for failure from day one. |

## Red Flags

- Agents pass full conversation history to other agents (context bloat)
- No timeout defined for any agent call
- Agents can call each other recursively without depth limits
- No human approval required for irreversible actions
- No distributed tracing across agent boundaries
- Agents making conflicting state changes with no conflict resolution

## Verification

- [ ] Agent network designed with clear roles and data contracts
- [ ] Context is minimized at each agent boundary
- [ ] Failure handling (timeout, retry, fallback) for every agent call
- [ ] Infinite loop prevention via call depth limits
- [ ] Human-in-the-loop checkpoints for high-risk operations
- [ ] Distributed tracing implemented across agents
- [ ] End-to-end test of failure scenarios

## References

- [task-decomposition skill](../task-decomposition/SKILL.md)
- [observability skill](../observability/SKILL.md)
- [prompt-injection-defense skill](../prompt-injection-defense/SKILL.md)
- [hallucination-prevention skill](../hallucination-prevention/SKILL.md)
