# Available Skills

Overview of all skills synced from the Claude meta-framework.

## Skills

| Skill | Description |
|-------|-------------|
| a11y-personas | Library of accessibility personas representing people with various disabilities, impairments, and situational limitations. Use this skill when users ask about disability types, accessibility personas, user needs for specific conditions, how people with disabilities use technology, assistive technology users, or designing for accessibility. |
| a11y-tester | Run automated accessibility tests on URLs or HTML content using axe-core engine to WCAG 2.2 AA standards, then format findings as standardized issue reports. Use this skill when users want to test website accessibility, find WCAG violations, audit pages for accessibility issues, or create accessibility issue tickets. |
| magentaa11y | MagentaA11y accessibility acceptance criteria reference. Use this skill when users ask for accessibility criteria, acceptance criteria (AC), Gherkin tests, developer notes, or how to test components for accessibility. Supports both Web and Native (iOS/Android) platforms. |
| skill-creator | Guide for creating effective skills. Use when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations. |
| wcag-expert | Expert knowledge of WCAG 2.2 (Web Content Accessibility Guidelines). Use when users ask about accessibility requirements, success criteria, conformance levels (A, AA, AAA), WCAG principles, or need help understanding or implementing WCAG guidelines. |

## Usage

Skills are located in `.cursor/skills/`. Each skill contains a `SKILL.md` with detailed instructions and may include:

- `data/` - Reference data and resources
- `scripts/` - Executable scripts
- `references/` - Additional documentation
- `assets/` - Templates and assets

To use a skill, reference its `SKILL.md` for guidance on when and how to apply it.

