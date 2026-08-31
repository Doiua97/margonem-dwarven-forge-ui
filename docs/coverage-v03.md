# Dwarven Forge v0.3 — coverage plan

Basis:
- `style.Bjtb6ElF.css` — current client stylesheet supplied by the user.
- `podglądowy.css` — reference theme supplied by the user, used as an implementation-coverage model (not as an asset source).

The reference stylesheet contains 297 CSS rule blocks / 457 selector entries and demonstrates that a complete theme must target families of components separately instead of relying on only a few global overrides.

## Covered in v0.3

- permanent top and bottom interface bars
- HUD container and dynamic client data container styling
- generic game windows, transparent windows and headers
- buttons, tabs, dropdowns, inputs, radio/checkbox controls
- scrollbar families used across game windows
- left chat column / new chat UI
- right character column, equipment, inventory and bags navigation
- extended statistics
- minimap panel and minimap content
- dialogue/trade surfaces and answer rows
- battle controller and battle log states
- quest/recovery/friends reusable surfaces
- settings, addons, help and grouped-list panels
- clan windows, clan tables and green information boxes
- auctions / auction tables
- depot panels and slot area
- shop surfaces and canopy
- premium/chests/promo panels
- matchmaking, achievements, item changer, news and outfit panels
- tooltips and popup menus
- shared section headers and bottom bars

## Hard rules

1. Native item rarity/highlight rendering is not overridden.
2. Item graphics, skill icons, buffs/debuffs, profession icons, currencies and quest-state markers remain client-driven.
3. Dynamic data such as character name, level, HP/mana/energy/EXP, world/map names and values is never baked into theme graphics.
4. No new mechanics or JS-created UI are introduced by the theme.
5. `podglądowy.css` is used only to learn the breadth and targeting strategy of a complete CSS theme; none of its third-party graphics are copied.

## Testing

v0.3 should be checked in the same representative views used in the first integration test: normal gameplay HUD, battle, small addon widgets, clans, world list, shop and auctions. Additional screens should include inventory/stats expanded, dialogue, quest log, settings, addons, mail, depot, premium and tooltip states.
