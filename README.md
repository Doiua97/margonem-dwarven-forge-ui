# Corner Forge 0.6.0

Corner Forge zmienia układ i oprawę klasycznego klienta Margonem na czarno-czerwony interfejs. Motyw nie kopiuje pól z danymi: CSS przestawia i skórkuje te same elementy DOM, które klient aktualizuje informacjami z serwera.

## Instalacja

Zainstaluj [install/dwarven-forge.user.js](install/dwarven-forge.user.js), wyłącz inne motywy i odśwież kartę gry. Userscript jest jedynym plikiem JS i wyłącznie dołącza arkusz stylów.

- `css/dwarven-forge.css` — jedyny produkcyjny arkusz CSS.
- `install/dwarven-forge.user.js` — mały loader CSS, wersja 0.6.0.
- `assets/` — jeden płaski katalog ośmiu grafik używanych przez motyw.
- `docs/main.min.53XkBRxF.zip` — materiał źródłowy audytu klienta, nie jest ładowany przez motyw.

## Zachowane kontrakty klienta

- HUD zachowuje istniejące pola nicku, poziomu, mapy, świata, złota i smoczych łusek.
- Czat korzysta z `new-chat-window`; kanały, wiadomości, pole wpisywania i przewijanie pozostają klientowe.
- Prawa kolumna zachowuje `right-column > inner-wrapper > right-main-column-wrapper`, natywne wyposażenie 104×138, statystyki oraz ekwipunek 232×198.
- Rozwinięte statystyki używają natywnego `.active` i `right:100%`, wysuwają się w lewo i kończą nad dolną ramą.
- HP zachowuje pionowe sterowanie wysokością `bar-horizontal=false`; EXP zachowuje dwie poziome części `left/right`.
- `battle-bars-wrapper` nie ma w CSS wymuszonego `display`; stan walki nadal ustala klient.
- Osiem natywnych slotów pozostaje dostępnych podczas walki.
- Sześć `main-buttons-container` pozostaje oddzielnymi kontenerami. Motyw zmienia ich wspólną belkę i kafle, ale pozostawia oryginalne ikony widgetów, puste pozycje edytora oraz hamburgery.
- Grafiki przedmiotów, rarity, ramki przedmiotów, ikony umiejętności i tło pola walki pozostają klientowe.
- Aktualności i kalendarz zachowują treść i grafiki wydarzeń; motyw zmienia ich oprawę panelu.
- Pozostałe powierzchnie, obramowania, ikony oprawy, przyciski i moduły korzystają z nowego zestawu Corner Forge.

## Test w grze

Wydanie jest przygotowane do testu w zalogowanym kliencie. Należy sprawdzić:

- dialog NPC od otwarcia do zakończenia zadania;
- leczenie, niski HP, przyrost EXP oraz wejście i wyjście z walki;
- wszystkie umiejętności, zmianę celu, szybką walkę i zakończenie walki;
- rozwijanie statystyk oraz brak kolizji z HP, walką i ekwipunkiem;
- sześć grup widgetów, podpowiedzi po najechaniu, edytor i zapis pozycji;
- czat w dostępnych `chat-size-*` oraz prawą kolumnę w `eq-column-size-*`;
- pocztę, klan, łupy, dodatki, ustawienia, minimapę, aktualności i kalendarz;
- różne rozdzielczości `body[data-res]`, szczególnie 1024×768, 1366×768, 1600×900 i 1920×1080.

Jeżeli przeglądarka zachowa starszy CSS, zaktualizuj userscript do 0.6.0 i wykonaj twarde odświeżenie strony.
