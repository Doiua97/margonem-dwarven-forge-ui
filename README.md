# Corner Forge 0.5.0

Motyw CSS nowego interfejsu Margonem: ciemne żelazo, miedziane krawędzie i jasne napisy. Zmienia oprawę istniejących elementów. Dane serwera, treść komunikatów, przedmioty, ikony funkcji i logika klienta pozostają natywne. Nie dodaje avatara, funkcji ani nowych pasków.

## Instalacja i jeden punkt wejścia

Zainstaluj lub zaktualizuj [userscript](install/dwarven-forge.user.js), wyłącz inne loadery motywu i odśwież grę. Wersja loadera oraz klucze cache CSS i grafik: **0.5.0**.

- [css/dwarven-forge.css](css/dwarven-forge.css) — jedyny produkcyjny CSS; edytowany w miejscu, bez importów i generowanego bundla.
- [install/dwarven-forge.user.js](install/dwarven-forge.user.js) — jedyny JS: dodaje odnośnik do CSS. Nie przenosi ani nie kopiuje elementów gry, nie czyta danych konta, nie wywołuje API klienta.
- [assets/](assets/) — jeden płaski katalog, 11 grafik. Każda ścieżka występuje raz w zmiennych CSS; komponenty współdzielą te zmienne.
- [docs/asset-manifest.csv](docs/asset-manifest.csv) — spis grafik produkcyjnych, sumy SHA-256 oraz decyzje dla wszystkich 108 zewnętrznych URL i 13 osadzonych SVG z badanego oryginalnego CSS.

Usunięto historyczne pliki v03, osobne moduły CSS, bundle oraz dawne katalogi assets/gui i assets/ui. Stare odnośniki do tych plików przestają działać — należy używać powyższego loadera. Historia pozostaje w Git, bez kopii w bieżącym drzewie.

## Kontrakty komponentów

| Element | Zachowany kontrakt klienta | Oprawa Corner Forge |
|---|---|---|
| HUD | 342×65, te same hero-data/map-data/waluty/profesja i pola tekstowe | Nowa powierzchnia z otworami odsłaniającymi dwie ikony walut osadzone w oryginalnym sprite. Dekoracja nie przechwytuje kliknięć |
| Dolny panel | Kontener 664×82, te same dzieci i identyfikatory | HP/EXP nad slotami, panel nad sześcioma grupami widgetów |
| HP | blood z bar-horizontal=false; klient nadal ustala wysokość i ostrzeżenie niskiego HP | Obrót pionowego wskaźnika 16×144 do 144×16; tekst obrócony przeciwnie. Brak nadpisania wysokości blood |
| EXP | Dwie części left/right z bar-horizontal=true; szerokość inner sterowana przez klienta | Dwie sąsiadujące połówki po 72 px. Zachowane noexp/end-game oraz rzeczywiste pointer-exp/pointer-ttl |
| Walka | Natywne show/hide battle-bars-wrapper, osobne ukrywanie EXP | Tylko skórka i położenie. Brak display/visibility/opacity w regułach tych pasków; brak wymyślonych klas body.battle |
| Sloty | Osiem usable-slot, data-slot-index 1–8, osobne natywne skill-usable-slots | Dwie grupy po cztery pod HP/EXP; bez zmiany itemów, cooldownów i sterowania |
| Widgety | Sześć main-buttons-container, po siedem natywnych pozycji edytora; rozmiary 32/36/44 i offsety klienta | Układ 3×2 pod slotami. Zmiana położenia rodziców, bez przenoszenia dzieci w DOM. Zachowane static-widget-position, empty-slot-widget i widget-edit-mode |
| Prawa kolumna | right-column > inner-wrapper > right-main-column-wrapper z character_wrapper + battle-set-wrapper + inventory_wrapper | Tła i rezerwa miejsca nad dokiem; bez zmiany struktury i geometrii dzieci |
| Equipment | 104×138 w classic, wszystkie natywne pozycje slotów | Wyłącznie podkład i obrys wrappera; sprite wyposażenia oraz ramki przedmiotów pozostają natywne |
| Stats | Istniejący przycisk Rozwiń/Zwiń | Tło i skórka tego samego przycisku |
| Extended stats | Natywne .active i right:100%, szerokość 225; wysuwanie w lewo | Powierzchnia, tekst i scrollbar; bez własnego sterowania widocznością |
| Inventory | Siatka 232×198 = 7×6; inner-grid 231×197, natywne przewijanie i stany toreb | Podkład wrappera; siatka, rarity i item frames nietknięte |
| Torby | Cztery rzeczywiste .item.bag po 35×35, tworzone przez klienta w bags-navigation | Oryginalne grafiki toreb i aktywny stan, bez numerów. Pozostają nad siatką; tutorial-bag jest osobną natywną warstwą instruktażu |
| Czat | new-chat-window i chat-input-wrapper, natywne kanały, edycja i kolory wiadomości | Powierzchnie i obramowania; bez starych selektorów chat-tpl |
| Okna i dodatki | Oryginalne komponenty border-window, middle-1/2/3/4, header/card i scroll | Współdzielone grafiki, zachowane border-image-slice i border-width. Podmiana zarówno tła, jak i starego border-image; nie tylko zewnętrznej ramy |
| Minimap i małe moduły | Osobne otwierane okna i ich zdarzenia | Skórka istniejących komponentów, bez stałego panelu minimapy w HUD |

Przesunięcie panelu nie zmienia miejsca docelowego aktualizacji z backendu: nie powstają kopie pól ani napisy wpisane w grafikę. CSS zmienia pozycję tych samych elementów, do których klient wpisuje wartości. Ochronę przepływu danych potwierdzono w źródłach; pełny test aktualizacji podczas gry nadal wymaga zalogowanej sesji.

## Grafiki i czytelność okien

Pięć własnych SVG to wyłącznie powierzchnie: forge-surface, forge-middle, forge-window, forge-header i forge-hud. Nie zawierają tekstu, avatara, ikon ani danych gracza. Księga i pięć krawędzi dymków są pojedynczymi lokalnymi kopiami oryginalnych grafik; CSS przyciemnia tylko ich warstwę tła i dobiera kolory tekstu. Pochodzenie i sumy kontrolne znajdują się w manifeście. Oryginalne grafiki Margonem należą do ich właścicieli.

Wspólne komponenty skórkują m.in. dodatki, ustawienia, pocztę, klan, aukcje, questy, sklep, depo, umiejętności, świat, pomoc, znajomych, loot, crafting, premium, statystyki, minimapę i mniejsze moduły korzystające z tych samych warstw. Dodatkowe reguły obejmują nagłówki, karty, pola aukcji, istniejące paski postępu, przewijanie, księgi i dymki. Przyciski są objęte listą konkretnych modułów; podmieniana jest ich powierzchnia, nie sprite ikon. Nie ma globalnego podmieniania obrazka wszystkich .button lub .widget-button.

Usunięto wykryte czarne lub słabo widoczne napisy na zmienionych powierzchniach dodatków, poczty, handlu, umiejętności, pomocy, dzielenia łupów i innych wskazanych modułów. Akceptacja/odmowa nadal mają znaczenie zielone/czerwone. Nie nadpisujemy rarity ani treści/kolorów wiadomości czatu. Mieszane sprite’y zawierające funkcjonalne ikony, treści wydarzeń, oferty i oznaczenia stanu pozostają po stronie klienta; neutralne, wydzielone powierzchnie dostają skórkę. Spis odwołań z CSS nie jest spisem wszystkich obrazów pobieranych dynamicznie z backendu.

## Responsywność

Pełny układ Corner Forge dotyczy **desktop classic-interface**. Rozmiar widgetów wynika z body[data-res]: 32 px dla 920×555/1173×555, 36 px dla 1024×768 i 44 px domyślnie. Natywne chat-size-0/1/2 oraz eq-column-size-0/1 nadal odpowiadają za szerokość i widoczność kolumn. Nie nadpisujemy zoomu klienta.

Light/mobile zachowują natywną orientację, układ oraz hamburgery i otrzymują wspólne skórki. Nie wymuszamy w nich desktopowego doku: klient używa innej geometrii przeciągania. Przy wysokości poniżej natywnych 555 px oraz szerokości poniżej 940 px przy domyślnych widgetach 44 px nie gwarantujemy braku kolizji. Preset 920×555 używa mniejszych przycisków i został sprawdzony.

## Weryfikacja wydania

Wykonano analizę składni CSS, kontrolę istniejących klas, ścieżek i cache, porównanie zmian Git oraz kontrolę zakazanych nadpisań. Sprawdzono **147 reguł CSS**: brak ingerencji w warstwy item/rarity/icon, brak fałszywych stanów walki, brak sterowania wysokością blood lub szerokością exp inner, brak zmiany wewnętrznej geometrii wyposażenia/siatki i brak JS poza loaderem.

W przeglądarce użyto oryginalnego CSS i lokalnego DOM z natywnych template’ów; nie uruchamiano całej gry. Sprawdzono 12 scenariuszy classic oraz osobny wariant light: 920×555, 1024×768, 1366×768, 1920×1080, HP 0/25/50/100%, połówki EXP, natywne stany walki, rozwiniętych statystyk, edytora oraz kolumn. Pomiar potwierdził wyposażenie 104×138, siatkę 232×198, cztery węzły toreb 35×35, osiem niekolidujących slotów i dostępność wszystkich 42 możliwych pozycji widgetów. To pozycje testowe, nie dodane funkcje. Osobno obejrzano okno dodatków i sprawdzono tła middle-2/middle-3 oraz kolory tekstu.

**Nie wykonano testu w zalogowanym kliencie.** Lista do sprawdzenia w grze:

- [ ] Aktualizacja nicku, poziomu, mapy, walut, HP/EXP i statystyk po zdarzeniach z serwera; długie wartości i tooltipy trafiają do istniejących pól.
- [ ] Leczenie, niski HP, noexp/end-game; wejście/wyjście z walki, mana/energia właściwe dla profesji i powrót EXP.
- [ ] Skróty 1–8, użycie przedmiotów/skilli, cooldown, disable-slots, drag/drop wyposażenia i toreb, battle-set, natywne rarity.
- [ ] Sześć grup widgetów: włączanie dodatkowych grup, edycja pustych pozycji, przeciąganie między grupami, zapis i powrót ustawień po odświeżeniu.
- [ ] Rozwiń/Zwiń i przewijanie extended-stats do końca; chat-size/eq-column-size, kanały, menu czatu, zoom i wszystkie używane rozdzielczości.
- [ ] Każde używane okno i wbudowany dodatek z rzeczywistą treścią: opisy, listy, inputy, zaznaczenia, scroll, otwieranie/zamykanie i przeciąganie. Osobno księga, dymki, minimapa, kalendarze i premium.
- [ ] Ustawienia przezroczystości transparent/data-opacity-lvl oraz light/mobile — zachowanie natywnych hamburgerów i układu.

## Źródła audytu

Podglądowy motyw jest źródłem techniki komponentowej podmiany i border-image, nie źródłem docelowego layoutu. Aktualny klient min został odczytany z istniejącego w repo [archiwum źródłowego](docs/main.min.53XkBRxF.zip); starszy main.js służył do porównania. Oryginalnych CSS i JS nie dodano jako kolejnych produkcyjnych kopii.

| Plik | Rozmiar | SHA-256 |
|---|---:|---|
| style.Bjtb6ElF.css | 810692 B | 67bc9624cfe650a2fdae964244678f9b835f4444df9f7d0052ae8d226d1059bc |
| podglądowy.css | 43296 B | 305eaf148461037f51b91b034f8c9aa666ed6893fba25c70b20d8e78f19e9eb7 |
| main.min.53XkBRxF.js | 3019667 B | 16590fc1a50bba4a71cbe69c115acdffe53671dafaff830e8e954dc145c1648e |
| main.js | 5367803 B | 21006e04645e8955eb24f3498b613449e38961e22274c82db386b952a328c60a |
