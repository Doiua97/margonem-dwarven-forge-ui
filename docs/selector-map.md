# Mapa selektorów użytych w v0.4.0

| Funkcja | Selektor klienta | Działanie motywu |
|---|---|---|
| HUD | `.positioner.top .hud-container` | nowy poziomy layout |
| Nick | `.hero-data .heroname` | repozycjonowanie |
| Level | `.hero-data .herolvl` | repozycjonowanie |
| Mapa/dane lokacji | `.hud-container .map-data` | środek HUD |
| Złoto | `.herogold`, `.gold-btn` | prawa sekcja HUD |
| Smocze Łuski | `.herocredits`, `.credits-btn` | prawa sekcja HUD |
| Chat | `.main-column.left-column`, `.new-chat-window` | lewy panel |
| Equipment | `.character_wrapper .equipment-wrapper` | zachowana natywna geometria slotów |
| Statystyki | `.character_wrapper .stats-wrapper` | kompaktowy panel + natywny przycisk Rozwiń/Zwiń |
| Pełne statystyki | `.main-column .extended-stats` | otwieranie w lewo |
| Inventory | `.inventory_wrapper .inventory-grid` | 232×198 / 7×6 |
| Torby | `.inventory_wrapper .bags-navigation` | 4 realne sloty |
| HP | `.hp-indicator-wrapper` | bez kuli, poziomy pasek |
| EXP | `.exp-bar-wrapper` | poziomy pasek obok HP |
| Sloty | `.bottom-panel > .slots`, `.skill-usable-slots` | pozycja pod HP/EXP |
| Widgety | 6× `.main-buttons-container.*` | wizualnie jeden pas |
| Edycja widgetów | `.empty-slot-widget`, `.widget-edit-mode` | zachowana |
| Battle bars | `.battle-bars-wrapper` | brak stałego pola w normalnym widoku |

## Elementy celowo nietknięte
- `.item .highlight.h-exist` i cały natywny sprite rarity.
- Grafiki przedmiotów.
- Ikony skilli/buffów.
- Semantyczne ikony klienta.
