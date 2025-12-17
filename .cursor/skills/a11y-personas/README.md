# A11y Personas Skill

Library of 60+ accessibility personas for understanding diverse user needs, powered by [joe-watkins/a11y-personas](https://github.com/joe-watkins/a11y-personas).

## Important Note

**These synthetic personas are educational tools—they do not replace working directly with real people with disabilities.** Each person's experience is unique. Always prioritize user research and direct feedback from people with disabilities.

## Setup

This skill uses the a11y-personas repository as a git submodule.

**The skill will automatically initialize the submodule** if it detects the `repo/` folder is missing when you first use it.

### Manual Setup (optional)

```bash
cd .cursor/skills/a11y-personas
./setup.sh
```

Or from your project root:

```bash
git submodule update --init --recursive
```

### Updating Content

To pull the latest personas:

```bash
git submodule update --remote .cursor/skills/a11y-personas/repo
```

## What This Skill Does

Provides accessibility personas to help understand user needs. Ask about:

- **Specific disabilities** — "How does a screen reader user navigate?"
- **Assistive technology** — "What does a braille display user need?"
- **Design considerations** — "What should I consider for users with ADHD?"
- **Temporary disabilities** — "How would someone with a broken arm use this?"

## Folder Structure

```
a11y-personas/
├── README.md          # This file
├── SKILL.md           # Skill definition (read by AI)
├── setup.sh           # Submodule setup script
└── repo/              # Git submodule
    └── data/personas/
        ├── blindness-screen-reader-nvda.md
        ├── deafness-sign-language-user.md
        ├── adhd-attention.md
        ├── temp-broken-dominant-arm.md
        └── ... (60+ personas)
```

## Persona Categories

| Category | Examples |
|----------|----------|
| Vision | Screen reader users, low vision, color blindness |
| Hearing | Deaf, hard of hearing, late-deafened |
| Motor/Physical | Wheelchair users, tremor, one-handed |
| Cognitive | Memory loss, dyslexia, ADHD |
| Autism Spectrum | Sensory sensitive, communication differences |
| Mental Health | Anxiety, depression, PTSD |
| Temporary/Situational | Broken arm, holding child, noisy environment |

## Requirements

- Git (for submodule)
- No build step required — reads markdown files directly

## License

MIT

