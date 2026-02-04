---
name: a11y-base-web
description: Foundational accessibility patterns and requirements for AI-generated web code. Load this skill first before accessibility analysis/remediation/validation. Other a11y skills build on these fundamentals.
---

# Accessibility Fundamentals (Web)

## Scope / sources (traceability)
- WCAG 2.1 + WCAG 2.2, WAI-ARIA 1.2+, WAI-ARIA Authoring Practices (APG).
- Preference order: **native HTML** → **minimal ARIA** → **custom widgets only when necessary** (then follow APG).

## Quick Baseline Checklist (always)
- Semantic HTML first (`button`, `a[href]`, `label`, headings, lists).
- Keyboard works (Tab/Shift+Tab; Enter/Space; Esc where applicable).
- **Visible focus** is never removed; custom focus is OK if clearly visible.
- Every form control has a programmatic label (not placeholder-only).
- Visible label text is included in the accessible name (WCAG 2.1 SC 2.5.3).
- Color isn’t the only cue; contrast meets minimums.
- Motion respects `prefers-reduced-motion`.
- Images/icons: confirm decorative vs informative before writing alt text.
- ARIA only when needed; no redundant roles/states; references point to real IDs.

## LLM behavior & tone
- Use respectful, inclusive language.
- Be verification-oriented; state uncertainty.
- Be concise; avoid overconfidence.

---

## Anti-patterns to avoid (high-signal)
- Placeholder-only “labels”.
- `outline: none` (or equivalent) without an equal-or-better focus indicator.
- Positive `tabindex` (almost always).
- Click handlers on non-interactive elements without full keyboard + name/role.
- Redundant/conflicting ARIA (e.g., `role="button"` on `<button>`).
- `aria-hidden="true"` on focusable content or its ancestor.

### Common ARIA misuse (redundant roles)
Bad:
```html
<button role="button">Click me</button>
<a role="link" href="/x">Read more</a>
```
Good:
```html
<button type="button">Click me</button>
<a href="/x">Read more</a>
```

### `aria-label` rule of thumb
- Avoid `aria-label` when the control already has clear visible text (it can cause label-in-name mismatches).
- Use `aria-label` for **icon-only** or otherwise unlabeled controls.

Icon-only example:
```html
<button type="button" aria-label="Close dialog">
  <svg aria-hidden="true" viewBox="0 0 24 24">...</svg>
</button>
```

---

## Required accessibility patterns

### Page-level structure (layout pages)
- Set document language: `<html lang="en">` (or appropriate BCP 47 tag)
- Meaningful `<title>` per view/route
- Skip link to main content (when there’s repeated nav)
- Landmarks: `header/nav/main/footer` **sparingly**; **one** main per view

### Keyboard & focus
- All interactive elements reachable with Tab; no traps.
- Buttons activate with Enter/Space; links activate with Enter.
- Composite widgets (menus/tabs/listbox/combobox/grid) must follow APG keyboard rules.
- Dialogs/overlays: move focus into the dialog on open; restore focus on close; prevent focus escaping while open.
- Do not remove focus styles. Prefer the native focus ring; if customizing, keep it clearly visible.

### Touch targets
- Minimum target size: **24×24 CSS px** aligns with WCAG 2.2 SC **2.5.8** (AA).
- Preferred (usability / many platform guides): **44×44**.
- Exception handling: if constrained, don’t go below 24×24.

### Semantics
- Use native controls (`<button>`, `<a href>`, `<input>`, etc.).
- For non-submit buttons inside forms, set `type="button"`.

### Forms
- Labels: use `<label for>` (or wrap input). Placeholder is supplemental only.
- Group related controls with `<fieldset>` + `<legend>` (e.g., radio groups).
- Required fields: use native `required`; communicate requirements in text (not color alone).
- Errors/help: associate via `aria-describedby`; use `aria-invalid` when relevant.

### Contrast
- Text: 4.5:1 normal, 3:1 large.
- Non-text UI (incl. focus indicators, input borders): 3:1 against adjacent colors.
- Don’t rely on color alone for meaning.

### Motion
- Respect `prefers-reduced-motion: reduce`.
- Don’t rely on hover-only interaction; provide keyboard/touch equivalents.

### Tables (when truly tabular)
- Use `<table>` for data, not layout.
- Use `<th>` + `scope` (or `headers`/`id` for complex headers).
- Add `<caption>` when it improves understanding.

---

## Quick testing workflow (fast heuristics)
1) Keyboard pass (2 min): reach everything, focus visible, activate controls.
2) Semantics pass (1 min): buttons are buttons, links navigate, headings/lists correct.
3) Name/label pass (2 min): inputs labeled; icon-only controls named.
4) Contrast/zoom pass (2–5 min): spot-check focus indicator + UI boundaries; 200% text and ~400% zoom/reflow.
5) Automation (supplement): axe/Lighthouse/eslint-plugin-jsx-a11y where available.
