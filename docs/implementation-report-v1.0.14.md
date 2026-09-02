# Poprawki po testach v1.0.13 — wersja 1.0.14

## Dolny HUD i jakość

Przyczyną zasłonięcia procentów EXP i czasu wyczerpania było ustawienie grafiki tarczy na z-index 2 bez podniesienia natywnego kontenera liczników. Kontener `.bottom-panel-pointer-bg` oraz paski zasobów walki mają teraz warstwę 4, ponad ornamentem. Nie zmieniono wartości liczników ani ich obsługi. Oba liczniki są wyśrodkowane w osobnych polach 60 × 18 px nad bocznymi odcinkami EXP, poza obrysem tarczy razem z jej ornamentami.

Przywrócono dokładną kopię zatwierdzonego pliku `custom/buttony-elements/approved/bottom-panel-hp-shield-integrated-590x100.png` pod nowym adresem `v114/shield-restored.png`. Nie progowano ponownie jasności ani kanału alfa. Wcześniejsze `clear_shield()` usuwało także ciemne detale metalu, przez co kontury wyglądały na poszarpane. Nowa maska SVG wyznacza zewnętrzny obrys, otwór HP oraz oba tory EXP niezależnie od pikseli bitmapy. Pozostaje natywny rozmiar 590 × 100 i dotychczasowa logika procentów.

Dodatkowo obie części toru EXP spotykają się teraz w środku HUD-u pod tarczą. Otwory maski sięgają jej metalowych krawędzi, więc nie ma pustych odcinków przed i za tarczą. Liczniki nadal pokazują natywne wartości.

## Okna i kolory

- Wspólne komponenty stopek otrzymały ciemną stalową powierzchnię zamiast bordowej, wypukłej ornamentyki. Obejmuje to m.in. Umiejętności, Rzemiosło, Otchłań i Łupy korzystające z tych komponentów. Wymiary i kontrolki stopek pozostają natywne.
- Obramowanie SVG ma ciągły zewnętrzny i wewnętrzny kontur, wspólny dla boków oraz górnej i dolnej belki, także w krótkich komunikatach.
- Nadpisano oba warianty wspólnego `interface-element-green-box-background`. Zmieniają one panel informacji o klanie, rekrutację, skarbiec, zarządzanie, dyplomację i inne panele systemowe korzystające z tego samego komponentu.
- Pola formularzy klanu, aktywne zakładki oraz podświetlenie listy klanów korzystają z ciemnej stali, przygaszonego burgundu i starego złota. Nie zmieniano treści stron klanowych.
- Mały dialog NPC ma jedną ramkę i osobny grot. Usunięto nachodzące na siebie fragmenty jego obramowania; wysokość uwzględnia odpowiedzi pływające w prawo.

## Rozszerzenia widgetów

Tło ma ciągłą powierzchnię bez linii podcinającej ikony. Główna dolna belka i rozszerzenia używają zgodnych odcieni. Zmieniono również jasne puste pola edycji na ciemny burgund. Nie zmieniono natywnego display, width, height, transform ani położenia widgetów.

## Premium

Przygotowano od nowa atlas 20 kategorii, zachowując ich kolejność i natywne pozycje CSS. Nowy plik jest używany w wysokiej rozdzielczości, z rozmiarem tła 362 × 456 CSS px. Ikony mają gładkie krawędzie na jednolitym ciemnym tle kafelka; nie wycinano białej szachownicy progowaniem. Nie podmieniano właściwych sprite'ów przedmiotów w ekwipunku ani ofert sklepu.

Grafika: `assets-production/lupus.margonem.pl/img/gui/dwarven-forge/v114/premium-atlas.png`. Użyto wbudowanego imagegen. Pierwsza wygenerowana próba miała namalowaną szachownicę i została odrzucona. Prompty zapisano w `v1.0.14-image-prompts.md`.

## GIF-y — rozstrzygnięcie z kodu klienta

W publicznym `main.min.ne0iTNdg.js` klasa modułu Fuzji używa `updateResultItemSlot(t)`:

- start i czyszczenie gniazda wywołują wariant czerwony `frame-1`;
- po otrzymaniu `composePreview`, kompletu składników i cen klient sprawdza `composePreview.productId > 0`;
- wynik prawdziwy pozostawia czerwony `frame-1`;
- wynik fałszywy wybiera turkusowy `frame-2` i dodaje podpowiedź `preview-item-tip`.

To dwa stany tego samego miejsca: Rzemiosło → Fuzja → gniazdo wyniku. Nie znaleziono w tym pakiecie JS innych miejsc użycia klasy animowanej ramki. Wcześniejsze wersje robocze GIF-ów nie są kolejnymi animacjami do pokazania w innych oknach. Nie dodano sztucznie animacji do ekwipunku, depozytu ani sklepu. Drugi stan jest potwierdzony w kodzie, nie w zalogowanej sesji gry.

## Testy

Lokalny Chromium: pełny natywny szablon dolnego HUD-u, liczniki, sloty, HP i EXP 0/50/100%, warianty ram, obie klasy GIF-ów, atlas premium, zielony panel, formularz, hover listy klanów, stopka i dymek NPC. Kontrola geometrii przy szerokościach 800/1200/1920 i skalach 0,8/1/1,25; zachowanie natywnych rozmiarów widgetów i podmiany krzyża. Szczegóły: `v1.0.14-validation.json`.

Poprzedni test HUD-u pomijał licznik EXP i wyczerpania. Nowy test używa całego pobranego szablonu i nie pomija tych elementów. Nadal nie jest to test w zalogowanej grze. Otwarcie wszystkich okien i ich wariantów w grze pozostaje do potwierdzenia po aktualizacji. Nie zmieniono tła dodatku trybu okienkowego.
