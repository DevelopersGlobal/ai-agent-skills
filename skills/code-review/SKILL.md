---
name: code-review
description: Structured code review focusing on correctness, security, and maintainability. Correctness before style. Every reviewer comment must be actionable.
category: review
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Code review is the last line of defense before code reaches production. This skill structures the review process to catch real issues — not just style preferences — and ensures every comment is actionable and proportionate.

## When to Use

- Before merging any pull request
- When reviewing AI-generated code
- When auditing existing code for quality

## Process

### Step 1: Understand the Change

1. Read the PR description fully — understand the intent before reading code.
2. Check: Does the implementation match the stated intent?
3. Identify the risk level: data mutation? auth changes? public API?

**Verify:** You understand what the PR is trying to accomplish.

### Step 2: Correctness Review

4. Does the code do what it claims to do?
5. Are there off-by-one errors, null dereferences, or race conditions?
6. Are all error cases handled?
7. Do tests cover the happy path AND key failure paths?

**Verify:** You can trace the execution path for the primary use case and 2 failure cases.

### Step 3: Security Review

8. Apply [security-hardening skill](../security-hardening/SKILL.md) to any auth/input/data changes.
9. Does this change open any OWASP Top 10 vulnerabilities?
10. Are any secrets or PII handled correctly?

### Step 4: Maintainability Review

11. Will the next developer understand this code without the author present?
12. Are functions doing one thing?
13. Are names descriptive and accurate?
14. Is complexity proportionate to the problem?

### Step 5: Provide Actionable Feedback

15. Every comment must be one of:
    - **Blocker**: Must be fixed before merge
    - **Suggestion**: Optional improvement
    - **Question**: Needs clarification (not necessarily a problem)
16. Blockers must be specific: *"This SQL query is vulnerable to injection via `{username}` — use parameterized queries."*
17. Never leave vague comments like *"this doesn't look right"* without explaining why.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "I'll review it quickly" | A rushed review is not a review. Take the time or ask someone who can. |
| "The tests pass so it's fine" | Tests prove the code works for tested inputs, not that it's secure or maintainable. |
| "I'll comment on style later" | Style comments without blocker separation waste everyone's time. Label them. |

## Verification

- [ ] Correctness verified for primary and failure paths
- [ ] Security review applied to sensitive changes
- [ ] All comments labeled (blocker/suggestion/question)
- [ ] Tests reviewed for meaningful coverage
- [ ] No vague or unactionable comments

## References

- [security-hardening skill](../security-hardening/SKILL.md)
- [references/security-checklist.md](../../references/security-checklist.md)
