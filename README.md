# A11y Skills

A collection of accessibility-centric skills for AI agents and editors.

## Structure

Core skills are authored in `.claude/` as the current industry standard. Until IDEs align on a common format, use the sync process to copy skills to your IDE's preferred location:

- **Claude Code**: Skills work natively from `.claude/skills/`
- **Cursor**: Sync skills to `.cursor/skills/` and generate `AGENTS.md`
- **GitHub Copilot**: Use `.github/copilot-instructions.md` with references to `.claude/skills/` paths

## Syncing Skills

To sync skills from `.claude/` to `.cursor/` (for Cursor IDE):

1. Open Cursor in this project
2. Ask the AI: **"sync skills"**

This will:
- Copy all skills from `.claude/skills/` to `.cursor/skills/`
- Initialize any git submodules (like magentaa11y)
- Generate `AGENTS.md` with an overview of available skills

### When to Sync

- After cloning this repository
- After pulling updates that add or modify skills
- After making changes to skills in `.claude/`

## Available Skills

See `AGENTS.md` for a complete list of skills after syncing, or browse `.claude/skills/` directly.

| Skill | Purpose |
|-------|---------|
| a11y-personas | Accessibility personas for diverse user needs |
| a11y-tester | Automated WCAG testing with axe-core |
| magentaa11y | Component accessibility acceptance criteria |
| skill-creator | Guide for creating new skills |
| wcag-expert | WCAG 2.2 guidelines reference |
