# Margonem Dwarven Forge UI 1.0.4

Dwarven Forge przebudowuje klasyczny interfejs Margonem w stylu mrocznej krasnoludzkiej kuźni. Motyw używa czernionej stali, starego brązu, głębokiego burgundu, ciemnego drewna i oszczędnych turkusowych akcentów.

## Instalacja

1. Zainstaluj rozszerzenie Tampermonkey lub Violentmonkey.
2. Otwórz [instalator Dwarven Forge](https://raw.githubusercontent.com/Doiua97/margonem-dwarven-forge-ui/main/install/dwarven-forge.user.js).
3. Zatwierdź instalację userscriptu.
4. Wyłącz inne motywy interfejsu i odśwież kartę gry.

Userscript nie modyfikuje mechaniki gry. Dołącza wersjonowany arkusz CSS, który korzysta z grafik znajdujących się w tym repozytorium.

## Zakres

- główny panel, dynamiczna tarcza HP, EXP, zasoby i sloty;
- dialogi NPC, czat, komunikaty, podpowiedzi i menu;
- ekwipunek, statystyki, umiejętności i klan;
- handel, sklepy, aukcje, depozyt i poczta;
- walka, zadania, kalendarze i okna systemowe;
- kolory tekstu, nagłówków, formularzy oraz stanów aktywnych i nieaktywnych.

Wersja 1.0.4 używa wyłącznie warstwy zmian motywu i nie dołącza kopii arkusza układu gry. Dzięki temu aktualny klient Margonem zachowuje własne wymiary, pozycje i zachowanie okien. Autorskie grafiki są używane dla 91 bezpiecznych elementów. Jedenaście atlasów funkcyjnych, które sterują pozycjami ikon i stanów, pozostaje w wersji dostarczanej przez grę.

## Struktura

- `install/dwarven-forge.user.js` — instalator motywu;
- `css/dwarven-forge.css` — produkcyjny arkusz stylów;
- `assets-production/` — zasoby zachowujące strukturę hostów gry;
- `docs/` — raporty kontroli wymiarów, klatek i kompilacji.

## Aktualizacja

Tampermonkey i Violentmonkey sprawdzają numer wersji userscriptu automatycznie. Jeśli przeglądarka zachowa starsze zasoby, wykonaj twarde odświeżenie strony.
