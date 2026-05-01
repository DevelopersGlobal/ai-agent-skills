---
name: idea-to-spec
description: Converts vague ideas into concrete, testable specifications with acceptance criteria. No implementation begins without a spec.
category: think
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Vague ideas produce vague implementations. This skill transforms any idea — no matter how fuzzy — into a concrete specification with clear scope, acceptance criteria, and non-goals.

## When to Use

- At the start of any new feature
- When a request is ambiguous
- Before creating tasks or writing any code

## Process

### Step 1: Capture the Core Problem

1. Write: *"Users currently can't [do X], which causes [pain Y]."*
2. Identify: who has this problem? How often? What's the impact?
3. Distinguish problem from solution — don't spec a solution until the problem is understood.

**Verify:** You can state the problem without mentioning any implementation.

### Step 2: Define Success

4. Write 3–7 acceptance criteria in this format:
   ```
   Given [context]
   When [action]
   Then [outcome]
   ```
5. Each criterion must be binary — either it passes or it doesn't.
6. Include negative cases: *"Given X, the system must NOT do Y."*

**Verify:** A QA engineer can test each criterion without asking for clarification.

### Step 3: Define Scope

7. **In scope**: List what is explicitly included.
8. **Out of scope**: List what is explicitly excluded — as important as what's included.
9. **Open questions**: List any decisions that still need resolution before implementation.

**Verify:** The out-of-scope list has at least 2 items.

### Step 4: Define Non-Functional Requirements

10. Performance: response time, throughput, scale targets.
11. Security: auth requirements, data sensitivity.
12. Reliability: uptime SLA, acceptable error rate.

## Verification

- [ ] Problem statement written without mentioning implementation
- [ ] Acceptance criteria in Given/When/Then format
- [ ] Each criterion is binary (pass/fail)
- [ ] Explicit out-of-scope list
- [ ] Open questions listed

## References

- [think-before-coding skill](../think-before-coding/SKILL.md)
- [task-decomposition skill](../task-decomposition/SKILL.md)
