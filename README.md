# A11y Skills

A collection of accessibility-centric skills for AI agents and editors.

## Available Skills

| Skill | Purpose | Path | Setup |
|-------|---------|------|-------|
| a11y-audit-fix-agent-orchestrator | Coordinate full accessibility audit workflow across multiple skills | `a11y-audit-fix-agent-orchestrator/SKILL.md` | |
| a11y-base-web | Foundational accessibility patterns and requirements for AI-generated web code | `a11y-base-web/SKILL.md` | |
| a11y-personas | Accessibility personas for diverse user needs | `a11y-personas/SKILL.md` | ✓ |
| a11y-remediator | Generate accessibility fixes for identified issues | `a11y-remediator/SKILL.md` | |
| a11y-tester | Automated WCAG testing with axe-core | `a11y-tester/SKILL.md` | |
| a11y-validator | Verify that accessibility fixes resolve identified issues | `a11y-validator/SKILL.md` | |
| skill-creator | Guide for creating new skills | `skill-creator/SKILL.md` | |
| web-standards | Static HTML/CSS/ARIA analysis without requiring a browser | `web-standards/SKILL.md` | |

> Skills with ✓ in Setup have a `setup.sh` script to download reference data.

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
   - Generates detailed reports with violation descriptions and affected elements

3. **web-standards** - Analyzes HTML/CSS/ARIA patterns
   - Reviews the page structure for semantic HTML usage
   - Validates ARIA attributes and roles
   - Checks for proper landmark structure and heading hierarchy

4. **a11y-personas** - Considers diverse user perspectives
   - Evaluates the site from the perspective of users with disabilities
   - Identifies potential barriers for screen reader users, keyboard-only users, etc.
   - Suggests improvements based on real-world user needs

5. **a11y-remediator** (if issues found) - Generates accessibility fixes
   - Creates code patches to resolve identified violations
   - Provides alternative implementations that meet WCAG standards
   - Suggests best practices for preventing similar issues

6. **a11y-validator** (after fixes) - Verifies remediation success
   - Re-tests the page to confirm fixes resolve the original issues
   - Ensures no new accessibility problems were introduced
   - Validates that the site meets target WCAG conformance level

The orchestrator skill manages this entire pipeline, ensuring comprehensive testing and remediation.

## MCP Resources (Separate Repositories)

For detailed reference data, use MCP servers instead of skills:

| Resource | Purpose | Use As |
|----------|---------|--------|
| wcag-expert | WCAG 2.2 guidelines, success criteria, techniques | MCP server |
| aria-expert | WAI-ARIA roles, states, properties, patterns | MCP server |
| magentaa11y | Component accessibility acceptance criteria | MCP server |

> **Philosophy:** Skills are "doers" that perform actions. MCP servers are "resources" that provide reference data. Skills can query MCP servers when they need specifications or patterns.

## Setup

### Quick Start with Deployment Script

The easiest way to use these skills with your IDE is to use the deployment script:

```bash
# Deploy to all IDEs (Claude Code, Cursor, GitHub Copilot)
./deploy-skills.sh --all

# Deploy to specific IDE
./deploy-skills.sh --claude
./deploy-skills.sh --cursor
./deploy-skills.sh --github

# Deploy with automatic setup (downloads external resources)
./deploy-skills.sh --all --setup

# Deploy with symlinks (for development - changes sync automatically)
./deploy-skills.sh --all --symlink

# List all available skills
./deploy-skills.sh --list

# Clean up IDE deployments
./deploy-skills.sh --clean
```

The deployment script automatically:
- Copies skills to IDE-specific directories (`.claude/skills/`, `.cursor/skills/`, `.github/skills/`)
- Ensures compatibility with all IDE implementations
- Optionally runs setup scripts to download external reference data

### IDE-Specific Directories

After running the deployment script, skills will be available in:

- **Claude Code**: `.claude/skills/` directory
- **Cursor**: `.cursor/skills` directory
- **GitHub Copilot**: `.github/skills/` directory

> The deployment script copies files by default for maximum compatibility. Use `--symlink` flag if you prefer symlinks (changes to source skills are immediately reflected, but may not work with all IDEs).

### Manual Setup (Alternative)

If you prefer manual setup, clone this repository into your IDE's skills folder:

- **Claude Code**: Clone/symlink into `.claude/skills/`
- **Cursor**: Clone/symlink into `.cursor/skills/`
- **GitHub Copilot**: Clone/symlink into `.github/skills/` (or use `.github/copilot-instructions.md`)

Each skill folder contains a `SKILL.md` file with instructions, reference data, and any associated scripts.
