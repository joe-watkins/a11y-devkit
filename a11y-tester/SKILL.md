---
name: a11y-tester
description: Run automated accessibility tests on URLs or HTML content using axe-core engine to WCAG 2.2 AA standards, then format findings as standardized issue reports. Use this skill when users want to test website accessibility, find WCAG violations, audit pages for accessibility issues, check if sites are accessible, analyze HTML for accessibility problems, or create accessibility issue tickets. Triggers on requests like "test accessibility", "check for WCAG violations", "audit this URL", "is this page accessible", "find accessibility issues", or "write accessibility issues".
---

# Accessibility Tester

Run automated accessibility testing and format findings as standardized issue reports.

## Prerequisites: Playwright MCP Setup

Before running accessibility tests, you need the Playwright MCP (Model Context Protocol) server configured in VS Code. This provides the browser automation tools needed to test web pages.

### Initial Setup (First-Time Users)

If you don't have Playwright MCP set up, follow these steps:

1. **Install the Playwright extension** (if not already installed):
   - Open Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
   - Search for and run: **Extensions: Install Extensions**
   - Search for "Playwright" and install the official extension

2. **Add the Playwright MCP server**:
   - Open Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`)
   - Run: **MCP: Browse MCP Servers**
   - Search for "Playwright" and add it
   
   **OR** manually add via:
   - Run: **MCP: Add Server...**
   - Follow prompts to add Playwright MCP

3. **Verify MCP access** (if needed):
   - Ensure **chat.mcp.access** setting allows MCP server access
   - Ensure **chat.mcp.autostart** is enabled for automatic startup

### Quick Check

To verify Playwright MCP is available, look for these tools in your chat context:
- `mcp_playwright_browser_navigate`
- `mcp_playwright_browser_evaluate`
- `mcp_playwright_browser_snapshot`

If these tools are not available, you need to complete the setup above.

## Prerequisites: Accessibility Issues Template MCP

This skill uses the **accessibility-issues-template-mcp** to format axe-core violations into standardized, JIRA-ready issue templates. Ensure this MCP server is configured in your IDE.

**Repository:** [github.com/joe-watkins/accessibility-issues-template-mcp](https://github.com/joe-watkins/accessibility-issues-template-mcp)

The MCP provides these tools:
- `format_axe_violation` - Convert axe violations to formatted issue reports
- `list_issue_templates` - List all available issue templates
- `get_issue_template` - Get a specific template by name
- `validate_issue` - Validate formatted issue content

## Testing Workflow

1. **Navigate to URL**: Use `mcp_playwright_browser_navigate` to load the page
2. **Run axe-core**: Use `mcp_playwright_browser_evaluate` to inject and run axe-core
3. **Format violations as issues**: Use `format_axe_violation` for each violation from the accessibility-issues-template-mcp
4. **Present results**: Output a summary table followed by each formatted issue

## Expected Output Format

Always present results in this order:

### 1. Report Header
```
# Accessibility Test Report: [Site Name]

**URL Tested:** https://example.com  
**Date:** [Current Date]  
**Tool:** Axe-core 4.8.4 via Playwright  
**Browser:** Chromium  
**Operating System:** Windows
```

### 2. Summary Tables
```
## Summary

| Metric | Count |
|--------|-------|
| **Total Violations** | X issues |
| **Rules Failed** | X |
| **Rules Passed** | X |
| **Needs Review** | X |

### Issues by Severity

| Severity | Count | WCAG Level |
|----------|-------|------------|
| **Critical** | X | A |
| **Severe** | X | AA |
| **Minor** | X | Best Practice |

### Issues by Type

| Rule ID | Description | Impact | Count |
|---------|-------------|--------|-------|
| `rule-id` | Description | Impact | X |
```

### 3. Formatted Issues
After the summary, output each issue using the full template format (see Issue Output Format below).

### 4. Recommendations Summary
```
## Recommendations Summary

| Priority | Action |
|----------|--------|
| **High** | Description of fix |
| **Low** | Description of fix |
```

## Step 1: Navigate to the Page

```
mcp_playwright_browser_navigate(url: "https://example.com")
```

## Step 2: Run Axe-core via Browser Evaluate

Use `mcp_playwright_browser_evaluate` with this function to inject axe-core and run the analysis:

```javascript
async () => {
  // Load axe-core if not already present
  if (typeof axe === 'undefined') {
    const script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.8.4/axe.min.js';
    document.head.appendChild(script);
    await new Promise((resolve, reject) => {
      script.onload = resolve;
      script.onerror = reject;
    });
  }
  // Run axe and return results
  const results = await axe.run();
  return { 
    violations: results.violations, 
    passes: results.passes.length, 
    incomplete: results.incomplete.length 
  };
}
```

This returns JSON with a `violations` array needed for issue formatting.

## Step 3: Format Violations as Issues

Use the **accessibility-issues-template-mcp** tools to format violations into standardized issues.

### Option A: Format Individual Violations

For each violation in the axe-core results, call `format_axe_violation`:

```
format_axe_violation(
  violation: {
    id: "color-contrast",
    impact: "serious",
    tags: ["wcag2aa", "wcag143"],
    description: "Ensures the contrast between foreground and background colors meets WCAG 2 AA contrast ratio thresholds",
    help: "Elements must have sufficient color contrast",
    helpUrl: "https://dequeuniversity.com/rules/axe/4.8/color-contrast",
    nodes: [{ /* node data from axe */ }]
  },
  context: {
    url: "https://example.com",
    browser: "Chromium",
    operatingSystem: "Windows"
  }
)
```

### Option B: Use Pre-built Templates

For known violation types, get the template directly:

```
# List all available templates
list_issue_templates()

# Get a specific template
get_issue_template(templateName: "color-contrast")
```

### Option C: Validate Custom Issues

After formatting, validate the issue content:

```
validate_issue(issue: { /* formatted issue object */ })
```

### Available Tools (accessibility-issues-template-mcp)

| Tool | Purpose |
|------|---------|
| `format_axe_violation` | Convert a single axe violation to a formatted issue report |
| `list_issue_templates` | List all 28+ available issue templates |
| `get_issue_template` | Get a specific template by axe rule ID |
| `validate_issue` | Validate formatted issue content for completeness |

## Issue Output Format

Each formatted issue should be fully filled in (no placeholder ###### marks). Example:

```
### Issue X: [Rule Name] - [Brief Description]

**Severity:** 2-Severe  
**Priority:** High

**[URL/Path]**  
https://example.com/

**[Steps to reproduce]**  
1. Navigate to https://example.com/
2. Locate the [element description]

**[Element]**  
The [element type] located in [location description]

**[What is the issue]**  
[Specific description of the accessibility failure, including measurements like contrast ratios]

**[Why it is important]**  
[Explanation of impact on users with disabilities]

**[Code reference]**
```html
<element class="example">Failing code</element>
```

**[How to fix]**  
[Specific remediation guidance]

**[Compliant code example]**
```html
<element class="example" aria-label="Fixed">Compliant code</element>
```

**[How to test]**  
- Automated: Axe-core `rule-id` rule
- Manual: [Specific manual testing steps]

**[MagentaA11y]**  
www.magentaa11y.com/checklist-web/[relevant-page]/

**[Resources]**  
https://dequeuniversity.com/rules/axe/4.8/[rule-id]

**[WCAG]**  
X.X.X Success Criterion Name (A or AA)

**[Operating system]** Windows  
**[Browser]** Chromium (Playwright)  
**[Assistive technology]** [Relevant AT: Keyboard, JAWS, NVDA, VoiceOver, etc.]
```

### Key Requirements for Issue Output

1. **No placeholders**: Fill in all ###### marks with actual content
2. **Specific element descriptions**: Describe where the element is in the UI
3. **Actionable fixes**: Provide concrete remediation steps
4. **Complete code examples**: Show both failing and fixed code
5. **Relevant MagentaA11y links**: Match to the issue type

## Severity Mapping

| axe Impact | Issue Severity | Priority |
|------------|----------------|----------|
| critical | Critical | Blocker |
| serious | Severe | High |
| moderate | Average | Medium |
| minor | Low | Low |

## Quick Reference: Common Issues

| axe Rule | Template Available |
|----------|-------------------|
| `color-contrast` | Color contrast issue template |
| `label` | Control lacks a label template |
| `heading-order` | Heading levels incorrectly nested template |
| `image-alt` | Image alternative text template |
| `button-name` | Button name template |
| `link-name` | Link name template |

Use `get_issue_template(templateName: "color-contrast")` to retrieve pre-formatted issue templates, or `list_issue_templates()` to see all 28+ available templates.

## Optional: Enrich Results with MCP Servers

After running axe-core tests, you can enrich results by querying accessibility MCP servers:

### WCAG Mapping (wcag-mcp)
```
wcag-mcp: get-criterion("4.1.2")
→ Returns full SC details, understanding docs, techniques
```

### Component Patterns (magentaa11y-mcp)
```
magentaa11y-mcp: get_web_component("button")
→ Returns acceptance criteria and developer notes
```

### User Impact (a11y-personas-mcp)
```
a11y-personas-mcp: get-personas(["blindness-screen-reader-nvda"])
→ Returns persona details showing who is affected
```

## Notes

- Use Playwright browser tools (`mcp_playwright_browser_navigate` + `mcp_playwright_browser_evaluate`) to run axe-core
- Axe-core is injected from CDN: `https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.8.4/axe.min.js`
- The `violations` array from axe results feeds into `format_axe_violation` from the accessibility-issues-template-mcp
- The MCP provides 28 specialized templates covering common AxeCore rules plus a fallback for 100+ additional rules
- Each failing element becomes a separate issue
- Axe-core catches ~30-40% of issues; combine with manual review of `mcp_playwright_browser_snapshot` for comprehensive testing
- **Always output a summary first**, then the detailed issues, then recommendations
- **Fill in all template fields** - do not leave ###### placeholders in final output
- **Group similar issues** when presenting (e.g., "Issues 3-8: Color Contrast in Footer Section")
