# Web project rules (paste into the web repo's CLAUDE.md under "Rules")

- Browser baseline: <Baseline Widely available | Baseline Newly available | a stated browserslist>. New browser code uses what that baseline allows; a feature outside it needs a fallback and a note.
- Before writing UI or browser-API code, follow `webdev` (webdev-playbook) and, if installed, the `modern-web-guidance` skill. Say in the PR which was used.
- Reviewers check the diff against the legacy-patterns checklist of webdev-playbook; an item allowed by the baseline is an issue.
- Never silently change the baseline, the supported-browser list or a CSP. Flag it and ask.
- Run the repo's own accessibility and performance checks listed in Verify; write "not run: <reason>" for the rest.
