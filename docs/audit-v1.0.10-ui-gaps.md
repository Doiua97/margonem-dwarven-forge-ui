# Audyt braków interfejsu po v1.0.10

Data audytu: 2026-09-02

Zakres: wspólne ramy i nagłówki okien, separatory, widgety, przyciski, górny i dolny HUD, dolne rozszerzenia interfejsu oraz zgodność z dodatkiem „Tryb okienkowy”. Audyt dotyczy całych rodzin komponentów, a nie pojedynczych okien ze screenów.

## Najważniejszy wniosek

Motyw nadal miesza trzy różne systemy wizualne: nową stalową ramę, oryginalne drewniane elementy klienta oraz własne bordowe belki. Problem trzeba usunąć na poziomie współdzielonych komponentów i stanów. Poprawianie osobno okna umiejętności, dziennika zadań czy rzemiosła tylko powieli wyjątki.

## P0 — błędy konstrukcyjne

### 1. Drewniane pionowe podziały nadal są wspólnym zasobem klienta

Źródłem widocznych drewnianych kolumn jest wspólny `middle_graphics.png`, używany przez:

- `.interface-element-vertical-wood`,
- `.interface-element-middle-1-background` do `.interface-element-middle-4-background`,
- warianty `*-background-stretch`.

Te komponenty występują między innymi w umiejętnościach, dzienniku zadań, rzemiośle, depozycie, liście znajomych, łupach, odzyskiwaniu przedmiotów, sklepach i części okien dodatków. Obecny plik produkcyjny jest oznaczony jako własny, ale wizualnie nadal przedstawia drewno.

**Do poprawy:** przygotować jeden skalowalny zestaw stalowych separatorów dla wszystkich klas `interface-element-middle-*` i `interface-element-vertical-wood`. Zachować ich oryginalne wymiary, wycinki i zachowanie `border-image`, aby różne wysokości okien nadal skalowały się według CSS klienta.

### 2. Belki pod czatem są widoczne w nieprawidłowym stanie

Duży skośny element pod czatem pochodzi z:

- `.bg-additional-widget-left`,
- `.bg-additional-widget-right`.

Oryginalny komponent ma rozmiar `437 × 109 px`. Samo przemalowanie jego wycinka nie rozwiązuje problemu. Na screenie lewa belka jest wyświetlana mimo braku faktycznie rozwiniętego dodatkowego rzędu widgetów i tworzy klin wchodzący pod czat.

**Do poprawy:** domyślnie ukryć oba rozszerzenia i pokazywać właściwą stronę wyłącznie w stanie DOM odpowiadającym dodatkowemu rzędowi widgetów. Wysokość, warstwę i kolor rozszerzenia powiązać z dolną belką. Nie zmieniać widoczności na podstawie liczby ikon „na oko”; trzeba użyć klasy stanu nadawanej przez klienta.

### 3. Tryb okienkowy i tło poza ekranem gry — odłożone

Statyczna kontrola aktualnie publikowanego arkusza v1.0.10 wykazała:

- brak reguły ustawiającej tło `html` lub `body`,
- brak wymuszenia `100vw × 100vh` na `.game-window-positioner`,
- tła motywu są przypięte do konkretnych paneli interfejsu.

Aktualny motyw nie wymusza więc bezpośrednio czarnego tła poza pomniejszonym ekranem gry. Czarny kolor istnieje w bazowym CSS klienta. W starym pełnym arkuszu roboczym również znajdowała się kopia `body { background:#000; width:100vw; height:100vh }`, lecz nie jest ona częścią aktualnego publikowanego arkusza delty.

**Do sprawdzenia w grze:** ustawić kolejno kilka teł w dodatku „Tryb okienkowy” i ustalić, czy dodatek nakłada obraz na `body`, osobną warstwę pod grą czy pseudoelement. Następnie sprawdzić kolejność arkuszy i `z-index`. Jeżeli obraz istnieje w DOM, lecz jest zasłonięty, wyłączyć tło wyłącznie na kolidującej warstwie. Nie dodawać własnego tła zastępczego i nie zmieniać tła całej strony.

**Warunek odbioru:** przy rozmiarze gry `1200 × 675` wybrane tło dodatku jest widoczne na całym obszarze poza kontenerem gry, a po wyłączeniu dodatku wraca oryginalne zachowanie klienta.

Ten punkt został wyłączony z bieżącego etapu decyzją użytkownika. Nie należy dodawać dla niego reguł CSS ani zasobów podczas realizacji pozostałej części audytu.

## P1 — wspólne komponenty wizualne

### 4. Nagłówki wewnętrzne nie tworzą jednej rodziny

Napisy takie jak „Lista umiejętności”, „Punkty umiejętności”, „Umiejętności”, „Społeczność”, zakładki dziennika zadań i rzemiosła są osadzone na kilku różnych komponentach:

- `table_header.png`,
- `width-card-button.png`,
- `width-card-button-active.png`,
- `.interface-element-header-1-background`,
- `.interface-element-active-card-*` i `.interface-element-card-*`,
- lokalne belki poszczególnych okien.

Grafiki zostały częściowo przebudowane, ale zachowano stare metryki tekstu. Dlatego etykieta wygląda jak osobna nakładka, a w części okien nadal dominuje szara lub drewniana belka.

**Do poprawy:** zbudować jedną rodzinę stalowych belek dla nagłówka sekcji i zakładki. Każdy wariant musi mieć lewy koniec, rozciągliwy środek i prawy koniec. Tekst należy centrować przez `display:flex`, `align-items:center`, `justify-content:center` i właściwy `line-height`, bez lokalnych wartości `top` dla pojedynczego okna. Stany aktywny, nieaktywny, hover i disabled muszą pochodzić z tej samej palety.

### 5. Widgety: zachować ikony, ujednolicić wyłącznie oprawę

Przywrócone natywne ikony są prawidłowe. Zielone, niebieskie, czerwone, fioletowe i pomarańczowe tła nadal pochodzą ze stanów `.widget-button`.

Zakres obejmuje:

- górny lewy i prawy rząd,
- dolny lewy i prawy rząd,
- oba dodatkowe dolne rzędy,
- panel dodatków,
- widgety `bm-register` i `onc-btn`,
- przyciski widoczności i edycji paska widgetów,
- wszystkie dodatki korzystające ze wspólnej klasy `.widget-button`.

**Do poprawy:** nadać jednolite tło, obramowanie i cień wariantom `green`, `red`, `blue`, `purple`, `violet`, `orange`, `black` i `transparent` oraz stanom hover, active, pressed, `window-is-open`, disabled i blink. Nie zmieniać `background-image` elementu `.icon`; ikony pozostają natywne.

### 6. Wszystkie rodziny przycisków i menu kontekstowe

Ogólna reguła obejmuje `.button`, `.btn-min`, standardowe `button`, `card-button-test`, `tw-tabs`, `tw-one-tab` i `tabs-nav`, ale nie pokrywa wprost wielu wyspecjalizowanych kontrolek:

- `.btn-opt`,
- `.change-state-btn`,
- `.change-visible-button`,
- `.chat-config-wrapper-button`,
- `.copy-btn` i `.item-details__copy-btn`,
- `.delete-button`, `.divide-button`, `.info-btn`,
- `.mission-next-button`, `.mission-prev-button`,
- `.pvp-btn`, `.settings-button`, `.toggle-size-button`,
- `.widget-bar-visible-btn`.

Menu `.popup-menu`, `.dropdown-menu` i `.menu-list` mają już częściowe pokrycie, lecz trzeba sprawdzić menu po PPM, opcje alertów, `mAlert`, konsolę, submenu oraz stany disabled i selected.

**Do poprawy:** podzielić kontrolki na przyciski tekstowe i ikonowe. Tekstowym nadać pełną oprawę motywu. W ikonowych zachować natywny sprite i pozycję ikony, zmieniając tylko tło kontenera, ramkę i stany interakcji. Nie stosować jednej reguły zmieniającej sprite wszystkich ikon.

## P1 — górny HUD

Oryginalny HUD ma `342 × 65 px`. Obecne pozycje tekstów nadal opierają się na polach starego atlasu:

- nazwa postaci: `top:2`, `left:39`, szerokość `262`,
- kropka mapy: `top:22`, `left:26`, rozmiar `15 × 15`,
- lokacja: `left:51`, szerokość `145`,
- świat: `top:23`, `left:249`, szerokość `52`,
- pola walut: obszary `.gold-tip` i `.credits-tip` po `21 × 21 px`.

Nowa grafika ma inne optyczne środki pól, więc zachowanie starych współrzędnych powoduje przesunięcie tekstu i kropki.

**Do poprawy:** 

1. Wyznaczyć rzeczywiste prostokąty pól na nowej grafice i zapisać je jako zmienne CSS.
2. Dodać w grafice gniazdo `15 × 15 px` na zieloną, żółtą, czerwoną lub pomarańczową kropkę mapy i ustawić `.map_ball` na jego środku.
3. Osobno wycentrować nazwę, poziom, lokację, współrzędne, świat, złoto i Smocze Łuski; zachować obcinanie długich wartości.
4. Wyświetlić natywne `goldIconNormal.png` i `draconiteIconNormal.gif` w obszarach `.gold-tip` i `.credits-tip`. Nie podmieniać tych plików globalnie.
5. Sprawdzić HUD dla krótkiej i długiej nazwy postaci, długiej nazwy mapy, czterech kolorów mapy oraz dużych wartości obu walut.

## P1 — dolny HUD i pozycjonowanie

Dolny panel ma kontener `.bottom-panel-of-bottom-positioner` o rozmiarze `664 × 82 px`. Obecny techniczny wariant używa tarczy `102 × 92 px`, ustawionej `left:281px` i `bottom:-16px`. Sloty umiejętności korzystają ze starych, niezależnych kotwic: `.skill-usable-slots.left` ma `left:64px`, a `.skill-usable-slots.right` ma `right:61px`. Paski doświadczenia również mają niezależne pozycje (`left:33px` i `left:379px`).

Na screenie skutkiem jest brak jednej osi: tarcza siedzi za nisko, oba ramiona mają różne optyczne odstępy, a końcówki belek i pola slotów nie tworzą wspólnej linii.

**Do poprawy jako jeden komponent:** 

1. Wprowadzić jedną zmienną osi środka panelu i od niej wyliczać tarczę, oba paski slotów, paski doświadczenia oraz końcówki ramion.
2. Ustalić wspólną linię bazową i podnieść cały środkowy moduł tak, aby tarcza nie zlewała się z dolną belką.
3. Ustawić lewy i prawy pasek lustrzanie względem tarczy; usunąć asymetrię `64px` kontra `61px`.
4. Wyrównać komórki umiejętności do otworów w grafice, zachowując jednakowe odstępy po obu stronach.
5. Sprawdzić nakładki doświadczenia, stan końca poziomu, energię/manę podczas walki, licznik laga i dodatkowy panel umiejętności — nadal opierają się na współrzędnych starego atlasu.
6. Zweryfikować stany z 0, 1, 4 i pełną liczbą umiejętności oraz rozdzielczości `1200 × 675`, `1366 × 768`, `1600 × 900` i `1920 × 1080`.

## P2 — spójność dolnych belek i paneli

`quests/quest_bar.png` oraz inne bordowe belki są własnymi grafikami, ale miejscami mają inny odcień i głębokość niż stalowa rama. To nie jest już oryginalne drewno, lecz nadal wygląda jak osobny zestaw.

**Do poprawy:** zachować ich skalowanie z CSS klienta, lecz ujednolicić metaliczne brzegi, ciemny środek i kolor akcentu. Dolna belka rozszerza się tylko wtedy, gdy zawartość tego wymaga; jej środek powtarza się, a końce pozostają nierozciągnięte.

## Kolejność wdrożenia

1. Separatory `middle_graphics` i warunkowa widoczność dolnych rozszerzeń.
2. Ujednolicenie czcionki oraz usunięcie starego globalnego wymuszenia Arial.
3. Wspólna rodzina nagłówków i zakładek wraz z metrykami tekstu.
4. Tła wszystkich widgetów przy zachowaniu natywnych ikon.
5. Pełna macierz przycisków, menu PPM i stanów interakcji.
6. Kalibracja górnego HUD wraz z nickiem postaci, kropką mapy i ikonami walut.
7. Przebudowa geometrii dolnego HUD wokół jednej osi.
8. Test regresji wszystkich okien korzystających ze wspólnych komponentów.

Test dodatku „Tryb okienkowy” pozostaje osobnym, późniejszym etapem.

## Proponowane rozwiązanie techniczne

### Pakiet A — jeden skalowalny system okien

1. Przebudować `middle_graphics.png` jako neutralny stalowy separator o dokładnie zachowanych wymiarach i strefach cięcia. Grafika powinna mieć delikatną fakturę, światło na krawędzi i cień styku z panelem; nie może być płaskim kolorem ani drewnem.
2. Zachować oryginalne klasy i mechanikę `border-image`. Dzięki temu dziennik, umiejętności, rzemiosło, depozyt i pozostałe okna automatycznie dostaną ten sam separator bez osobnych reguł.
3. Rozdzielić wspólne belki na trzy role: tytuł całego okna, nagłówek sekcji oraz zakładkę. Dla każdej roli przygotować rozciągliwy środek oraz nierozciągane zakończenia.
4. Zlikwidować lokalne przesunięcia napisów tam, gdzie komponent może używać wspólnego centrowania. Jednostkowe pozycje pozostawić tylko elementom, które rzeczywiście mają inną konstrukcję DOM.
5. Nie rozciągać całej bitmapy razem z narożnikami. Narożniki i ozdoby zachowują stały rozmiar, a rozszerza się wyłącznie środek i proste odcinki ramy.

### Pakiet B — nagłówki i tekst

1. Wprowadzić wspólne klasy typograficzne dla tytułu okna, tytułu sekcji, aktywnej i nieaktywnej zakładki.
2. Użyć właściwości `height`, `line-height` lub centrowania flex zgodnego z wysokością danej belki. Usunąć stare `top:12px` i podobne przesunięcia z elementów objętych wspólną klasą.
3. Zachować złoty kolor pisma, lecz zmniejszyć kontrast obwódki i cienia, aby napis wyglądał jak część belki, a nie osobna naklejka.
4. Sprawdzić krótkie i długie napisy oraz polskie znaki. Tekst nie może dotykać ozdobnych końców belki.

### Pakiet B1 — jedna czcionka dla całego motywu

1. Przyjąć `Segoe UI` jako podstawową czcionkę całego motywu. `Arial` i `sans-serif` mogą pozostać wyłącznie jako techniczne fonty awaryjne, gdy podstawowa czcionka nie jest dostępna.
2. Usunąć starą uniwersalną regułę `* { font-family: Arial !important; font-weight: 200; }`, ponieważ wymusza inny krój i jedną grubość na wszystkich elementach, niezależnie od ich roli.
3. Ustawić wspólną rodzinę na głównym kontenerze interfejsu oraz warstwach okien, czatu, komunikatów, podpowiedzi, walki i menu. Dziedziczenie powinno zastąpić powielanie `font-family` w pojedynczych oknach.
4. Zachować świadome grubości: zwykły tekst `400`, etykiety i przyciski `500–600`, najważniejsze tytuły i wartości HUD `600–700`. Jeden typ czcionki nie oznacza jednej grubości dla wszystkich napisów.
5. Wykluczyć klasy korzystające z fontów ikonowych. Narzucenie im `Segoe UI` mogłoby zamienić ikony w puste kwadraty lub błędne znaki.
6. Sprawdzić polskie znaki, liczby, skróty walut, tekst czatu oraz napisy przy najmniejszych obsługiwanych rozdzielczościach.

### Pakiet C — widgety bez zmiany natywnych ikon

1. Zostawić `background-image` na `.widget-button .icon` bez zmian.
2. Oprawę widgetu zbudować na kontenerze `.widget-button` lub jego pseudoelementach pod ikoną. Zastosować wspólną, lekko teksturowaną stalowo-bordową powierzchnię zamiast płaskiej zieleni albo jednolitego gradientu.
3. Warianty kolorystyczne klienta sprowadzić do jednej palety motywu, ale zachować czytelne stany: zwykły, hover, otwarte okno, wciśnięty, powiadomienie i disabled.
4. Jedna reguła rodziny musi obejmować wszystkie sześć położeń pasków, panel dodatków i specjalne widgety HUD. Wyjątki dopuszczać wyłącznie dla różnego rozmiaru kontenera, nie dla koloru pojedynczej ikony.

### Pakiet D — wszystkie przyciski i menu

1. Utworzyć wspólną klasę wizualną przez grupę selektorów `:is(...)` obejmującą standardowe oraz wyspecjalizowane przyciski tekstowe.
2. Dla kontrolek ikonowych zmieniać oprawę, obramowanie i stan interakcji, pozostawiając współrzędne natywnego sprite'a.
3. Zbudować jedną macierz stanów: normal, hover, active/pressed, selected, disabled i focus. Kolory nie mogą być definiowane osobno w każdym oknie.
4. Tę samą powierzchnię zastosować w menu PPM, submenu, rozwijanych listach, alertach i `mAlert`, z odrębnym, czytelnym podświetleniem zaznaczonego wiersza.
5. Przetestować przyciski dostępne dopiero po PPM, najechaniu, rozwinięciu listy lub otwarciu dodatkowego panelu.

### Pakiet E — górny HUD

1. Na podstawie grafiki `342 × 65 px` sporządzić mapę pól: nazwa i poziom, mapa i współrzędne, świat, złoto oraz Smocze Łuski.
2. Zapisać współrzędne jako zmienne CSS przypisane do HUD, aby grafika i pozycje tekstu miały jedno źródło prawdy.
3. Wkomponować w grafikę osobne gniazdo dla `.map_ball`; kolorową kropkę nadal pobierać z natywnego sprite'a klienta.
4. Wyświetlić natywne ikony walut jako małe elementy wewnątrz istniejących obszarów `.gold-tip` i `.credits-tip`.
5. Dopasować `line-height`, szerokości i obcinanie tekstu do rzeczywistych otworów grafiki, zamiast kopiować pozycje z oryginalnego HUD.
6. Zmienić wygląd `.heroname`, aby nick postaci był częścią motywu: użyć wspólnej czcionki `Segoe UI`, złotego koloru z palety nagłówków zamiast jaskrawej żółci, grubości `600–700` i delikatnego ciemnego cienia. Nick ma być wycentrowany w przeznaczonym polu, nie może nachodzić na poziom postaci ani ozdoby ramy i nadal musi używać `text-overflow: ellipsis` dla długich nazw.

### Pakiet F — dolny HUD

1. Zdefiniować środek kontenera `664 px` jako jedną zmienną. Pozycję tarczy obliczać ze środka i jej szerokości, a nie wpisywać niezależne `left`.
2. Ustawić ramiona, sloty i paski doświadczenia lustrzanie względem osi. Ich odstęp od tarczy powinien wynikać ze wspólnej zmiennej.
3. Podnieść środkowy moduł i wyznaczyć jedną linię bazową dla tarczy, slotów oraz końców belek.
4. Dopasować grafikę ramion do oryginalnego systemu slotów. Nie przesuwać każdego slotu osobno w celu skompensowania źle przygotowanej bitmapy.
5. Przygotować stany testowe dla doświadczenia, walki, many/energii, końca poziomu i rozwiniętego panelu umiejętności.

### Pakiet G — dolne rozszerzenia widgetów

1. Ustalić klasy stanu nadawane kontenerowi gry po utworzeniu dodatkowego lewego lub prawego rzędu.
2. Ukryć `.bg-additional-widget-left` i `.bg-additional-widget-right` w stanie podstawowym.
3. Pokazywać wyłącznie właściwe rozszerzenie i nadać mu ten sam teksturowany środek co dolnej belce.
4. Rozciągać wyłącznie środkowy fragment tła do szerokości faktycznej liczby widgetów; zakończenie belki zachowuje stały rozmiar.

### Pakiet H — grafiki świata gry pozostają oryginalne

Z podmian motywu należy nadal wykluczać grafiki postaci i obiektów świata używane przy NPC oraz w walce, w tym `def-npc.gif`, `battle.gif`, `rip1.gif` i `rip2.gif`. Motyw ma zmieniać interfejs, a nie obrazki stojące na mapie. Test powinien potwierdzić ich natywną przezroczystość.

## Warunki odbioru całego etapu

- Żadne okno oparte na `interface-element-middle-*` nie pokazuje drewna.
- Cały interfejs używa `Segoe UI`, z wyjątkiem świadomie zachowanych fontów ikonowych.
- Wszystkie nagłówki i zakładki korzystają z jednej stalowej rodziny oraz poprawnie centrują tekst przy różnych szerokościach.
- Każdy widget zachowuje natywną ikonę, lecz ma oprawę motywu we wszystkich stanach.
- Wszystkie przyciski tekstowe, ikonowe i menu kontekstowe mają odpowiednią kolorystykę bez uszkodzenia sprite'ów.
- Górny HUD ma poprawne pozycje tekstów, spójnie wystylizowany nick postaci, kropkę mapy i obie ikony walut.
- Dolny HUD jest symetryczny, ma jedną oś i pozostaje poprawny podczas walki oraz po rozwinięciu umiejętności.
- Dodatkowe dolne tło pojawia się tylko przy rzeczywistym dodatkowym rzędzie widgetów.
- Wybrane tło dodatku „Tryb okienkowy” jest widoczne poza kontenerem gry i nie jest zastępowane przez motyw.
