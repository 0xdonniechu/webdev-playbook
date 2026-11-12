# webdev-playbook: how coding agents write web code in 0xdonniechu repos (modern platform first, checked by review)

## What it does
Rules, one skill (`webdev`), a project-rules snippet and a legacy-pattern review checklist for any repo that ships HTML, CSS or JavaScript to a browser. It builds on `coding-playbook` (models, review loop, task rating) and adds only what is web-specific; it never repeats or overrides that repo. Markdown and one stdlib Python check script, no runtime code. A bug here means agents keep writing 2019-style web code or follow a wrong rule in every web repo; nothing is lost or published by a wrong line.

## Verify
- `python3 scripts/check.py`: required files exist, the skill's frontmatter is valid, the snippet and checklist keep their section headings, no file names a private project, path or secret.
- Owner-only or other-machine checks: installing `modern-web-guidance` in a web repo (network, plugin) is not run by `check.py`; record "not run" unless a session ran it.

## HARD: the main session does it directly, then hard-reviewer
- Nothing in this repo moves data, money or secrets. A rule change is HARD only when it tells sessions to do or not do something in every web repo and a revert would leave repos already changed by it (a rule copied into a project's `CLAUDE.md`).
- Anything that publishes the repo or a copy of it.

## MEDIUM: builder builds, reviewer reviews
- The skill's steps, the snippet's rules, the checklist's items, `scripts/check.py`.

## EASY: transcriber or builder, no review
- README wording, typos, examples that do not change a rule, status lines.

## Rules
- Universal web rules only: no project's names, paths or commands. A project's own choices live in its `CLAUDE.md`.
- State what is verified and what is not. A claim about a third-party tool (`modern-web-guidance`) is written only when a primary page says it; mark the rest "unverified".
- Guidance is not a gate: the skill and the snippet steer the writer, the checklist is for the reviewer. Do not describe either as enforcement.
- Git: English only; account `0xdonniechu` (check with `gh api user --jq .login` before any GitHub write); branches `slug`, never a push to `main`; this repo is not Ambysto's, so no Ambysto account, PR or memory workflow.
- A merge to `main` publishes nothing until a remote and Pages or a release exist; say so here when that changes.

## Session state
- Work in progress lives in `HANDOFF.md` (gitignored). If it exists at session start, read it first.
