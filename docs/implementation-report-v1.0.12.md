# Raport wdrożenia — v1.0.12

Data: 2026-09-02

## Wdrożone zmiany

- wspólna rama okien oparta na symetrycznym układzie dziewięciu części;
- identyczna optycznie górna i dolna belka, nierozciągane narożniki oraz powtarzalne boki;
- tytuł wycentrowany wewnątrz ramy i stała strefa przycisku zamknięcia;
- ciągłe wewnętrzne nagłówki bez dekoracyjnych znaków na początku i końcu;
- autorski mały dialog `.bubbledialog`;
- dolna belka widgetów zależna wyłącznie od faktycznie widocznych widgetów;
- ujednolicona geometria i typografia górnego HUD-u oraz bliższe położenie ikon walut;
- usunięte czarne wypełnienie i półprzezroczysta czarna otoczka tarczy HP;
- autorski dwustronny pasek EXP z przezroczystą prowadnicą;
- autorski wskaźnik opóźnienia `ms`;
- cienka wspólna kratka przedmiotów;
- autorska prowadnica postępu ulepszania w Rzemiośle;
- czerwone, niebieskie i żółte paski zasobów zgodne z motywem;
- autorski znacznik kliknięcia mapy;
- jedna rodzina czcionek dla interfejsu motywu;
- zachowane oryginalne grafiki postaci, NPC, walki, ikon widgetów, `away.gif` i `buffs.gif`.

## Userskrypt

Userskrypt zawiera krótkie funkcje o jednym zadaniu. Obserwator widgetów śledzi wyłącznie dwa kontenery dodatkowej dolnej belki. Zmiany układu są grupowane przez `requestAnimationFrame`.

## Walidacja

- testy układu: 1200 × 675, 1600 × 900 i 1920 × 1080;
- brak poziomego przepełnienia w podglądzie;
- odchylenie osi tytułu od osi okna: 0–0,01 px;
- górna i dolna część ramy są dokładnym odbiciem pikselowym;
- 108 z 108 zasobów zachowuje wymagane wymiary i liczbę klatek;
- brak brakujących i nierozwiązanych adresów zasobów w paczce GitHub;
- userskrypt przechodzi kontrolę składni Node.js;
- stan belki widgetów poprawnie wraca do bazowego po usunięciu ostatniego widocznego widgetu.

## Poza zakresem

Tło dodatku „Tryb okienkowy” pozostaje odłożone do osobnego testu runtime.
