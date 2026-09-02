# Plan zmian motywu — v1.0.12

Data: 2026-09-02

Dokument opisuje zmiany planowane po teście v1.0.11 w działającym kliencie. Zakres wynika z zaakceptowanych propozycji i audytu zrzutów użytkownika.

## Główna zasada wdrożenia

Zmiany będą wprowadzane na poziomie wspólnego typu komponentu. Jeżeli wiele okien używa tej samej klasy ramy, tytułu, przycisku, kratki lub dymku, otrzymają jedną wspólną implementację. Nie będą tworzone pojedyncze wyjątki dla Umiejętności, Rzemiosła, Dziennika zadań albo Depozytu, chyba że klient rzeczywiście używa innej struktury DOM.

## Zakres v1.0.12

### 1. Wspólny nagłówek okien

Zmiana obejmie kompletną zewnętrzną ramę `.border-window`, a nie tylko kolor tekstu lub plakietkę tytułu. Górna belka, dolna belka, pionowe boki, narożniki, nazwa i strefa zamknięcia będą jednym systemem graficznym.

Zmiany:

- przebudowanie ramy jako układu dziewięciu części: cztery stałe narożniki, dwa pionowe boki, górny i dolny skalowalny środek oraz powierzchnia treści;
- wspólne punkty łączenia górnej i dolnej belki z pionowymi bokami;
- usunięcie podwójnych linii, przerw, uskoków oraz końcówek niewyrównanych do boków okna;
- zachowanie nierozciąganych narożników i ornamentów;
- powtarzanie albo kontrolowane rozciąganie wyłącznie prostych środkowych odcinków;
- zakończenie górnej i dolnej belki dokładnie na osiach pionowych boków niezależnie od rozmiaru okna;
- oddzielenie zewnętrznej dolnej ramy od funkcjonalnej belki wewnętrznej danego okna, aby nie powstawały dwie konkurujące krawędzie;
- własne lewe i prawe zakończenie nagłówka oraz skalowalny środek;
- usunięcie oryginalnych dekoracji z `dialogue/dialogi.png`;
- usunięcie osobnego tła i wielowarstwowego cienia spod nazwy okna;
- osadzenie nazwy bezpośrednio w belce, z centrowaniem flex w pionie i poziomie;
- jednakowa wysokość oraz pozycja tytułu we wszystkich oknach typu `.border-window`;
- obsługa długich nazw przez kontrolowane skracanie tekstu, bez zmiany geometrii ramy;
- wspólne warianty dla zwykłych okien, `fixed-wnd`, `transparent` i wersji mobilnej.

Zmiana obejmie między innymi: Świat, Rzemiosło, Umiejętności, Dziennik zadań, Społeczność, Depozyt, Klany oraz pozostałe okna korzystające z tego komponentu.

Duże okno Klanu będzie jednym z obowiązkowych testów ramy, ponieważ pokazuje jednocześnie długie pionowe boki, szeroką górną i dolną belkę, wewnętrzną nawigację oraz strefę `X`.

### 2. Stała strefa przycisku zamknięcia

Aktualny przycisk ma dekorację 51 × 52 px i korzysta z `right:-20px`, przez co raz wystaje poza ramę, a innym razem nagłówek wchodzi pod przycisk.

Zmiany:

- wydzielenie po prawej stałej strefy zamknięcia;
- zakotwiczenie `X` w środku tej strefy;
- zakończenie skalowalnej części nagłówka przed strefą `X`;
- usunięcie zależności położenia przycisku od długości tytułu;
- zachowanie braku przycisku w rzeczywistych oknach `no-exit-button`;
- osobna, zgodna geometria dla okien `transparent`.

### 3. Małe dialogi nad NPC

Mały biały dialog ze zrzutu to `.bubbledialog`, a nie wcześniej stylizowany `.dialogue-window`.

Zmiany:

- autorski skalowalny zestaw górnej, dolnej i bocznych ramek;
- ciemne tło treści zgodne z motywem zamiast `#f2f2f2`;
- wspólna typografia i kolory odpowiedzi;
- zachowanie grotu wskazującego NPC;
- obsługa prawego i lewego wariantu dymku;
- pozostawienie dużego `.dialogue-window` jako odrębnego komponentu.

### 4. Dodatkowa dolna belka widgetów

Obecna reguła CSS rozpoznaje również pozostawione po edycji, niewidoczne elementy. Dlatego belka nie wraca do naturalnego rozmiaru.

Zmiany:

- obserwowanie zmian widgetów przez `MutationObserver` w userskrypcie;
- liczenie tylko faktycznie widocznych i przypisanych widgetów;
- wykluczenie pustych pól, placeholderów i elementów przeciąganych;
- natychmiastowe usuwanie rozszerzenia po zapisaniu pustej sekcji;
- przywracanie dokładnie bazowego wariantu pokazanego na zrzucie bez pozostałości po edycji;
- obliczanie szerokości rozszerzenia z faktycznej zawartości;
- zastąpienie stałej dużej grafiki zakończeniami i powtarzalnym środkiem;
- osobny wariant połączenia z otwartą kolumną czatu, aby belka nie zlewała się z jego dolną ramą;
- zachowanie natywnych ikon widgetów i zmiana wyłącznie ich tła zgodnie z motywem.

### 5. Górny HUD

Wszystkie pola zostaną powiązane z jednym układem lokalnym HUD-u 342 × 65 px.

Zmiany:

- dokładne wycentrowanie nicku w jego górnym polu;
- wspólne pionowe i poziome centrowanie lokacji, współrzędnych oraz nazwy świata;
- usunięcie niezależnych korekt, które rozjeżdżają się przy zmianie skali;
- skalowanie całego HUD-u razem z jego napisami i ikonami;
- przeniesienie ikon złota i smoczej łuski do kontenerów odpowiadających wartości;
- ustawienie ikon bezpośrednio przy liczbach z odstępem 2–3 px;
- pozostawienie pól interakcji walut jako osobnych, przezroczystych obszarów;
- zachowanie i prawidłowe osadzenie wskaźnika rodzaju mapy.

### 6. Dolny HUD — tarcza życia

Obecna grafika ma poprawną przezroczystość poza ornamentem, lecz wewnątrz sylwetki zapisano duże czarne wypełnienie widoczne wokół czerwonego zbiornika życia.

Zmiany:

- rozdzielenie metalowej ramy, wnętrza tarczy, szkła i krwi;
- usunięcie nieprzezroczystej czarnej plamy z grafiki bazowej;
- pozostawienie krycia tylko w obszarze metalu i świadomie zaprojektowanego wnętrza;
- zastosowanie grafitowo-bordowej tekstury lub kontrolowanej przezroczystości wewnątrz tarczy;
- zachowanie dynamicznego poziomu życia i czytelności wartości procentowej;
- ponowne wycentrowanie całego zespołu względem dolnego HUD-u.

### 7. Autorski pasek doświadczenia

Zaakceptowano nowy kierunek bez oryginalnych prostokątnych segmentów.

Zmiany:

- ciągłe pole postępu;
- cienka grafitowo-stalowa prowadnica;
- dyskretna krawędź w kolorze starego złota;
- bordowo-złote wypełnienie sterowane przez aktualny procent doświadczenia;
- lustrzane lewe i prawe zakończenie;
- przezroczysty środek grafiki ramy, przez który widoczne jest dynamiczne wypełnienie;
- dopasowanie obu stron do nowej tarczy bez czarnego pola;
- autorskie warianty końca gry `ribbon`, `ribbon-up` i `ribbon-down`;
- usunięcie zależności wizualnej od przekolorowanych regionów oryginalnego `buttony.png`.

Zaakceptowany podgląd: `previews/audit-v111/proposed-authored-exp-bar-preview.png`.

### 8. Dolny HUD — wskaźnik opóźnienia `ms`

Obecny `.lagmeter` nadal używa niezmienionych klatek oryginalnego `buttony.png`.

Zmiany:

- własne małe, zagłębione pole zgodne z pozostałymi odczytami HUD-u;
- centrowanie wartości i jednostki `ms`;
- wspólna czcionka motywu;
- zachowanie funkcjonalnych kolorów sygnalizujących jakość połączenia;
- dopasowanie położenia do prowadnicy EXP i tarczy.

### 9. Dolny HUD — wspólna geometria

Zmiany:

- jeden centralny kontener dla tarczy, pasków EXP, slotów i odczytów;
- wspólne zmienne wymiarów zamiast niezależnych marginesów;
- usunięcie czarnych lub nieprzezroczystych teł z kontenerów, które nie powinny ich rysować;
- wyrównanie bocznych slotów względem osi tarczy;
- sprawdzenie kompozycji na jasnych i ciemnych mapach.

### 10. Wspólna kratka przedmiotu

Zaakceptowano wariant z cienkim rantem i maksymalną powierzchnią ikony.

Zmiany:

- obramowanie ograniczone do 1–2 px;
- brak dużych narożników, nitów i dekoracji konkurujących z przedmiotem;
- niemal całe pole 33 × 33 px przeznaczone dla grafiki przedmiotu;
- tylko subtelny cień oddzielający ikonę od tła;
- jeden wzorzec źródłowy dla wszystkich wariantów technicznych;
- wygenerowanie nowego `oneItemSlotToRepeat.png`;
- podmiana odpowiednich regionów `buttony.png`;
- przygotowanie zgodnego `item-slot.png` oraz dekoracyjnych wariantów slotów;
- przygotowanie większego wariantu pola akcji używanego przez `.enhance__item` i `.interface-element-one-item-slot-decor`, o tej samej stylistyce i równie cienkim rancie;
- zastosowanie w ekwipunku, obu torbach, sklepie, depozycie, handlu, nagrodach i pozostałych wspólnych siatkach;
- sprawdzenie obramowań jakości, liczb przedmiotów, blokady, zaznaczenia i animowanych nakładek.

Zaakceptowany podgląd: `previews/audit-v111/proposed-thin-rim-item-slot-preview.png`.

### 10a. Pasek ulepszania w Rzemiośle

Pasek pomiędzy dwoma górnymi polami przedmiotów ma własny komponent `.enhance__progressbar` o wymiarach 138 × 16 px. Jego rama nadal pochodzi z regionu `progressbary.png` na pozycji `0 -104px`, a aktualny i przewidywany postęp używają prostych zielonych kolorów CSS.

Zmiany:

- zastąpienie oryginalnego regionu dedykowaną autorską miniaturową prowadnicą;
- wspólna stylistyka z zaakceptowanym paskiem EXP: grafitowa stal i dyskretne stare złoto;
- zachowanie funkcjonalnego zielonego koloru bieżącego ulepszenia oraz jaśniejszego podglądu;
- przezroczysty środek ramy, aby szerokość postępu nadal była sterowana przez grę;
- dopasowanie zakończeń prowadnicy do większych pól przedmiotów;
- brak podmiany całego `progressbary.png`, ponieważ inne jego regiony obsługują grupę, czas walki, zadania klanowe i matchmaking.

### 11. Autorski znacznik kliknięcia na mapie

Zmiany:

- zidentyfikowanie w działającym kliencie warstwy rysującej obecny czerwony krzyż;
- przygotowanie autorskiego znacznika ruchu/dojścia;
- przygotowanie bordowego wariantu celu niedostępnego lub anulowanego;
- opcjonalny krótki stan aktywny bez trwałego zasłaniania mapy;
- przezroczyste tło i stylistyka stalowo-runiczna;
- wdrożenie przez CSS, jeżeli znacznik jest elementem DOM, albo przez userskrypt, jeżeli rysuje go canvas/silnik.

### 12. Jedna czcionka motywu

Punkt został już wprowadzony w v1.0.11 i będzie w v1.0.12 przede wszystkim weryfikowany. Obecnie `--df-font` oraz reguła z `!important` obejmują całe `.game-window-positioner`, alerty, konsolę, komunikaty systemowe i tooltipy.

Kontrola i uzupełnienia:

- jedna zmienna `--df-font-family` na korzeniu interfejsu;
- potwierdzenie objęcia nagłówków, HUD-ów, przycisków, formularzy, menu kontekstowych, dialogów i paneli dodatków;
- jawne objęcie `.bubbledialog` i elementów tworzonych bezpośrednio pod `body`, jeżeli znajdują się poza `.game-window-positioner`;
- kontrola paneli dodatków, które tworzą własny korzeń DOM;
- usunięcie lokalnych deklaracji powodujących różnice między oknami;
- zachowanie wyjątku tylko wtedy, gdy symbol lub liczba wymaga technicznie innego kroju;
- niewymuszanie czcionki wewnątrz zewnętrznych iframe i tekstu canvas, których CSS dokumentu gry nie może bezpiecznie zmienić.

### 12a. Natywne skalowanie w każdej rozdzielczości

Motyw ma skalować się razem z natywnym oknem całej gry i korzystać z tych samych stanów responsywnych co oryginalny interfejs. Nie będzie tworzył niezależnego systemu rozdzielczości.

Audyt v1.0.11 wykazał, że bazowy klient zawiera setki reguł `data-res`, `zoom-factor` i `mobile-version`, natomiast ostatnia warstwa geometrii motywu nie zawiera własnych wariantów tych stanów. Górny i dolny HUD używają stałych współrzędnych pikselowych. Działa to tylko w sytuacji, gdy klient skaluje cały kontener; może zawieść, gdy natywny CSS zmienia układ wewnętrzny.

Zmiany:

- zachowanie natywnych wymiarów i pozycjonowania `.game-window-positioner`;
- brak reguł wymuszających `100vw`, `100vh` lub własny rozmiar całego okna gry;
- skalowanie grafiki i dzieci przez ten sam natywny kontener oraz ten sam `zoom-factor`;
- brak niezależnego skalowania tekstu względem grafiki HUD-u;
- ograniczenie nadpisań geometrii do zmiennych lokalnych komponentu;
- powiązanie górnego HUD-u z jednym układem 342 × 65 px, który skaluje się jako całość;
- powiązanie dolnego HUD-u z jednym kontenerem bazowym, który skaluje tarczę, EXP, sloty i wskaźniki razem;
- użycie `border-image`, stałych zakończeń i powtarzalnych lub rozciągliwych środków w oknach o zmiennej szerokości i wysokości;
- unikanie bitmap rozciąganych w całości, jeżeli deformują narożniki albo ornamenty;
- respektowanie natywnych wariantów `mobile-version`, `light-interface`, `data-res`, `zoom-factor`, rozmiaru czatu i rozmiaru kolumny ekwipunku;
- dodanie wariantów zmiennych tylko tam, gdzie natywny klient rzeczywiście zmienia geometrię wewnętrzną;
- niezmienianie rozmiaru treści okien takich jak Rzemiosło, Umiejętności czy Dziennik zadań — motyw ma wyłącznie dopasować do ich aktualnego rozmiaru ramę, nagłówek i tło.

Kontrola obejmie płynne zmniejszanie i zwiększanie okna gry oraz wszystkie natywne klasy rozdzielczości dostępne w CSS klienta. Element zostanie uznany za poprawny tylko wtedy, gdy tekst, grafika, strefa `X` i pola interakcji skalują się razem.

### 13. Animowane ramki przedmiotów

Nie będą dodawane nowe GIF-y do pustych pól. Istniejące dwie autorskie animacje zostaną zweryfikowane jako wspólna warstwa przedmiotu:

- `item-slot-anim-frame1.gif` — 54 × 54 px, 32 klatki;
- `item-slot-anim-frame2.gif` — 54 × 54 px, 32 klatki.

Test obejmie ten sam przedmiot lub stan jakości w Rzemiośle, ekwipunku, depozycie, handlu i sklepie. Jeśli klient nadaje klasę animacji, zostaną poprawione `z-index`, przycięcie i rozmiar. Jeśli klasy nie ma, motyw nie będzie sztucznie wymuszał GIF-u bez uzasadnienia funkcjonalnego.

Userskrypt diagnostyczny zapisze dla każdego wykrytego elementu dokładną klasę wariantu, najbliższe okno i faktyczną widoczność. Obecnie potwierdzono tylko jedno wystąpienie w Rzemiośle; nie wolno raportować pozostałych miejsc jako wdrożonych bez wyniku pomiaru runtime. Wcześniej prezentowane wersje `structural`, v3 i v4 były rewizjami projektu. W produkcji znajdują się wyłącznie dwa finalne GIF-y v4.

Funkcjonalne animacje `away.gif` i `buffs.gif` nie będą podmieniane przez motyw. Ich override zostanie usunięty, aby klient używał oryginalnych zasobów.

### 13a. Wdrożenie zestawu `progressBar` w widocznych miejscach

Cztery grafiki 139 × 14 px z katalogu `img/gui/progressBar` są obecnie podpięte do `.progress-bar-wrapper`, ale jedyny konkretny kontekst ich użycia znajduje się w domyślnie ukrytym `.battle-controller .battle-content .stats-wrapper`. Samo umieszczenie ich w paczce i ukrytym komponencie nie jest uznawane za wdrożenie.

W v1.0.12 zostaną użyte zgodnie ze znaczeniem funkcjonalnym:

- `progress-bar.png` jako wspólna rama i tło pasków zasobów;
- `percent-red.png` dla życia;
- `percent-blue.png` dla many;
- `percent-yellow.png` dla energii.

Zakres obejmie widoczne paski zasobów w panelach walki i grupy, jeżeli ich rozmiar pozwala zachować czytelność wzoru. Dla pasków 2–4 px nad wojownikami zostaną wygenerowane cienkie warianty pochodne z tego samego wzorca. Pliki 139 × 14 px nie będą mechanicznie ściskane, ponieważ zniszczyłoby to rant i czytelność koloru.

Zestaw nie będzie używany do:

- zaakceptowanego paska EXP w dolnym HUD-zie;
- zielonego postępu ulepszania w Rzemiośle;
- czasu walki, postępu zadania lub matchmakingu, jeżeli semantycznie wymagają własnego wariantu.

Diagnostyka runtime nadal sprawdzi ukryty `.battle-controller .stats-wrapper`. Jeżeli klient posiada osiągalny stan wyświetlający ten panel, zachowa on natywne wymiary 139 × 14 px i będzie głównym miejscem użycia czterech plików.

### 14. Elementy pozostawiane w oryginale

Zgodnie z wcześniejszą decyzją motyw nie będzie podmieniał:

- grafik postaci i NPC;
- grafik wyświetlanych po najechaniu na NPC;
- grafik postaci i przeciwników w walce;
- funkcjonalnych znaczników NPC i usług;
- natywnych ikon widgetów dodatków.

Motyw może zmieniać tło kontenera widgetu, ale nie jego ikonę.

## Kolejność wykonania

1. Wspólny nagłówek, nazwa okna i strefa `X`.
2. Mały `.bubbledialog`.
3. Stan dodatkowej belki widgetów oraz połączenie z czatem.
4. Górny HUD i waluty.
5. Tarcza życia bez czarnego pola.
6. Autorski pasek EXP, warianty końca gry i wskaźnik `ms`.
7. Wspólna geometria dolnego HUD-u.
8. Zaakceptowana kratka przedmiotu, wszystkie jej warianty oraz pasek ulepszania Rzemiosła.
9. Wdrożenie czerwonych, niebieskich i żółtych pasków zasobów w widocznych komponentach.
10. Znacznik kliknięcia.
11. Weryfikacja czcionki, wdrożenie kontraktu natywnego skalowania i końcowy audyt selektorów.
12. Testy w podglądach lokalnych, budowa paczki i test w grze.

## Testy wymagane przed publikacją

### Rozdzielczości

- 1200 × 675;
- 1600 × 900;
- 1920 × 1080.
- płynna zmiana rozmiaru pomiędzy obsługiwanym minimum i maksimum;
- natywne stany `data-res` obecne w CSS klienta;
- natywne poziomy `zoom-factor`;
- tryb zwykły, `light-interface` i `mobile-version`, jeżeli jest dostępny dla danego układu.

### Okna

- Świat;
- Rzemiosło;
- Umiejętności;
- Dziennik zadań;
- Społeczność;
- Depozyt;
- Klany, w tym szerokie okno strony oficjalnej;
- okna z długą nazwą;
- okna `fixed-wnd`, `transparent` i `no-exit-button`.

### Widgety i czat

- czat zamknięty i otwarty;
- brak widgetów;
- widgety po lewej, prawej i po obu stronach;
- tryb edycji;
- zapis po usunięciu wszystkich widgetów;
- ponowne otwarcie klienta po zapisaniu układu.

### HUD-y

- krótki i długi nick;
- krótkie i długie wartości złota oraz smoczej łuski;
- różne rodzaje mapy;
- kilka wartości doświadczenia i życia;
- kilka poziomów opóźnienia;
- jasne i ciemne mapy.

### Kratki i animacje

- pola puste i zajęte;
- wszystkie jakości przedmiotów;
- liczba przedmiotów;
- blokada i zaznaczenie;
- obie animowane ramki;
- ekwipunek, torby, sklep, depozyt, handel, nagrody i Rzemiosło.

### Dialogi i kliknięcie

- duży `.dialogue-window`;
- mały `.bubbledialog` z grotem po lewej i prawej;
- ruch możliwy;
- cel niedostępny lub anulowany;
- kilka szybkich kolejnych kliknięć.

## Kryterium publikacji

Wersja v1.0.12 będzie gotowa do publikacji dopiero wtedy, gdy:

- wspólne komponenty nie wymagają wyjątków dla pojedynczych wymienionych okien;
- górna belka, dolna belka, pionowe boki i narożniki tworzą jedną ciągłą ramę bez przerw, podwójnych linii i uskoków;
- dolna rama zewnętrzna nie koliduje z funkcjonalną belką wewnętrzną okna;
- motyw nie zmienia natywnego rozmiaru całego okna gry i skaluje się razem z jego kontenerem w każdym obsługiwanym stanie rozdzielczości;
- grafika, tekst oraz pola interakcji HUD-ów zachowują wspólną skalę i pozycję;
- przycisk `X` nie zmienia położenia i nie koliduje z nagłówkiem;
- pusta dodatkowa belka zawsze wraca do naturalnego rozmiaru;
- tarcza nie rysuje czarnej plamy;
- pasek EXP i kratki korzystają z zaakceptowanych autorskich wzorców;
- funkcjonalne grafiki NPC i walki pozostają oryginalne;
- paczka przechodzi test wymiarów, kanału alfa, brakujących zasobów i selektorów CSS.

## Zakres odłożony

Tło dodatku „Tryb okienkowy” poza obszarem gry pozostaje poza v1.0.12. Wymaga osobnego testu warstwy dodatku, kolejności arkuszy i `z-index` w działającym kliencie.
