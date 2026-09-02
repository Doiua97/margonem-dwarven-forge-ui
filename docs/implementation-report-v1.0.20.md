# Dwarven Forge 1.0.20

Poprawka obejmuje wyłącznie elementy wskazane na ostatnich zrzutach.

- Maska tarczy usuwa czarne kliny nad bocznymi ornamentami. Plik PNG tarczy pozostaje bez zmian.
- Pole ms przesunięte o 6 px w prawo, bez zmiany wymiarów ani położenia slotów.
- Górny HUD wyśrodkowany pionowo względem belki, z zachowaniem natywnego skalowania i środka w poziomie.
- Filtry recept i statystyk świata oraz przyciski konfiguracji, aktywności i poczty wyśrodkowane w stopce 34 px.
- Szare nagłówki tabel sterowania, statystyk i aktywności otrzymują ustalone bordo i złoty obrys.
- Dodatkowy panel umiejętności otrzymuje bordowy nagłówek. Dolny panel walki i jego przyciski podniesione o 5 px.
- Wyłącznie ramki wymagań i działania umiejętności otrzymują prosty złoty obrys bez bocznych ozdobnych linii.
- Jasny tekst wiadomości pocztowych; tło listy otrzymanych i wysłanych wiadomości dochodzi do stopki. Geometria edytora nowej wiadomości pozostaje bez zmian.

Walidacja lokalna w Chromium na CSS i szablonach klienta: sześć widoków w dwóch wysokościach, 12 wariantów rozdzielczości HUD, wyrównanie etykiet i przycisków walki, maska tarczy i obrysy opisów umiejętności. Wszystkie badane kontrolki mieszczą się w stopkach i mają zerową różnicę środka pionowego. Analiza pikseli sześciu podglądów nie wykryła tła testowego wewnątrz ram.

Ponownie sprawdzono wcześniejsze poprawki dziewięciu okien, pozycję przedmiotów w rzemiośle, wariant maksymalnego ulepszenia i stykanie pasków many/energii z polami wartości. Puste okno umiejętności, premium oraz łupy są identyczne pikselowo przed i po tej poprawce. Brak globalnych zmian przycisków, slotów, ramek okien i atlasów grafik.

Ograniczenie: nie przeprowadzono kontroli w zalogowanej grze. Dynamiczne stany klienta mogą wymagać osobnej weryfikacji na zrzucie użytkownika.
