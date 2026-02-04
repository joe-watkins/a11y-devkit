---
name: a11y-issue-writer
description: Format accessibility violations into standardized, JIRA-ready issue reports using the accessibility-issues-template-mcp. Use this skill when users want to write accessibility issues, format axe-core violations as tickets, create accessibility bug reports, generate issue templates from test results, or convert violations to standardized formats. Triggers on requests like "write issues for these violations", "format as JIRA tickets", "create accessibility bug reports", or "generate issue from axe results".
---

# Accessibility Issue Writer

Format accessibility violations into standardized issue reports using the accessibility-issues-template-mcp.

## Prerequisites

Requires the **accessibility-issues-template-mcp** server configured in your IDE.

**Repository:** [github.com/joe-watkins/accessibility-issues-template-mcp](https://github.com/joe-watkins/accessibility-issues-template-mcp)

Verify these tools are available:
- `format_axe_violation`
- `list_issue_templates`
- `get_issue_template`
- `validate_issue`

## Workflow

1. **Receive violations** - Accept axe-core violations array or individual violation objects
2. **Format each violation** - Call `format_axe_violation` with violation data and context
3. **Output formatted issues** - Present issues in requested format (markdown, JIRA, etc.)

## Issue Quality Checklist (Make It Actionable)

Every issue should answer, in plain language:

- **Expected result:** What should happen for an accessible experience
- **Actual result:** What currently happens (observable failure)
- **User impact:** Who is impacted and how (keyboard-only, screen reader, low vision, cognitive, etc.)
- **Evidence:** One or more of:
  - Failing DOM snippet + selector
  - Count of instances / pages affected
  - Screenshot (if available) or SR output transcript (if provided)
- **Acceptance criteria (Definition of Done):**
  - Concrete pass/fail statements (e.g., “Control has an accessible name exposed to AT”)
  - Include regression-safe constraints (don’t break visible label, don’t change focus order unexpectedly)
- **How to verify:** Minimal steps for QA to confirm the fix (automated + manual)

## MCP Tools

### format_axe_violation

Convert a single axe-core violation to a formatted issue report.

```
format_axe_violation(
  violation: {
    id: "color-contrast",
    impact: "serious",
    tags: ["wcag2aa", "wcag143"],
    description: "Ensures contrast between foreground and background colors meets WCAG 2 AA thresholds",
    help: "Elements must have sufficient color contrast",
    helpUrl: "https://dequeuniversity.com/rules/axe/4.8/color-contrast",
    nodes: [{ html: "<p class='low-contrast'>...</p>", target: [".low-contrast"] }]
  },
  context: {
    url: "https://example.com",
    browser: "Chromium",
    operatingSystem: "Windows"
  }
)
```

### list_issue_templates

List all 28+ available issue templates.

```
list_issue_templates()
```

### get_issue_template

Retrieve a specific template by axe rule ID.

```
get_issue_template(templateName: "color-contrast")
```

### validate_issue

Check formatted issue for completeness.

```
validate_issue(issue: { /* formatted issue object */ })
```

## Input Formats

### Full axe-core Results

When receiving complete axe-core output, iterate over the `violations` array:

```javascript
// From axe.run() results
results.violations.forEach(violation => {
  format_axe_violation(violation, context)
})
```

### Single Violation

Format individual violations as received:

```
format_axe_violation(violation: singleViolation, context: contextObject)
```

### Manual Input

For manually reported issues, use `get_issue_template` to get the appropriate template structure:

```
get_issue_template(templateName: "button-name")
```

## Output Format

Each formatted issue includes:

- **Title**: Rule name and brief description
- **Severity**: Mapped from axe impact (critical/serious/moderate/minor)
- **URL/Path**: Where the issue was found
- **Steps to reproduce**: Navigation instructions
- **Element**: Description and location
- **What is the issue**: Specific failure description
- **Why it is important**: User impact explanation
- **Code reference**: Failing HTML snippet
- **How to fix**: Remediation guidance
- **Compliant code example**: Fixed HTML snippet
- **How to test**: Automated and manual verification steps
- **Resources**: Deque University link, WCAG reference

### Environment + AT Matrix (when relevant)

If the failure is AT- or browser-dependent (or likely to be), include:

- **Test environment (if known):** OS, browser, assistive technology + version
- **AT/Browser matrix (template):**

| OS | Browser | Assistive Tech | Result | Notes |
|----|---------|----------------|--------|------|
| Windows | Chrome/Edge | NVDA/JAWS | [Pass/Fail/Untested] | |
| macOS | Safari/Chrome | VoiceOver | [Pass/Fail/Untested] | |
| iOS | Safari | VoiceOver | [Pass/Fail/Untested] | |
| Android | Chrome | TalkBack | [Pass/Fail/Untested] | |

Guidance:
- If you only have axe output and no manual testing, mark rows as **Untested** and do not invent results.
- Still include the matrix when you suspect AT differences (custom widgets, ARIA heavy UI, focus management, dialogs/menus/tabs).

### Severity Mapping

| axe Impact | Issue Severity | Priority |
|------------|----------------|----------|
| critical | Critical | Blocker |
| serious | Severe | High |
| moderate | Average | Medium |
| minor | Low | Low |

## WCAG Mapping Guidance (Keep It Precise)

When including WCAG references:

- Prefer **one primary Success Criterion** that best represents the failure.
- Add **secondary SCs** only when clearly applicable (avoid “SC spam”).
- Common mappings:
  - Missing accessible name for interactive control → **4.1.2 Name, Role, Value** (often primary)
  - Missing programmatic label/relationships → **1.3.1 Info and Relationships**
  - Keyboard inoperable interactions → **2.1.1 Keyboard**
  - Focus not visible due to CSS → **2.4.7 Focus Visible**
  - Duplicate IDs / broken ARIA references / invalid markup impacting parsing → **4.1.1 Parsing**
  - Non-text alternative missing → **1.1.1 Non-text Content**

If axe provides tags like `wcag143`:
- Preserve them, but also translate to the human-readable SC name/number in the final issue.

## Batch Processing

When processing multiple violations:

1. **Group by rule** - Combine similar violations
2. **Order by severity** - Critical first, then serious, moderate, minor
3. **Number sequentially** - Issue #1, Issue #2, etc.
4. **Prefer one root cause per ticket**:
   - If multiple nodes share the same underlying fix, keep them together.
   - If nodes differ materially (different components, different fixes), split into separate issues.
5. **Include instance count + sampling**:
   - Provide total occurrences if known (e.g., “12 instances across 3 pages”)
   - Include 1–3 representative selectors/snippets, not an overwhelming dump

Example output structure:

```markdown
# Accessibility Issues Report

**URL:** https://example.com
**Total Issues:** 12

## Critical (2 issues)

### Issue #1: color-contrast - Insufficient contrast ratio
[formatted issue content]

### Issue #2: button-name - Button missing accessible name
[formatted issue content]

## Serious (5 issues)
...
```

## Integration with Other Skills

This skill is called by `a11y-tester` after running axe-core tests. It can also be invoked directly with violations from any source.

**From a11y-tester:**
```
1. a11y-tester runs axe-core → collects violations
2. a11y-tester delegates to a11y-issue-writer → formats issues
3. Output: Summary + formatted issues
```

**Standalone usage:**
```
User provides violations → a11y-issue-writer formats → Output issues
```
