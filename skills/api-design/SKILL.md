---
name: api-design
description: Design stable, versioned, self-documenting APIs. Easy to use correctly, hard to use incorrectly. Apply Hyrum's Law from day one.
category: build
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

APIs are contracts. Once published, every behavior — documented or not — becomes something users depend on (Hyrum's Law). This skill enforces the discipline of designing APIs that are stable, self-documenting, and difficult to misuse.

## When to Use

- Creating any public API endpoint
- Designing function/library APIs
- Extending or versioning existing APIs

## Process

### Step 1: Design the Interface First

1. Write the usage examples before writing the implementation.
2. Ask: Is this easy to use correctly? Is it hard to use incorrectly?
3. Apply the principle of least surprise — the API should do what it looks like it does.
4. Design for the caller, not the implementer.

**Verify:** You can write 3 example usages without looking at the implementation.

### Step 2: Apply Hyrum's Law

5. Every observable behavior of your API will be depended upon by someone.
6. Document what IS and IS NOT guaranteed:
   - Stable: return type, error codes, semantic behavior
   - Unstable: response time, field ordering, internal implementation
7. Be conservative in what you expose — you can always add, never remove.

**Verify:** Every public field and behavior is either documented as stable or marked as internal.

### Step 3: Versioning Strategy

8. Version from day one: `/api/v1/`, `Content-Type: application/vnd.myapi.v1+json`
9. Breaking changes require a new version.
10. Maintain old versions for at least 6 months with deprecation notices.
11. Additive changes (new optional fields) are non-breaking.

**Verify:** API version is in the URL or headers. Deprecation policy is documented.

### Step 4: Self-Documentation

12. Every endpoint: purpose, inputs, outputs, error codes — documented.
13. Error messages tell the caller what went wrong AND how to fix it.
14. Schema validation on all inputs with meaningful error messages.
15. OpenAPI/Swagger spec generated (not hand-written).

**Verify:** A new developer can use the API from documentation alone, without reading source code.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "We'll document it later" | Undocumented APIs become black boxes. Document as you build. |
| "We can break it, it's internal" | Internal APIs become external. Design them well from the start. |
| "Versioning is premature" | Retrofitting versioning into an unversioned API is painful. Start versioned. |

## Verification

- [ ] Interface designed before implementation
- [ ] Stable vs. unstable behaviors documented
- [ ] Versioning strategy in place
- [ ] All endpoints documented (OpenAPI/Swagger)
- [ ] Error messages actionable
- [ ] Breaking vs. non-breaking changes policy defined

## References

- [security-hardening skill](../security-hardening/SKILL.md)
- Hyrum's Law: https://www.hyrumslaw.com/
