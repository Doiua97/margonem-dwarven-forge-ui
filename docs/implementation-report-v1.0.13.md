# Poprawki po teście w grze — 1.0.13

## Zmiany

- Usunięto małą plakietkę, dekoracje i tło spod tytułów okien. Napis jest bezpośrednio na głównej belce.
- Ramę okna zastąpiono skalowalnym SVG z identycznym przekrojem górnej i dolnej belki, bez ozdobnych zakończeń pod tekstem. Natywne wymiary obramowania pozostają 32/20 px. Stopka opcjonalna nadal obsługuje swoje kontrolki.
- X zamknięcia jest wyśrodkowany geometrycznie, niezależnie od fontu i domyślnego paddingu przycisku.
- Górny HUD: nick, lokalizacja, współrzędne i świat otrzymały pozycje odpowiadające polom grafiki 342 × 65. Ikony walut i kwoty są wspólnie centrowane; przyciski + zajmują osobne miejsca, a podpowiedzi zachowują obszary aktywne.
- Usunięto prostokątne rozszerzenia widgetów, reguły wymuszające display/width/height oraz obserwator DOM. Natywny klient znów steruje widocznością, szerokością i układem pasków. Natywny kontur używa kolorowanego atlasu motywu.
- Usunięto dodatkową strzałkę, element `.df-click` i obsługę kliknięć motywu. Podmieniany jest obraz `/img/cross.gif` używany przez MapGoMark na autorski krzyż 32 × 32. Położenie kafelka, zanikanie i ruch pozostają po stronie klienta.
- Wymiana krzyża ma ograniczoną liczbę prób oczekiwania na klienta. Obraz jest wstępnie ładowany z CORS; błąd pobrania pozostawia natywny obraz, a błąd końcowej podmiany przywraca go.
- EXP: usunięto drugą ramkę nakładaną na kutą grafikę. Wypełnienie trafia do istniejących ramion grafiki motywu, zachowując natywne wartości procentowe.
- HP: maska obejmuje wnętrze większej tarczy. Wypełnienie jest pod metalowym obramowaniem, a druga mniejsza ramka szkła została wyłączona. Pusta część jest ciemna; na zewnątrz zachowano przezroczystość.

## Ustalenia z klienta

Sprawdzono publiczny `main.min.ne0iTNdg.js` oraz CSS `9ba6b5fe1722a`. MapGoMark rysuje obraz z ImgLoader na canvasie; zwykła reguła CSS nie podmieniała tego obrazu. Kod widgetów sam ustawia inline display i width rozszerzeń — nie należy tego zastępować obserwatorem motywu.

## Weryfikacja i ograniczenia

Test w lokalnym Chrome używa pobranych natywnych szablonów HTML, pełnego CSS klienta i rzeczywistej funkcji MapGoMark z podstawionym silnikiem testowym. Sprawdzono przezroczystość plakietki, środek przycisku zamknięcia, rozdzielenie przycisków i liczników, HP 0/50/100%, natywną geometrię rozszerzeń oraz skalowanie HUD przy szerokościach 800/1200/1920 i skalach 0,8/1/1,25. Podmiana krzyża zachowała ten sam obiekt obrazu oraz pojedyncze rysowanie w natywnych współrzędnych.

To nie jest test zalogowanej sesji gry. Kolejny test w grze powinien objąć edycję i usuwanie widgetów po obu stronach, długie nazwy map/nicki, okna ze stopką, różne HP/EXP oraz skalowanie dodatkiem trybu okienkowego. Nie zmieniano tła poza ekranem gry.

Po aktualizacji userscriptu należy przeładować całą kartę. Samo podmienienie CSS nie usunie listenera kliknięć uruchomionego przez poprzednią wersję.
