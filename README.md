# A11y Skills

A collection of accessibility-centric skills for AI agents and editors.

## Available Skills

| Skill | Purpose | Path |
|-------|---------|------|
| a11y-audit-fix-agent-orchestrator | Coordinate full accessibility audit workflow across multiple skills | `a11y-audit-fix-agent-orchestrator/SKILL.md` |
| a11y-base-web | Foundational accessibility patterns and requirements for AI-generated web code | `a11y-base-web/SKILL.md` |
| a11y-remediator | Generate accessibility fixes for identified issues | `a11y-remediator/SKILL.md` |
| a11y-tester | Automated WCAG testing with axe-core | `a11y-tester/SKILL.md` |
| a11y-validator | Verify that accessibility fixes resolve identified issues | `a11y-validator/SKILL.md` |
| skill-creator | Guide for creating new skills | `skill-creator/SKILL.md` |
| web-standards | Static HTML/CSS/ARIA analysis without requiring a browser | `web-standards/SKILL.md` |

## MCP Resources (Separate Repositories)

For detailed reference data, query these MCP servers:

| Resource | Purpose | Repository |
|----------|---------|------------|
| wcag-mcp | WCAG 2.2 guidelines, success criteria, techniques | [github.com/joe-watkins/wcag-mcp](https://github.com/joe-watkins/wcag-mcp) |
| aria-mcp | WAI-ARIA roles, states, properties, patterns | [github.com/joe-watkins/aria-mcp](https://github.com/joe-watkins/aria-mcp) |
| magentaa11y-mcp | Component accessibility acceptance criteria | [github.com/joe-watkins/magentaa11y-mcp](https://github.com/joe-watkins/magentaa11y-mcp) |
| a11y-personas-mcp | Accessibility personas for diverse user needs | [github.com/joe-watkins/a11y-personas-mcp](https://github.com/joe-watkins/a11y-personas-mcp) |

> **Philosophy:** Skills are "doers" that perform actions. MCP servers are "resources" that provide reference data. Skills query MCP servers when they need specifications, patterns, or user impact data.

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
