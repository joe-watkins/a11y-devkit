---
name: a11y-audit-fix-agent-orchestrator
description: Coordinate an end-to-end accessibility workflow across a11y skills (analysis → remediation → validation). Use for comprehensive audits of a URL, a repo/path, or a snippet.
---

# Accessibility Orchestrator

Coordinates a full accessibility pass by delegating to specialized skills.

## Operating mode (audit-only vs audit+fix)
Determine mode from the user’s request:
- **Audit-only (default):** user asks to audit/review/find issues → do **not** edit files.
- **Audit+Fix:** user asks to fix/remediate/apply changes/PR/patch → apply **minimal, low-risk** edits.

Stop and ask a targeted question if:
- target is ambiguous (no URL/path/snippet)
- auth/paywall blocks runtime testing
- fix requires product/content/design decisions (copy, meaningful alt text, new headings)

## Inputs
One of:
- URL (public or local dev URL)
- repo/path(s)
- code snippet (static-only)

## Outputs
Always produce:
- prioritized issue list (confirmed vs potential)
- what would be changed vs manual review
If Audit+Fix:
- patch/diff summary + re-test results

## Tool boundaries & safety
Default to **minimal, localized diffs**.

Do not:
- invent visible text/copy
- invent destinations/URLs
- redesign layouts
- refactor unrelated code

Escalate to **Needs Manual Review** when:
- a conformant fix requires new content/structure
- a fix likely impacts visuals (focus indicators/contrast/CSS)
- composite widgets need deeper interaction testing

## Workflow (3 stages)
1) **Analysis**
- Static scan: `web-standards`
- Runtime scan (when runnable): `a11y-tester`
- De-dupe + prioritize; record baseline evidence (rule id + selector + state)

2) **Remediation** (Audit+Fix only)
- Apply changes via `a11y-remediator`
- Keep behavior stable; document what changed

3) **Validation**
- Validate via `a11y-validator` (and/or re-run `a11y-tester`)
- Confirm fixes + note remaining manual review items

## Progress reporting (recommended)
- Stage 1: X static findings; Y axe violations; Z incomplete
- Stage 2: N issues fixed; M flagged manual review
- Stage 3: re-test summary + regressions (if any)

## Report skeleton
- Target + mode (audit-only vs audit+fix)
- Environment (browser/OS; AT if tested)
- Findings (grouped by severity)
- Changes (files changed + summary) (Audit+Fix only)
- Validation results (what’s fixed / manual review / still failing)
- Risks / gotchas / next steps
