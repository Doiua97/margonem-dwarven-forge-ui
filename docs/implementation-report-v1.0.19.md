# Dwarven Forge 1.0.19

Punktem odniesienia jest opublikowana wersja 1.0.18. Nie zmieniono jej arkuszy źródłowych ani wspólnych grafik. Nowe reguły znajdują się wyłącznie w `css/v1.0.19.source.css`.

## Zakres ze zrzutów

- Rzemiosło, dziennik, świat, konsola, konfiguracja, społeczność, aukcje i depozyt: nieprzezroczyste wypełnienie wewnątrz istniejącej ramy. Selektor ramy wymaga konkretnego głównego komponentu okna; nie obejmuje innych okien.
- Rzemiosło, dziennik, konfiguracja, społeczność i aukcje: wskazane wewnętrzne panele doprowadzone do górnej krawędzi stopki. Obramowanie list rzemiosła/dziennika używa istniejącego złotego koloru `#806648`.
- Konsola z dodatkami globalnymi: pole wprowadzania ma osobne 20 px nad stopką; lista komunikatów nie zajmuje tego miejsca.
- Ulepszanie w rzemiośle: centrowany jest rzeczywisty kontener `.slot`, wewnątrz którego klient umieszcza ikonę. Ikona pozostaje 32×32, pole 46×46. Komunikat pod paskiem postępu nie jest przycinany przez `overflow: hidden`.
- Maksymalne ulepszenie: zachowane natywne ukrywanie pola wyniku przez klasę `upgraded-5`. Nie zmieniono logiki gry ani stanów dostępności ulepszenia.
- Lista dodatków: ciemne tło wierszy i bordowe podświetlenie po najechaniu/naciśnięciu. Nie dodano obsługi kliknięć ani obserwatorów.
- Mana i energia: tory pasków stykają się z krawędziami pól wartości, bez przerwy i nakładania na liczby.
- Depozyt: zmieniono wyłącznie oprawę i typografię panelu `.right-part` z ilością złota i datą ważności. Natywna szerokość etykiety została zachowana. Wyszukiwarka, pole kwoty oraz przyciski wpłat i wypłat nie mają nowych reguł.

## Weryfikacja

`tools/check_v119.cjs` korzysta z zagnieżdżonych szablonów klienta i natywnych kontekstów pozycjonowania. W poprzednich podglądach dodatkowe `position: relative` zmieniało punkt odniesienia elementów absolutnych, a brak klasy `default` w testowych inputach tworzył białe pola. Te błędy były w podglądach, nie zostały dodane do produkcyjnego CSS.

- Szczelina między wskazanymi panelami a stopką: 0 px.
- Na renderach po zmianach brak pikseli kontrastowego tła kontrolnego wewnątrz ramy.
- Przedmiot w zagnieżdżonym polu: środek pokrywa się z środkiem slotu; wielkość ikony 32×32; ramka pozostaje obecna.
- Konsola: pole wprowadzania kończy się nad stopką.
- Depozyt: położenie i szerokość lewej części formularza identyczne przed i po zmianie; data mieści się w panelu informacyjnym.
- Umiejętności, premium i łupy: rendery identyczne bajtowo przed i po dodaniu warstwy 1.0.19.
- `tools/check_v119_hud.cjs`: 12 trybów HUD, kontrola kolizji; mana i energia dla 0%, 50%, 100%, odstęp toru od pola wartości 0 px.

## Dolny HUD i ograniczenia

Pełne zrzuty użytkownika pokazują zewnętrzną ramę trybu okienkowego. Jej nie zmieniono. Odtworzono natomiast defekt maski HUD-u: zewnętrzny kontur maski 1.0.14 przycinał ozdobniki istniejącej grafiki. Nowa maska zachowuje natywny kanał alfa PNG, usuwa oderwane resztki nad bocznymi odcinkami listwy oraz wycina pola HP/EXP. Pusta część EXP otrzymała nieprzezroczyste tło #100f12. Plik PNG, rozmiar tarczy, sloty, liczniki i obramowanie gry pozostają bez zmian.

Nie ma połączenia z otwartą grą użytkownika. Testy dotyczą lokalnych szablonów i CSS klienta; nie zastępują sprawdzenia pełnego stanu gry.
