# Fire pit math

Backyard fire pit planning arithmetic: the diameter names the blocks, the margin names the gravel, and the space names the verdict.

Live at https://ilanis-agent.github.io/firepitmath/

## The three tools

- **Ring plan** - blocks per course = ceil(pi x diameter / labeled 40 cm); stack = per course x labeled 3 courses, with tabletop, classic and bonfire bands.
- **Gravel plan** - base = diameter + labeled 30 cm margin each side; area at labeled 10 cm deep becomes liters and bags of labeled 25 L, with wheelbarrow, few-trips and delivery bands.
- **Clearance plan** - clear circle = diameter + labeled 3 m each side, checked against your space: room to spare, right at the labeled clearance, or too tight.

## Formulas and limits

- Areas and clearances are rounded to one decimal (round half up), mirroring the oracle float-for-float.
- Every number the app borrows is labeled in the interface: block length, courses, margin, depth, bag size, clearance.
- Illustrative planning arithmetic only. Real fire pits follow local fire rules, burn bans and code clearances; a fire is never left alone. This is not a fire permit.

## Development

- `engine.js` - calculation and render engine (browser global `FirepitMath`, CommonJS for tests).
- `oracle.py` - Python mirror of the engine; regenerates `expected.json`.
- `test.js` - runs every case through the engine and compares fields and render strings: `node test.js`.
