---
name: documentation
description: Document decisions, not just implementations. ADRs for architectural choices, inline docs for non-obvious code, and runbooks for operational knowledge.
category: review
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Code explains what. Documentation explains why. The most valuable documentation records decisions that aren't obvious from reading the code: why this architecture, why this tradeoff, why not the obvious alternative.

## When to Use

- After any significant architectural decision
- Before complex code that future maintainers will question
- When an operational procedure isn't self-evident
- When a non-obvious tradeoff was made

## Process

### Step 1: Architectural Decision Records (ADRs)

For every significant architectural decision:
1. Write an ADR with:
   - **Context**: What was the situation requiring a decision?
   - **Decision**: What was decided?
   - **Alternatives considered**: What else was evaluated and why rejected?
   - **Consequences**: What are the positive and negative consequences?
   - **Status**: Proposed | Accepted | Deprecated | Superseded
2. Store ADRs in `docs/decisions/` as numbered markdown files.

**Verify:** Every significant decision in the last sprint has an ADR.

### Step 2: Code-Level Documentation

3. Document the WHY, not the WHAT:
   - ✅ `// Using exponential backoff here — the payment API has strict rate limits (3 req/sec)`
   - ❌ `// Retry the request`
4. Document non-obvious algorithmic choices.
5. Document external constraints (rate limits, API quirks, platform limitations).
6. Remove comments that state the obvious — they add noise.

**Verify:** Every non-obvious code block has a "why" comment.

### Step 3: Runbooks

7. For every production process that humans execute, write a runbook:
   - When is this runbook used?
   - What steps to execute?
   - What does "done" look like?
   - What could go wrong and how to recover?
8. Runbooks live in `docs/runbooks/`.

**Verify:** Every on-call alert has a linked runbook.

### Step 4: README Currency

9. README reflects current state (not v1 state).
10. Setup instructions work on a fresh machine.
11. Architecture diagram updated after significant changes.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "The code is self-documenting" | Code says what; documentation says why. Both are needed. |
| "I'll document it later" | The context in your head right now is irreplaceable. Write it now. |
| "Docs go stale" | Outdated docs are better than no docs. Update when you touch the code. |

## Verification

- [ ] ADRs written for significant architectural decisions
- [ ] Non-obvious code blocks have "why" comments
- [ ] Every production alert has a linked runbook
- [ ] README is current and setup instructions work

## References

- [git-workflow skill](../git-workflow/SKILL.md)
- [Michael Nygard's ADR template](https://github.com/joelparkerhenderson/architecture-decision-record)
