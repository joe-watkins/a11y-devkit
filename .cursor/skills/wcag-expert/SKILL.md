---
name: wcag-expert
description: Expert knowledge of WCAG 2.2 (Web Content Accessibility Guidelines). Use when users ask about accessibility requirements, success criteria, conformance levels (A, AA, AAA), WCAG principles (perceivable, operable, understandable, robust), specific success criteria by number (e.g., 1.4.3), accessibility techniques, or need help understanding or implementing WCAG guidelines. Also use for questions about accessibility terminology, color contrast requirements, keyboard accessibility, screen reader compatibility, or any web accessibility compliance questions.
license: W3C Document License
---

# WCAG Expert

Expert resource for WCAG 2.2 (Web Content Accessibility Guidelines) questions and implementation guidance.

## Auto-Initialize Submodule

**Before reading any WCAG files**, check if the `repo/` folder exists in this skill directory. If it doesn't exist or is empty, run the setup script:

```bash
cd .cursor/skills/wcag-expert && ./setup.sh
```

This clones the official W3C WCAG repository as a git submodule. Only needs to run once.

## Manual Setup (for reference)

```bash
# Initialize submodule
cd .cursor/skills/wcag-expert
git submodule add https://github.com/w3c/wcag.git repo

# Update to latest
git submodule update --remote repo
```

## Data Source

This skill uses the **official W3C WCAG repository** as a git submodule at `repo/`. Content is in HTML format.

### Understanding Documents (Success Criteria Details)

Located in `repo/understanding/` organized by WCAG version:

| Path | Content |
|------|---------|
| `repo/understanding/20/{sc-id}.html` | WCAG 2.0 success criteria understanding docs |
| `repo/understanding/21/{sc-id}.html` | WCAG 2.1 success criteria understanding docs |
| `repo/understanding/22/{sc-id}.html` | WCAG 2.2 success criteria understanding docs |

**File naming**: `{handle}.html` (e.g., `contrast-minimum.html`, `keyboard.html`)

### Techniques

Located in `repo/techniques/` organized by technology:

| Path | Content |
|------|---------|
| `repo/techniques/aria/` | ARIA techniques (ARIA1, ARIA2, etc.) |
| `repo/techniques/html/` | HTML techniques (H1, H2, etc.) |
| `repo/techniques/css/` | CSS techniques (C6, C7, etc.) |
| `repo/techniques/general/` | General techniques (G1, G2, etc.) |
| `repo/techniques/failures/` | Failure patterns (F1, F2, etc.) |
| `repo/techniques/pdf/` | PDF techniques |
| `repo/techniques/client-side-script/` | JavaScript techniques (SCR1, etc.) |
| `repo/techniques/server-side-script/` | Server-side techniques (SVR1, etc.) |

### Guidelines & Terms

| Path | Content |
|------|---------|
| `repo/guidelines/index.html` | Main WCAG 2.2 guidelines document |
| `repo/guidelines/terms/22/` | WCAG 2.2 term definitions |
| `repo/guidelines/sc/22/` | Success criteria normative text |

## How to Answer WCAG Questions

### For Success Criteria Questions (e.g., "1.4.3" or "contrast")

1. Determine the SC handle from the number:
   - 1.4.3 → `contrast-minimum`
   - 2.1.1 → `keyboard`
   - 2.4.7 → `focus-visible`
   
2. Read the Understanding doc from the appropriate version folder:
   - Most criteria: `repo/understanding/20/{handle}.html`
   - WCAG 2.1 additions: `repo/understanding/21/{handle}.html`
   - WCAG 2.2 additions: `repo/understanding/22/{handle}.html`

### For Technique Questions

1. Identify the technique ID (e.g., "ARIA1", "H37", "G94", "F1")
2. Read from `repo/techniques/{technology}/{id}.html`

### For Terminology Questions

Read from `repo/guidelines/terms/22/{term}.html`

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

### WCAG 2.2 New Success Criteria

| Number | Name | Level |
|--------|------|-------|
| 2.4.11 | Focus Not Obscured (Minimum) | AA |
| 2.4.12 | Focus Not Obscured (Enhanced) | AAA |
| 2.4.13 | Focus Appearance | AAA |
| 2.5.7 | Dragging Movements | AA |
| 2.5.8 | Target Size (Minimum) | AA |
| 3.2.6 | Consistent Help | A |
| 3.3.7 | Redundant Entry | A |
| 3.3.8 | Accessible Authentication (Minimum) | AA |
| 3.3.9 | Accessible Authentication (Enhanced) | AAA |

### Common Success Criteria by Topic

| Topic | Key Criteria | Understanding Doc Handle |
|-------|-------------|--------------------------|
| Color Contrast | 1.4.3 (AA), 1.4.6 (AAA), 1.4.11 (AA) | contrast-minimum, contrast-enhanced, non-text-contrast |
| Keyboard | 2.1.1 (A), 2.1.2 (A), 2.4.7 (AA) | keyboard, no-keyboard-trap, focus-visible |
| Images | 1.1.1 (A) | non-text-content |
| Forms | 1.3.1 (A), 3.3.1 (A), 3.3.2 (A), 4.1.2 (A) | info-and-relationships, error-identification, labels-or-instructions, name-role-value |
| Focus | 2.4.3 (A), 2.4.7 (AA), 2.4.11 (AA) | focus-order, focus-visible, focus-not-obscured-minimum |
| Headings | 1.3.1 (A), 2.4.6 (AA) | info-and-relationships, headings-and-labels |
| Links | 2.4.4 (A), 2.4.9 (AAA) | link-purpose-in-context, link-purpose-link-only |
| Motion/Animation | 2.3.1 (A), 2.3.3 (AAA) | three-flashes-or-below-threshold, animation-from-interactions |
| Text Resize | 1.4.4 (AA), 1.4.10 (AA) | resize-text, reflow |
| Captions | 1.2.2 (A), 1.2.4 (AA) | captions-prerecorded, captions-live |
| Target Size | 2.5.5 (AAA), 2.5.8 (AA) | target-size-enhanced, target-size-minimum |

### Technique Categories

| Prefix | Technology | Path |
|--------|------------|------|
| ARIA | WAI-ARIA | `repo/techniques/aria/` |
| H | HTML | `repo/techniques/html/` |
| C | CSS | `repo/techniques/css/` |
| G | General | `repo/techniques/general/` |
| F | Failures | `repo/techniques/failures/` |
| SCR | Client-side Script | `repo/techniques/client-side-script/` |
| PDF | PDF | `repo/techniques/pdf/` |
| SVR | Server-side | `repo/techniques/server-side-script/` |

## Attribution

> This skill uses material from the W3C WCAG Repository. Copyright © 2023 W3C® (MIT, ERCIM, Keio, Beihang). See [W3C Document License](https://www.w3.org/Consortium/Legal/2015/doc-license).
