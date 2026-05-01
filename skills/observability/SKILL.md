---
name: observability
description: Structured logging, distributed tracing, and alerting for AI systems and traditional services. You can't fix what you can't see.
category: harden
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Observability is the ability to understand the internal state of a system from its external outputs. For AI systems this is especially critical: agents make decisions that are hard to interpret without detailed telemetry.

The three pillars: **Logs** (what happened), **Traces** (how long and where), **Metrics** (aggregate health).

## When to Use

- Before deploying any new service to production
- When adding AI agent capabilities to an existing system
- When debugging production issues
- When designing multi-agent pipelines

## Process

### Step 1: Structured Logging

1. All logs must be **structured** (JSON, not free text). Fields: `timestamp`, `level`, `service`, `traceId`, `message`, `context`.
2. Log levels used correctly:
   - `ERROR`: Something failed that requires immediate attention
   - `WARN`: Something unexpected happened but the system recovered
   - `INFO`: Normal significant events (requests received, jobs completed)
   - `DEBUG`: Detailed diagnostic information (off in production by default)
3. **Never log secrets, PII, or auth tokens.**
4. For AI systems, log: prompt inputs (sanitized), model outputs, token counts, latency, model version.

**Verify:** Logs are structured JSON. No secrets in logs. AI interactions logged.

### Step 2: Distributed Tracing

5. Every request gets a unique `traceId` generated at the entry point.
6. `traceId` is propagated through all downstream calls (HTTP headers, message queues, agent calls).
7. Each service/agent creates a **span** for its work, with: start time, end time, parent span ID.
8. Use OpenTelemetry as the standard instrumentation library.

**Verify:** You can trace a single request across all services/agents in a single view.

### Step 3: Metrics

9. Define and track key metrics:
   - **RED metrics**: Rate (requests/sec), Errors (error rate %), Duration (latency p50/p95/p99)
   - **AI-specific**: Token usage, prompt cost, model latency, hallucination rate, retrieval precision
10. Dashboards: one dashboard per service with RED metrics, one dashboard for AI system health.

**Verify:** RED metrics are tracked for every service. AI-specific metrics tracked for AI systems.

### Step 4: Alerting

11. Alerts must be **actionable** — every alert should have a runbook.
12. Alert on symptoms (high error rate, high latency), not just causes.
13. AI-specific alerts: token budget exceeded, model error rate spike, retrieval failure rate spike.
14. On-call rotation: someone is responsible for every alert at all times.

**Verify:** Every alert has a runbook. On-call rotation defined.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "We'll add monitoring after launch" | You'll be fighting fires blind. Add it before. |
| "Console.log is enough" | In production, console.log is noise. Structured logs with context are signals. |
| "The AI model handles it internally" | Model internals are a black box. You must observe the inputs and outputs. |

## Verification

- [ ] Structured JSON logging on all services
- [ ] No secrets in logs
- [ ] Distributed tracing with trace ID propagation
- [ ] RED metrics tracked for all services
- [ ] AI-specific metrics tracked (tokens, cost, latency)
- [ ] Alerts configured with runbooks

## References

- [production-deployment skill](../production-deployment/SKILL.md)
- [multi-agent-orchestration skill](../multi-agent-orchestration/SKILL.md)
- OpenTelemetry documentation
