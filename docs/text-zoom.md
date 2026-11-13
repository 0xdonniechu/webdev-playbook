# Text zoom: boxes that grow with the user's text size

Guidance, not a gate. Users raise the browser's text size (a larger default root font size); a layout built in px keeps its boxes and the text spills, clips or collides. Write layout so it survives 150% and 200% root sizes, and check it.

## Write it
- **Sizes in rem** for font sizes and for boxes that hold text (widths, heights, padding, gaps, `min-width`). At the default 16 px root the sizes are unchanged; with a larger root the boxes grow with their text. A fixed px `height` on a box with text is the usual cause of clipping: use `min-height` or let content size it.
- **The clamp pitfall.** `clamp(2.75rem, 6.6vw, 5.94rem)` stops growing with the root as soon as the `vw` middle term wins (wide viewports): the heading stays the same size at 200% text. Give the middle term a root-relative part that is zero at the default root, for example `clamp(2.75rem, calc(6.6vw + (1rem - 16px) * 3), 5.94rem)`: same size at 16 px, bigger when the root grows. The `(1rem - 16px)` term assumes the author leaves the root size alone: with `html { font-size: 62.5% }` it goes negative, so use it only where the root is the user's default. Dividing one length by another (typed arithmetic, to get a unitless ratio) would be cleaner, but whether it is Baseline is unverified here (no primary page was checked): check the repo's baseline and a primary page before using it. Same fix for any px `clamp` on headings. Check the size at 16 px and at 32 px roots; it should grow (about 1.5x or more at 200%).
- **Container queries** to stack a component that gets squeezed: when text grows, a two-column grid in a fixed-width column leaves a column of a few characters per line. Make the component a container and switch it to one column at a width (in `rem`, so the threshold also moves with text size) rather than on the viewport width.
- Let rows wrap (`flex-wrap`), keep an icon and its first line of text on one row, and keep controls inside the page at 320 and 360 px.

## Check it
Add a browser check (any browser-automation library) that, for each page block, at root sizes of 24 px and 32 px (150% and 200% of 16) and at widths of at least 1440, 768, 390, 360 and 320, sets the root font size, waits for fonts, and runs these tests. One result line per width, size and block, so a failure names where it is.

Setting `document.documentElement.style.fontSize` only approximates a user's default font size. Gaps: it overrides an author's own root size, so a page that pins `html { font-size: 16px }` (or uses `62.5%`) ignores the user's setting in real life yet passes this check; and `rem`/`em` in media queries resolve against the initial (user default) size, not the root element, so those queries do not move in this check. Where the automation library can set the browser's own default font size, prefer that (unverified: check the library's primary documentation for whether and how it does), and treat the root override as a fallback. Say in the report which one the check used.
- **Clipped**: an element that clips (`overflow` not visible) must fit its content (`scrollWidth/Height <= client + 1`).
- **Spilling**: each text range's rect lies inside its block's box and inside every ancestor that clips (1 px slack). Judge line boxes, not glyph boxes: remove the half-leading, or tight line heights give false alarms.
- **Squeezed**: a text element whose width is near zero is obviously broken, but the real failure is a column a few characters wide. Use a rule on characters per line, for example: an element that wraps onto more than one line and is narrower than about N of its own characters (pick N, for example 20, from a case you know is bad, and keep it only if it still passes the good pages). A threshold of a few px catches nothing real.
- **Overlapping text**: no two text elements of one block (not ancestor and descendant) have overlapping line rects.
- **Past the page edge**: no box runs beyond the page's left or right edge, at 360 and 320 px too, unless a smaller box inside the page crops it on purpose.
- **Decorative boxes over controls**: a sticker, mascot or tag must not cover a button, link or pill (box intersection over 2 px, using the visible box). Text-with-text tests do not see this.
- **Hit tests**: for every link and button, scroll it into view first (`elementFromPoint` returns null outside the viewport), then `elementFromPoint` at about 10%, 50% and 90% of its width (vertical centre) returns it or a child, at each width and root size, and at widths just inside each breakpoint. A control placed over another control fails here.
- **Disclosures opened**: closed `<details>` content is not laid out as shown; open every one (remove a shared `name` first so all can be open) and run the tests again.
- **Fixed and floating elements** (badge, sticky bar, chat button) are blocks of their own: include them, after scrolling.

## Exemptions
Keep the list in the check file, each entry with its reason, as narrow as the thing it excuses (one decorative image frame, not everything inside its section). Typical honest reasons: decorative and hidden from assistive technology; a band cropped on purpose by its parent; text that types in and is repeated in a screen-reader-only line. Review the list whenever it grows; a broad selector silently exempts controls placed later.

## Bite-test each check
On a scratch copy, break the layout the way each test is meant to catch (a px height on a text box, remove a container query, put a sticker over a button, widen a control past 320 px) and see the check fail; then restore. A check never shown failing is not a check. Run heavy browser jobs under a memory cap (`docs/layout-parity.md`).
