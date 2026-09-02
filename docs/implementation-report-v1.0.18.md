# Dwarven Forge 1.0.18

## Okna

Zaakceptowany układ okna umiejętności obejmuje jedną bordową stopkę na pełną szerokość, boczne krawędzie połączone z jej dolnym końcem i brak wystającego stalowego pasa. Wersja 1.0.18 stosuje ten układ we wspólnym komponencie stopki oraz w oknach z osobnym kontenerem kontrolek.

- Wspólna stopka `c-window__bottom-bar` rysuje jedyne tło, niezależnie od marginesów wewnętrznych paneli. Natywne przyciski pozostają w swoich kontenerach; drugie tła pod nimi są wyłączone.
- Rama kończy się 4 px poniżej tła stopki, zachowując cienki obrys. Jej boczne linie nie urywają się nad belką.
- Górne i dolne belki używają tego samego gradientu wskazanego przez użytkownika, bez ornamentowanej tekstury stopki: `#5c2026`, `#351418`, `#241114`, `#120c0d`.
- Dodatkowe złote pionowe kreski wewnętrznych paneli zostały usunięte. Zewnętrzna rama i separator kolumn umiejętności pozostają.
- Stopka ma wysokość 34 px, a jej przyciski 24 px. Tekst jest wyśrodkowany w obu osiach przez flex, niezależnie od wysokości przycisku. Nagłówki kolumn umiejętności mają jednakową wysokość.
- Konsola zachowuje czyste tło bez dodatkowego wewnętrznego paska informacji; podgląd samej ramy świata nie zawiera pustej sekcji danych.
- Zakładki mają równe komórki i wewnętrzne obramowanie; tła nie wychodzą poza ich kontener.

Obsługiwane układy: natywna stopka wspólna (m.in. klan, premium, dodatki i aktualności), umiejętności, łupy, konsola z dodatkami globalnymi, poczta, społeczność, aukcje, podział przedmiotów, zmiana stroju, edycja kolorów, ustawienia, depozyt, osiągnięcia, otchłań i jej podsumowanie, świat, dziennik/rzemiosło i inne okna korzystające z komponentu listy z opisem, karnet bitewny.

Przezroczyste okna, komunikaty bez stopki, wewnętrzne paski nagłówków poczty oraz kontroler walki poza standardową ramą nie otrzymują automatycznie nowej zewnętrznej stopki.

## Pozostałe poprawki z bieżącej serii zgłoszeń

- Premium: osobne pozycje wycinków atlasu i stałe miejsce na podpisy, bez ponownej kompresji grafiki.
- Duże pola przedmiotu: centrowanie natywnej ikony 32×32 w polu 46×46, bez rozciągania ikony.
- Walka: usunięcie starej oprawy pasków many/energii i ikon wchodzących pod liczby; oddzielne pola wartości i wypełnień.
- HUD: odsunięcie od dolnej krawędzi o 4 px, wskaźnik opóźnienia poza polem wyczerpania, wyrównanie powierzchni widgetów i belki.
- Tryb 1024×768: dodatkowy rząd widgetów podniesiony z 30 do 36 px, aby uwzględnić natywny rozmiar widgetów. Natywne skale HUD 82%/90% pozostają bez zmian.

## Weryfikacja i ograniczenia

Lokalny Chromium z arkuszem i szablonami klienta oraz jego regułami trybu okienkowego:

- 19 wariantów okien przy szerokościach treści 250, 520 i 725 px, każdy w 3 skalach: 171 kontroli krawędzi wspólnej stopki. Kontrolki testowe sprawdzono pod kątem położenia, wyśrodkowania tekstu i rzeczywistej obsługi kliknięcia. To test geometrii ramy z reprezentatywną kontrolką, nie kompletnej treści każdego okna.
- 2 przypadki negatywne: zwykły komunikat bez stopki oraz przezroczyste okno nie dostają dodatkowej belki.
- 12 trybów HUD, każdy poza walką i podczas walki; brak wykrytych kolizji kontrolowanych pól, slotów i reprezentatywnych widgetów.
- Oba paski walki sprawdzone przy 0%, 50% i 100%; pole wartości nie przecina wypełnienia.
- Kontrola równych zakładek, centrowania przedmiotu i połączeń nagłówków/kolumn okna umiejętności.

To nie jest test w zalogowanej grze. Dane w renderach są przykładowe; nie odtwarzają wszystkich stanów serwera, wszystkich treści okien ani dowolnego rozmieszczenia widgetów. Poprawki są oparte na istniejących komponentach klienta, bez nowej obsługi kliknięć i bez dodatkowego obserwatora DOM w userscripcie.
