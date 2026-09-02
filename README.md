# Margonem Dwarven Forge UI 1.0.14

Dwarven Forge przebudowuje klasyczny interfejs Margonem w stylu mrocznej krasnoludzkiej kuźni. Motyw używa czernionej stali, starego brązu, głębokiego burgundu, ciemnego drewna i oszczędnych turkusowych akcentów.

## Instalacja

1. Zainstaluj rozszerzenie Tampermonkey lub Violentmonkey.
2. Otwórz [instalator Dwarven Forge](https://raw.githubusercontent.com/Doiua97/margonem-dwarven-forge-ui/main/install/dwarven-forge.user.js).
3. Zatwierdź instalację userscriptu.
4. Wyłącz inne motywy interfejsu i odśwież kartę gry.

Userscript dołącza wersjonowany arkusz CSS i podmienia obraz natywnego znacznika celu ruchu. Nie dodaje obsługi kliknięć ani nie zmienia ruchu postaci. Układem widgetów nadal steruje klient gry.

## Zakres

- główny panel, dynamiczna tarcza HP, EXP, zasoby i sloty;
- dialogi NPC, czat, komunikaty, podpowiedzi i menu;
- ekwipunek, statystyki, umiejętności i klan;
- handel, sklepy, aukcje, depozyt i poczta;
- walka, zadania, kalendarze i okna systemowe;
- kolory tekstu, nagłówków, formularzy oraz stanów aktywnych i nieaktywnych.

Wersja 1.0.14 łączy ramy i nagłówki okien w jeden skalowalny system, poprawia HUD-y, widgety, małe dialogi, kratki przedmiotów oraz paski postępu. Motyw używa jednej czcionki Segoe UI i zachowuje natywne grafiki postaci, NPC oraz walki.

## Struktura

- `install/dwarven-forge.user.js` — instalator motywu;
- `css/dwarven-forge.css` — produkcyjny arkusz stylów;
- `assets-production/` — zasoby zachowujące strukturę hostów gry;
- `docs/` — raporty kontroli wymiarów, klatek i kompilacji.

## Aktualizacja

Tampermonkey i Violentmonkey sprawdzają numer wersji userscriptu automatycznie. Jeśli przeglądarka zachowa starsze zasoby, wykonaj twarde odświeżenie strony.
