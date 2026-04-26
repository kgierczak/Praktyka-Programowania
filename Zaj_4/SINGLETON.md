Instrukcja wykonana przez Mateusz Hypta:

Wzorzec: Singleton

1.
Problem

Potrzebujemy tego wzorca, gdy w całym programie musi istnieć tylko jeden obiekt danej klasy.

    Przykłady: jedno połączenie z bazą danych, jeden wspólny logger błędów lub jedna konfiguracja systemu.

    Warunek: tworzenie większej liczby tych obiektów to strata pamięci lub ryzyko, że różne części programu będą miały inne dane.

2.
Rozwiązanie

W Pythonie musimy przejąć kontrolę nad tworzeniem obiektu w pamięci.

    Krok 1 (Schowek): Wewnątrz klasy stwórz zmienną statyczną _instance i ustaw ją na None. Będzie ona trzymać nasz jedyny obiekt.

    Krok 2 (Przejmowanie kontroli): Nadpisz metodę __new__. To ona decyduje, czy stworzyć nowe miejsce w pamięci.

    Krok 3 (Logika): W metodzie sprawdź, czy _instance jest puste. Jeśli tak, stwórz obiekt przez super().__new__ i zapisz go do schowka.

    Krok 4 (Zawsze ten sam adres): Na końcu metody zawsze zwracaj zawartość _instance. Dzięki temu każdy dostanie ten sam obiekt.

    Krok 5 (Ważny detal): Pamiętaj, że Python zawsze wywoła __init__. Żeby nie resetować danych przy każdym wywołaniu klasy,
	dodaj prostą flagę, która pozwoli odpalić kod startowy tylko raz.

3.
Konsekwencje

    Zalety:

        Oszczędzasz zasoby, bo nie dublujesz ciężkich obiektów.

        Masz jeden pewny punkt dostępu do danych.

        Twój kod trzyma standardy znane innym programistom.

    Wady:

        Trudniej pisze się testy, bo Singleton trzyma stan przez cały czas działania programu.

        Jeśli go nadużyjesz, niepotrzebnie skomplikujesz strukturę kodu.