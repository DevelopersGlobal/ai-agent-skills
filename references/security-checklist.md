# Security Checklist

Quick-reference for the [security-hardening](../skills/security-hardening/SKILL.md) and [prompt-injection-defense](../skills/prompt-injection-defense/SKILL.md) skills.

## Authentication & Authorization
- [ ] All endpoints require authentication (except explicitly public ones)
- [ ] Authorization checked at the resource level, not just route level
- [ ] Principle of least privilege applied to all roles
- [ ] Session tokens are rotated after privilege escalation
- [ ] Brute-force protection on login (rate limiting, lockout)

## Input Validation
- [ ] All user input validated: type, length, format, allowlist
- [ ] No raw SQL constructed from user input (parameterized queries only)
- [ ] No shell commands constructed from user input
- [ ] File uploads: type validated server-side, stored outside web root
- [ ] JSON/XML input size limited to prevent DoS

## Secrets Management
- [ ] No secrets in source code (run: `git grep -i 'password\|secret\|token\|key'`)
- [ ] Secrets in environment variables or secrets manager
- [ ] `.env` files in `.gitignore`
- [ ] Secrets not in logs or error messages
- [ ] Secret rotation policy defined

## Transport Security
- [ ] HTTPS enforced for all endpoints
- [ ] HSTS header set
- [ ] TLS 1.2+ only (1.3 preferred)
- [ ] No sensitive data in URL query parameters

## AI-Specific
- [ ] User data separated from system instructions in prompts
- [ ] Agent tool list limited to minimum required
- [ ] AI inputs and outputs logged
- [ ] Prompt injection test cases run before launch
- [ ] AI-generated outputs validated before use/display

## Dependencies
- [ ] Dependency vulnerability scan run (`npm audit`, `pip-audit`, `cargo audit`)
- [ ] No known critical/high CVEs in production dependencies
- [ ] Lock file committed (`package-lock.json`, `Cargo.lock`, etc.)
