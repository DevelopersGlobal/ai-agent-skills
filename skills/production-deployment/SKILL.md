---
name: production-deployment
description: Zero-downtime deployments with pre-flight checks, staged rollouts, and rollback plans. Never ship to production without a verified rollback strategy.
category: ship
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Production is not a test environment. Every deployment is a live operation with real consequences — user impact, data integrity risks, and potential outages. This skill encodes the discipline senior engineers apply before, during, and after every production deployment.

The core rule: **never deploy without a rollback plan you've verified can execute in under 5 minutes.**

## When to Use

- Before any deployment to a production or production-equivalent environment
- When reviewing deployment scripts or CI/CD pipelines
- When adding new services or infrastructure changes

## Process

### Step 1: Pre-Deployment Checklist

1. **All tests pass** — CI is green on the exact commit being deployed. Not "mostly green."
2. **Migrations are backward-compatible** — The old code must work with the new schema (for zero-downtime). New columns are nullable; columns aren't dropped until after full rollout.
3. **Feature flags configured** — New features are behind flags, off by default.
4. **Rollback plan written** — Document exactly how to rollback: which commands, which configs, estimated time.
5. **Deployment window confirmed** — Low-traffic period? On-call engineer available?
6. **Stakeholders notified** — Anyone affected by downtime or behavior change knows.

**Verify:** All 6 checklist items confirmed. Do not proceed if any is blocked.

### Step 2: Staged Rollout

7. Never deploy to 100% of traffic immediately. Use a staged rollout:
   - Canary: 1–5% of traffic
   - Staged: 10% → 25% → 50% → 100%
8. Monitor key metrics at each stage for at least 15 minutes before expanding:
   - Error rate (baseline vs. current)
   - Latency p50, p95, p99
   - Business metrics (conversion, orders, etc.)
9. **Define your abort threshold before starting**: *"If error rate exceeds X% or latency p99 exceeds Y ms, rollback immediately."*

**Verify:** Rollout stages and abort thresholds are documented before deployment begins.

### Step 3: Deploy

10. Execute the deployment using your CI/CD pipeline (not manual commands).
11. Monitor dashboards in real-time during the rollout.
12. Keep communication channel open with on-call engineer.
13. Do not perform any other changes during a deployment (no "quick fixes").

**Verify:** Deployment running via CI/CD, dashboards being monitored actively.

### Step 4: Post-Deployment Verification

14. Smoke tests pass on production.
15. Key user journeys manually verified.
16. Error rate within normal range (15 minutes post-deploy).
17. No unexpected alerts triggered.
18. Run post-deploy integration tests if available.

**Verify:** All post-deploy checks confirmed green. Deployment marked successful.

### Step 5: Rollback (if needed)

19. If any abort threshold is hit: **rollback immediately, without debate.**
20. Execute the pre-written rollback plan.
21. Verify rollback complete: service restored, error rate normalized.
22. Write an incident report — even for near-misses.

**Verify:** Rollback completes in under 5 minutes. Service restored.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "It works in staging" | Staging is not production. Different data, traffic, and configuration. |
| "It's just a small change" | Small changes cause the majority of outages. |
| "We don't have time for staged rollout" | You have even less time for an incident. |
| "I'll watch it for a few minutes" | 15 minutes minimum. Most production failures take time to materialize under load. |
| "We can rollback if needed" | Do you have a written, tested rollback plan? No? Then you can't. |

## Red Flags

- Deploying directly to 100% without a staged rollout
- No rollback plan documented before deployment
- Deploying breaking schema changes without backward compatibility
- Running deployment from a local machine, not CI/CD
- Deploying during high-traffic periods without approval
- "I'll fix any issues after we deploy"

## Verification

- [ ] All tests passing on exact commit being deployed
- [ ] Migrations are backward-compatible
- [ ] Rollback plan written and executable in <5 minutes
- [ ] Staged rollout plan with abort thresholds defined
- [ ] Post-deploy smoke tests passed
- [ ] Dashboards clean for 15 minutes post-deploy

## References

- [ci-cd-pipelines skill](../ci-cd-pipelines/SKILL.md)
- [observability skill](../observability/SKILL.md)
- [git-workflow skill](../git-workflow/SKILL.md)
- [references/deployment-checklist.md](../../references/deployment-checklist.md)
