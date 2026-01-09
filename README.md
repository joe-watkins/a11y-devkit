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
| aria-expert | WAI-ARIA roles, states, properties, and API mappings | `aria-expert/SKILL.md` | ✓ |
| magentaa11y | Component accessibility acceptance criteria | `magentaa11y/SKILL.md` | ✓ |
| skill-creator | Guide for creating new skills | `skill-creator/SKILL.md` | |
| wcag-expert | WCAG 2.2 guidelines reference | `wcag-expert/SKILL.md` | ✓ |
| web-standards | Static HTML/CSS/ARIA analysis without requiring a browser | `web-standards/SKILL.md` | |

> Skills with ✓ in Setup have a `setup.sh` script to download reference data.

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

# List all available skills
./deploy-skills.sh --list

# Clean up IDE deployments
./deploy-skills.sh --clean
```

The deployment script automatically:
- Creates symlinks to skills in IDE-specific directories (`.claude/skills/`, `.cursor/skills/`, `.github/skills/`)
- Keeps skills in sync with the source (changes are immediately reflected)
- Optionally runs setup scripts to download external reference data

### IDE-Specific Directories

After running the deployment script, skills will be available in:

- **Claude Code**: `.claude/skills/` directory
- **Cursor**: `.cursor/skills` directory
- **GitHub Copilot**: `.github/skills/` directory

> The deployment script uses symlinks by default, so any changes you make to the source skills are immediately reflected in all IDE locations. Use `--copy` flag if you prefer to copy files instead.

### Manual Setup (Alternative)

If you prefer manual setup, clone this repository into your IDE's skills folder:

- **Claude Code**: Clone/symlink into `.claude/skills/`
- **Cursor**: Clone/symlink into `.cursor/skills/`
- **GitHub Copilot**: Clone/symlink into `.github/skills/` (or use `.github/copilot-instructions.md`)

Each skill folder contains a `SKILL.md` file with instructions, reference data, and any associated scripts.
