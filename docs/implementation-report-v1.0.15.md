# 1.0.15 — odstępy liczników dolnego HUD-u

Ta wersja zawiera cały pakiet 1.0.14 oraz ostatnią korektę zgłoszoną w trakcie pracy. W 1.0.14 pola zostały przeniesione nad EXP, ale były jeszcze zbyt blisko ozdób wystających ponad tor. Przesunięto oba pola o kolejne 30 px na zewnątrz.

W lokalnym układzie HUD-u 664 × 82 pole EXP zajmuje x=136..196, a pole wyczerpania x=468..528. Oba mają y=0..18 i znajdują się nad prostymi odcinkami toru, którego wypełnienie zaczyna się na y=22. Obszar ozdób między x=208 a x=452 pozostaje wolny od obu pól. Teksty mają te same prostokąty co ich tła, więc są wyśrodkowane. Sloty pozostają na natywnych pozycjach.

Test kontroluje oddzielenie od kontenera HP, rezerwy na ornamenty i toru EXP. Przeszły też wcześniejsze testy HP/EXP 0/50/100%, połączenia segmentów EXP, widgetów, kolorów, skalowania i znacznika ruchu. Podgląd obejmuje pełny natywny szablon dolnego HUD-u. Nie jest to test zalogowanej sesji gry.

Zakres pozostałych zmian i rozstrzygnięcie użycia GIF-ów opisuje `implementation-report-v1.0.14.md`. Atlas premium i prompty imagegen pozostają w plikach wersji 1.0.14; tej grafiki nie zmieniano w 1.0.15.
