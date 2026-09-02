# Faktyczne użycie GIF-ów i `progressBar` w v1.0.11

Data: 2026-09-02

Audyt wykonano na publikowanej paczce `E:\Motywy\margonem-dwarven-forge-ui`, ładowanej przez userskrypt z tagu v1.0.11. Rozróżniono plik obecny w paczce od pliku faktycznie wskazanego przez arkusz motywu.

## Najważniejsza korekta

Wcześniejsze prezentacje kilku wersji animowanych ramek pokazywały kolejne rewizje robocze (`structural`, v3 i v4). Nie były to różne animacje przeznaczone do jednoczesnego występowania w grze. Do produkcji trafiły wyłącznie dwa finalne pliki v4:

- `item-slot-anim-frame1.gif`;
- `item-slot-anim-frame2.gif`.

Oba mają 54 × 54 px i po 32 klatki. Sumy kontrolne produkcji są identyczne z plikami `custom/quality-rework-v4`.

## Dwie autorskie animowane ramki przedmiotu

| Plik | Selektor w arkuszu v1.0.11 | Sposób aktywacji | Potwierdzone miejsce |
|---|---|---|---|
| `item-slot-anim-frame1.gif` | `.ie-item-slot-anim-frame` oraz `.ie-item-slot-anim-frame--frame-1` | Klient musi utworzyć element z klasą bazową albo wariantem `frame-1`. Sam motyw nie dodaje tej klasy. | Potwierdzono wizualnie czerwoną animację `frame1` w **Rzemiosło → Gniazdo przedmiotu → Fuzja**, na centralnym gnieździe wyniku pod trzema polami składników. |
| `item-slot-anim-frame2.gif` | `.ie-item-slot-anim-frame--frame-2` | Klient musi utworzyć wariant `frame-2`. Sam motyw nie dodaje tej klasy. | Brak potwierdzonego wystąpienia w dostarczonych testach gry. |

Selektory są globalne i nie wymieniają Rzemiosła, ekwipunku, sklepu ani depozytu. Miejsce pojawienia się animacji zależy od logiki klienta, która nadaje klasy runtime. Arkusz CSS nie zawiera informacji, jaki konkretny typ przedmiotu lub stan wybiera `frame-1` albo `frame-2`.

Wniosek: obecnie można potwierdzić jedno rzeczywiste wystąpienie czerwonego `item-slot-anim-frame1.gif`. Turkusowy `item-slot-anim-frame2.gif` nie ma jeszcze potwierdzonego miejsca w grze. Nie ma podstaw, aby twierdzić, że obie animacje są widoczne w wielu oknach.

### Działanie dla v1.0.12

Do userskryptu diagnostycznego zostanie dodana obserwacja elementów:

```js
.ie-item-slot-anim-frame,
.ie-item-slot-anim-frame--frame-1,
.ie-item-slot-anim-frame--frame-2
```

Obserwacja zapisze klasę wariantu, najbliższe okno oraz widoczność elementu. Test obejmie Rzemiosło, ekwipunek, depozyt, handel i sklep. Dopiero ten pomiar pozwoli wskazać wszystkie faktyczne miejsca tworzone przez logikę gry.

## Pozostałe GIF-y wskazywane przez arkusz motywu

| Plik | Klatki | Selektor | Ocena |
|---|---:|---|---|
| `away.gif` | 13 | lista obecnych graczy ze stanem `stasis-incoming.active`; członek grupy ze stanem `stasis-incoming` | Aktywna funkcjonalna animacja stazy. Nie jest autorską dekoracją motywu. Zgodnie z decyzją o zachowaniu grafik funkcjonalnych powinna wrócić do wersji klienta bez podmiany. |
| `buffs.gif` | 4 | `.battle-window .one-warrior .warrior .buff` | Funkcjonalna animacja buffa w walce. Powinna korzystać z oryginału klienta; override motywu zostanie usunięty. |
| `X-blackoutline.gif` | 1 | ikona wyłączenia przedmiotu w ekwipunku, wyposażeniu i listach przedmiotów | Statyczna ikona mimo rozszerzenia GIF. |
| `ok-blackoutline.gif` | 1 | ikona wyboru przedmiotu w tych samych listach | Statyczna ikona mimo rozszerzenia GIF. |
| `mail-gold.gif` | 1 | załącznik złota w wiadomości | Statyczna ikona. |
| `honorIconNormal.gif` | 1 | ikona honoru w komponencie kosztu | Statyczna ikona. |
| `original-draconite.gif` | 1 | ikona smoczej łuski dodana w górnym HUD-zie | Statyczna, świadomie zachowana oryginalna ikona waluty. |

Rozszerzenie `.gif` nie oznacza automatycznie animacji. W aktywnych odwołaniach CSS animowane są tylko `away.gif`, `buffs.gif` oraz dwie ramki przedmiotów.

## GIF-y obecne w paczce, lecz niewskazywane przez CSS motywu

W paczce znajdują się również między innymi:

- `def-npc.gif`;
- `rip1.gif` i `rip2.gif`;
- `img/emo/battle.gif`;
- `draconite_small.gif` i `draconiteIconNormal.gif`;
- lokalne kopie znaczników usług NPC: sklep, depozyt, poczta, leczenie, aukcje, zadania i karczma.

Arkusz `dwarven-forge.css` v1.0.11 ich nie wskazuje. Samo umieszczenie pliku w `assets-production` nie powoduje jego użycia. Bazowy klient może nadal ładować swoje oryginalne wersje bezpośrednio ze swoich adresów, ale lokalne kopie z paczki motywu są dla tego arkusza niepodpięte.

## Cztery pliki `progressBar`

| Plik | Rozmiar | Selektor |
|---|---:|---|
| `progress-bar.png` | 139 × 14 px | `.progress-bar-wrapper .background` |
| `percent-red.png` | 139 × 14 px | `.progress-bar-wrapper.red .bar-percentage` |
| `percent-blue.png` | 139 × 14 px | `.progress-bar-wrapper.blue .bar-percentage` |
| `percent-yellow.png` | 139 × 14 px | `.progress-bar-wrapper.yellow .bar-percentage` |

Pliki produkcyjne są identyczne z wariantami `custom/quality-rework-v4/progressBar`, a nie z oryginałami klienta. Zostały więc faktycznie skopiowane do produkcji. Wcześniejszy wpis `production_promoted:false` w `quality-rework-v4-style-accepted.json` jest nieaktualny.

## Gdzie komponent `progressBar` jest używany

Zebrany CSS zawiera tylko jeden konkretny kontekst dla graficznego komponentu 139 × 14 px:

```css
.battle-controller .battle-content .stats-wrapper {
  display: none;
  position: absolute;
  top: -100px;
}

.battle-controller .battle-content .stats-wrapper .progress-bar-wrapper {
  width: 140px;
  margin-top: 2px;
}
```

Oznacza to panel statystyk kontrolera walki, który jest domyślnie ukryty. W zebranym CSS nie ma stanu zmieniającego jego `display` na widoczny. Logika JavaScript klienta może ustawić styl bezpośrednio, lecz nie ma jej w paczce motywu i nie udało się znaleźć publicznego źródła potwierdzającego taki stan.

### Czego te pliki nie obsługują

Te cztery grafiki nie są używane przez:

- dolny pasek doświadczenia postaci;
- tarczę życia w dolnym HUD-zie;
- paski życia i zasobów postaci widoczne nad wojownikiem w walce;
- pasek czasu walki;
- postęp zadania klanowego;
- postęp matchmakingu;
- pasek ulepszania w Rzemiośle.

Powyższe elementy używają innych regionów `buttony.png`, pliku `progressbary.png` albo prostych kolorów CSS.

### Kolizja nazwy klasy w oknie walki

Wojownicy w `.battle-window` również mają kontener nazwany `.progress-bar-wrapper`, ale ich widoczne paski są zbudowane z elementów `.stat-bar` i `.inner`, kolorowanych przez CSS. Nie korzystają z dzieci `.background` i `.bar-percentage`, do których przypisano cztery grafiki `progressBar`.

## Wniosek produkcyjny

Cztery grafiki `progressBar` są obecnie zasobami skopiowanymi do produkcji i podpiętymi do ukrytego komponentu, ale bez potwierdzonego, widocznego zastosowania w normalnym interfejsie testowanym przez użytkownika. Nie należy przedstawiać ich jako widocznej części motywu. W v1.0.12 zostaną wykonane następujące czynności:

1. runtime zostanie sprawdzony pod kątem pojawienia się widocznego `.battle-controller .stats-wrapper .progress-bar-wrapper`;
2. czerwony wariant zostanie zastosowany do widocznych pasków życia o odpowiednich wymiarach;
3. niebieski wariant zostanie zastosowany do many;
4. żółty wariant zostanie zastosowany do energii;
5. dla pasków nad wojownikami o wysokości 2–4 px powstaną cienkie warianty pochodne, zamiast skalowania pełnych grafik 139 × 14 px.

Zaakceptowany nowy pasek EXP dolnego HUD-u jest osobnym projektem i nie będzie korzystał z tych czterech grafik 139 × 14 px.

## Oryginalny pasek pomiędzy polami przedmiotów w Rzemiośle

Pasek pokazany między dwoma górnymi polami w **Rzemiosło → Gniazdo przedmiotu → Ulepszanie** nie korzysta z katalogu `img/gui/progressBar`. Jest to osobny komponent:

```css
.enhance__progressbar {
  width: 138px;
  height: 16px;
}

.enhance__progress-bg {
  background: url(/img/gui/progressbary.png) 0 -104px;
}

.enhance__progress--current { background: #4bcc12; }
.enhance__progress--preview { background: #96f56c; }
```

Komponent korzysta z oryginalnego regionu atlasu `progressbary.png` i prostych zielonych kolorów CSS. Nie został zastąpiony autorskim odpowiednikiem motywu.

Górne pola przedmiotów korzystają z większej dekoracji slotu przez `.enhance__item` oraz wspólny wariant `.interface-element-one-item-slot-decor`. Siatka „Składniki” używa małych powtarzalnych pól. Funkcjonalnie rozmiary mogą pozostać różne, ale w v1.0.12 oba warianty muszą powstać z jednego zaakceptowanego wzorca z cienkim rantem.
