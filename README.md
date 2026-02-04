# A11y Devkit

A collection of accessibility-centric skills bundled with MCP (Model Context Protocol) servers for AI agents and editors.

> **Note:** These skills are designed to work together in an orchestrated workflow and require MCP servers to provide reference data, but can also be used independently as needed. Each skill focuses on a specific aspect of accessibility auditing and remediation, allowing for modular use based on the task at hand.

This is experimental and evolving, so expect new skills to be added over time. The goal is to create a comprehensive toolkit for AI-driven accessibility improvements in development.

## Available Skills

| Skill | npm Package | Purpose |
|-------|-------------|---------|
| a11y-audit-fix-agent-orchestrator | `a11y-audit-fix-agent-orchestrator-skill` | Coordinate full accessibility audit workflow across multiple skills |
| a11y-base-web | `a11y-base-web-skill` | Foundational accessibility patterns and requirements for AI-generated web code |
| a11y-issue-writer | `a11y-issue-writer-skill` | Format axe-core violations into standardized JIRA-ready issue reports |
| a11y-remediator | `a11y-remediator-skill` | Generate accessibility fixes for identified issues |
| a11y-tester | `a11y-tester-skill` | Automated WCAG testing with axe-core (outputs raw violations or delegates formatting) |
| a11y-validator | `a11y-validator-skill` | Verify that accessibility fixes resolve identified issues |
| skill-creator | `skill-creator-skill` | Guide for creating new skills |
| web-standards | `web-standards-skill` | Static HTML/CSS/ARIA analysis without requiring a browser |

## Installation

### Easiest: Use the CLI Tool

The fastest way to set up these skills is using the npm CLI tool:

```bash
npx a11y-devkit-deploy
```

This interactive CLI will guide you through:
- Selecting which IDE(s) to deploy to (Claude Code, Cursor, GitHub Copilot)
- Choosing deployment options
- Automatic installation to the correct IDE directories

For more information, visit [a11y-devkit-deploy on npm](https://www.npmjs.com/package/a11y-devkit-deploy).

### Install Individual Skills via npm

You can also install skills individually:

```bash
npm install a11y-tester-skill
npm install a11y-issue-writer-skill
npm install a11y-remediator-skill
# etc.
```

### Install All Skills

```bash
npm install a11y-base-web-skill a11y-issue-writer-skill a11y-tester-skill a11y-remediator-skill a11y-validator-skill web-standards-skill a11y-audit-fix-agent-orchestrator-skill skill-creator-skill
```

## MCP Dependencies (Separate Repositories)

These MCP (Model Context Protocol) servers are needed for these Skills to work best. Make sure you have these MCP servers running and accessible to your IDE/agent for the skills to query reference data effectively.

- See **docs/mcp-mapping.md** for the full Skill → MCP mapping: `docs/mcp-mapping.md`

For detailed reference data, query these MCP servers:

| Resource | Purpose | Repository |
|----------|---------|------------|
| wcag-guidelines-mcp | WCAG 2.2 guidelines, success criteria, techniques | [github.com/joe-watkins/wcag-guidelines-mcp](https://github.com/joe-watkins/wcag-guidelines-mcp) |
| aria-mcp | WAI-ARIA roles, states, properties, patterns | [github.com/joe-watkins/aria-mcp](https://github.com/joe-watkins/aria-mcp) |
| magentaa11y-mcp | Component accessibility acceptance criteria | [github.com/joe-watkins/magentaa11y-mcp](https://github.com/joe-watkins/magentaa11y-mcp) |
| a11y-personas-mcp | Accessibility personas for diverse user needs | [github.com/joe-watkins/a11y-personas-mcp](https://github.com/joe-watkins/a11y-personas-mcp) |
| accessibility-issues-template-mcp | Format AxeCore violations into standardized JIRA-ready issue templates | [github.com/joe-watkins/accessibility-issues-template-mcp](https://github.com/joe-watkins/accessibility-issues-template-mcp) |

> **Philosophy:** Skills are "doers" that perform actions. MCP servers are "resources" that provide reference data. Skills query MCP servers when they need specifications, patterns, or user impact data.

## Prompt Examples

### Testing a Website for Accessibility

**Prompt:** "Test https://example.com/ for accessibility"

This prompt would trigger a comprehensive accessibility workflow using multiple skills:

1. **a11y-audit-fix-agent-orchestrator** - Coordinates the overall accessibility audit workflow
   - Manages the testing, remediation, and validation cycle
   - Orchestrates communication between specialized skills

2. **a11y-tester** - Performs automated WCAG testing
   - Runs axe-core automated accessibility tests on the website
   - Identifies WCAG violations, best practice issues, and warnings
   - Outputs raw violations for orchestrator or delegates to a11y-issue-writer for formatted reports

3. **a11y-issue-writer** (optional) - Formats violations as standardized issues
   - Converts axe-core violations into JIRA-ready issue templates
   - Provides detailed remediation guidance and code examples
   - Uses accessibility-issues-template-mcp for standardized formatting and pre-formatted issues

4. **web-standards** - Analyzes HTML/CSS/ARIA patterns
   - Reviews the page structure for semantic HTML usage
   - Validates ARIA attributes and roles
   - Checks for proper landmark structure and heading hierarchy

5. **a11y-personas** - Considers diverse user perspectives
   - Evaluates the site from the perspective of users with disabilities
   - Identifies potential barriers for screen reader users, keyboard-only users, etc.
   - Suggests improvements based on real-world user needs

6. **a11y-remediator** (if issues found) - Generates accessibility fixes
   - Creates code patches to resolve identified violations
   - Provides alternative implementations that meet WCAG standards
   - Suggests best practices for preventing similar issues

7. **a11y-validator** (after fixes) - Verifies remediation success
   - Re-tests the page to confirm fixes resolve the original issues
   - Ensures no new accessibility problems were introduced
   - Validates that the site meets target WCAG conformance level

The orchestrator skill manages this entire pipeline, ensuring comprehensive testing and remediation.

## Orchestrated Workflow

The `a11y-audit-fix-agent-orchestrator` coordinates a 3-stage workflow where skills query MCP servers for authoritative data:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  INITIALIZATION: Load Base Patterns                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│  a11y-base-web ───────► Foundational accessibility patterns loaded          │
│                         Provides core requirements for all other skills     │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  STAGE 1: ANALYSIS                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│  web-standards ──────► Static HTML/ARIA analysis                            │
│       │                                                                     │
│       ├── aria-mcp: validate-role-attributes(), get-required-attributes()  │
│       └── wcag-guidelines-mcp: get-criterion() for WCAG mapping                        │
│                                                                             │
│  a11y-tester ────────► Runtime axe-core testing (returns raw violations)    │
│       │                                                                     │
│       ├── wcag-guidelines-mcp: enrich violations with SC details                       │
│       └── a11y-personas-mcp: identify affected user groups                  │
│                                                                             │
│  a11y-issue-writer ──► (Optional) Format violations as standardized issues  │
│       │                                                                     │
│       └── accessibility-issues-template-mcp: format_axe_violation()         │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  STAGE 2: REMEDIATION                                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│  a11y-remediator ────► Generate fixes for each issue                        │
│       │                                                                     │
│       ├── magentaa11y-mcp: get_web_component() for correct patterns         │
│       ├── aria-mcp: get-role(), validate-role-attributes()                  │
│       ├── wcag-guidelines-mcp: get-techniques-for-criterion()                          │
│       └── a11y-personas-mcp: get-personas() for user impact                 │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  STAGE 3: VALIDATION                                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│  a11y-validator ─────► Verify fixes resolved issues                         │
│       │                                                                     │
│       └── magentaa11y-mcp: get_web_component() for acceptance criteria      │
│                                                                             │
│  a11y-tester ────────► Re-run tests to confirm                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Example: Fixing a Button Issue

```
1. web-standards finds: "div with onclick has no accessible name"
   └── Queries aria-mcp: get-role("button") → confirms role requirements

2. a11y-remediator generates fix:
   ├── Queries magentaa11y-mcp: get_web_component("button") → gets pattern
   ├── Queries aria-mcp: get-required-attributes("button") → validates ARIA
   ├── Queries wcag-guidelines-mcp: get-criterion("4.1.2") → maps to WCAG SC
   └── Queries a11y-personas-mcp: get-personas([...]) → documents impact

3. a11y-validator confirms:
   └── Queries magentaa11y-mcp: get_web_component("button") → checks criteria
```

## Skill Delegation Model

The skills use a **delegation pattern** for specialized tasks, particularly for issue formatting:

### a11y-tester → a11y-issue-writer Delegation

**a11y-tester** has two output modes:

1. **Raw violations** (default for orchestrator):
   - Returns axe-core violations array as JSON
   - Used when called by orchestrator or when programmatic processing is needed
   - Provides raw data for further analysis

2. **Formatted issues** (via delegation):
   - Delegates to **a11y-issue-writer** when user requests "write issues" or "create tickets"
   - a11y-issue-writer calls `format_axe_violation` from accessibility-issues-template-mcp
   - Outputs JIRA-ready issue templates with remediation guidance

**Example delegation flow:**

```
User: "Test this site for accessibility and write issues"
  │
  ├─► a11y-tester runs axe-core → collects violations
  │
  └─► a11y-tester delegates to a11y-issue-writer
        │
        └─► a11y-issue-writer formats each violation using
            accessibility-issues-template-mcp → outputs standardized issues
```

**When to use each mode:**
- **Raw violations**: "test accessibility", when called by orchestrator, for CI/CD pipelines
- **Formatted issues**: "write issues", "create tickets", "format as JIRA", for bug tracking

This separation keeps testing logic separate from formatting logic, making skills more focused and reusable.

## IDE-Specific Directories

After installation, skills will be available in:

- **Claude Code**: `.claude/skills/` directory
- **Cursor**: `.cursor/skills` directory
- **GitHub Copilot**: `.github/skills/` directory

## Development

This repository uses npm workspaces to manage multiple skill packages.

### Setup

```bash
npm install
```

### Publishing

```bash
# Bump versions
npm version patch --workspaces

# Publish all packages
npm publish --workspaces --access public
```

## License

MIT
