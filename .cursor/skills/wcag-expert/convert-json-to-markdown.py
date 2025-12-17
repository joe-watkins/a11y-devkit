#!/usr/bin/env python3
"""
WCAG JSON to Markdown Converter

Converts the large WCAG JSON file into organized markdown partials
with a logical folder structure for fast retrieval.

Output structure:
data/
├── principles/
│   ├── 1-perceivable.md
│   ├── 2-operable.md
│   ├── 3-understandable.md
│   └── 4-robust.md
├── guidelines/
│   ├── 1.1-text-alternatives.md
│   ├── 1.2-time-based-media.md
│   └── ...
├── success-criteria/
│   ├── level-a/
│   │   ├── 1.1.1-non-text-content.md
│   │   └── ...
│   ├── level-aa/
│   │   └── ...
│   └── level-aaa/
│       └── ...
└── terms/
    ├── a-c/
    │   ├── abbreviation.md
    │   └── ...
    ├── d-f/
    ├── g-i/
    ├── j-l/
    ├── m-o/
    ├── p-r/
    ├── s-u/
    └── v-z/
"""

import json
import os
import re
from pathlib import Path
from html import unescape

# Configuration
SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "data" / "wcag.json"
OUTPUT_DIR = SCRIPT_DIR / "data" / "markdown"


def clean_html(html_content: str) -> str:
    """Convert HTML to clean markdown-friendly text."""
    if not html_content:
        return ""
    
    # Unescape HTML entities
    text = unescape(html_content)
    
    # Convert common HTML to markdown
    text = re.sub(r'<p[^>]*>', '', text)
    text = re.sub(r'</p>', '\n\n', text)
    text = re.sub(r'<strong>([^<]+)</strong>', r'**\1**', text)
    text = re.sub(r'<em>([^<]+)</em>', r'*\1*', text)
    text = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>([^<]*)</a>', r'[\2](\1)', text)
    text = re.sub(r'<code>([^<]+)</code>', r'`\1`', text)
    text = re.sub(r'<li>\s*', '- ', text)
    text = re.sub(r'</li>', '\n', text)
    text = re.sub(r'<ul[^>]*>', '\n', text)
    text = re.sub(r'</ul>', '\n', text)
    text = re.sub(r'<ol[^>]*>', '\n', text)
    text = re.sub(r'</ol>', '\n', text)
    text = re.sub(r'<dl[^>]*>', '\n', text)
    text = re.sub(r'</dl>', '\n', text)
    text = re.sub(r'<dt>([^<]+)</dt>', r'**\1**: ', text)
    text = re.sub(r'<dd>\s*', '', text)
    text = re.sub(r'</dd>', '\n\n', text)
    text = re.sub(r'<div[^>]*class="note"[^>]*>.*?<span>([^<]+)</span>.*?<p[^>]*>([^<]+)</p>.*?</div>', r'\n> **\1**: \2\n', text, flags=re.DOTALL)
    text = re.sub(r'<aside[^>]*class="example"[^>]*>.*?<div[^>]*>([^<]+)</div>.*?<p>([^<]+)</p>.*?</aside>', r'\n> **\1**: \2\n', text, flags=re.DOTALL)
    
    # Remove remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Clean up whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()
    
    return text


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def get_term_folder(term_name: str) -> str:
    """Get the alphabetical folder for a term."""
    first_char = term_name[0].lower() if term_name else 'a'
    
    folders = {
        'a': 'a-c', 'b': 'a-c', 'c': 'a-c',
        'd': 'd-f', 'e': 'd-f', 'f': 'd-f',
        'g': 'g-i', 'h': 'g-i', 'i': 'g-i',
        'j': 'j-l', 'k': 'j-l', 'l': 'j-l',
        'm': 'm-o', 'n': 'm-o', 'o': 'm-o',
        'p': 'p-r', 'q': 'p-r', 'r': 'p-r',
        's': 's-u', 't': 's-u', 'u': 's-u',
        'v': 'v-z', 'w': 'v-z', 'x': 'v-z', 'y': 'v-z', 'z': 'v-z'
    }
    
    return folders.get(first_char, 'a-c')


def create_principle_md(principle: dict) -> str:
    """Generate markdown content for a WCAG principle."""
    content = f"""---
id: {principle['id']}
num: "{principle['num']}"
handle: {principle['handle']}
versions: {', '.join(principle['versions'])}
---

# Principle {principle['num']}: {principle['handle']}

{clean_html(principle['content'])}

## Guidelines

"""
    
    for guideline in principle.get('guidelines', []):
        content += f"- **{guideline['num']} {guideline['handle']}**: {clean_html(guideline.get('title', ''))}\n"
    
    return content


def create_guideline_md(guideline: dict, principle: dict) -> str:
    """Generate markdown content for a WCAG guideline."""
    content = f"""---
id: {guideline['id']}
num: "{guideline['num']}"
handle: {guideline['handle']}
principle: {principle['handle']}
principle_num: "{principle['num']}"
versions: {', '.join(guideline['versions'])}
---

# Guideline {guideline['num']}: {guideline['handle']}

**Principle**: {principle['num']} {principle['handle']}

{clean_html(guideline['content'])}

## Success Criteria

"""
    
    for sc in guideline.get('successcriteria', []):
        level = sc.get('level', 'A')
        content += f"- **{sc['num']} {sc['handle']}** (Level {level})\n"
    
    return content


def format_techniques(techniques_data: dict) -> str:
    """Format techniques section for success criteria."""
    if not techniques_data:
        return ""
    
    content = "\n## Techniques\n"
    
    # Sufficient techniques
    sufficient = techniques_data.get('sufficient', [])
    if sufficient:
        content += "\n### Sufficient Techniques\n\n"
        for item in sufficient:
            if isinstance(item, dict):
                if 'title' in item:
                    content += f"**{clean_html(item['title'])}**\n\n"
                
                for tech in item.get('techniques', []):
                    if isinstance(tech, dict):
                        tech_id = tech.get('id', '')
                        tech_title = tech.get('title', '')
                        content += f"- **{tech_id}**: {tech_title}\n"
                
                for group in item.get('groups', []):
                    if isinstance(group, dict):
                        content += f"\n*{group.get('title', '')}*\n\n"
                        for tech in group.get('techniques', []):
                            if isinstance(tech, dict):
                                tech_id = tech.get('id', '')
                                tech_title = tech.get('title', '')
                                content += f"- **{tech_id}**: {tech_title}\n"
    
    # Advisory techniques
    advisory = techniques_data.get('advisory', [])
    if advisory:
        content += "\n### Advisory Techniques\n\n"
        for tech in advisory:
            if isinstance(tech, dict):
                tech_id = tech.get('id', '')
                tech_title = tech.get('title', '')
                content += f"- **{tech_id}**: {tech_title}\n"
    
    # Failure techniques
    failure = techniques_data.get('failure', [])
    if failure:
        content += "\n### Common Failures\n\n"
        for tech in failure:
            if isinstance(tech, dict):
                tech_id = tech.get('id', '')
                tech_title = tech.get('title', '')
                content += f"- **{tech_id}**: {tech_title}\n"
    
    return content


def create_success_criterion_md(sc: dict, guideline: dict, principle: dict) -> str:
    """Generate markdown content for a WCAG success criterion."""
    level = sc.get('level', 'A') or 'A'  # Handle None or empty string
    
    content = f"""---
id: {sc['id']}
num: "{sc['num']}"
handle: {sc['handle']}
level: {level}
guideline: {guideline['handle']}
guideline_num: "{guideline['num']}"
principle: {principle['handle']}
principle_num: "{principle['num']}"
versions: {', '.join(sc.get('versions', ['2.0', '2.1', '2.2']))}
---

# {sc['num']} {sc['handle']} (Level {level})

**Guideline**: {guideline['num']} {guideline['handle']}  
**Principle**: {principle['num']} {principle['handle']}

## Understanding

{clean_html(sc.get('title', ''))}

## Full Description

{clean_html(sc.get('content', ''))}
"""
    
    # Add details if present
    details = sc.get('details', [])
    if details:
        content += "\n## Details\n\n"
        for detail in details:
            if isinstance(detail, dict) and detail.get('type') == 'ulist':
                for item in detail.get('items', []):
                    if isinstance(item, dict):
                        handle = item.get('handle', '')
                        text = item.get('text', '')
                        content += f"- **{handle}**: {text}\n"
    
    # Add techniques
    content += format_techniques(sc.get('techniques', {}))
    
    # Add WCAG reference link
    content += f"\n\n---\n\n📖 **Reference**: [WCAG 2.2 - {sc['num']} {sc['handle']}](https://www.w3.org/WAI/WCAG22/Understanding/{sc['id']})\n"
    
    return content


def create_term_md(term: dict) -> str:
    """Generate markdown content for a WCAG glossary term."""
    term_name = term.get('name', 'Unknown')
    term_id = term.get('id', '')
    
    content = f"""---
id: {term_id}
term: {term_name}
---

# {term_name.title()}

{clean_html(term.get('definition', ''))}

---

📖 **Reference**: [WCAG 2.2 Glossary - {term_name}](https://www.w3.org/TR/WCAG22/#{term_id})
"""
    
    return content


def create_index_files(data: dict, output_dir: Path):
    """Create index files for easy navigation."""
    
    # Main index
    main_index = """---
id: wcag-index
title: WCAG 2.2 Quick Reference
---

# WCAG 2.2 Quick Reference

## Folder Structure

- `principles/` - The 4 WCAG principles (POUR)
- `guidelines/` - All guidelines organized by number
- `success-criteria/` - All success criteria organized by level
  - `level-a/` - Level A (minimum)
  - `level-aa/` - Level AA (recommended)
  - `level-aaa/` - Level AAA (enhanced)
- `terms/` - Glossary terms organized alphabetically

## Quick Links by Principle

### 1. Perceivable
Content must be presentable in ways users can perceive.

### 2. Operable
UI components and navigation must be operable.

### 3. Understandable
Information and UI operation must be understandable.

### 4. Robust
Content must be robust enough for assistive technologies.

## Usage

Search for specific criteria by number (e.g., "1.1.1") or by topic (e.g., "color contrast", "keyboard").
"""
    
    index_path = output_dir / "README.md"
    index_path.write_text(main_index, encoding='utf-8')
    print(f"Created: {index_path}")


def convert_wcag_json():
    """Main conversion function."""
    print(f"Reading JSON from: {INPUT_FILE}")
    
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Create output directories
    dirs = [
        OUTPUT_DIR / "principles",
        OUTPUT_DIR / "guidelines",
        OUTPUT_DIR / "success-criteria" / "level-a",
        OUTPUT_DIR / "success-criteria" / "level-aa",
        OUTPUT_DIR / "success-criteria" / "level-aaa",
        OUTPUT_DIR / "terms" / "a-c",
        OUTPUT_DIR / "terms" / "d-f",
        OUTPUT_DIR / "terms" / "g-i",
        OUTPUT_DIR / "terms" / "j-l",
        OUTPUT_DIR / "terms" / "m-o",
        OUTPUT_DIR / "terms" / "p-r",
        OUTPUT_DIR / "terms" / "s-u",
        OUTPUT_DIR / "terms" / "v-z",
    ]
    
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {d}")
    
    stats = {
        'principles': 0,
        'guidelines': 0,
        'success_criteria': {'A': 0, 'AA': 0, 'AAA': 0},
        'terms': 0
    }
    
    # Process principles
    for principle in data.get('principles', []):
        filename = f"{principle['num']}-{slugify(principle['handle'])}.md"
        filepath = OUTPUT_DIR / "principles" / filename
        filepath.write_text(create_principle_md(principle), encoding='utf-8')
        stats['principles'] += 1
        print(f"Created: {filepath}")
        
        # Process guidelines within principle
        for guideline in principle.get('guidelines', []):
            filename = f"{guideline['num']}-{slugify(guideline['handle'])}.md"
            filepath = OUTPUT_DIR / "guidelines" / filename
            filepath.write_text(create_guideline_md(guideline, principle), encoding='utf-8')
            stats['guidelines'] += 1
            print(f"Created: {filepath}")
            
            # Process success criteria within guideline
            for sc in guideline.get('successcriteria', []):
                level = sc.get('level', 'A') or 'A'  # Handle None or empty
                level_folder = f"level-{level.lower()}"
                filename = f"{sc['num']}-{slugify(sc['handle'])}.md"
                filepath = OUTPUT_DIR / "success-criteria" / level_folder / filename
                filepath.write_text(create_success_criterion_md(sc, guideline, principle), encoding='utf-8')
                stats['success_criteria'][level] = stats['success_criteria'].get(level, 0) + 1
                print(f"Created: {filepath}")
    
    # Process terms
    for term in data.get('terms', []):
        term_name = term.get('name', 'unknown')
        folder = get_term_folder(term_name)
        filename = f"{slugify(term_name)}.md"
        filepath = OUTPUT_DIR / "terms" / folder / filename
        filepath.write_text(create_term_md(term), encoding='utf-8')
        stats['terms'] += 1
        print(f"Created: {filepath}")
    
    # Create index files
    create_index_files(data, OUTPUT_DIR)
    
    # Print summary
    print("\n" + "="*50)
    print("CONVERSION COMPLETE")
    print("="*50)
    print(f"Principles:        {stats['principles']}")
    print(f"Guidelines:        {stats['guidelines']}")
    print(f"Success Criteria:")
    print(f"  - Level A:       {stats['success_criteria'].get('A', 0)}")
    print(f"  - Level AA:      {stats['success_criteria'].get('AA', 0)}")
    print(f"  - Level AAA:     {stats['success_criteria'].get('AAA', 0)}")
    print(f"Glossary Terms:    {stats['terms']}")
    print(f"\nOutput directory:  {OUTPUT_DIR}")


if __name__ == "__main__":
    convert_wcag_json()
