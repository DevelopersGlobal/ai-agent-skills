---
name: ci-cd-pipelines
description: Automated quality gates from commit to production. Every merge to main is potentially shippable. No manual steps in the deployment path.
category: ship
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

CI/CD is the automation layer that enforces quality gates consistently, without relying on human memory or discipline. When CI is green, you know the code is tested, linted, and deployable. When it's red, nothing ships.

## When to Use

- Setting up a new project
- Adding a new quality gate
- Reviewing CI/CD pipeline configuration

## Process

### Step 1: CI Gates (Every PR)

1. All gates must pass before merge is allowed:
   - Lint: code style and static analysis
   - Unit tests: all pass
   - Integration tests: key boundaries covered
   - Security scan: SAST, dependency vulnerabilities
   - Build: production artifact builds successfully
2. Gates run in parallel where possible (speed matters).
3. Maximum CI time: 10 minutes. If slower, optimize.

**Verify:** Merging is blocked when any gate fails.

### Step 2: CD Pipeline (Every Main Merge)

4. Main branch is always deployable.
5. Deployment pipeline:
   - Deploy to staging → run smoke tests → deploy to production (canary) → full rollout
6. Every step is automated — no manual "click to deploy."
7. Rollback is automated and tested.

**Verify:** A push to main triggers automated deployment with no human intervention required.

### Step 3: Feature Flags Over Feature Branches

8. Incomplete features go behind feature flags — not long-lived branches.
9. Feature flags allow dark launching, A/B testing, and instant rollback without redeployment.
10. Feature flag state is tracked in a dashboard.

**Verify:** New features are behind flags. No feature branches > 2 days old.

### Step 4: Pipeline as Code

11. CI/CD config is in the repo (`.github/workflows/`, `.gitlab-ci.yml`, etc.).
12. Pipeline changes go through code review like any other change.
13. Pipeline config is tested: changes to CI don't break CI.

**Verify:** CI config is in the repo and reviewed.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "It's a small change, CI is optional" | Every "small change" that skipped CI is in the origin story of a major incident. |
| "Manual deployment gives us control" | Manual steps introduce human error. Automation gives you control. |
| "CI is too slow" | Optimize it. Don't skip it. |

## Verification

- [ ] All quality gates run on every PR
- [ ] Merge blocked when any gate fails
- [ ] Main → production deployment is fully automated
- [ ] Rollback is automated and tested
- [ ] Feature flags in place for incomplete features

## References

- [production-deployment skill](../production-deployment/SKILL.md)
- [git-workflow skill](../git-workflow/SKILL.md)
