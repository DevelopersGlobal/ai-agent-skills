---
name: hallucination-prevention
description: Detects and mitigates LLM hallucinations in production pipelines. Validates AI-generated facts, code, and decisions before they reach end users or downstream systems.
category: harden
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

LLMs hallucinate — they generate plausible-sounding but factually incorrect content with high confidence. In production systems, hallucinations cause incorrect medical advice, broken code, wrong legal citations, fabricated API calls, and erroneous financial data.

This skill builds hallucination detection and mitigation into your AI pipeline architecture — before output reaches users or downstream systems.

## When to Use

- Any AI pipeline where factual accuracy matters
- When agents generate code, SQL, or API calls that will be executed
- When agents retrieve information that will influence decisions
- RAG (Retrieval-Augmented Generation) systems
- Agentic pipelines with tool use and multi-step reasoning

## Process

### Step 1: Classify Your Hallucination Risk

1. Map all AI outputs in your system. For each, classify:
   - **Critical**: Incorrect output causes harm (medical, legal, financial, code execution)
   - **High**: Incorrect output wastes significant user/system resources
   - **Medium**: Incorrect output is annoying but recoverable
   - **Low**: Incorrect output is cosmetic
2. Apply this skill's full rigor to Critical and High outputs. Lighter checks for Medium and Low.

**Verify:** Every AI output in your pipeline has a hallucination risk classification.

### Step 2: Ground LLM Outputs

3. For factual queries: **always provide source documents** in the prompt (RAG pattern). Instruct the model to cite sources and refuse to answer if the information isn't in the provided documents.
4. For code generation: run the code in a sandbox and verify it produces the expected output before returning to the user.
5. For structured outputs (JSON, SQL, etc.): validate against a schema before using.
6. For numerical claims: require the model to show its work step-by-step and verify key calculations independently.

**Verify:** Every Critical/High output is grounded in provided sources or verified by execution.

### Step 3: Build Verification Layers

7. **Self-consistency checking**: Ask the model the same question 2–3 ways and compare answers. Divergent answers signal uncertain ground.
8. **Chain-of-thought with verification**: Prompt the model to reason step-by-step, then verify the reasoning chain, not just the conclusion.
9. **Separate generation from verification**: Use one prompt to generate, a different prompt to critically evaluate. Never use the same model call for both.
10. **Human-in-the-loop for Critical outputs**: Require human review before Critical AI-generated content reaches end users.

**Verify:** Critical outputs have at least two independent verification mechanisms.

### Step 4: Design Fail-Safe Defaults

11. When the model is uncertain, it should say so — never present uncertain information as confident fact.
    - Prompt pattern: *"If you're not sure, say 'I don't know' rather than guessing."*
12. Confidence scores: Where available, expose confidence thresholds. Route low-confidence outputs to human review.
13. Graceful degradation: If the AI cannot answer accurately, show the user relevant source documents instead.

**Verify:** The system has a defined behavior for when AI confidence is low.

### Step 5: Monitor for Hallucinations in Production

14. Log all AI inputs and outputs.
15. Implement feedback mechanisms (thumbs up/down, explicit corrections).
16. Regularly audit a sample of outputs for accuracy.
17. Track and alert on: sudden changes in output patterns, high user correction rates, model responses contradicting grounded sources.

**Verify:** A feedback mechanism exists and hallucination incidents are tracked.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "This model is highly accurate" | All LLMs hallucinate. Accuracy ≠ 100%. Design for the failure case. |
| "Users will catch errors" | Users often can't distinguish hallucinated content from real content. Don't rely on them. |
| "It's a demo/MVP" | Hallucinations that reach demos become the baseline expectation. Fix them early. |
| "We'll add verification in v2" | Hallucinations that cause harm in v1 may not give you a v2. |

## Red Flags

- AI-generated code is executed without testing or sandbox verification
- AI-generated facts are displayed without source citations
- No human review for medical, legal, or financial AI outputs
- The same model is used to generate and verify its own output
- No logging or monitoring of AI outputs in production

## Verification

- [ ] All AI outputs classified by hallucination risk
- [ ] Critical/High outputs are grounded in source documents or execution
- [ ] At least two independent verification mechanisms for Critical outputs
- [ ] System has a defined low-confidence fallback behavior
- [ ] Human-in-the-loop for Critical outputs
- [ ] Production monitoring and feedback mechanism in place

## References

- [prompt-injection-defense skill](../prompt-injection-defense/SKILL.md)
- [ai-output-validation skill](../ai-output-validation/SKILL.md)
- [rag-and-memory skill](../rag-and-memory/SKILL.md)
- [OWASP LLM09: Overreliance](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
