## Zadania do wykonania na zaliczenie przedmiotu  

### Wytyczne:
> 1 Można korzystać z dokumentacji online oraz zrealizowanych przez siebie wcześniejszych zadań!  
> 2. Każde zadanie wykonujemy w osobnym pliku z rozszerzeniem `.py`.  
> 3. Każdy program nazywamy w postaci `imie-nazwisko-nr_albumu-zadanie-1.py`, czyli np. `jan-kowalski-34567-zadanie-1.py`.  
> 4. W każdym zadaniu należy wygenerować obraz (za pomocą metody `imwrite`) o nazwie `imie-nazwisko-nr_albumu-zadanie-1.jpg`.

### Zadania:

##### Zad. 1. 
  - wczytaj kolorowy obraz,
  - wyświetl jego wysokość, szerokość i liczbę kanałów,
  - przekonwertuj obraz wejściowy na obraz w skali szarości,
  - wyświetl liczbę kanałów obrazu w skali szarości,
  - zapisz obraz wyjściowy w sposób podany w wytycznych.  

##### Zad. 2. 
  - utwórz macierz o wymiarach 400 x 400 z samymi zerami, która będzie tłem do rysowania,
  - narysuj zielone koło, czerwony prostokąt i białą linię na ww. macierzy,  
  - umieść napis ze swoim numerem albumu w lewym dolnym rogu macierzy,
  - zapisz obraz wyjściowy w sposób podany w wytycznych.  

##### Zad. 3. 
  - wczytaj kolorowy obraz,
  - zmień kolor lewego górnego rogu obrazu (o wymiarach 30 x 30) na zielony,  
  - zmień kolor prawego dolnego rogu obrazu (o wymiarach 25 x 25) na czerwony,
  - zapisz obraz wyjściowy w sposób podany w wytycznych.  

##### Zad. 4. 
  - wczytaj kolorowy obraz,
  - wyświetl jego wysokość i szerokość,
  - zmień jego rozmiar korzystając z pakietu `imutils`, tak aby wysokość wynosiła 400 px,
  - dokonaj odbicia pionowego obrazu,  
  - wyświetl jego wysokość i szerokość po zmianach,  
  - zapisz obraz wyjściowy w sposób podany w wytycznych.  

##### Zad. 5. 
  - wczytaj kolorowy obraz,
  - wyświetl wartości RGB punktu o współrzędnych (0, 0),  
  - utwórz macierz `M1` o takich samych wymiarach jak obraz wejściowy zawierający same liczby 30,
  - od obrazu wejściowego odejmij macierz M1 i zapisz wynik jako nową zmienną,  
  - wyświetl wartości RGB punktu o współrzędnych (0, 0) w nowym obrazie,  
  - zapisz obraz wyjściowy w sposób podany w wytycznych.  

##### Zad. 6. 
  - wczytaj kolorowy obraz i przekonwertuj go na obraz w skali szarości,
  - zastosuj progowanie adaptacyjne z rozmiarem bloku 13 i stałą C o wartości 3,
  - zapisz obraz wyjściowy w sposób podany w wytycznych.  

##### Zad. 7. 
  - wczytaj kolorowy obraz i przekonwertuj go na obraz w skali szarości,  
  - dokonaj na obrazie rozmycia medianowego o rozmiarze 5,  
  - zastosuj progowanie Otsu,  
  - zapisz obraz wyjściowy w sposób podany w wytycznych.  


##### Zad. 8. 
  - utwórz listę `obrazki`, a w niej zapisz dwie ścieżki do dwóch różnych obrazków, ale o takich samych rozmiarach,  
  - w pętli `for` wyświetl ich wysokość, szerokość, liczbę kanałów i współrzędne środka,
  - przekonwertuj oba obrazy wejściowe na obrazy w skali szarości,
  - na pierwszym obrazie zastosuj proste progowanie z progiem ustawionym na 127,  
  - na drugim obrazie zastosuj rozmycie Gaussowskie o rozmiarze (3, 3),  
  - utwórz obraz wyjściowy będący połączeniem obu ww. obrazów za pomocą funkcji `hconcat()`,  
  - zapisz obraz wyjściowy w sposób podany w wytycznych.  

