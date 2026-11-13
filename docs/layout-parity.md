# Matching a reference layout (geometry only)

Guidance, not a gate: use it when the owner asks for a page whose layout geometry matches a reference page while the media and the copy stay your own. The tolerances below are an example that worked on one page, not a law; the owner or the repo's `CLAUDE.md` sets the real ones.

## What may be copied
- Numbers only: box positions, sizes, font sizes, breakpoints, page height. Store them in a snapshot file.
- Never copy the reference's assets, copy, markup or code. Your images, video and words fill the same boxes.

## Method
1. **Measure the reference at fixed widths** (for example 1440, 1024, 768, 390, 900 px tall) in one local browser, with reduced motion so reveal transforms are settled. Write the numbers to a stored snapshot with the date measured. The gate compares against the file, so it does not depend on the network or on the reference changing.
2. **Mark your components** with a data attribute (`data-p="<block>.<name>"`) and keep a map file that pairs each of your blocks and components with a selector on the reference. The markup then carries the contract; every mapped name is used once and no top-level box is left unmapped.
3. **Compare**: block list and order; block tops and heights; component boxes (position relative to the block's corner, so one block can be checked alone while building); heading font sizes; breakpoints (the `max-width` and, for a mobile-first site, `min-width` values in the stylesheets); page height.
4. **Measure carefully**: wait for `document.fonts.ready` and fail if your fonts did not load; scroll the whole page once so lazy and revealed content is laid out; measure fixed or floating elements (a badge, a chat button) against the viewport after scrolling, not as part of the block order; fix the clock if early or late content depends on a date.
5. **Exit codes**: 0 all rows pass, 1 some row differs, 2 could not measure (font missing, no snapshot, no browser). Keep "differs" and "could not measure" apart so a broken run is never read as a pass or as drift.
6. **Report**: write a table of every row (reference, ours, difference, PASS/FAIL) and full-page screenshots of both pages side by side per width. The owner's eye check on those pairs is the last step; mark it "not run" until the owner did it. The reference screenshots, and any other captured reference material, stay out of the repo: write them to a gitignored folder, because committing them republishes a third party's images and copy.
7. **A snapshot refresh is its own reviewed change**, never bundled with layout work: a refresh that quietly moves the target hides drift.
8. **Memory**: a gate that launches browsers is heavy; follow the memory-cap practice in `coding-playbook`'s working practice.

## Tolerances that worked (example)
- Block height: +-3% or 24 px, whichever is larger. Block top and page height: +-1% or 24 px.
- Block x: +-12 px. Block width: +-4% with a 2 px floor. Thin blocks that are components themselves (a header, a ticker): +-4% on height too.
- Component position (x and y) +-12 px; component width and height +-4% with a 2 px floor on the allowed difference.
- Heading font size +-2%. Breakpoints: the same values. Blocks: the same list in the same order.

## Known limits to write down
Breakpoints read from `max-width` only miss a mobile-first (`min-width`) site: read both, or name the gap; they also come only from `@media` rules (not from `media` attributes or script); fonts counted per family, not per weight; a hidden duplicate of a marked element counts as a duplicate.

## Bite tests before you trust it
A gate that cannot fail proves nothing. On a scratch copy, inject (a) a breakpoint shift (change one `max-width` by 60 px) and (b) a size change (one component 10% wider). The gate must exit 1 and name the failing rows; unchanged, it exits 0. Record both results.

## Keep the boxes responsive to text size
Matching geometry at the default root size must not freeze the layout in px. Size boxes in rem so they grow with the user's text size and keep the reference size at the default root, and run the check in `docs/text-zoom.md` for every block you match.
