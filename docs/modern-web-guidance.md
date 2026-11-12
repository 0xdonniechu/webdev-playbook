# Modern Web Guidance (Chrome): what is verified

Checked 2026-11-12 against [developer.chrome.com/docs/modern-web-guidance](https://developer.chrome.com/docs/modern-web-guidance) and one third-party article ([dev.to](https://dev.to/highflyer910/modern-web-guidance-teaching-ai-agents-to-stop-coding-like-its-2019-508b), not an official source). The short link `goo.gl/modern-web-guidance` returned 404.

## Verified (a primary page says it)
- A set of skills for coding agents that carries web platform practice and browser compatibility data into the agent's context. Early preview, announced at Google I/O 2026-05-19.
- Install: `npx modern-web-guidance@latest install`; Claude Code plugin `claude plugin install modern-web-guidance@claude-plugins-official`; also `npx skills add GoogleChrome/modern-web-guidance`.
- Source: GitHub `GoogleChrome/modern-web-guidance`, Apache 2.0 (from search results; not read in the repo).

## Reported only by the third-party article or search snippets
- 100+ use cases on accessibility, performance and security (dialog, Popover, container queries, View Transitions, passkeys, CSP, LCP/INP).
- Default target "Baseline Widely available" (30 months interoperable), changeable in `AGENTS.md`.
- Agents can ignore it; coverage is thin in niche areas (advanced WebGL, complex Service Workers).

## Not verified
- What the installer writes into a repo or the agent context.
- The exact `AGENTS.md` key for the baseline target.
- Whether the plugin installs at project scope.
- Whether it changes the output on our repos at all.

## First trial (not run)
1. Pick one small web repo. Record its baseline target in its `CLAUDE.md` (`templates/web-project-rules.md`).
2. Install the plugin at project scope; read what changed (`git status`, the plugin's files) before committing anything.
3. Give an agent the same small UI task with and without it; compare the diffs against `docs/legacy-patterns-checklist.md`.
4. Record the result here. Keep the tool only if the diffs differ for the better.
