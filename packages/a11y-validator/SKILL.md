---
name: a11y-validator
description: Verify that accessibility fixes resolve identified issues by re-running tests and checking against acceptance criteria. Use this skill after fixes have been generated to confirm they work correctly. Uses a11y-tester for runtime re-testing and magentaa11y-mcp for acceptance criteria verification. Part of the a11y-orchestrator workflow.
---

# Accessibility Validator

Confirms that generated fixes resolve accessibility issues.

## Validation Workflow

1. **Apply fixes** to the code
2. **Re-run tests** to check if issues are resolved
3. **Check acceptance criteria** — query `magentaa11y-mcp`:
   - `get_web_component("button")` → Returns acceptance criteria
   - `get_component_gherkin("button")` → Returns Gherkin test syntax
4. **Categorize results** as fixed, needs-manual, or still-failing

## Re-Testing Process

### For Runtime Issues (from a11y-tester)

Re-run the `a11y-tester` skill on the modified code:

1. Serve or load the updated HTML
2. Execute axe-core scan
3. Compare violations to original list
4. Mark resolved issues as fixed

**Issue is fixed when:**
- axe-core no longer reports the violation
- The specific element/selector passes

### For Static Issues (from web-standards)

Re-apply the `web-standards` skill analysis:

1. Parse the updated code
2. Run the same checks that found the issue
3. Verify the problematic pattern is resolved

**Issue is fixed when:**
- The anti-pattern is no longer present
- Proper semantic/ARIA structure exists

## Acceptance Criteria Verification

**Query magentaa11y-mcp** for component acceptance criteria:
- `get_web_component("button")` → Returns full acceptance criteria
- `get_component_gherkin("button")` → Returns Gherkin test syntax
- `get_component_developer_notes("button")` → Returns implementation notes

For each fix, verify it meets the documented acceptance criteria:

### Example: Button Fix Validation

From magentaa11y-mcp button criteria, verify:
- [ ] Has accessible name (visible text or aria-label)
- [ ] Role is "button" (native or ARIA)
- [ ] Keyboard operable (Enter/Space activates)
- [ ] Focus visible when focused
- [ ] State communicated if applicable (pressed, expanded)

### Example: Form Input Fix Validation

From magentaa11y-mcp text-input criteria, verify:
- [ ] Label programmatically associated
- [ ] Required state communicated
- [ ] Error messages associated via aria-describedby
- [ ] Input purpose identifiable

### Example: Link Fix Validation

From magentaa11y-mcp link criteria, verify:
- [ ] Has accessible name
- [ ] Role is "link"
- [ ] Keyboard operable (Enter activates)
- [ ] Purpose clear from link text or context

## Result Categories

### ✅ Fixed

Issue confirmed resolved:
- Automated test passes
- Acceptance criteria met
- No regression introduced

```markdown
### Issue #N: [Description]
**Status:** ✅ Fixed
**Verification:** axe-core passes / static check passes
**Criteria Met:** [List from magentaa11y-mcp]
```

### ⚠️ Needs Manual Review

Cannot automatically verify:
- Visual verification required (contrast, focus style)
- Content quality check needed (alt text appropriateness)
- Complex interaction testing required
- User judgment needed

```markdown
### Issue #N: [Description]
**Status:** ⚠️ Needs Manual Review
**Reason:** [Why automated verification isn't possible]
**Manual Check:** [What human should verify]
**Guidance:** Query magentaa11y-mcp for component pattern
```

### ❌ Still Failing

Fix did not resolve the issue:
- Automated test still fails
- Pattern still detected
- Different approach needed

```markdown
### Issue #N: [Description]
**Status:** ❌ Still Failing
**Reason:** [Why fix didn't work]
**Suggestion:** [Alternative approach to try]
```

## Validation Checklist by Issue Type

### Accessible Name Issues
- [ ] Element now has accessible name
- [ ] Name is meaningful and descriptive
- [ ] Name matches visible label (if applicable)

### Semantic Structure Issues
- [ ] Correct HTML element used
- [ ] No redundant ARIA
- [ ] Proper nesting maintained

### Keyboard Issues
- [ ] Element is focusable
- [ ] Expected keys work (Enter, Space, Escape, Arrows)
- [ ] Focus order logical
- [ ] Focus visible

### Form Issues
- [ ] All inputs labeled
- [ ] Errors associated with inputs
- [ ] Required fields indicated
- [ ] Instructions associated

### Landmark Issues
- [ ] Required landmarks present
- [ ] No duplicate main landmarks
- [ ] Landmarks properly labeled if multiple

### Image Issues
- [ ] Alt attribute present
- [ ] Alt content appropriate (descriptive or empty)
- [ ] Decorative images marked correctly

## Evidence Expectations (Make Validation Actionable)

For each “✅ Fixed” issue, include at least one of:
- The **before/after** axe rule status (rule id + instance count)
- The **selector / snippet** that was previously failing and now passes
- Any **manual verification note** required for final confidence (e.g., focus visibility, reflow)

## Output Format

```markdown
## Validation Results

**Total Issues:** X
**Fixed:** Y
**Needs Manual Review:** Z
**Still Failing:** W

### Fixed Issues

| Issue | Description | Verification Method |
|-------|-------------|---------------------|
| #1 | Missing button name | axe-core: button-name passes |
| #2 | Skipped heading | Static: h1→h2→h3 present |

### Needs Manual Review

| Issue | Description | Manual Check Required |
|-------|-------------|-----------------------|
| #3 | Image alt text | Verify alt describes image content |
| #4 | Focus visibility | Verify focus ring meets 3:1 contrast |

### Still Failing

| Issue | Description | Reason | Next Step |
|-------|-------------|--------|-----------|
| #5 | Complex table | Headers not properly associated | Review table structure |
```

## Regression Checks

After validation, verify no new issues introduced:

1. Run full axe-core scan on modified code
2. Compare total violation count
3. Flag any new issues not in original list

### WCAG 2.2-Focused Regression Checks (Often Manual)

Even if axe-core is clean, explicitly verify or flag for manual review:
- **Focus Not Obscured (Minimum) (2.4.11 AA):** focused control remains visible with sticky headers/footers, banners, dialogs
- **Dragging Movements (2.5.7 AA):** drag-and-drop has an alternative (keyboard/buttons)
- **Target Size (Minimum) (2.5.8 AA):** small icon buttons/controls meet 24×24 CSS px or have an equivalent exception rationale
- **Accessible Authentication (Minimum) (3.3.8 AA):** login supports password managers; no cognition-only “puzzles” without alternatives

```markdown
## Regression Check

**New Issues Found:** X

| New Issue | Description | Introduced By |
|-----------|-------------|---------------|
| ... | ... | Fix for Issue #N |
```

## Quick Reference

| Validation Type | Tool/Resource | Pass Criteria |
|-----------------|---------------|---------------|
| axe violations | a11y-tester skill | Violation no longer reported |
| Static patterns | web-standards skill | Anti-pattern removed |
| Acceptance criteria | magentaa11y-mcp | All criteria checked |
| Visual checks | Manual | Human verification |
