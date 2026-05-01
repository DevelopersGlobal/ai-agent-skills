#!/usr/bin/env python3
"""
Auto-generates skills/index.json by scanning all skills/*/SKILL.md files
and parsing their YAML frontmatter. Run by GitHub Actions on every push.
"""

import os
import json
import re

SKILLS_DIR = os.path.join(os.path.dirname(__file__), '..', 'skills')

def parse_frontmatter(content):
    """Extract YAML frontmatter between --- delimiters."""
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).splitlines():
        if ':' in line:
            key, _, val = line.partition(':')
            key = key.strip()
            val = val.strip()
            # Parse YAML lists like [a, b, c]
            if val.startswith('[') and val.endswith(']'):
                val = [v.strip().strip('"').strip("'") for v in val[1:-1].split(',') if v.strip()]
            fm[key] = val
    return fm

def kebab_to_title(name):
    """Convert kebab-case to Title Case."""
    return ' '.join(word.capitalize() for word in name.split('-'))

def main():
    skills = []

    for entry in sorted(os.listdir(SKILLS_DIR)):
        skill_path = os.path.join(SKILLS_DIR, entry, 'SKILL.md')
        if not os.path.isfile(skill_path):
            continue

        with open(skill_path, 'r', encoding='utf-8') as f:
            content = f.read()

        fm = parse_frontmatter(content)
        name = fm.get('name', entry)
        category = fm.get('category', 'general')
        description = fm.get('description', '')
        applies_to = fm.get('applies-to', ['any'])
        if isinstance(applies_to, str):
            applies_to = [applies_to]

        # Extract first non-frontmatter line after ## Overview as fallback description
        if not description:
            overview = re.search(r'## Overview\s*\n+(.*?)(?:\n\n|\n##)', content, re.DOTALL)
            if overview:
                description = overview.group(1).strip().replace('\n', ' ')[:200]

        skills.append({
            'name': name,
            'title': kebab_to_title(name),
            'category': category,
            'description': description,
            'applies-to': applies_to,
            'path': f'skills/{entry}/SKILL.md'
        })
        print(f"  + {name} [{category}]")

    output_path = os.path.join(SKILLS_DIR, 'index.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(skills, f, indent=2)

    print(f"\n✅ Generated {len(skills)} skills → skills/index.json")

if __name__ == '__main__':
    main()
