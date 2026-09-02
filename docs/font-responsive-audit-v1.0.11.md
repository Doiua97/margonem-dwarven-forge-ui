# Audyt czcionki i skalowania v1.0.11

Data: 2026-09-02

## Czcionka

Wdrożenie jednej czcionki istnieje i obejmuje główny interfejs. Zmienna `--df-font` wskazuje `"Segoe UI", Arial, sans-serif`, a reguła z `!important` obejmuje:

- `.game-window-positioner` i wszystkie jego dzieci;
- alerty;
- konsolę;
- duże i mobilne komunikaty;
- tooltipy;
- osobno górny HUD oraz elementy dolnego HUD-u.

Do sprawdzenia w runtime pozostają:

- `.bubbledialog`, jeśli zostanie umieszczony poza `.game-window-positioner`;
- panele dodatków tworzące własny korzeń bezpośrednio pod `body`;
- portale i nakładki tworzone poza objętymi warstwami.

CSS dokumentu gry nie zmieni bezpiecznie treści zewnętrznego iframe ani tekstu rysowanego na canvasie. Nie będą one traktowane jako błąd dziedziczenia czcionki motywu.

## Skalowanie

Bazowy klient posiada rozbudowany system responsywny:

- setki selektorów `data-res`;
- setki selektorów `zoom-factor`;
- warianty `mobile-version`;
- osobne stany szerokości czatu i kolumny ekwipunku;
- tryb `light-interface`.

Warstwa `accepted-audit-package.source.css` w v1.0.11 nie zawiera reguł `data-res`, `zoom-factor`, `mobile-version` ani media queries. Jednocześnie ustawia stałymi pikselami między innymi:

- pola górnego HUD-u;
- położenie tarczy dolnego HUD-u;
- położenie lewego i prawego paska EXP;
- położenie slotów umiejętności;
- widoczność dodatkowych teł widgetów.

Część tych reguł skaluje się poprawnie, gdy klient transformuje cały kontener. Nie gwarantują jednak zgodności w stanach, w których klient zmienia geometrię wewnętrzną zamiast samej skali.

## Kontrakt v1.0.12

1. Motyw nie ustawia wymiarów całego okna gry.
2. Motyw nie wymusza `100vw` ani `100vh`.
3. Natywny `.game-window-positioner`, `data-res` i `zoom-factor` pozostają źródłem rozmiaru.
4. Każdy HUD skaluje grafikę, tekst i pola interakcji jako jeden komponent.
5. Okna o różnych wymiarach używają skalowalnych ramek, a nie bitmap o sztywnej szerokości.
6. Stałe narożniki i zakończenia nie są deformowane; rozciąga się lub powtarza wyłącznie środek.
7. Reguły wariantowe są dodawane tylko dla natywnych stanów, które naprawdę zmieniają układ wewnętrzny.
8. Test obejmuje płynną zmianę rozmiaru oraz natywne stany rozdzielczości, zoomu, czatu, ekwipunku i interfejsu mobilnego.
9. Zewnętrzna rama okna jest jednym skalowalnym układem: górna i dolna belka kończą się na osiach pionowych boków, a narożniki nie zmieniają proporcji.
10. Duże okno Klanu jest obowiązkowym testem szerokiej i wysokiej ramy oraz połączenia jej z wewnętrznymi belkami treści.
