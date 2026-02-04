---
name: a11y-issue-writer
description: Format accessibility violations into standardized, JIRA-ready issue reports using the accessibility-issues-template-mcp. Optimized for developer-actionable reports: clear repro, expected vs actual, WCAG mapping, evidence, and assistive technology (AT) coverage.
---

# Accessibility Issue Writer

Format accessibility violations into standardized issue reports using **accessibility-issues-template-mcp**.

## What “good” looks like (minimum fields)
- **Where**: URL/route + state (e.g., modal open, validation errors shown)
- **Environment**: OS + version; browser + version; viewport/breakpoint; auth state/flags (if relevant)
- **AT** (if tested): NVDA/JAWS/VoiceOver/TalkBack + version
- **Repro steps** (deterministic) incl. keyboard steps when relevant
- **Actual** vs **Expected** (required)
- **WCAG mapping** (SC + level) when known; otherwise “Needs confirmation”
- **Impact**: severity based on user impact (not just tool impact)
- **Evidence**: selector/target + snippet; screenshot/video for interaction issues
- **Acceptance criteria** + **How to test** (automated + manual)

## Prerequisites
- MCP server: `accessibility-issues-template-mcp`
- Tools expected:
  - `format_axe_violation`
  - `list_issue_templates`
  - `get_issue_template`
  - `validate_issue`

Repo: https://github.com/joe-watkins/accessibility-issues-template-mcp

## Workflow
1. **Receive violations + context** (URL/route, OS/browser).
2. **Collect missing context** (ask if absent): viewport, auth state, AT tested, expected vs actual, evidence links.
3. **Format each violation** via `format_axe_violation(violation, context)`.
4. **Add report-quality fields**: actual/expected, impact, acceptance criteria, how-to-test.
5. **Validate** with `validate_issue` and fill gaps (or ask targeted questions).
6. **Batch output** grouped for fixability (see Batch Processing).

## WCAG mapping guidance (practical)
- Use `violation.tags`:
  - `wcag143` → SC 1.4.3
  - `wcag2aa` / `wcag21aa` / `wcag22aa` → level/version context
- Prefer the most specific SC tags; list multiple SCs if present.
- If tags are missing/unclear: mark **Needs confirmation** and include axe rule id + helpUrl.

## AT matrix guidance (keep lightweight)
Each issue should state:
- **Likely affected** user groups (e.g., screen reader users; keyboard-only; low vision).
- **Validated with** (if tested) or explicitly “Not tested”.

Suggested minimum combos:
- NVDA + Firefox/Chrome (Windows)
- VoiceOver + Safari (macOS)
- TalkBack + Chrome (Android) (if mobile is in scope)

## Batch processing (don’t over-merge)
1. Group by **rule + page/route + component**.
2. Preserve instances:
   - include an Instances list (selectors/targets + count)
   - split if across different pages/flows or different fixes
3. Order by severity.

## Output format (JIRA-ready)
Each issue should include:
- Title
- Severity/Priority
- WCAG mapping
- URL/route
- Environment + AT
- Preconditions
- Steps to reproduce
- Actual result
- Expected result
- Affected element(s) / instances
- User impact
- Acceptance criteria
- How to test
- Evidence + resources

## Integration
- Commonly called by `a11y-tester` after an axe scan.
- Can also be used standalone with manual reports (use `get_issue_template`).
