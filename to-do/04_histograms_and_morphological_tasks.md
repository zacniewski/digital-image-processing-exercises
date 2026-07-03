# Zadania: Histogramy, equalizacja i operacje morfologiczne

### Instrukcja oddawania zadań

- Każde rozwiązanie musi być zapisane w **osobnym pliku Pythona**.
- Nazwa pliku musi zawierać **Twoje nazwisko** (np. `01_nazwisko.py`).
- Wybieramy 15 dowolnych zadań. Pamiętajmy o numeracji, gdy wybierzemy np. zadania z takim samym numerem z różnych sekcji (można nazwać plik np. `10b_Kowalski.py`)
- Tam, gdzie zadanie generuje wynik wizualny, wykonaj **zrzut ekranu** i zapisz go jako plik obrazu.
- W pozostałych przypadkach umieść rezultat działania w osobnym pliku tekstowym lub jako komentarz w pliku z rozwiązaniem.
- Po realizacji wszystkich zadań należy je wysłać (wraz ze zrzutami ekranu) na **maila prowadzącego**.
- **Nie wysyłamy środowiska wirtualnego (`.venv` lub `my_env` lub inna nazwa )**.
- Proszę pamiętać, że do zaliczenia przedmiotu konieczne jest m.in. wysłanie zadań ze wszystkich laboratoriów!

______________________________________________________________________

Poniżej znajduje się 10 zadań dotyczących histogramów i equalizacji obrazów w OpenCV oraz 10 zadań z operacji morfologicznych.

1. **Histogram obrazu w skali szarości**

   - Zadanie: Wczytaj obraz w skali szarości i oblicz jego histogram za pomocą funkcji `cv2.calcHist()`. Wyświetl histogram jako wykres przy użyciu `matplotlib`.
   - Podpowiedź: `cv2.calcHist([img], [0], None, [256], [0, 256])`. Użyj `plt.plot()` do rysowania.
   - Pomocne skrypty: `scripts/opencv_histogram_grayscale.py`

1. **Histogram obrazu kolorowego**

   - Zadanie: Wczytaj kolorowy obraz i oblicz osobne histogramy dla kanałów B, G i R. Wyświetl je na jednym wykresie w odpowiednich kolorach.
   - Podpowiedź: Iteruj po kanałach: `for i, kolor in enumerate(["b", "g", "r"])` i wywołuj `cv2.calcHist()` dla każdego kanału osobno.
   - Pomocne skrypty: `scripts/opencv_histograms_color.py`

1. **Equalizacja histogramu (skala szarości)**

   - Zadanie: Wczytaj obraz w skali szarości, zastosuj equalizację histogramu i wyświetl obraz przed i po operacji obok siebie.
   - Podpowiedź: Użyj funkcji `cv2.equalizeHist()`. Do wyświetlenia obok siebie użyj `np.hstack()`.
   - Pomocne skrypty: `scripts/opencv_histogram_equalize.py`

1. **CLAHE — adaptacyjna equalizacja histogramu**

   - Zadanie: Zastosuj metodę CLAHE (Contrast Limited Adaptive Histogram Equalization) na obrazie w skali szarości i porównaj wynik ze zwykłą equalizacją.
   - Podpowiedź: Utwórz obiekt CLAHE: `clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))`, a następnie wywołaj `clahe.apply(img)`.
   - Pomocne skrypty: `scripts/opencv_histogram_equalize.py`

1. **Skumulowany histogram (CDF)**

   - Zadanie: Oblicz i wyświetl skumulowany histogram (CDF — Cumulative Distribution Function) dla obrazu w skali szarości.
   - Podpowiedź: Użyj funkcji `np.cumsum()` na tablicy histogramu. Wyświetl wynik za pomocą `plt.plot()`.

1. **Rozciąganie kontrastu**

   - Zadanie: Wczytaj obraz o niskim kontraście (lub sztucznie go zmniejsz). Zastosuj rozciąganie kontrastu tak, aby minimalna wartość piksela wynosiła 0, a maksymalna 255.
   - Podpowiedź: Użyj `cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)`.

1. **Equalizacja obrazu kolorowego (przestrzeń HSV)**

   - Zadanie: Wczytaj kolorowy obraz, przekonwertuj go do przestrzeni HSV, zastosuj equalizację histogramu tylko na kanale V (jasność), a następnie przekonwertuj z powrotem do BGR i zapisz wynik.
   - Podpowiedź: `hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)`, następnie `hsv[:,:,2] = cv2.equalizeHist(hsv[:,:,2])`.
   - Pomocne skrypty: `scripts/opencv_histogram_equalize.py`

1. **Detekcja prześwietlenia i niedoświetlenia**

   - Zadanie: Napisz funkcję, która na podstawie histogramu obrazu w skali szarości ocenia, czy obraz jest prześwietlony (zbyt wiele pikseli o wartości bliskiej 255) lub niedoświetlony (zbyt wiele pikseli o wartości bliskiej 0).
   - Podpowiedź: Sprawdź, jaki procent pikseli ma wartość powyżej 240 (prześwietlenie) lub poniżej 15 (niedoświetlenie).

1. **Histogram z maską lub w obszarze ROI**

   - Zadanie: Wczytaj obraz w skali szarości lub kolorowy, wybierz prostokątny obszar ROI albo maskę binarną, a następnie oblicz histogram tylko dla wskazanego fragmentu. Porównaj go z histogramem całego obrazu.
   - Podpowiedź: W `cv2.calcHist()` jako trzeci argument przekaż maskę. Dla ROI możesz wyciąć fragment obrazu przez `img[y1:y2, x1:x2]`.

1. **Dopasowanie histogramu do obrazu referencyjnego**

   - Zadanie: Wczytaj dwa obrazy w skali szarości: źródłowy i referencyjny. Zaimplementuj dopasowanie histogramu obrazu źródłowego do histogramu obrazu referencyjnego na podstawie CDF.
   - Podpowiedź: Oblicz histogramy, przekształć je do CDF, a potem zbuduj mapowanie intensywności pikseli ze źródła na wartości z obrazu referencyjnego.

______________________________________________________________________

## Operacje morfologiczne

1. **Erozja obrazu binarnego**

   - Zadanie: Wczytaj obraz w skali szarości, zbinaryzuj go progowaniem, a następnie zastosuj erozję z jądrem 5×5. Wyświetl obraz przed i po operacji obok siebie.
   - Podpowiedź: Utwórz jądro: `kernel = np.ones((5, 5), np.uint8)`, następnie wywołaj `cv2.erode(img, kernel, iterations=1)`.
   - Pomocne skrypty: `scripts/opencv_morphological_ops.py`

1. **Dylatacja obrazu binarnego**

   - Zadanie: Wczytaj obraz w skali szarości, zbinaryzuj go progowaniem, a następnie zastosuj dylatację z jądrem 5×5. Wyświetl obraz przed i po operacji obok siebie.
   - Podpowiedź: Użyj `cv2.dilate(img, kernel, iterations=1)`. Porównaj efekt z erozją z poprzedniego zadania.
   - Pomocne skrypty: `scripts/opencv_morphological_ops.py`

1. **Otwarcie morfologiczne (Opening)**

   - Zadanie: Wczytaj obraz zawierający tekst lub drobne obiekty z szumem. Zastosuj operację otwarcia z jądrami o rozmiarach 3×3, 5×5 i 7×7. Porównaj wyniki i opisz, jak zmienia się efekt wraz z rozmiarem jądra.
   - Podpowiedź: `opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)`. Otwarcie = erozja + dylatacja — usuwa małe szumy z tła.
   - Pomocne skrypty: `scripts/opencv_morphological_ops.py`

1. **Domknięcie morfologiczne (Closing)**

   - Zadanie: Wczytaj obraz binarny z obiektami posiadającymi małe dziury lub przerwy. Zastosuj operację domknięcia z jądrami o rozmiarach 3×3, 5×5 i 7×7. Porównaj wyniki.
   - Podpowiedź: `closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)`. Domknięcie = dylatacja + erozja — wypełnia małe dziury wewnątrz obiektów.
   - Pomocne skrypty: `scripts/opencv_morphological_ops.py`

1. **Gradient morfologiczny**

   - Zadanie: Oblicz gradient morfologiczny obrazu binarnego (różnica między dylatacją a erozją). Wyświetl wynik i opisz, co przedstawia.
   - Podpowiedź: `gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)`. Gradient morfologiczny uwydatnia krawędzie obiektów.
   - Pomocne skrypty: `scripts/opencv_morphological_ops.py`

1. **Top Hat i Black Hat**

   - Zadanie: Zastosuj transformacje Top Hat (`MORPH_TOPHAT`) i Black Hat (`MORPH_BLACKHAT`) na obrazie w skali szarości. Wyświetl oryginał oraz oba wyniki obok siebie i opisz różnicę.
   - Podpowiedź: `tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)` wyodrębnia jasne szczegóły mniejsze od jądra; `blackhat` — ciemne.
   - Pomocne skrypty: `scripts/opencv_morphological_hats.py`

1. **Różne kształty jąder strukturalnych**

   - Zadanie: Zastosuj erozję na tym samym obrazie binarnym, używając trzech różnych kształtów jądra: prostokątnego (`MORPH_RECT`), eliptycznego (`MORPH_ELLIPSE`) i krzyżowego (`MORPH_CROSS`). Porównaj wyniki.
   - Podpowiedź: `kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))`. Zmień typ jądra i porównaj efekty wizualnie.
   - Pomocne skrypty: `scripts/opencv_morphological_ops.py`

1. **Wpływ liczby iteracji operacji morfologicznej**

   - Zadanie: Na tym samym obrazie binarnym zastosuj erozję i dylatację z różną liczbą iteracji, np. 1, 3 i 5. Porównaj, jak zmienia się wynik wraz ze wzrostem liczby iteracji.
   - Podpowiedź: Użyj parametru `iterations` w `cv2.erode()` i `cv2.dilate()`.

1. **Wypełnianie dziur w obiektach binarnych**

   - Zadanie: Wczytaj binarny obraz zawierający obiekty z dziurami wewnętrznymi. Zastosuj operację, która wypełni te dziury i wyświetl wynik przed oraz po przetworzeniu.
   - Podpowiedź: Możesz wykorzystać kombinację `floodFill()`, negacji obrazu i operacji morfologicznych albo domknięcie z odpowiednio dobranym jądrem.

1. **Czyszczenie obrazu sekwencją opening i closing**

   - Zadanie: Wczytaj binarny obraz z drobnym szumem i przerwami w obiektach. Najpierw zastosuj otwarcie, a potem domknięcie morfologiczne. Porównaj efekt z obrazem wyjściowym.
   - Podpowiedź: Połącz `cv2.MORPH_OPEN` i `cv2.MORPH_CLOSE`, aby jednocześnie usuwać drobne zakłócenia i uzupełniać niewielkie luki.
