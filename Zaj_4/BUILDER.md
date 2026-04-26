Intrukcja wykonana przez Konrad Gierczak:

Wzorzec projektowy: Builder (Budowniczy)

1. Nazwa wzorca

Builder (Budowniczy)

2. Problem

Wzorzec Builder stosuje się w sytuacjach, gdy proces tworzenia obiektu jest złożony i składa się z wielu kroków, a sam obiekt może występować w różnych konfiguracjach.

Typowe problemy, które uzasadniają użycie tego wzorca:

- obiekt posiada wiele parametrów konfiguracyjnych,
- konstruktor klasy staje się bardzo rozbudowany i nieczytelny,
- istnieje potrzeba tworzenia różnych wariantów tego samego obiektu,
- chcemy oddzielić proces tworzenia obiektu od jego reprezentacji.

Bez zastosowania wzorca Builder kod może zawierać:

- tzw. „telescoping constructors” (wiele przeciążonych konstruktorów),
- trudne do utrzymania i mało czytelne inicjalizacje obiektów,
- duplikację kodu przy tworzeniu różnych konfiguracji.


3. Rozwiązanie

Wzorzec Builder polega na rozdzieleniu procesu tworzenia obiektu na etapy oraz delegowaniu tego procesu do osobnego obiektu czyli budowniczego (Buildera).

Elementy wzorca:

1. Produkt
   Klasa reprezentująca tworzony obiekt.

2. Builder (interfejs lub klasa abstrakcyjna)
   Definiuje metody odpowiedzialne za budowanie poszczególnych części obiektu.

3. Konkretny builder
   Implementuje metody Buildera i tworzy konkretną reprezentację produktu.

4. Director (opcjonalny)
   Klasa zarządzająca procesem budowy wywołuje metody Buildera w odpowiedniej kolejności.


Sposób działania:

1. Tworzony jest obiekt typu Builder.
2. Wywoływane są kolejne metody konfigurujące obiekt.
3. Builder przechowuje tworzony obiekt.
4. Na końcu zwracany jest gotowy produkt.


4. Konsekwencje

Zalety:

- oddzielenie procesu tworzenia obiektu od jego reprezentacji,
- poprawa czytelności kodu,
- możliwość tworzenia różnych wariantów obiektu przy użyciu tych samych kroków,
- większa kontrola nad procesem budowy.

Wady:

- zwiększona liczba klas w projekcie,
- większa złożoność implementacji,
- może być niepotrzebny dla prostych obiektów.


