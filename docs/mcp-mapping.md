# MCP Mapping (A11y DevKit)

This doc maps each **Agent Skill** in `packages/` to the **MCP (Model Context Protocol) servers** it expects, and the **tools/functions** it calls.

> Goal: make it obvious (a) what to install/run, (b) what each skill can query, and (c) how the skills compose into an Audit → Issues → Fix → Validate workflow.

## Canonical MCP servers (by capability)

### Reference data (a11y + web standards)

- **magentaa11y-mcp** (npm: `magentaa11y-mcp`)
  - Purpose: component acceptance criteria + implementation notes ("what good looks like")
  - Common tools used (examples from skill docs):
    - `get_web_component("button")`
    - `get_component_developer_notes("modal")`

- **a11y-personas-mcp** (npm: `a11y-personas-mcp`)
  - Purpose: user-impact context; helps prioritize and describe impact beyond “fails SC X.Y.Z”
  - Common tools:
    - `list-personas()`
    - `get-personas(["blindness-screen-reader-nvda", ...])`

- **aria-mcp** (npm: `aria-mcp`)
  - Purpose: authoritative ARIA role/state/property validation and lookups
  - Common tools:
    - `get-role("button")`
    - `validate-role-attributes("button", ["aria-pressed"])`
    - `get-required-attributes("dialog")` *(or equivalent in your server)*

- **wcag-guidelines-mcp** (npm: `wcag-guidelines-mcp`)
  - Purpose: WCAG success criteria + techniques + Understanding documentation lookup for grounding and ticket writing
  - Common tools (from repo):
    - `get-criterion("4.1.2")` (includes Understanding docs)
    - `get-success-criteria-detail("4.1.2")` (normative text only)
    - `get-techniques-for-criterion("1.3.1")`
    - `get-failures-for-criterion("1.3.1")`
    - `search-wcag("focus visible")`

### Issue formatting

- **accessibility-issues-template-mcp** *(repo docs currently reference this name)*
  - Purpose: standardize issue/ticket output from raw violations (axe-core, etc.)
  - Common tools:
    - `format_axe_violation(...)`
    - `list_issue_templates()` / `get_issue_template(...)`

### Browser automation / auditing runtime

- **Playwright MCP** (commonly provided by an editor integration)
  - Purpose: navigate pages, execute JS, snapshot DOM for audits
  - Common tools referenced by skills:
    - `mcp_playwright_browser_navigate`
    - `mcp_playwright_browser_evaluate`
    - `mcp_playwright_browser_snapshot`

- **Microsoft Playwright (PLA) MCP** *(referenced by orchestrator skill)*
  - Tools referenced:
    - `mcp_microsoft_pla_browser_navigate`
    - `mcp_microsoft_pla_browser_evaluate`

## Skill → MCP dependency map

### 1) `a11y-base-web` (Role: General Accessibility Guidance)

- MCP required: **none** (guidance-only)
- MCP optional (if you want grounded citations / deeper lookups):
  - `wcag-guidelines-mcp`, `aria-mcp`, `magentaa11y-mcp`

### 2) `web-standards` (Role: Web Standards + Best Practices)

- MCP required:
  - `aria-mcp`
  - `wcag-guidelines-mcp`
- MCP optional:
  - `magentaa11y-mcp` (for “recommended implementation pattern”)

### 3) `a11y-tester` (Role: Testing / Audit execution)

- MCP required:
  - Playwright MCP (`mcp_playwright_browser_*`) for navigation/evaluate/snapshot
- MCP optional (enrichment):
  - `wcag-guidelines-mcp` (SC grounding)
  - `magentaa11y-mcp` (recommended patterns)
  - `a11y-personas-mcp` (impact)
  - `accessibility-issues-template-mcp` (if generating tickets)

### 4) `a11y-issue-writer` (Role: Issue Writing)

- MCP required:
  - `accessibility-issues-template-mcp`
- MCP optional:
  - `wcag-guidelines-mcp` (SC details/techniques)
  - `a11y-personas-mcp` (impact language)

### 5) `a11y-remediator` (Role: Remediation / Coder)

- MCP optional-but-recommended (for grounded fixes):
  - `magentaa11y-mcp` (patterns/criteria)
  - `aria-mcp` (valid ARIA)
  - `wcag-guidelines-mcp` (SC + techniques)
  - `a11y-personas-mcp` (impact)

### 6) `a11y-validator` (Role: Validation / “did we actually fix it?”)

- MCP required:
  - `magentaa11y-mcp` (acceptance criteria checklists)
- MCP optional:
  - `a11y-tester` runtime (re-test loop)
  - `wcag-guidelines-mcp`, `aria-mcp` (grounding)

### 7) `a11y-audit-fix-agent-orchestrator` (Role: Orchestration)

- MCP required (runtime):
  - One of the browser MCP stacks (Playwright MCP or Microsoft PLA MCP) to run audits
- MCP optional-but-recommended (decision support):
  - `a11y-personas-mcp`
  - `magentaa11y-mcp`
  - `aria-mcp`
  - `wcag-guidelines-mcp`
  - `accessibility-issues-template-mcp`

## Naming note (important)

Joe’s note includes these npm packages:
- `magentaa11y-mcp`
- `a11y-personas-mcp`
- `arc-issues-mcp`
- `aria-mcp`
- `wcag-guidelines-mcp`

This repo’s current docs mention **`wcag-guidelines-mcp`** and **`accessibility-issues-template-mcp`**. If `wcag-guidelines-mcp` and/or `arc-issues-mcp` are the new canonical packages, we should:
1) decide the canonical names, then
2) update SKILL docs + README to match, and
3) add a short “migration / alias” section so users don’t get stuck.

## Other MCP servers worth considering (ecosystem)

These aren’t wired into the current skills yet, but are likely relevant if we want broader audit coverage or alternative runtimes:

- **a11y-mcp / a11y-mcp-server** (axe-core driven auditing MCP servers found in the wild)
  - Useful if you want a dedicated MCP server that returns axe-like results without relying on an editor-provided Playwright MCP.

- **ARC / issue taxonomy MCPs** (e.g., `arc-issues-mcp`)
  - Useful if you want standardized issue categories/severity language aligned to a specific program.

## Suggested next step (implementation)

- Update each `packages/*/SKILL.md` with a small, consistent **“MCP dependencies”** block:
  - **Required** (skill cannot function without)
  - **Optional** (for enrichment)
  - Example tool calls

