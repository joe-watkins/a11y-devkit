---
name: web-standards
description: Static HTML/CSS/ARIA analysis without requiring a browser. Use this skill when analyzing code for semantic HTML issues, ARIA validity, landmark structure, heading hierarchy, form labeling, or any accessibility problems detectable from source code. Queries aria-mcp for ARIA rules and wcag-mcp for success criteria mapping. Part of the a11y-orchestrator workflow.
---

# Web Standards Analyzer

Static accessibility analysis of HTML, CSS, and ARIA without browser execution.

## Analysis Categories

Work through each category, noting any issues found.

### 1. Semantic HTML

Check for proper semantic element usage:

| Check | Issue Pattern | Fix Direction |
|-------|--------------|---------------|
| Buttons | `<div onclick>`, `<span onclick>`, `<a role="button">` | Use `<button>` |
| Links | `<span onclick>` for navigation, `<button>` with href behavior | Use `<a href>` |
| Headings | `<div class="title">`, skipped levels (h1→h3) | Use `<h1>`-`<h6>` in order |
| Lists | Series of `<div>` for list items | Use `<ul>/<ol>` with `<li>` |
| Tables | `<div>` grids for tabular data | Use `<table>` with proper headers |
| Nav | `<div class="nav">` | Use `<nav>` landmark |
| Main | Content without `<main>` | Wrap primary content in `<main>` |
| Forms | Inputs without associated labels | Add `<label for="">` |

### 2. ARIA Validity

Query `aria-mcp` for authoritative ARIA rules:
- `get-role("button")` → Returns role requirements
- `validate-role-attributes("button", ["aria-pressed"])` → Validates ARIA usage
- `get-prohibited-attributes("button")` → Returns disallowed attributes

Check for:

**Invalid ARIA on semantic elements:**
- `<button role="button">` — redundant
- `<a role="link">` — redundant
- `<a role="button">` — misuse (use `<button>` instead)

**Missing required ARIA:**
- Custom widgets without appropriate roles
- Interactive elements without accessible names
- Dynamic content without live regions

**Invalid ARIA combinations:**
- `aria-checked` on non-checkbox/switch roles
- `aria-expanded` on elements without expandable content
- `aria-selected` outside selection contexts

**Query aria-mcp** for role-specific requirements when custom widgets are found:
- `get-required-attributes("tabpanel")` → Returns required attributes
- `get-required-context("tab")` → Returns required parent context
- `suggest-role("dropdown menu")` → Suggests appropriate role

### 3. Landmark Structure

Check page has appropriate landmarks:

| Landmark | Expected | Issue If Missing |
|----------|----------|------------------|
| `<main>` or `role="main"` | One per page | No main landmark |
| `<nav>` or `role="navigation"` | For navigation | Navigation not identified |
| `<header>` or `role="banner"` | Top-level header | No banner landmark |
| `<footer>` or `role="contentinfo"` | Top-level footer | No content info |

**Watch for:**
- Multiple `<main>` elements
- Landmarks inside landmarks of same type
- Overuse of landmarks (every section doesn't need one)

### 4. Heading Hierarchy

Verify heading structure:

1. Page should have exactly one `<h1>`
2. Headings should not skip levels (h1→h2→h3, not h1→h3)
3. Headings should reflect content hierarchy
4. Visual headings should be semantic headings

**Query wcag-mcp:** `get-criterion("1.3.1")` for Info and Relationships

### 5. Form Accessibility

Check all form controls:

| Element | Required | Check |
|---------|----------|-------|
| `<input>` | Label | Has `<label for="">` or `aria-label` |
| `<select>` | Label | Has associated label |
| `<textarea>` | Label | Has associated label |
| Required fields | Indication | `required` or `aria-required` |
| Errors | Association | `aria-describedby` to error message |
| Groups | Labeling | `<fieldset>`/`<legend>` for radio/checkbox groups |

**Invalid patterns:**
- Placeholder as only label
- Label not programmatically associated
- Hidden label without accessible alternative

### 6. Image Accessibility

Check all images and graphics:

| Element | Check | Issue |
|---------|-------|-------|
| `<img>` | Has `alt` attribute | Missing alt |
| Informative `<img>` | `alt` describes content | Empty alt on meaningful image |
| Decorative `<img>` | `alt=""` | Descriptive alt on decorative image |
| `<svg>` | Has accessible name or `aria-hidden` | SVG not labeled or hidden |
| Icon fonts | Has text alternative | Icon-only with no text |

**Query wcag-mcp:** `get-criterion("1.1.1")` for Non-text Content

### 7. Keyboard Accessibility

Static checks for keyboard support:

| Check | Issue Pattern |
|-------|--------------|
| `tabindex` > 0 | Disrupts natural tab order |
| `tabindex="-1"` on interactive | Removes from tab order |
| `onclick` without keyboard handler | Mouse-only interaction |
| Non-focusable interactive | Custom widget without `tabindex="0"` |

**Query wcag-mcp:** `get-criterion("2.1.1")` for Keyboard

### 8. Text and Contrast (CSS)

Check CSS for potential issues:

| Check | Issue Pattern |
|-------|--------------|
| `outline: none` | Removes focus indicator |
| `outline: 0` | Removes focus indicator |
| Fixed font sizes | May prevent text resize |
| `user-select: none` | May prevent text selection |

**Query wcag-mcp:** `get-criterion("2.4.7")` for Focus Visible, `get-criterion("1.4.4")` for Resize Text

## Output Format

Report issues in this structure:

```markdown
## Static Analysis Results

Found X accessibility issues:

### Issue 1: [Brief description]
- **Location:** [file:line or element path]
- **Category:** [Semantic HTML/ARIA/Landmarks/etc.]
- **Severity:** [Critical/Serious/Moderate/Minor]
- **WCAG:** [Success criterion from wcag-mcp]
- **Code:**
```html
[problematic code]
```
- **Problem:** [What's wrong]

---
```

## Severity Guidelines

| Severity | Criteria |
|----------|----------|
| Critical | Blocks access entirely (no keyboard, no name) |
| Serious | Major barrier (skipped headings, no labels) |
| Moderate | Degrades experience (redundant ARIA, poor semantics) |
| Minor | Best practice violation (optimization opportunities) |

## MCP Server Queries

When you encounter these situations, query the referenced MCP server:

| Situation | Query MCP | Example Tool |
|-----------|-----------|--------------|
| Custom ARIA widget | `aria-mcp` | `get-required-attributes("dialog")` |
| WCAG criterion details | `wcag-mcp` | `get-techniques-for-criterion("1.3.1")` |
| Correct implementation | `magentaa11y-mcp` | `get_component_developer_notes("modal")` |
