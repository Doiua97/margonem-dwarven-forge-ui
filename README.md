# Dwarven Forge — Corner Forge v0.4.0

Pakiet do bezpośredniego wrzucenia do katalogu głównego repozytorium `Doiua97/margonem-dwarven-forge-ui`.

## Założenia
- CSS-only: userscript wyłącznie ładuje CSS.
- Brak avatarów i nowych funkcji.
- Natywne rarity/item frames nie są nadpisywane.
- Equipment wrapper zachowuje geometrię slotów klienta.
- Inventory zachowuje natywny rozmiar 232×198, odpowiadający siatce 7×6.
- Bags navigation: 4 realne kwadratowe sloty na torby, bez numerów generowanych przez motyw.
- Extended stats rozwijają się w lewo nad mapę.
- Dolny HUD: HP + EXP, sloty 1–8, poniżej wszystkie istniejące widgety.
- Battle bars nie mają stałego miejsca w widoku podstawowym.
- Responsywność utrzymuje tę samą kompozycję na różnych rozdzielczościach.

## Instalacja w repo
Skopiuj zawartość folderu do root repo. Następnie zaktualizuj userscript w Tampermonkey/Violentmonkey.

## Ważne przed testem
Klient ma własne stany `body[data-res]`, `chat-size-*`, `eq-column-size-*`, `static-widget-position`.
Pakiet je neutralizuje tylko tam, gdzie przebudowujemy layout. Testy w prawdziwym kliencie nadal są konieczne.
