---
name: wcag-expert
description: Expert knowledge of WCAG 2.2 (Web Content Accessibility Guidelines). Use when users ask about accessibility requirements, success criteria, conformance levels (A, AA, AAA), WCAG principles (perceivable, operable, understandable, robust), specific success criteria by number (e.g., 1.4.3), accessibility techniques, or need help understanding or implementing WCAG guidelines. Also use for questions about accessibility terminology, color contrast requirements, keyboard accessibility, screen reader compatibility, or any web accessibility compliance questions.
license: W3C Document License
---

# WCAG Expert

Expert resource for WCAG 2.2 (Web Content Accessibility Guidelines) questions and implementation guidance.

## Reference Data Structure

All WCAG reference material is in `data/markdown/`:

| Folder | Content | Use For |
|--------|---------|---------|
| `principles/` | 4 POUR principles | High-level accessibility concepts |
| `guidelines/` | 13 guidelines by number | Understanding guideline categories |
| `success-criteria/level-a/` | Level A criteria (minimum) | Basic accessibility requirements |
| `success-criteria/level-aa/` | Level AA criteria (recommended) | Standard compliance (most common target) |
| `success-criteria/level-aaa/` | Level AAA criteria (enhanced) | Advanced accessibility requirements |
| `terms/` | Glossary (alphabetical folders a-c through v-z) | Definitions of WCAG terminology |

## How to Answer WCAG Questions

### For Specific Success Criteria Questions

When user asks about a numbered criterion (e.g., "1.4.3" or "contrast"):

1. Read from `data/markdown/success-criteria/level-{a|aa|aaa}/` 
2. File naming: `{number}-{handle}.md` (e.g., `1.4.3-contrast-minimum.md`)

### For Principle/Guideline Questions

- Principles (POUR): Read from `data/markdown/principles/`
- Guidelines: Read from `data/markdown/guidelines/`

### For Terminology Questions

Read from `data/markdown/terms/{letter-range}/` (e.g., `terms/a-c/contrast-ratio.md`)

## Quick Reference

### WCAG Principles (POUR)

1. **Perceivable** - Information must be presentable in perceivable ways
2. **Operable** - UI components must be operable
3. **Understandable** - Information and UI must be understandable  
4. **Robust** - Content must work with assistive technologies

### Conformance Levels

| Level | Description | Common Use |
|-------|-------------|------------|
| A | Minimum accessibility | Baseline requirements |
| AA | Standard accessibility | Most regulations require this |
| AAA | Enhanced accessibility | Specialized contexts |

### Common Success Criteria by Topic

| Topic | Key Criteria |
|-------|-------------|
| Color Contrast | 1.4.3 (AA), 1.4.6 (AAA), 1.4.11 (AA) |
| Keyboard | 2.1.1 (A), 2.1.2 (A), 2.4.7 (AA) |
| Images | 1.1.1 (A) |
| Forms | 1.3.1 (A), 3.3.1 (A), 3.3.2 (A), 4.1.2 (A) |
| Focus | 2.4.3 (A), 2.4.7 (AA), 2.4.11 (AA) |
| Headings | 1.3.1 (A), 2.4.6 (AA) |
| Links | 2.4.4 (A), 2.4.9 (AAA) |
| Motion/Animation | 2.3.1 (A), 2.3.3 (AAA) |
| Text Resize | 1.4.4 (AA), 1.4.10 (AA) |
| Captions | 1.2.2 (A), 1.2.4 (AA) |

## File Search Patterns

To find relevant files, use these grep patterns:

- By criterion number: `num: "1.4.3"`
- By level: `level: AA`
- By guideline: `guideline: Distinguishable`
- By principle: `principle: Perceivable`
