# CSS verification report

Basis: `style.Bjtb6ElF.css` supplied by the user.

## Result

- Every selector used in `css/dwarven-forge.css` was checked against the supplied client CSS.
- Verified theme selectors: **147**
- Missing theme selectors after correction: **0**
- The theme does not globally replace `/img/gui/buttony.png`.
- Original game/content imagery that is not intentionally restyled is not copied to this repository.
- Dynamic game data is not baked into any production asset.

## Important implementation choices

1. Shared UI chrome (`window-frame`, panel dividers, slots, tab backgrounds, table headers, search, top/bottom bars, right-column background) is replaced directly.
2. Selected structural regions that were originally stored inside the multipurpose `buttony.png` sprite are overridden selector-by-selector with dedicated assets.
3. Semantic/gameplay icons left inside original sprites remain untouched.
4. Inventory choose/disable marks and item rarity frames are intentionally replaced because they are UI state chrome and the client exposes dedicated selectors for them.
5. Shop canopy selectors were verified against `.shop-wrapper .shop-background.normal-shop-zl .canopy` and `.shop-wrapper .shop-background.normal-shop-sl .canopy`.
