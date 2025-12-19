# A11y Skills

A collection of accessibility-centric skills for AI agents and editors.

## Available Skills

| Skill | Purpose | Path | Setup |
|-------|---------|------|-------|
| a11y-personas | Accessibility personas for diverse user needs | `a11y-personas/SKILL.md` | ✓ |
| a11y-tester | Automated WCAG testing with axe-core | `a11y-tester/SKILL.md` | |
| aria-expert | WAI-ARIA roles, states, properties, and API mappings | `aria-expert/SKILL.md` | ✓ |
| magentaa11y | Component accessibility acceptance criteria | `magentaa11y/SKILL.md` | ✓ |
| skill-creator | Guide for creating new skills | `skill-creator/SKILL.md` | |
| wcag-expert | WCAG 2.2 guidelines reference | `wcag-expert/SKILL.md` | ✓ |

> Skills with ✓ in Setup have a `setup.sh` script to download reference data.

## Setup

Clone this repository into your IDE's skills folder:

- **GitHub Copilot**: `.github/copilot-instructions.md` references skill paths
- **Claude Code**: `.claude/skills/` directory
- **Cursor**: `.cursorrules` or `.cursor/skills` directory

Each skill folder contains a `SKILL.md` file with instructions, reference data, and any associated scripts.

### GitHub Copilot Example

Add a catalog to `.github/copilot-instructions.md`:

```markdown
# Skills Catalog

| Skill Name | Description | Path |
|------------|-------------|------|
| A11y Personas | Accessibility personas for diverse user needs | `a11y-personas/SKILL.md` |
| A11y Tester | Automated WCAG testing with axe-core | `a11y-tester/SKILL.md` |
| ARIA Expert | WAI-ARIA roles, states, and properties reference | `aria-expert/SKILL.md` |
| MagentaA11y | Component accessibility acceptance criteria | `magentaa11y/SKILL.md` |
| WCAG Expert | WCAG 2.2 guidelines reference | `wcag-expert/SKILL.md` |

## How to Use Skills

When you encounter a task related to a skill:
1. Read the skill file at the listed path
2. Follow any guidance, standards, or templates provided
3. Use any scripts referenced in the skill file
```
