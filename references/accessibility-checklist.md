# Accessibility Checklist

Supporting reference for [frontend-engineering](../skills/frontend-engineering/SKILL.md).

## Keyboard Navigation
- [ ] All interactive elements reachable by Tab
- [ ] All interactive elements operable by Enter/Space
- [ ] Visible focus indicator on all focused elements (not removed with `outline:none`)
- [ ] Focus trapped in modals/dialogs; restored on close
- [ ] Skip navigation link at top of page

## Screen Reader
- [ ] Meaningful alt text on all images (`alt=""` for decorative)
- [ ] Form inputs have associated `<label>` elements
- [ ] Buttons and links have descriptive text (not "click here")
- [ ] ARIA roles used only when semantic HTML won't suffice
- [ ] Live regions (`aria-live`) for dynamic content updates
- [ ] Icons without text have `aria-label`

## Visual
- [ ] Color contrast ≥ 4.5:1 for normal text
- [ ] Color contrast ≥ 3:1 for large text (18px+ regular, 14px+ bold)
- [ ] Information not conveyed by color alone
- [ ] Text resizable up to 200% without horizontal scrolling
- [ ] No content flashing more than 3 times per second

## Structure
- [ ] Single `<h1>` per page; heading hierarchy is logical
- [ ] Page language set (`<html lang="en">`)
- [ ] Meaningful page title (`<title>`)
- [ ] Landmark regions used (`<nav>`, `<main>`, `<header>`, `<footer>`)

## Testing
- [ ] Automated: axe DevTools or Lighthouse accessibility audit ≥ 90
- [ ] Manual: navigate entire page with keyboard only
- [ ] Screen reader test (VoiceOver/NVDA) on critical flows
