---
name: a11y-validator
description: Verify that accessibility fixes resolve identified issues by re-running tests and checking against acceptance criteria. Uses a11y-tester for runtime re-testing and magentaa11y-mcp for acceptance criteria verification.
---

# Accessibility Validator

## Core validation principles
Validation must answer:
1) **Did the original failure disappear?** (same rule id + same element/state)
2) **Did we meet acceptance criteria?** (behavior + semantics)
3) **Did we avoid regressions?** (global invariants still hold)

### Evidence (required)
For each issue, record:
- rule id + selector/locator + before/after result
- manual steps performed (keyboard/SR) + observations
- screenshots/notes when visual checks apply (focus indicator, contrast)

## Validation workflow
1. Establish baseline (original violations + state).
2. Re-run tests (runtime and/or static) after changes.
3. Check component acceptance criteria via `magentaa11y-mcp`.
4. Categorize: fixed / needs manual / still failing.

## Validation invariants (do not change between baseline and re-test)
- Same route + same component state (expanded/collapsed, dialog open, errors shown) + same data.
- Same viewport/breakpoint and input modality (keyboard-only where relevant).
- Same scan scope (don’t narrow to hide the issue).
- No “fix by suppression” (disabling rules, excluding selectors) unless explicitly requested.
- Keep baseline evidence so you can prove it’s the same element.

## Global invariants (must remain true after any fix)
### Semantics / ARIA
- Prefer native elements over role patches.
- No redundant/conflicting ARIA.
- ARIA only when needed; name/role/value computable.
- `aria-*` references point to existing, unique IDs.

### Keyboard & focus
- All controls reachable with Tab; no traps.
- Focus order matches reading/task flow.
- Focus indicator is clearly visible.
- Focus is managed after dynamic actions (dialogs, errors).

### Name / label
- Accessible name is meaningful.
- Visible label and accessible name do not conflict.
- Icon-only controls have an accessible name.

## Common anti-patterns to reject (even if tools go green)
- Fixing missing name with `aria-label="button"` or other non-descriptive text.
- `tabindex="0"` on div-buttons without full keyboard semantics.
- `aria-hidden="true"` added to silence audits.
- Global focus outline removal.
- State changes not reflected in ARIA (`aria-expanded`, `aria-pressed`, etc.).

## Re-testing process

### Runtime issues (from a11y-tester)
Re-run `a11y-tester`.

**Fixed when (runtime):**
- axe no longer reports the **same rule id** for the **same element** under the same user state
- element wasn’t hidden/removed just to evade detection
- no new equal-or-higher severity violation appears on that element

### Static issues (from web-standards)
Re-run `web-standards`.

**Fixed when (static):**
- anti-pattern removed without introducing an equivalent alternative anti-pattern
- resulting markup is semantically correct (native-first; ARIA only when needed)
- if interaction is implicated, also perform runtime validation

## Acceptance criteria verification
Query magentaa11y-mcp:
- `get_web_component("button")`
- `get_component_condensed(platform=web, component=...)`
- `get_component_gherkin(platform=web, component=...)`

### Turning criteria into checks
Restate criteria as:
- Invariant (always true)
- Interaction (keyboard/SR behavior)
- State mapping (UI state reflected in ARIA/state)

Record each as Pass/Fail/Needs-manual.

## Manual test protocol (fast, consistent)
Use whenever interaction/focus/dialogs/errors/custom widgets are involved.

### Keyboard-only smoke
- Tab/Shift+Tab: reach all controls; no traps
- Enter/Space works where expected; Esc closes dismissibles
- Focus lands sensibly after open/close and after validation errors
- Focus indicator clearly visible

### Screen reader sanity (minimum)
- Role + name (+ state) announced correctly
- Form errors/helper text announced when focusing the field

## Result categories (templates)

### ✅ Fixed
```markdown
### Issue #N: [Description]
**Status:** ✅ Fixed
**Repro/State:** [Route + component state]
**Verification:** [axe rule id no longer present + locator evidence] / [static check passes]
**Criteria Met:** [Acceptance criteria checked]
```

### ⚠️ Needs manual review
```markdown
### Issue #N: [Description]
**Status:** ⚠️ Needs Manual Review
**Repro/State:** [Route + component state]
**Reason:** [Why automated verification isn’t possible]
**Manual check:** [What to verify]
```

### ❌ Still failing
```markdown
### Issue #N: [Description]
**Status:** ❌ Still Failing
**Repro/State:** [Route + component state]
**Reason:** [Why fix didn’t work]
**Next step:** [Alternative approach]
```

## Regression checks
- Re-run a broader scan on affected views.
- Flag any new serious violations (name/role/value, keyboard, focus mgmt, form labeling).
- Any new minor violations must be justified and ticketed.

## Common failure modes (do not mark as fixed)
- Rule suppression / excluded selectors.
- Fix-by-hiding/removal without replacement.
- Partial fix that breaks another criterion (e.g., tabindex without key handling).
- Accessible name mismatch (visible text vs aria-label).
- Static-only validation for interactive bugs.
