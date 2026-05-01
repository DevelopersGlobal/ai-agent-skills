---
name: research-and-summarize
description: Distill complex topics into layered, actionable summaries. Start with the key insight, layer in detail, end with recommended next action.
category: everyday
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Information overload is the default state. This skill transforms any research task into a structured summary: headline insight first, context second, detail third, action last. Designed for decision-makers who need clarity, not comprehensiveness.

## When to Use

- Summarizing technical documentation or papers
- Researching a technology choice
- Briefing a team on a topic
- Distilling a long document for a specific decision

## Process

### Step 1: Define the Research Question

1. State the specific question being answered: *"Should we use Kafka or RabbitMQ for our event pipeline?"*
2. State who the answer is for and what decision it enables.
3. This scopes the research — don't gather information beyond what the decision needs.

**Verify:** Research question is specific enough to have a clear answer.

### Step 2: Gather and Evaluate Sources

4. Identify 3–5 high-quality, authoritative sources.
5. For each source, note: recency, authority, potential bias.
6. Cross-reference key claims across sources.
7. Flag conflicting information — don't silently pick one side.

**Verify:** Key claims are supported by at least 2 independent sources.

### Step 3: Write the Layered Summary

8. **Headline (1 sentence)**: The single most important insight.
9. **Key findings (3–5 bullets)**: Supporting evidence for the headline.
10. **Context and nuance (1–2 paragraphs)**: Caveats, tradeoffs, conditions under which the headline doesn't hold.
11. **What we don't know**: Gaps in the available information.
12. **Recommended action**: Given the findings, what should the reader do next?

**Deliver:** A structured summary with all 5 sections.

### Step 4: Cite Sources

13. Every factual claim is linked to a source.
14. Include the date of each source (recency matters in fast-moving fields).

**Verify:** Every claim has a citation.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "The topic is too complex to summarize" | The goal is to enable a decision, not to be comprehensive. Scope to the decision. |
| "I'll just share the links" | Links are not summaries. Distillation is the value. |

## Verification

- [ ] Research question defined before research begins
- [ ] Key claims cross-referenced across 2+ sources
- [ ] Summary has: headline, findings, context, unknowns, action
- [ ] Every factual claim has a citation with date

## References

- [think-before-coding skill](../think-before-coding/SKILL.md)
- [idea-to-spec skill](../idea-to-spec/SKILL.md)
