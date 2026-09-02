# 1.0.16 — liczniki przy dolnych rogach tarczy

Zgodnie z korektą użytkownika wycofano umieszczenie liczników ponad torem EXP. Pola tła i tekstu mają 48 × 18 px i leżą przy dolnych bocznych rogach tarczy, w przerwach między HP a slotami.

W lokalnych współrzędnych kontenera 664 × 82:

- EXP: x=232, y=60;
- wyczerpanie: x=384, y=60;
- znacznik ms: x=618, nadal przy dolnej krawędzi panelu.

Nie przesuwano slotów ani tarczy. W teście pełnego natywnego szablonu prostokąty liczników nie przecinają kontenera HP, slotów, toru EXP ani znacznika ms. Środek każdego napisu pokrywa się ze środkiem jego pola. Sprawdzono też renderowanie całego HUD-u przy HP/EXP 0/50/100%.

Wersja zachowuje pozostałe poprawki pakietu 1.0.14: przywróconą bitmapę HUD-u z oddzielną maską, tor EXP biegnący pod tarczą, nowe powierzchnie widgetów, spójne ramy i stopki, kolory paneli klanu, hover oraz odświeżony atlas premium. Raport użycia obu GIF-ów znajduje się w `implementation-report-v1.0.14.md`.

Test wykonano lokalnie na szablonach i CSS klienta, nie w zalogowanej sesji gry. Podgląd: `v1.0.16-hud-detail.png`. Wyniki: `v1.0.16-validation.json`.
