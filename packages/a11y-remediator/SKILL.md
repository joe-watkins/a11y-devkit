---
name: a11y-remediator
description: Generate accessibility fixes for identified issues using MCP servers for component patterns (magentaa11y-mcp), ARIA guidance (aria-mcp), WCAG criteria (wcag-mcp), and user impact (a11y-personas-mcp). Fixes are minimal and localized, with verification/regression guidance. Part of the a11y-orchestrator workflow.
---

# Accessibility Remediator

Generates fixes for accessibility issues by querying MCP sources for authoritative guidance.

## Critical constraint: Fix what exists

**Only remediate code that already exists in the file.** This skill must NOT:
- add new structural elements (new headings/landmarks/sections/regions)
- add or invent user-visible content (copy, new labels, new heading text)
- invent destinations/URLs/routes or change navigation intent
- redesign page structure or interaction patterns
- refactor unrelated code

This skill SHOULD:
- fix accessibility issues in existing elements
- add attributes to existing elements (`aria-*`, `alt`, etc.) when needed
- convert inaccessible elements to accessible equivalents **while preserving behavior**
- flag structural/content/UX decisions as **Needs Manual Review** with safe options

## Guardrails: preserve behavior & avoid regressions
- Prefer native elements/semantics over ARIA.
- Preserve existing visible text/labels unless the issue explicitly requires change and the correct text already exists elsewhere.
- Keep DOM order/focus order consistent unless the issue is about order.
- Avoid adding `tabindex`; never add positive tabindex.
- If you add ARIA, ensure it matches actual behavior/state in code.

## Fix generation workflow
For each issue:
1. Identify component type (button/link/form field/image/dialog/etc.).
2. Query MagentaA11y for the pattern:
   - `magentaa11y-mcp.get_web_component(component)`
   - `magentaa11y-mcp.get_component_developer_notes(component)`
3. If ARIA is needed, query `aria-mcp` for role/attribute validity.
4. Query `wcag-mcp` for SC details/techniques.
5. Query `a11y-personas-mcp` for impacted users (when helpful).
6. Propose minimal code change(s) + rationale.
7. Include “How to verify” + regression notes.

## Risk gates (escalate to Manual Review)
Escalate when:
- meaningful wording is required (alt text, link text, heading text, error copy)
- destination/URL is unknown (don’t guess an `href`)
- composite widgets (combobox/dialog/menu/tabs/grid) lack clear state management
- multiple valid patterns exist and the right one depends on UX/business logic
- fix would require new structure/landmarks/major CSS changes

## Common fix patterns (examples)

### Missing accessible name
```html
<!-- Icon-only button (existing button, missing name) -->
<button type="button" aria-label="Close dialog"><svg aria-hidden="true">…</svg></button>

<!-- Input missing label: prefer existing visible text; otherwise Manual Review -->
<label for="email">Email</label>
<input id="email" type="email" />
```

### Fake interactive elements
```html
<!-- Before -->
<div class="btn" onclick="submit()">Submit</div>

<!-- After (preserve handler; keep styling class) -->
<button type="button" class="btn" onclick="submit()">Submit</button>

<!-- Link-like span with onclick: don't invent href -->
<span class="link" onclick="navigate()">Learn more</span>
<button type="button" class="link" onclick="navigate()">Learn more</button>
```

## Testing & verification loop (include in output when practical)
- Automated: re-run axe (or equivalent) for the affected view.
- Keyboard: Tab reachability, Enter/Space activation, focus visible; Esc closes dismissibles.
- SR smoke (as needed): correct role+name (+ state); errors/helper text announced.

**Definition of done (per issue):**
- reported violation resolved
- no new serious violations introduced in the modified area
- behavior preserved (click/submit/nav) and keyboard remains functional

## Output format (per issue)
- Issue summary
- Proposed change (before/after or patch)
- Why it works (pattern + WCAG/ARIA notes)
- How to verify (automated + manual)
- Manual Review flags (if any)
