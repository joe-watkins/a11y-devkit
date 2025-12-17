---
name: magentaa11y
description: MagentaA11y accessibility acceptance criteria reference. Use this skill when users ask for accessibility criteria, acceptance criteria (AC), Gherkin tests, developer notes, or how to test components for accessibility. Supports both Web and Native (iOS/Android) platforms. Triggers on requests like "give me the Button AC", "how to test a checkbox", "accessibility criteria for modal", "native button Gherkin", "web link developer notes", or any MagentaA11y component query.
---

# MagentaA11y Accessibility Reference

Single source of truth for accessibility acceptance criteria across Web and Native platforms.

## Auto-Initialize Submodule

**Before reading any component files**, check if the `repo/` folder exists in this skill directory. If it doesn't exist or is empty, run the setup script:

```bash
cd .cursor/skills/magentaa11y && ./setup.sh
```

This clones the MagentaA11y repository as a git submodule. Only needs to run once.

## Manual Setup (for reference)

```bash
# Initialize submodule
cd .cursor/skills/magentaa11y
git submodule add https://github.com/tmobile/magentaA11y.git repo

# Update to latest
git submodule update --remote repo
```

> **Note:** No build step is required. The skill reads the raw markdown source files directly.

## Data Source

Component documentation is located in the submodule at:

```
repo/public/content/documentation/
├── how-to-test/type/       # Testing guidance by issue type
├── native/                  # Native (iOS/Android) components
│   ├── controls/           # button, checkbox, toggle-switch, etc.
│   ├── notifications/      # alert-dialog, modal, snackbar-toast
│   └── patterns/           # animation, headings, focus, etc.
└── web/                     # Web components
    ├── component/          # button, checkbox, link, modal, tabs, etc.
    └── page-level/         # header, footer, main, navigation, form, etc.
```

## How to Use

When a user asks for component accessibility criteria:

1. **Identify the platform**: Web or Native (iOS/Android)
2. **Identify the component**: button, checkbox, modal, link, etc.
3. **Find the file**: Use `grep_search` for the component name, or go directly to the file path

### Search Process

1. **Use grep_search** to find the component file (e.g., search for `button.md`)
2. **Read the markdown file** directly from the appropriate path
3. Return the relevant section (Gherkin, Condensed, Developer Notes, etc.)

### Direct File Paths

| Query Type | File Path Pattern |
|------------|-------------------|
| Web component | `repo/public/content/documentation/web/component/{component}.md` |
| Web page-level | `repo/public/content/documentation/web/page-level/{component}.md` |
| Native control | `repo/public/content/documentation/native/controls/{component}.md` |
| Native notification | `repo/public/content/documentation/native/notifications/{component}.md` |
| Native pattern | `repo/public/content/documentation/native/patterns/{component}.md` |
| How to test | `repo/public/content/documentation/how-to-test/type/{topic}.md` |

### Example Queries

| User Query | File Path |
|------------|-----------|
| "Button AC for Native" | `repo/public/content/documentation/native/controls/button.md` |
| "Web checkbox criteria" | `repo/public/content/documentation/web/component/checkbox.md` |
| "How to test a modal dialog" | `repo/public/content/documentation/web/component/modal-dialog.md` |
| "Native toggle switch" | `repo/public/content/documentation/native/controls/toggle-switch.md` |
| "Web link accessibility" | `repo/public/content/documentation/web/component/link.md` |
| "Skip link criteria" | `repo/public/content/documentation/web/page-level/skip-link.md` |
| "Native alert dialog" | `repo/public/content/documentation/native/notifications/alert-dialog.md` |
| "How to test color contrast" | `repo/public/content/documentation/how-to-test/type/color-contrast.md` |

## Available Components

### Web - Components
alert-notification, animation, autocomplete, breadcrumbs, button, carousel-slideshow, checkbox, complex-graphics, date-picker, decorative-image, expander-accordion, figure, footnote, heading, help-hint-error, iframe, informative-image, link, list, modal-dialog, number-input, pagination-nav, password-input, progress-indicator, radio-button, range-slider, scrolling-container, search, select-dropdown, separator-horizontal-rule, star-rating, stepper-input, sticky-element, strikethrough-content, table, tabs, text-input, textarea-multiline-input, tidbit, toast-snackbar, toggle-switch, tooltip, video-audio-player

### Web - Page Level
basic-web-page, footer-landmark, form, header-landmark, main-landmark, navigation-landmark, single-page-application, skip-link

### Native - Controls
button, calendar-date-picker, captcha, carousel, checkbox, chip, date-time-picker, dropdown, expandable, link, menu, pagination-control, progress-indicator, radio-button, reorder-data-row, search, segmented-control, sheet, sidebar-menu, slider, step-indicator, stepper, table-row-button, text-input, time-picker, timer, toggle-switch

### Native - Notifications
alert-dialog, modal, snackbar-toast

### Native - Patterns
animation, field-errors, focus, graphics-visual-elements, headings, image-decorative, loading-icon, loading-spinner, strike-through, table, tidbit, webview

### How to Test
color-contrast, forms-&-inputs, images, keyboard-&-focus, links-&-buttons, native-apps, not-sure-if-it-is-an-issue, web-screen-readers
