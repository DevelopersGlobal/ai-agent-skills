---
name: code-explanation
description: Get layered, context-aware explanations of unfamiliar code. Understand what it does, why it was written that way, and how to work with it safely.
category: everyday
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Understanding unfamiliar code is a daily engineering task — onboarding to a codebase, debugging a library, or reviewing a PR. AI agents can explain code, but without structure, explanations are either too high-level to be useful or too detailed to absorb.

This skill produces layered, targeted explanations: start with what it does, then why, then how to work with it.

## When to Use

- Onboarding to an unfamiliar codebase
- Understanding a complex function or algorithm before modifying it
- Debugging code you didn't write
- Reviewing a PR for a part of the system you don't know well

## Process

### Step 1: The 30-Second Summary

1. In 2–3 sentences: What does this code do? What problem does it solve?
2. What is the expected input? What is the output/effect?
3. Where does this fit in the larger system?

**Deliver:** A 2–3 sentence plain-English summary a junior engineer can understand.

### Step 2: Key Concepts and Patterns

4. What design patterns does this use? (observer, factory, pipeline, etc.)
5. What external libraries or frameworks are being used and why?
6. Are there any non-obvious algorithmic choices? (Why O(n log n) and not O(n²)?)
7. What are the key data structures and why were they chosen?

**Deliver:** 3–5 bullet points explaining the key design decisions.

### Step 3: Execution Walkthrough

8. Walk through the primary execution path step by step.
9. For each significant step: what happens? what state changes?
10. Highlight any surprising or non-obvious behavior.
11. Show example input → output.

**Deliver:** A numbered step-by-step walkthrough of the happy path.

### Step 4: Edge Cases and Gotchas

12. What inputs cause unexpected behavior?
13. What are the performance characteristics? (O(n) per call? Expensive on large inputs?)
14. What side effects does this have? (Modifies global state? Makes network calls?)
15. What could go wrong? What does failure look like?

**Deliver:** A "watch out for" section with at least 2 gotchas.

### Step 5: How to Work With This Code Safely

16. What should you not change without fully understanding? (Invariants, contracts)
17. What tests cover this code? Are there gaps?
18. What would break if you changed X?

**Deliver:** Specific guidance for safely modifying or extending this code.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "I'll just read it" | Reading unfamiliar code without structure is slow and error-prone. Use the layered approach. |
| "I'll ask a colleague" | Colleagues are often unavailable. AI can give a first-pass explanation 24/7. |
| "I understand it well enough" | "Well enough" has caused many production incidents. Confirm your understanding. |

## Red Flags

- Making changes to code you don't understand
- Assuming behavior without verifying it
- Skipping the "gotchas" section when under time pressure

## Verification

- [ ] 30-second summary written (would pass the "elevator test")
- [ ] Key design decisions explained
- [ ] Happy path walkthrough complete with example
- [ ] At least 2 gotchas identified
- [ ] Guidance on safe modification provided

## References

- [surgical-changes skill](../surgical-changes/SKILL.md)
- [debugging-methodology skill](../debugging-methodology/SKILL.md)
