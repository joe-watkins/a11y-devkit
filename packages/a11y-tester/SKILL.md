---
name: a11y-tester
description: Run automated accessibility tests on URLs using axe-core via Playwright browser tooling. Output raw violations or formatted issues (delegates to a11y-issue-writer). Automation is one layer; include keyboard + screen reader smoke guidance.
---

# Accessibility Tester

Run automated accessibility testing using axe-core and output violations in raw format or as formatted issues.

## Prerequisites: browser automation available
You need Playwright-style browser automation available in this chat context (navigate/evaluate/snapshot). If it’s not available, fall back to static analysis (`web-standards`) and clearly mark runtime checks as “not run”.

## Recommended layered workflow (fast → deeper)
Automated scans do **not** prove conformance.

1) **Automated scan (axe)**: key pages + key states (modals, errors, menus).
2) **Keyboard smoke** (2–5 min/page): Tab order, visible focus, Enter/Space, Esc.
3) **Screen reader smoke** (5–10 min/flow): role/name/state, headings/landmarks, form errors.
4) Targeted deep dive as needed: contrast, reflow/zoom, reduced motion, forced colors.

## Output options
- **Raw violations**: return violations array + summary counts.
- **Formatted issues**: delegate to `a11y-issue-writer`.

## Automated workflow (this skill)
1. Navigate to the target URL.
2. Run `axe.run()` and return:
   - `violations` (full array)
   - `passes` count
   - `incomplete` count
   - `inapplicable` count
3. Present summary first; then either:
   - raw JSON violations, or
   - delegate violations to a11y-issue-writer.

## Expected raw output (shape)
```json
{
  "violations": [/* axe violations */],
  "passes": 0,
  "incomplete": 0,
  "inapplicable": 0
}
```

## CI strategy (practical)
- PR: small smoke set of routes/states (fast)
- Nightly/pre-release: broader coverage
- Gating: fail on new `critical`/`serious` (or delta vs baseline)
- Save artifacts: `axe-results.json` (+ optional screenshots)

## Notes / limits
- Axe catches a subset of issues; always pair with keyboard + SR smoke on critical flows.
- Prefer deterministic axe setups for CI (e.g., `@axe-core/playwright`) when you control the harness; CDN injection is acceptable for ad-hoc checks.
