---
name: ai-output-validation
description: Validates, parses, and sanitizes AI-generated outputs before they reach end users or downstream systems. Structured output enforcement, schema validation, and fallback handling.
category: test
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

AI models produce unstructured text by default. In production pipelines, unstructured outputs cause brittle parsing, unexpected behavior, and silent failures. This skill enforces structured output generation and validation at every AI system boundary.

## When to Use

- Any AI pipeline where output is used programmatically (not just displayed to a user)
- When AI output feeds into another system, database, or agent
- When building agentic systems that make decisions based on AI output
- When AI generates code, SQL, JSON, or other structured formats

## Process

### Step 1: Define Output Schema Before Prompting

1. Define the exact structure you need BEFORE writing the prompt.
2. Use JSON Schema or Pydantic/Zod models to formalize the expected output.
3. Example schema:
   ```json
   {
     "type": "object",
     "required": ["summary", "action", "confidence"],
     "properties": {
       "summary": {"type": "string", "maxLength": 200},
       "action": {"type": "string", "enum": ["approve", "reject", "review"]},
       "confidence": {"type": "number", "minimum": 0, "maximum": 1}
     }
   }
   ```
4. Design the schema to be **minimal** — only what you actually need.

**Verify:** Schema is defined and versioned before any prompt is written.

### Step 2: Prompt for Structured Output

5. Explicitly instruct the model to output in your defined format.
6. Include the schema or an example in the prompt.
7. Use models/APIs that support structured output natively where available (OpenAI structured outputs, Gemini JSON mode, Anthropic tool use).
8. Prompt pattern:
   ```
   Respond ONLY with valid JSON matching this schema:
   {schema}
   
   Do not include explanation or markdown. Output raw JSON only.
   ```

**Verify:** Prompt explicitly requests structured output with schema reference.

### Step 3: Validate and Parse Output

9. Parse the output against your schema — never use raw AI output directly.
10. If parsing fails:
    - Log the raw output and the parse error
    - Retry with a clarification prompt (max 2 retries)
    - After 2 failures: return a structured error, not a crash
11. Validate semantic constraints beyond the schema:
    - Is the `confidence` score consistent with the `action`?
    - Are referenced IDs in the database?
    - Are dates in the valid range?

**Verify:** All AI outputs pass schema validation before use. Failed validations are logged.

### Step 4: Sanitize for Downstream Use

12. If AI output will be rendered as HTML: sanitize against XSS.
13. If AI output will be executed as code: sandbox it and review before execution.
14. If AI output will be stored in a database: sanitize against injection.
15. Never trust AI output the way you'd trust your own code — it's user-generated content.

**Verify:** AI output is sanitized appropriate to its destination.

### Step 5: Monitor Output Quality

16. Log the schema validation pass/fail rate.
17. Sample and review AI outputs regularly for semantic correctness.
18. Alert on high validation failure rates (>5%).

**Verify:** Validation metrics are tracked. Alert configured.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "The model outputs valid JSON 99% of the time" | That 1% causes production incidents. Always validate. |
| "We display it to users, not parse it" | Users act on AI output. Wrong output drives wrong actions. |
| "Structured output adds latency" | Validation is microseconds. Debugging unvalidated output is hours. |
| "The model is deterministic enough" | No LLM is deterministic enough to skip validation. |

## Red Flags

- AI output used directly without schema validation
- `JSON.parse()` without try/catch around AI output
- AI-generated SQL or code executed without review
- No logging of validation failures
- AI output rendered as HTML without sanitization

## Verification

- [ ] Output schema defined and versioned
- [ ] Prompt explicitly requests structured output
- [ ] Schema validation on every AI response
- [ ] Retry logic for validation failures (max 2 retries)
- [ ] Semantic validation beyond schema (constraint checks)
- [ ] Sanitization applied appropriate to output destination
- [ ] Validation failure rate monitored

## References

- [hallucination-prevention skill](../hallucination-prevention/SKILL.md)
- [prompt-injection-defense skill](../prompt-injection-defense/SKILL.md)
- [security-hardening skill](../security-hardening/SKILL.md)
