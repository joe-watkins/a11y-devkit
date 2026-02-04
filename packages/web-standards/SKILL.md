---
name: web-standards
description: Static HTML/CSS/ARIA analysis without requiring a browser. Use for semantic HTML, ARIA validity, landmarks, headings, forms, keyboard/focus signals, tables, and other accessibility problems detectable from source. Queries aria-mcp for ARIA rules and wcag-mcp for SC mapping.
---

# Web Standards Analyzer

Static accessibility analysis of HTML, CSS, and ARIA without browser execution.

## Rules of thumb (HTML/ARIA)
1. Prefer native elements over ARIA.
2. Don’t add ARIA when native semantics already exist.
3. Every interactive control needs: keyboard operability + accessible name + visible focus.
4. ARIA can’t “fix” broken interaction. If you’re adding lots of ARIA, re-check the HTML choice.
5. Don’t hide focusable content from AT (`aria-hidden="true"` on focusable content is almost always a bug).

## Analysis categories

### 1) Semantic HTML

| Check | Issue pattern | Fix direction |
|---|---|---|
| Buttons | `<div onclick>`, `<span onclick>`, `<a role="button">` | Use `<button>` (and set `type="button"` unless it should submit a form) |
| Links | Clickable elements used for navigation without `<a href>` | Use `<a href>` |
| Headings | Styled `<div>` headings; skipped levels | Use `<h1>`–`<h6>` in logical order |
| Lists | Series of `<div>` items | Use `<ul>/<ol>` + `<li>` |
| Tables | `<div>` grids for tabular data | Use `<table>` + headers |
| Forms | Inputs without associated labels | Add `<label>` or appropriate ARIA |

Also check:
- correct input types (`email`, `tel`, etc.)
- avoid using heading tags purely for styling

### 2) ARIA validity

Query `aria-mcp`:
- `get-role("button")`
- `validate-role-attributes("button", ["aria-pressed"])`
- `get-prohibited-attributes("button")`

Check for:
- redundant/misleading ARIA on native elements
- missing accessible names (icon-only controls)
- `aria-labelledby` / `aria-describedby` referencing missing/duplicate IDs
- `aria-hidden="true"` on focusable elements (or ancestors)
- `role="presentation"/"none"` on interactive/focusable elements
- dialogs without accessible name (`aria-labelledby`/`aria-label`)

### 3) Landmarks
- one main per view
- nested `<header>/<footer>` inside sectioning content are **not** banner/contentinfo
- multiple nav landmarks should be distinguishable via an accessible name (e.g., `aria-label="Primary"`)

### 4) Heading hierarchy
- Prefer a single `<h1>` for the page/topic; multiple `<h1>` → flag for review.
- Don’t skip levels.

### 5) Forms
- labels are programmatically associated (not placeholder-only)
- errors/helper text associated via `aria-describedby`
- invalid state uses `aria-invalid` where relevant
- groups use `<fieldset>/<legend>`
- autocomplete present for common fields (when applicable)

### 6) Images/icons
- `<img>` has `alt` (empty for decorative)
- `<svg>` either named appropriately or `aria-hidden="true"` when decorative

### 7) Keyboard & focus signals (static heuristics)

| Check | Issue pattern |
|---|---|
| Positive tabindex | disrupts natural order |
| `tabindex="-1"` on interactive | usually removes from tab order (sometimes OK for focus mgmt only) |
| `onclick` on non-native controls | mouse-only unless role + tabindex + Enter/Space handling |
| Focus styles removed | `outline: none/0` without replacement |

Also check:
- presence of a skip link (`href="#main"` etc.)

### 8) Focus management (static signals)
- skip link targets exist + are unique
- hidden containers don’t contain focusable descendants

### 9) Tables
- `<th>` used for headers; `scope` for simple tables
- complex headers use `headers`/`id`
- `<caption>` when it improves understanding

### 10) Contrast (static hints)
> True contrast usually can’t be proven from CSS alone (variables/themes/images). Flag obvious risks/patterns.

## Output format

```markdown
## Static Analysis Results

Found X accessibility issues:

### Issue 1: [Brief description]
- **Location:** [file:line or element path]
- **Category:** [Semantic HTML / ARIA / Landmarks / Forms / Keyboard / Tables / CSS]
- **Severity:** [Critical/Serious/Moderate/Minor]
- **WCAG:** [SC from wcag-mcp if known]
- **Code:**
  ```html
  [problematic code]
  ```
- **Problem:** [What’s wrong]
- **Fix:** [What to change / recommended pattern]
```

## MCP lookups (common)
- WCAG: `wcag-mcp.get-criterion("1.3.1")`, `get-criterion("2.1.1")`, `get-criterion("2.4.7")`, `get-criterion("1.1.1")`
- ARIA: role/attribute validity via `aria-mcp`
- Correct patterns: `magentaa11y-mcp`
