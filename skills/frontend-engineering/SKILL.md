---
name: frontend-engineering
description: Accessible, performant, responsive UI patterns. Component design, state management discipline, and Core Web Vitals compliance.
category: build
applies-to: [claude, gemini, cursor, copilot, any]
version: 1.0.0
---

## Overview

Frontend code touches every user. Poor UI engineering causes accessibility barriers, performance degradation, and broken experiences on non-standard devices. This skill enforces the discipline of building UI that works for everyone.

## When to Use

- Building any user-facing UI component
- Reviewing frontend PRs
- Before any UI ships to production

## Process

### Step 1: Accessibility First

1. Every interactive element has a visible focus state.
2. All images have meaningful alt text (or `alt=""` for decorative).
3. Color contrast ratio ≥ 4.5:1 for normal text.
4. All functionality operable by keyboard alone.
5. Use semantic HTML: `<button>` not `<div onclick>`, `<nav>` not `<div class="nav">`.

**Verify:** Run axe DevTools or Lighthouse accessibility audit. Score ≥ 90.

### Step 2: Performance (Core Web Vitals)

6. LCP (Largest Contentful Paint) < 2.5s: Optimize images, preload critical resources.
7. FID/INP < 100ms: Avoid long tasks on the main thread.
8. CLS (Cumulative Layout Shift) < 0.1: Reserve space for dynamic content.
9. Lazy load below-the-fold images and non-critical JS.
10. Bundle size: measure before and after. No unneeded dependencies.

**Verify:** Lighthouse performance score ≥ 80. CWV within targets.

### Step 3: Responsive Design

11. Test at 320px, 768px, 1024px, 1440px viewports.
12. No horizontal scrolling at any standard viewport.
13. Touch targets ≥ 44px × 44px.

### Step 4: State Management Discipline

14. Server state vs. client state are separate concerns — don't mix.
15. No prop drilling more than 2 levels — use context or state management.
16. Loading, error, and empty states handled for every async operation.

**Verify:** Loading, error, and empty states all visible in Storybook/dev environment.

## Common Rationalizations (and Rebuttals)

| Excuse | Rebuttal |
|--------|----------|
| "Accessibility is for edge cases" | 1 in 4 adults has a disability. It's not an edge case. |
| "We'll optimize performance later" | Users leave after 3 seconds. "Later" is too late. |

## Verification

- [ ] Accessibility audit score ≥ 90
- [ ] Core Web Vitals within targets
- [ ] Responsive at 320px/768px/1024px/1440px
- [ ] Loading, error, empty states handled
- [ ] All interactive elements keyboard-operable

## References

- [references/accessibility-checklist.md](../../references/accessibility-checklist.md)
- [performance-optimization skill](../performance-optimization/SKILL.md)
