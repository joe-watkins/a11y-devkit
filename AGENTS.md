# Available Skills

Overview of all skills synced from the Claude meta-framework.

## Skills

| Skill | Description |
|-------|-------------|
| a11y-personas | Library of accessibility personas representing people with various disabilities, impairments, and situational limitations. Use for questions about disability types, accessibility personas, user needs, how people with disabilities use technology, or designing for accessibility. |
| a11y-tester | Run automated accessibility tests on URLs or HTML content using axe-core engine to WCAG 2.2 AA standards, then format findings as standardized issue reports. Use for testing website accessibility, finding WCAG violations, or auditing pages. |
| magentaa11y | MagentaA11y accessibility acceptance criteria reference. Use for accessibility criteria, acceptance criteria (AC), Gherkin tests, developer notes, or how to test components for accessibility. Supports Web and Native (iOS/Android) platforms. |
| skill-creator | Guide for creating effective skills. Use when creating a new skill or updating an existing skill that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations. |
| wcag-expert | Expert knowledge of WCAG 2.2 (Web Content Accessibility Guidelines). Use for accessibility requirements, success criteria, conformance levels, WCAG principles, specific success criteria, accessibility techniques, or implementation guidance. |

## Usage

Skills are located in `.cursor/skills/`. Each skill contains a `SKILL.md` with detailed instructions and may include:

- `repo/` - Cloned reference repositories (run setup.sh to initialize)
- `scripts/` - Executable scripts
- `references/` - Additional documentation
- `assets/` - Templates and assets

To use a skill, reference its `SKILL.md` for guidance on when and how to apply it.
