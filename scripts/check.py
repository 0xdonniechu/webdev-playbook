#!/usr/bin/env python3
"""Checks for webdev-playbook. Standard library only. Exit 0 ok, 1 problems."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = [
    "README.md", "CLAUDE.md", "AGENTS.md", ".gitignore",
    "skills/webdev/SKILL.md",
    "templates/web-project-rules.md",
    "docs/legacy-patterns-checklist.md",
    "docs/modern-web-guidance.md",
]
HEADINGS = {
    "CLAUDE.md": ["## What it does", "## Verify", "## HARD", "## MEDIUM", "## EASY", "## Rules"],
    "docs/legacy-patterns-checklist.md": ["## Layout and UI", "## JavaScript", "## Quality", "## Security", "## Output"],
    "docs/modern-web-guidance.md": ["## Verified", "## Not verified", "## First trial"],
}
# private project names, home paths, token-like strings
LEAK = re.compile(r"/home/|ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|ambysto", re.I)
# the AGENTS.md pointer names Ambysto on purpose (it says "not Ambysto's"); CLAUDE.md too.
LEAK_OK = {"AGENTS.md", "CLAUDE.md"}


def main() -> int:
    errors = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"missing file: {rel}")
    for rel, heads in HEADINGS.items():
        p = ROOT / rel
        if p.is_file():
            text = p.read_text(encoding="utf-8")
            for h in heads:
                if h not in text:
                    errors.append(f"{rel}: missing heading '{h}'")
    skill = ROOT / "skills/webdev/SKILL.md"
    if skill.is_file():
        text = skill.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        if not m:
            errors.append("skills/webdev/SKILL.md: no frontmatter")
        else:
            fm = m.group(1)
            if not re.search(r"^name: webdev$", fm, re.M):
                errors.append("skill frontmatter: name must be 'webdev'")
            if "description:" not in fm:
                errors.append("skill frontmatter: no description")
    for p in ROOT.rglob("*"):
        if p.is_file() and ".git" not in p.parts and p.suffix in {".md", ".py", ".json"}:
            rel = p.relative_to(ROOT).as_posix()
            if rel in LEAK_OK or rel == "scripts/check.py":
                continue
            m = LEAK.search(p.read_text(encoding="utf-8"))
            if m:
                errors.append(f"{rel}: private-looking text '{m.group(0)}'")
    for e in errors:
        print("FAIL", e)
    print("ok" if not errors else f"{len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
