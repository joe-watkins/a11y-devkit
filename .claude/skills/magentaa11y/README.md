# MagentaA11y Skill

Accessibility acceptance criteria reference powered by [MagentaA11y](https://www.magentaa11y.com/).

## Setup

This skill uses the MagentaA11y project as a git submodule. 

**The skill will automatically initialize the submodule** if it detects the `repo/` folder is missing when you first use it.

### Manual Setup (optional)

If you prefer to set up manually:

```bash
cd .cursor/skills/magentaa11y
./setup.sh
```

Or from your project root:

```bash
git submodule update --init --recursive
```

### Updating Content

To pull the latest MagentaA11y documentation:

```bash
git submodule update --remote .cursor/skills/magentaa11y/repo
```

## What This Skill Does

Provides accessibility acceptance criteria for Web and Native (iOS/Android) components. Ask for:

- **Acceptance Criteria** — "Button AC for Native", "Web checkbox criteria"
- **Gherkin Tests** — "Modal dialog Gherkin tests"
- **Developer Notes** — "Link developer notes for iOS"
- **How to Test** — "How to test color contrast"

## Folder Structure

```
magentaa11y/
├── README.md          # This file
├── SKILL.md           # Skill definition (read by AI)
├── setup.sh           # Submodule setup script
└── repo/              # Git submodule (MagentaA11y project)
    └── public/content/documentation/
        ├── how-to-test/type/    # Testing guidance
        ├── native/              # iOS/Android components
        │   ├── controls/
        │   ├── notifications/
        │   └── patterns/
        └── web/                 # Web components
            ├── component/
            └── page-level/
```

## Requirements

- Git (for submodule)
- No build step required — reads raw markdown files

## License

MagentaA11y is licensed under [Apache-2.0](https://github.com/tmobile/magentaA11y/blob/main/LICENSE.txt).
