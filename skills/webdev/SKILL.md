---
name: webdev
description: |
  Steps for writing or reviewing browser code (HTML, CSS, JavaScript) in a web repo: read the repo's browser baseline, prefer current platform features, use the modern-web-guidance skill when it is installed, and check the diff against a legacy-patterns list. Use when a task adds or changes UI, CSS, front-end JavaScript or browser APIs. Not for server-only code.
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
---

# webdev

Guidance, not enforcement: it steers the writer and gives the reviewer a list. Nothing here blocks a bad change.

## Before writing
1. Read the repo's `CLAUDE.md` for its browser baseline. If there is none, say so and use "Baseline Widely available" as a stated assumption; do not edit the project's rules.
2. If the `modern-web-guidance` skill is installed, use it for the feature you are about to write. If it is not, do not install it unasked: installing writes files and fetches code, so ask.
3. Prefer the platform to a library: `<dialog>`, Popover, container queries, `fetch`, `structuredClone`, View Transitions, where the baseline allows.

## While writing
- A feature outside the baseline gets a fallback and a one-line note.
- New controls get an accessible name, a keyboard path and visible focus.
- Do not add a dependency or a polyfill for something the baseline already has.

## Layout
- When the owner asks to match a reference layout (geometry only, never its assets or copy), follow `docs/layout-parity.md` of webdev-playbook.
- When writing layout CSS (and before handing over), follow `docs/text-zoom.md`: sizes in rem, no vw-dominated clamp on headings, and run or add a text-zoom check at 150% and 200% root sizes.

## Before handing over
- Walk the diff against `docs/legacy-patterns-checklist.md` of webdev-playbook (or the project's copy). List each hit and fix it or say why it stays.
- Run the repo's Verify. Write "not run: <reason>" for any accessibility, performance or cross-browser check you did not run.

## Stop and ask
- Changing the baseline, the supported browsers, a CSP or the sign-in method.
- Installing a plugin or tool into the repo.
