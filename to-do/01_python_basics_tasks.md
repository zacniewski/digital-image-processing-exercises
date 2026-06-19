# Zadania: Podstawy Pythona i środowisko pracy

### Instrukcja oddawania zadań

- Każde rozwiązanie musi być zapisane w **osobnym pliku Pythona**.
- Nazwa pliku musi zawierać **Twoje nazwisko** (np. `01_nazwisko.py`).
- Umieszczamy komentarze dotyczące zastosowanego kodu.
- Tam, gdzie zadanie generuje wynik wizualny, wykonaj **zrzut ekranu** i zapisz go jako plik obrazu.
- Tam, gdzie nie da się zrobić zrzutu ekranu, wskazane jest wyświetlenie informacji (funkcja `print`) o zmiennej, wyniku, itp.
- Po realizacji wszystkich zadań należy je wysłać (wraz ze zrzutami ekranu) na **maila prowadzącego**.
- **Nie wysyłamy środowiska wirtualnego (`venv`)**.
- Proszę pamiętać, że do zaliczenia przedmiotu konieczne jest m.in. wysłanie zadań ze wszystkich laboratoriów!

______________________________________________________________________

Poniżej znajduje się 15 zadań dotyczących podstaw języka Python w kontekście przetwarzania obrazów.

1. **Zmienne i typy danych**

   - Zadanie: Utwórz zmienne przechowujące: imię (string), wiek (int), wzrost (float) i status studenta (bool). Wyświetl je wszystkie wraz z ich typami.
   - Podpowiedź: Użyj funkcji `type()` oraz `print()`.

1. **Operacje na stringach**

   - Zadanie: Utwórz zmienną z pełnym imieniem i nazwiskiem, a następnie wyświetl ją wielkimi literami, małymi literami oraz sprawdź jej długość.
   - Podpowiedź: Skorzystaj z metod `.upper()`, `.lower()` i funkcji `len()`.

1. **Lista i indeksowanie**

   - Zadanie: Utwórz listę zawierającą nazwy pięciu plików graficznych (np. `"obraz1.jpg"`). Wyświetl pierwszy i ostatni element listy oraz jej długość.
   - Podpowiedź: Pamiętaj, że indeksowanie w Pythonie zaczyna się od 0. Ostatni element to `lista[-1]`.

1. **Pętla `for`**

   - Zadanie: Korzystając z listy plików z poprzedniego zadania, wypisz w pętli każdą nazwę pliku wraz z jej numerem porządkowym (zaczynając od 1).
   - Podpowiedź: Użyj funkcji `enumerate()`: `for i, nazwa in enumerate(lista, 1)`.

1. **Instrukcja warunkowa `if`**

   - Zadanie: Napisz program, który sprawdza, czy podana liczba (np. rozmiar obrazu w pikselach) jest parzysta czy nieparzysta, a następnie wyświetla odpowiedni komunikat.
   - Podpowiedź: Użyj operatora modulo `%`: `if liczba % 2 == 0`.

1. **Słownik (dictionary)**

   - Zadanie: Utwórz słownik opisujący właściwości obrazu: szerokość, wysokość, liczba kanałów i format pliku. Wyświetl wszystkie klucze, wszystkie wartości oraz wartość dla klucza `"format"`.
   - Podpowiedź: Użyj metod `.keys()`, `.values()` i odwołania `slownik["klucz"]`.

1. **Funkcja**

   - Zadanie: Napisz funkcję `oblicz_aspect_ratio(szerokosc, wysokosc)`, która zwraca współczynnik proporcji obrazu (szerokość podzielona przez wysokość). Wywołaj ją dla kilku par wartości.
   - Podpowiedź: Zdefiniuj funkcję za pomocą słowa kluczowego `def`. Pamiętaj o instrukcji `return`.

1. **Pętla `while`**

   - Zadanie: Napisz program, który w pętli `while` wyświetla kolejne potęgi liczby 2 (1, 2, 4, 8, ...) tak długo, jak wynik jest mniejszy niż 1000. Takie wartości często spotykamy jako rozmiary obrazów.
   - Podpowiedź: Zacznij od zmiennej `n = 1` i w każdej iteracji wykonaj `n = n * 2`.

1. **Obsługa wyjątków (`try/except`)**

   - Zadanie: Napisz program, który próbuje otworzyć plik o podanej nazwie. Jeśli plik nie istnieje, wyświetl czytelny komunikat błędu zamiast pozwolić programowi się wysypać.
   - Podpowiedź: Użyj bloku `try: ... except FileNotFoundError: ...`.

1. **Importowanie modułów**

   - Zadanie: Zaimportuj moduł `os` i wyświetl: bieżący katalog roboczy, listę plików w katalogu `obrazki/male/` oraz sprawdź, czy plik `obrazki/male/img_01.jpg` istnieje.
   - Podpowiedź: Użyj `os.getcwd()`, `os.listdir()` i `os.path.exists()`.

1. **Operacje na plikach tekstowych**

   - Zadanie: Utwórz plik tekstowy `wyniki.txt`, zapisz do niego trzy linie tekstu (np. wyniki obliczeń), a następnie wczytaj go i wyświetl jego zawartość w konsoli.
   - Podpowiedź: Użyj `open("wyniki.txt", "w")` do zapisu i `open("wyniki.txt", "r")` do odczytu. Pamiętaj o zamknięciu pliku lub użyciu `with open(...)`.

1. **Wyrażenia listowe (list comprehension)**

   - Zadanie: Masz listę nazw plików: `["obraz.jpg", "zdjecie.png", "dokument.pdf", "foto.jpg"]`. Korzystając z wyrażenia listowego, utwórz nową listę zawierającą tylko pliki z rozszerzeniem `.jpg`.
   - Podpowiedź: `[x for x in lista if x.endswith(".jpg")]`.

1. **Formatowanie napisów (f-string)**

   - Zadanie: Utwórz zmienne: `szerokosc = 1920`, `wysokosc = 1080`, `format = "JPG"`. Wyświetl zdanie: `"Obraz o wymiarach 1920x1080 pikseli zapisany w formacie JPG."` korzystając z f-stringa.
   - Podpowiedź: `f"Obraz o wymiarach {szerokosc}x{wysokosc} ..."`.

1. **Klasa i obiekt**

   - Zadanie: Napisz klasę `Obraz` z atrybutami `szerokosc`, `wysokosc` i `format` oraz metodą `info()`, która wyświetla podstawowe informacje o obrazie. Utwórz dwa obiekty tej klasy i wywołaj na nich metodę `info()`.
   - Podpowiedź: Zdefiniuj klasę za pomocą `class Obraz:` i metodę inicjalizującą `def __init__(self, ...)`.

1. **Moduł `math` i obliczenia**

   - Zadanie: Korzystając z modułu `math`, oblicz przekątną obrazu o wymiarach 1920x1080 pikseli (ze wzoru Pitagorasa) oraz wyświetl wynik zaokrąglony do dwóch miejsc po przecinku.
   - Podpowiedź: Użyj `math.sqrt()` i funkcji `round()`.
