# webdev-playbook

How coding agents write web code: use the current web platform, target a stated browser baseline, and have the reviewer check for legacy patterns.

It sits beside [`coding-playbook`](https://github.com/0xdonniechu/coding-playbook) (models, review loop, task rating) and adds only the web-specific part.

## What is here
- `skills/webdev/SKILL.md`: the steps a session follows before and while writing browser code.
- `templates/web-project-rules.md`: lines to paste into a web repo's `CLAUDE.md` (baseline target, guidance tool, review rule).
- `docs/legacy-patterns-checklist.md`: what a reviewer looks for in a web diff.
- `docs/modern-web-guidance.md`: what Chrome's Modern Web Guidance is, and what is and is not verified about it.
- `scripts/check.py`: `python3 scripts/check.py`.

## Status
Draft. Nothing here has been tried on a real web repo yet; the first trial is listed in `docs/modern-web-guidance.md`.
