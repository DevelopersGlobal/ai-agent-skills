---
name: debugging-methodology
description: Systematic root cause analysis for production and development bugs. Hypothesis-driven debugging — never guess-and-check.
category: test
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Random code changes in response to errors are not debugging — they're noise generation. This skill enforces a systematic, hypothesis-driven approach: understand the problem, form a hypothesis, test it, confirm the root cause, then fix.

AI agents often cycle through random fixes until something "works." This skill prevents that.

## When to Use

- Any time a test fails unexpectedly
- Any time you encounter an error or exception
- When behavior differs between environments
- When performance degrades unexpectedly

## Process

### Step 1: Reproduce Reliably

1. Before doing anything else: **reproduce the bug reliably**. If you can't reproduce it, you can't fix it.
2. Write a failing test that captures the bug — this becomes your regression test.
3. Note the exact conditions that trigger the bug: inputs, environment, sequence of actions.

**Verify:** You can trigger the bug on demand.

### Step 2: Understand Before Diagnosing

4. Read the full error message — not just the first line.
5. Read the stack trace from bottom to top — the root cause is usually near the bottom.
6. Identify: *What was the program trying to do? What happened instead?*

**Verify:** You can explain the bug in one sentence without using the word "error."

### Step 3: Form a Hypothesis

7. Based on what you know, form a specific hypothesis: *"I think the bug is X because Y."*
8. The hypothesis must be **falsifiable** — you can design a test that proves or disproves it.
9. Do not start making code changes until you have a hypothesis.

**Verify:** Your hypothesis is specific enough to design a test for.

### Step 4: Test the Hypothesis

10. Add targeted logging or a targeted test that confirms or refutes the hypothesis.
11. Run it. Read the output carefully.
12. If the hypothesis is **wrong**: update your understanding, form a new hypothesis, repeat.
13. If the hypothesis is **right**: you've found the root cause.

**Verify:** Root cause is confirmed by evidence, not assumed.

### Step 5: Fix the Root Cause (Not the Symptom)

14. Fix the root cause — not the symptom. Suppressing an error message is not a fix.
15. Make the minimum change that fixes the root cause.
16. Run the failing test you wrote in Step 1 — it should now pass.
17. Run the full test suite — no regressions.

**Verify:** The specific failing test now passes. Full suite still passes.

### Step 6: Prevent Recurrence

18. If the bug wasn't caught by existing tests: add a test that would have caught it.
19. If the bug was caused by a bad assumption: document the assumption or add a guard.
20. Consider: does this class of bug exist elsewhere in the codebase?

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "Let me just try this and see" | Random changes produce random results. Form a hypothesis first. |
| "It must be a framework bug" | It's almost never the framework. Prove it before blaming it. |
| "Works on my machine" | Environment differences are root causes. Find them. Don't dismiss them. |
| "I'll add a try/catch" | That hides the bug. Find and fix the root cause. |

## Red Flags

- Making code changes before understanding the bug
- Adding try/catch to silence errors without investigating root cause
- "I'll try this and see if it helps"
- Assuming the bug is in a dependency before proving it
- Fixing the symptom (error message) rather than the cause

## Verification

- [ ] Bug reproducible on demand
- [ ] Root cause identified (not just symptom)
- [ ] Fix targets root cause, not symptom
- [ ] Reproduction test written and now passes
- [ ] Full test suite passes with no regressions
- [ ] Regression test added to prevent future occurrence

## References

- [test-driven-development skill](../test-driven-development/SKILL.md)
- [observability skill](../observability/SKILL.md)
