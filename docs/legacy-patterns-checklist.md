# Legacy-patterns checklist (for the reviewer of a web diff)

A starting list, not a standard: edit it from what reviews actually find. Flag an item as an issue only when the repo's stated browser baseline allows the modern form.

## Layout and UI
- Hand-built modal or tooltip where `<dialog>` or the Popover API fits.
- Float or table layout, or JS measuring for what flex, grid or container queries do.
- A JS animation of page transitions where View Transitions fit.
- Font sizes in px, or a heading `clamp()` whose middle term is `vw` only, so the text does not grow with the user's text size (`docs/text-zoom.md`).
- Fixed px width or height on a box that holds text, where rem, `min-height` or content sizing fits.
- A viewport media query for a component that only depends on its own width, where a container query fits.
- A control (button, link, badge, sticker) placed over another control, so one hides or intercepts the other at some width or text size.

## JavaScript
- jQuery or a utility library added for something the platform now does (`fetch`, `querySelector`, `classList`, `structuredClone`).
- A polyfill or transpile step for a feature already inside the baseline.
- `var`, callback chains, `XMLHttpRequest` in new code.

## Quality
- Missing accessible names, focus handling or keyboard path on a new control; colour as the only signal.
- Images and fonts without size hints or lazy loading where they are below the fold; layout shift from them.
- Heavy work on the main thread in an input handler.

## Security
- Inline script or style that blocks a strict CSP; `innerHTML` with unescaped input.
- Passwords-only sign-in where the product could offer passkeys (a product decision: ask, do not change).

## Output
Reviewer lists numbered issues, each with the file and line, the legacy form, the modern form and the baseline it relies on.
