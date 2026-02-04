---
name: a11y-remediator
description: Generate accessibility fixes for identified issues using MCP servers for component patterns (magentaa11y-mcp), ARIA guidance (aria-mcp), WCAG criteria (wcag-mcp), and user impact (a11y-personas-mcp). Use this skill when you have a list of accessibility issues and need to produce corrected code with full context. Part of the a11y-orchestrator workflow.
---

# Accessibility Remediator

Generates fixes for accessibility issues by querying MCP servers for authoritative guidance.

## Critical Constraint: Fix What Exists

**Only remediate code that already exists in the file.** This skill should NOT:
- Add new structural elements (headings, landmarks, sections)
- Add content the developer didn't include
- Redesign the page structure
- Make opinionated additions

**This skill SHOULD:**
- Fix accessibility issues in existing elements
- Add attributes to existing elements (aria-*, alt, etc.)
- Convert inaccessible elements to accessible equivalents
- Report structural issues as "Needs Manual Review" with guidance

If an issue requires adding new elements (like a missing `<h1>`), categorize it as **Needs Manual Review** and provide guidance rather than auto-adding content.

## Behavior Preservation Guardrails (Do No Harm)

Accessibility fixes must preserve existing product behavior, styling intent, analytics hooks, and test selectors.

**Default to the smallest safe change:**
- Prefer adding/removing attributes on existing elements over replacing elements.
- If changing semantics is necessary (e.g., `<div onclick>` → `<button>`), keep:
  - Existing classes, ids, data-* attributes, and event handlers (or equivalent bindings)
  - Existing accessible name text (do not “improve copy”)
  - Existing layout behavior (avoid introducing new wrappers)

**Event + focus safety checklist (apply before outputting a fix):**
- Do not break click/press behavior:
  - Ensure keyboard activation works (Enter/Space for buttons; Enter for links)
  - If converting non-semantic to semantic, ensure key handling is not duplicated (avoid double-submit)
- Do not introduce unexpected focus changes:
  - Do not auto-focus elements unless explicitly required by the component’s current behavior
  - Preserve tab order; avoid adding `tabindex` unless required and justified
- Prefer native semantics over ARIA:
  - Avoid `role` on native controls unless required by a known pattern
  - Avoid adding ARIA that changes user expectations (e.g., `aria-live`) without strong evidence

**If you cannot guarantee behavior preservation, escalate to _Needs Manual Review_** and explain what must be validated (e.g., analytics, form submission, keyboard interactions).

## Fix Generation Workflow

For each accessibility issue:

1. **Identify the component type** — button, link, form field, image, etc.
2. **Get the correct pattern** — query `magentaa11y-mcp`:
   - `get_web_component("button")` → Returns acceptance criteria
   - `get_component_developer_notes("button")` → Returns implementation guidance
3. **Get ARIA guidance** — query `aria-mcp` if ARIA is needed:
   - `get-role("button")` → Returns role requirements
   - `validate-role-attributes("button", ["aria-pressed"])` → Validates ARIA usage
   - `get-required-attributes("button")` → Returns required attributes
4. **Map to WCAG** — query `wcag-mcp` for success criterion:
   - `get-criterion("4.1.2")` → Returns SC details and understanding docs
   - `get-techniques-for-criterion("4.1.2")` → Returns implementation techniques
5. **Document impact** — query `a11y-personas-mcp` for affected users:
   - `get-personas(["blindness-screen-reader-nvda"])` → Returns persona details
   - `list-personas()` → Returns all 69 personas for reference

## Verification Loop (Required)

After proposing a fix, include a brief verification plan that can be executed by a developer or CI:

**Re-run the detector(s):**
- Re-run the same linter/axe/test that reported the issue to confirm it is resolved.
- Confirm no new violations were introduced nearby (especially Name/Role/Value, focus order, and color contrast).

**Functional regression checks (minimum):**
- Keyboard-only:
  - Tab/Shift+Tab reaches the control
  - Enter/Space activation behaves as before
  - Focus indicator remains visible
- Screen reader sanity check (minimum expectation):
  - Control announces an appropriate role and accessible name
  - State is announced if applicable (checked/expanded/pressed/invalid)
- Forms:
  - Submission still works; validation and error messaging still appears as before

**If verification depends on runtime state, routing, or app-specific behavior, flag _Needs Manual Review_** and describe exactly what to test.

## Fix Strategies by Issue Type

### Missing Accessible Name

**Pattern:** Element has no accessible name for assistive technology

**Query magentaa11y-mcp:** `get_web_component("button")` for naming pattern

**Fix approaches:**
```html
<!-- Button with icon only → add aria-label -->
<button aria-label="Close dialog"><svg>...</svg></button>

<!-- Link with icon only → add visually hidden text -->
<a href="/home"><span class="visually-hidden">Home</span><svg>...</svg></a>

<!-- Input without label → add label element -->
<label for="email">Email address</label>
<input id="email" type="email">
```

**WCAG:** 4.1.2 Name, Role, Value — query `wcag-mcp`: `get-criterion("4.1.2")`

### Fake Interactive Elements

**Pattern:** Non-semantic elements used for interaction

**Query magentaa11y-mcp:** `get_web_component("button")` or `get_web_component("link")` for correct semantics

**Fix approaches:**
```html
<!-- div with onclick → native button -->
<!-- Before -->
<div class="btn" onclick="submit()">Submit</div>
<!-- After -->
<button class="btn" onclick="submit()">Submit</button>

<!-- span link → native anchor -->
<!-- Before -->
<span class="link" onclick="navigate()">Learn more</span>
<!-- After -->
<a href="/learn-more">Learn more</a>
```

**WCAG:** 4.1.2 Name, Role, Value

### Missing Form Labels

**Pattern:** Form inputs without programmatic labels

**Query magentaa11y-mcp:** `get_web_component("text-input")`, `get_web_component("select")`, `get_web_component("checkbox")`

**Fix approaches:**
```html
<!-- Explicit label -->
<label for="username">Username</label>
<input id="username" type="text">

<!-- Implicit label (wrapping) -->
<label>
  Username
  <input type="text">
</label>

<!-- aria-label for visually hidden label -->
<input type="search" aria-label="Search products">
```

**WCAG:** 1.3.1 Info and Relationships, 3.3.2 Labels or Instructions

### Invalid ARIA

**Pattern:** ARIA used incorrectly or redundantly

**Query aria-mcp:** `validate-role-attributes(role, states)` for correct combinations

**Fix approaches:**
```html
<!-- Redundant role → remove -->
<!-- Before -->
<button role="button">Click</button>
<!-- After -->
<button>Click</button>

<!-- Wrong role → correct or use semantics -->
<!-- Before -->
<a role="button" href="#">Action</a>
<!-- After: if it navigates -->
<a href="#">Action</a>
<!-- After: if it triggers action -->
<button>Action</button>

<!-- Invalid state → correct context -->
<!-- Before: aria-checked on div -->
<div aria-checked="true">Option</div>
<!-- After -->
<input type="checkbox" checked id="opt">
<label for="opt">Option</label>
```

### Heading Issues

**Pattern:** Skipped levels or non-semantic headings

**Query wcag-mcp:** `get-criterion("1.3.1")` for heading requirements

**Fix approaches:**
```html
<!-- Skipped level → add missing levels or restructure -->
<!-- Before -->
<h1>Title</h1>
<h3>Subsection</h3>
<!-- After -->
<h1>Title</h1>
<h2>Section</h2>
<h3>Subsection</h3>

<!-- Visual heading → semantic heading -->
<!-- Before -->
<div class="heading-2">Section Title</div>
<!-- After -->
<h2>Section Title</h2>
```

### Missing Landmarks

**Pattern:** Page lacks proper landmark structure

**Query aria-mcp:** `list-landmarks()` for landmark roles and regions

**Fix approaches:**
```html
<!-- Add main landmark -->
<main>
  <!-- primary content -->
</main>

<!-- Add navigation landmark -->
<nav aria-label="Main navigation">
  <ul>...</ul>
</nav>

<!-- Add header/footer landmarks -->
<header><!-- banner content --></header>
<footer><!-- contentinfo --></footer>
```

### Image Alt Text

**Pattern:** Images missing or with incorrect alt text

**Query magentaa11y-mcp:** `get_web_component("image")` for informative vs decorative patterns

**Fix approaches:**
```html
<!-- Informative image → descriptive alt -->
<img src="chart.png" alt="Sales increased 25% from Q1 to Q2">

<!-- Decorative image → empty alt -->
<img src="decorative-border.png" alt="">

<!-- Icon in button → aria-hidden, name on button -->
<button aria-label="Close">
  <svg aria-hidden="true">...</svg>
</button>
```

**WCAG:** 1.1.1 Non-text Content

### Focus Visibility

**Pattern:** Focus indicator removed or insufficient

**Query wcag-mcp:** `get-criterion("2.4.7")` for Focus Visible requirements

**Fix approaches:**
```css
/* Remove outline:none, add visible focus */
/* Before */
button:focus { outline: none; }

/* After */
button:focus { 
  outline: 2px solid #005fcc;
  outline-offset: 2px;
}

/* Or use focus-visible for keyboard only */
button:focus-visible {
  outline: 2px solid #005fcc;
  outline-offset: 2px;
}
```

## Documenting User Impact

**Query a11y-personas-mcp** to identify affected users:
- `list-personas()` → Returns all 69 personas
- `get-personas(["blindness-screen-reader-nvda", "motor-impairment-voice-control"])` → Returns specific personas

Include:

| Issue Type | Likely Affected Personas |
|------------|-------------------------|
| No accessible name | Screen reader users (blindness personas) |
| No keyboard access | Motor impairment, keyboard-only users |
| Missing labels | Screen reader users, voice control users |
| Poor contrast | Low vision, color vision deficiency |
| No focus indicator | Keyboard users, low vision |
| Motion/animation | Vestibular disorders, cognitive |

**Example impact statement:**
> Affects users like Sabina (screen reader user) who cannot identify the button's purpose, and Marcus (voice control user) who cannot target unlabeled controls.

## Output Format

For each fix:

```markdown
### Issue #N: [Brief description]

**WCAG:** [SC number] [SC name]
**Severity:** [Critical/Serious/Moderate/Minor]
**Impact:** [One sentence describing user impact]
**Persona:** [From a11y-personas-mcp]

**Before:**
```html
[original code]
```

**After:**
```html
[fixed code]
```

**Pattern:** [MagentaA11y component link]
**Rationale:** [Brief explanation of why this fix works]
```

## When Manual Review Required

Flag for manual review when:

**Escalation criteria (hard stops):** Mark as Manual Review if any are true:
- The fix changes interaction model (link vs button) but intent is ambiguous (navigate vs action).
- The control is part of a composite widget (menus, dialogs, comboboxes, tabs, grids, carousels) requiring:
  - managed focus, roving tabindex, aria-activedescendant, or complex keyboard maps
- Any change would require adding/removing DOM nodes beyond a direct semantic replacement.
- Dynamic announcements might be needed (`aria-live`, status messages) but timing/content is uncertain.
- The issue is “structural accessibility” (landmarks/headings/page outline) where the correct structure is a product decision.
- The correct accessible name/alt text requires understanding the UI purpose or business domain.

- Content decision needed (alt text content, heading text)
- Complex widget requiring design input
- Multiple valid approaches available
- Business logic affects accessibility choice

```markdown
### Issue #N: [Brief description] ⚠️ Manual Review

**Reason:** [Why automated fix isn't possible]
**Options:**
1. [Approach A with tradeoffs]
2. [Approach B with tradeoffs]

**Guidance:** Query relevant MCP server for patterns
**Personas Affected:** [Query a11y-personas-mcp]
```
