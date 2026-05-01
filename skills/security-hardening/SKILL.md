---
name: security-hardening
description: Applies OWASP Top 10, secrets management, and least-privilege principles before any code ships. Security is a build step, not an afterthought.
category: harden
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Security vulnerabilities are almost always cheaper to prevent than to remediate. This skill embeds security review as a required gate in the development workflow — not a separate audit that happens later (and often never).

## When to Use

- Before any code involving user input
- Before any code touching authentication, authorization, or sessions
- Before any API endpoint is created or modified
- Before any code that handles secrets, credentials, or PII
- Before any code that makes outbound network requests

## Process

### Step 1: Threat Model the Change

1. Ask: *Who are the attackers? What are they trying to achieve?*
2. Identify all trust boundaries in the code:
   - Where does user-controlled data enter the system?
   - Where does that data flow?
   - Where is it stored or transmitted?
3. For each trust boundary, name the top 3 attack vectors.

**Verify:** You can name at least one realistic attack scenario for this code.

### Step 2: Apply OWASP Top 10 Checklist

4. For each applicable item, confirm it is addressed:

| OWASP Item | Check |
|------------|-------|
| **A01 Broken Access Control** | Authorization checked at every endpoint? Principle of least privilege applied? |
| **A02 Cryptographic Failures** | No plaintext PII/secrets? Using modern algorithms (AES-256, SHA-256+)? TLS everywhere? |
| **A03 Injection** | All user input parameterized/sanitized? No raw SQL/shell construction? |
| **A04 Insecure Design** | Threat model done? Secure defaults? Fail closed (not open)? |
| **A05 Security Misconfiguration** | No default credentials? Unnecessary features disabled? Error messages don't leak internals? |
| **A06 Vulnerable Components** | Dependencies up to date? Known CVEs checked? |
| **A07 Auth Failures** | Brute-force protection? Session management correct? MFA available? |
| **A08 Software Integrity** | Dependencies verified? Supply chain integrity? |
| **A09 Logging Failures** | Security events logged? No secrets in logs? Logs protected from tampering? |
| **A10 SSRF** | Outbound requests validated? Internal IPs blocked from user-controlled URLs? |

**Verify:** Each applicable item is either addressed or explicitly accepted as a known risk.

### Step 3: Secrets Management

5. **No hardcoded secrets** — ever. Not even in dev/test code.
6. Secrets are stored in: environment variables, secrets manager (Vault, AWS Secrets Manager, etc.), or encrypted config.
7. Secrets are **never** logged, printed, or included in error messages.
8. Secrets are **never** committed to git (check `.gitignore` and use pre-commit hooks).

**Verify:** `git grep -i 'password\|secret\|key\|token'` returns no hardcoded values in code.

### Step 4: Input Validation

9. Every piece of external input is validated:
   - Type check
   - Length/size limits
   - Allowlist of expected values (not blocklist)
   - Reject and log unexpected input — never silently ignore
10. User-controlled data is **never** concatenated into SQL, shell commands, HTML, or file paths without proper escaping/parameterization.

**Verify:** All external input has explicit validation with reject-by-default behavior.

### Step 5: Least Privilege

11. Database connections use the minimum required permissions.
12. API tokens have the minimum required scopes.
13. Service accounts cannot access resources they don't need.
14. Default deny — access must be explicitly granted, not implicitly inherited.

**Verify:** List every permission granted by this code. Is each one required?

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "It's internal only" | Internal services get breached too. Zero-trust applies internally. |
| "We'll add auth later" | Auth bolted on later is always broken. Design it in from the start. |
| "The input is from our own frontend" | Attackers don't use your frontend. Validate on the server, always. |
| "It's a dev environment" | Dev environments get credentials from prod. Treat them accordingly. |
| "The secret is in a config file, not code" | Is the config file in git? Is it world-readable? Config files are not safe. |

## Red Flags

- User input directly interpolated into queries or commands
- Authentication middleware that can be bypassed
- Error messages that include stack traces or SQL queries
- API keys or passwords in source code or comments
- Missing authorization check on any endpoint
- HTTP used instead of HTTPS for any sensitive data

## Verification

- [ ] OWASP Top 10 checklist reviewed for applicable items
- [ ] No hardcoded secrets (`git grep` clean)
- [ ] All external input validated (type, length, allowlist)
- [ ] No raw SQL/shell from user input
- [ ] Least privilege applied to all credentials
- [ ] Security events are logged (but secrets are not)
- [ ] Dependency vulnerabilities checked

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [prompt-injection-defense skill](../prompt-injection-defense/SKILL.md)
- [references/security-checklist.md](../../references/security-checklist.md)
