# Zadania: Histogramy, equalizacja i operacje morfologiczne

### Instrukcja oddawania zadań

- Każde rozwiązanie musi być zapisane w **osobnym pliku Pythona**.
- Nazwa pliku musi zawierać **Twoje nazwisko** (np. `01_nazwisko.py`).
- Wybieramy 15 dowolnych zadań. Pamiętajmy o numeracji, gdy wybierzemy np. zadania z takim samym numerem z różnych sekcji (można nazwać plik np. `10b_Kowalski.py`)
- Tam, gdzie zadanie generuje wynik wizualny, wykonaj **zrzut ekranu** i zapisz go jako plik obrazu.
- W pozostałych przypadkach umieść rezultat działania w osobnym pliku tekstowym lub jako komentarz w pliku z rozwiązaniem.
- Po realizacji wszystkich zadań należy je wysłać (wraz ze zrzutami ekranu) na **maila prowadzącego**.
- **Nie wysyłamy środowiska wirtualnego (`venv`)**.
- Proszę pamiętać, że do zaliczenia przedmiotu konieczne jest m.in. wysłanie zadań ze wszystkich laboratoriów!

______________________________________________________________________

Poniżej znajduje się 15 zadań dotyczących histogramów i equalizacji obrazów w OpenCV oraz 10 zadań z operacji morfologicznych.

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

1. **Porównanie histogramów przed i po equalizacji**

   - Zadanie: Dla obrazu w skali szarości wyświetl na jednym wykresie dwa histogramy: przed equalizacją i po equalizacji. Opisz osie i dodaj legendę.
   - Podpowiedź: Wywołaj `cv2.calcHist()` dwukrotnie — raz dla oryginalnego obrazu, raz dla obrazu po `cv2.equalizeHist()`. Użyj `plt.legend()`.
   - Pomocne skrypty: `scripts/opencv_histogram_equalize.py`, `scripts/opencv_histogram_grayscale.py`

1. **CLAHE — adaptacyjna equalizacja histogramu**

   - Zadanie: Zastosuj metodę CLAHE (Contrast Limited Adaptive Histogram Equalization) na obrazie w skali szarości i porównaj wynik ze zwykłą equalizacją.
   - Podpowiedź: Utwórz obiekt CLAHE: `clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))`, a następnie wywołaj `clahe.apply(img)`.
   - Pomocne skrypty: `scripts/opencv_histogram_equalize.py`

1. **Histogram z maską**

   - Zadanie: Wczytaj obraz w skali szarości, utwórz maskę (np. prostokąt w centrum obrazu) i oblicz histogram tylko dla zamaskowanego obszaru.
   - Podpowiedź: Utwórz maskę jako czarną macierz (`np.zeros`) i ustaw wybrany obszar na 255. Przekaż maskę jako trzeci argument `cv2.calcHist()`.

1. **Normalizacja histogramu**

   - Zadanie: Oblicz histogram obrazu w skali szarości, a następnie znormalizuj go tak, aby suma wszystkich wartości wynosiła 1 (histogram prawdopodobieństwa). Wyświetl wynik.
   - Podpowiedź: Podziel wartości histogramu przez całkowitą liczbę pikseli: `hist / hist.sum()` lub użyj `cv2.normalize()`.

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

1. **Porównanie jasności dwóch obrazów**

   - Zadanie: Wczytaj dwa różne obrazy w skali szarości i wyświetl ich histogramy na jednym wykresie. Na podstawie histogramów oceń, który obraz jest jaśniejszy.
   - Podpowiedź: Oblicz średnią wartość pikseli (`img.mean()`) dla każdego obrazu i wyświetl ją w tytule wykresu.

1. **Detekcja prześwietlenia i niedoświetlenia**

   - Zadanie: Napisz funkcję, która na podstawie histogramu obrazu w skali szarości ocenia, czy obraz jest prześwietlony (zbyt wiele pikseli o wartości bliskiej 255) lub niedoświetlony (zbyt wiele pikseli o wartości bliskiej 0).
   - Podpowiedź: Sprawdź, jaki procent pikseli ma wartość powyżej 240 (prześwietlenie) lub poniżej 15 (niedoświetlenie).

1. **Histogram dla wybranego kanału koloru**

   - Zadanie: Wczytaj kolorowy obraz i wyświetl histogram tylko dla kanału czerwonego (R). Znajdź wartość jasności, która występuje najczęściej (dominantę).
   - Podpowiedź: Kanał czerwony w OpenCV to indeks 2: `img[:,:,2]`. Dominantę znajdziesz przez `np.argmax(hist)`.

1. **Backprojection (rzutowanie wsteczne)**

   - Zadanie: Korzystając z funkcji `cv2.calcBackProject()`, znajdź na obrazie obszary o podobnej kolorystyce do zadanego wzorca (np. wycinka obrazu).
   - Podpowiedź: Oblicz histogram wzorca w przestrzeni HSV, a następnie użyj go jako modelu w `cv2.calcBackProject()`.
   - Pomocne skrypty: `scripts/opencv_color_tracking.py`

1. **Zapis wykresu histogramu do pliku**

   - Zadanie: Oblicz histogram kolorowego obrazu dla wszystkich trzech kanałów i zapisz wykres jako plik graficzny `histogram.png` bez wyświetlania go na ekranie.
   - Podpowiedź: Zamiast `plt.show()` użyj `plt.savefig("histogram.png")`. Pamiętaj o wywołaniu `plt.close()` po zapisaniu.
   - Pomocne skrypty: `scripts/opencv_histograms_color.py`

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

1. **Wpływ liczby iteracji na erozję i dylatację**

   - Zadanie: Zastosuj erozję i dylatację na tym samym obrazie binarnym, zmieniając liczbę iteracji (1, 2, 3). Wyświetl wszystkie wyniki w jednym oknie i opisz zaobserwowane różnice.
   - Podpowiedź: Użyj pętli `for i in range(1, 4)` i wywołuj `cv2.erode()` / `cv2.dilate()` z parametrem `iterations=i`.
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

1. **Usuwanie szumu metodą otwarcia**

   - Zadanie: Wczytaj obraz z drobnym szumem (lub dodaj szum funkcją `cv2.randn()`). Zastosuj operację otwarcia, aby usunąć szum, a następnie domknięcia, aby wypełnić ewentualne dziury. Wyświetl kolejne etapy przetwarzania.
   - Podpowiedź: Szum sól i pieprz możesz dodać ręcznie, losowo ustawiając piksele na 0 lub 255. Następnie zastosuj `MORPH_OPEN`, a potem `MORPH_CLOSE`.

1. **Ekstrakcja szkieletu obiektu (Skeletonization)**

   - Zadanie: Zaimplementuj uproszczoną skeletonizację obiektu binarnego przy użyciu wielokrotnej erozji i gradientu morfologicznego. Wyświetl szkielet nałożony na oryginalny obraz.
   - Podpowiedź: W pętli wykonuj erozję obrazu, obliczaj otwarcie zerodowanego obrazu, a następnie odejmuj otwarcie od zerodowanego obrazu i dodawaj wynik do szkieletu: `skeleton = cv2.bitwise_or(skeleton, cv2.subtract(eroded, cv2.morphologyEx(eroded, cv2.MORPH_OPEN, kernel)))`. Powtarzaj, aż obraz stanie się pusty.
