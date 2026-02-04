# Digital-Image-Processing

## Spis treści
- [Opis projektu](#opis-projektu)
- [Wymagania i instalacja](#wymagania-i-instalacja)
- [Uruchamianie wybranych skryptów](#uruchamianie-wybranych-skryptów)
- [Przegląd skryptów](#przegląd-skryptów)
  - [Podstawy pracy z obrazami](#podstawy-pracy-z-obrazami)
  - [Transformacje geometryczne](#transformacje-geometryczne)
  - [Operacje arytmetyczne i logiczne](#operacje-arytmetyczne-i-logiczne)
  - [Histogramy i equalizacja](#histogramy-i-equalizacja)
  - [Progowanie (thresholding)](#progowanie-thresholding)
  - [Operacje morfologiczne](#operacje-morfologiczne)
  - [Krawędzie i kontury](#krawędzie-i-kontury)
  - [Wideo: odczyt, zapis, właściwości](#wideo-odczyt-zapis-właściwości)
  - [Detekcja obiektów i twarzy](#detekcja-obiektów-i-twarzy)
  - [Aplikacje webowe (Flask + OpenCV)](#aplikacje-webowe-flask--opencv)
  - [Inne narzędzia i przykłady](#inne-narzędzia-i-przykłady)
- [Teoria: wybrane algorytmy](#teoria-wybrane-algorytmy)
  - [Reprezentacja obrazu i przestrzenie barw](#reprezentacja-obrazu-i-przestrzenie-barw)
  - [Interpolacja i skalowanie](#interpolacja-i-skalowanie)
  - [Operacje arytmetyczne i logiczne na obrazach](#operacje-arytmetyczne-i-logiczne-na-obrazach)
  - [Histogram, equalizacja i CLAHE](#histogram-equalizacja-i-clahe)
  - [Filtrowanie liniowe i nieliniowe](#filtrowanie-liniowe-i-nieliniowe)
  - [Wykrywanie krawędzi (Sobel, Canny)](#wykrywanie-krawędzi-sobel-canny)
  - [Progowanie globalne i adaptacyjne, Otsu](#progowanie-globalne-i-adaptacyjne-otsu)
  - [Morfologia matematyczna](#morfologia-matematyczna)
  - [Kontury i momenty geometryczne](#kontury-i-momenty-geometryczne)
  - [Detektory obiektów: Haar Cascades](#detektory-obiektów-haar-cascades)
- [Licencja](#licencja)

## Opis projektu
Zbiór ćwiczeń z przetwarzania obrazów w Pythonie z wykorzystaniem bibliotek OpenCV oraz NumPy (i opcjonalnie Flask dla warstwy webowej). Repozytorium zawiera krótkie skrypty demonstrujące kluczowe techniki i algorytmy.

## Wymagania i instalacja
- Python 3.12+
- Pakiety z `requirements.txt`:
  - opencv-python, numpy, matplotlib, pillow, itp.
- Uwaga: część skryptów używa biblioteki `flask` (aplikacje webowe) oraz `imutils` (proste transformaty). Jeśli ich brakuje, zainstaluj:

```bash
pip install flask imutils
pip install -r requirements.txt
```

## Uruchamianie wybranych skryptów
- Większość skryptów przyjmuje parametr `--image` ze ścieżką do pliku, np.:

```bash
python scripts/images1.py --image obrazki/obrazek.jpg
```

- Aplikacje webowe (Flask):

```bash
python web/hello.py
python web/hello_opencv.py
```

Następnie odwiedź odpowiednie endpointy, np. `/canny?url=...` (zob. `web/links.md`).

## Przegląd skryptów
### Podstawy pracy z obrazami
- `scripts/images1.py` – odczyt pikseli, modyfikacja fragmentów, dzielenie obrazu na ćwiartki.
- `scripts/images2.py` – przesunięcie, rotacja (z i bez kadrowania), skalowanie, odbicia lustrzane.
- `scripts/images3.py` – kadrowanie (crop) wokół środka obrazu.
- `scripts/images4.py` – operacje arytmetyczne: rozjaśnianie i przyciemnianie.
- `scripts/images5.py` – operacje logiczne: AND, OR, XOR, NOT na maskach.
- `scripts/images6.py` – dodatkowe przykłady operacji na obrazach (jeśli występują).

### Transformacje geometryczne
- `scripts/image_drawing.py`, `scripts/rysowanie.py` – rysowanie prymitywów i tekstu.
- `scripts/mouse_and_trackbar_gui.py` – GUI: obsługa myszy i suwaków.

### Operacje arytmetyczne i logiczne
- `scripts/images4.py`, `scripts/images5.py` – suma/różnica, operacje bitowe na maskach.

### Histogramy i equalizacja
- `scripts/histogram_grayscale.py`, `scripts/histograms_color.py`, `scripts/histogram_equalize.py` – generowanie histogramów, equalizacja, CLAHE.

### Progowanie (thresholding)
- `scripts/thresholding.py`, `scripts/thresholding2.py`, `scripts/thresholding3.py`, `scripts/thresholding4.py`, `scripts/thresholding5.py` – progowanie globalne, Otsu, adaptacyjne i warianty flag.

### Operacje morfologiczne
- `scripts/morphological_ops.py`, `scripts/morphological_hats.py` – erozja, dylatacja, otwarcie, domknięcie, top-hat, black-hat.

### Krawędzie i kontury
- `scripts/edge_detection.py`, `scripts/contour_detection.py`, `scripts/canny_tracker.py` – filtry gradientowe, Canny, wykrywanie konturów i ich analiza.

### Wideo: odczyt, zapis, właściwości
- `scripts/video1_capture_properties.py`, `scripts/video2_reading_from_file.py`, `scripts/video3_writing_from_camera.py`, `scripts/video_from_image.py` – praca z kamerą/plikiem, zapis i generowanie wideo.

### Detekcja obiektów i twarzy
- `scripts/detect_faces.py`, `scripts/color_tracking.py`, `scripts/text_recognition.py` – detekcja twarzy (Haar), śledzenie koloru, OCR (jeśli skonfigurowany backend).

### Aplikacje webowe (Flask + OpenCV)
- `web/hello.py` – minimalny Hello World we Flask.
- `web/hello_opencv.py` – proste API obrazowe: Canny, blur, threshold adaptacyjny.

### Inne narzędzia i przykłady
- `scripts/check_cv_version.py` – wypisanie wersji OpenCV.
- `scripts/functions_import.py`, `scripts/functions_usage.py`, `scripts/numpy_basics.py`, `scripts/loops.py`, `scripts/opencv_tetris.py` – drobne przykłady i demonstratory składni/operacji.

## Teoria: wybrane algorytmy
### Reprezentacja obrazu i przestrzenie barw
- Obraz kolorowy reprezentowany jest zazwyczaj jako macierz H×W×3 w porządku BGR (w OpenCV). Skala 8-bit: wartości 0–255. Konwersje kolorów: `cv2.cvtColor`, np. BGR↔GRAY, BGR↔HSV, BGR↔LAB.
- HSV separuje barwę i jasność, ułatwiając segmentację koloru; LAB lepiej modeluje percepcję jasności (L*). Grayscale upraszcza obliczenia, gdy kolor nie jest istotny.

### Interpolacja i skalowanie
- Zmiana rozmiaru (`cv2.resize`) wymaga interpolacji: `INTER_NEAREST` (najszybsza, pikselowa), `INTER_LINEAR` (domyślna), `INTER_AREA` (skalowanie w dół), `INTER_CUBIC` (skalowanie w górę – wyższa jakość, wolniejsze).
- Rotacja i przesunięcie: macierz transformacji afinicznej (`cv2.getRotationMatrix2D`, `cv2.warpAffine`), a wysokopoziomowo funkcje z `imutils` upraszczają użycie.

### Operacje arytmetyczne i logiczne na obrazach
- `cv2.add`, `cv2.subtract` działają z nasyceniem (clamping). Operacje bitowe (`bitwise_and`, `bitwise_or`, `bitwise_xor`, `bitwise_not`) pracują najczęściej na maskach (obrazy binarne), ale i na obrazach 8-bitowych per kanał.

### Histogram, equalizacja i CLAHE
- Histogram obrazu to rozkład liczby pikseli po poziomach intensywności. Equalizacja (`cv2.equalizeHist`) rozszerza dynamiczny zakres jasności i zwiększa kontrast w obrazach o wąskim histogramie. CLAHE (Contrast Limited Adaptive Histogram Equalization) działa lokalnie i ogranicza wzmacnianie szumu.

### Filtrowanie liniowe i nieliniowe
- Rozmycie uśredniające (`cv2.blur`), Gaussa (`cv2.GaussianBlur`) – usuwanie szumu kosztem ostrości. Medianowe (`cv2.medianBlur`) – dobrze redukuje szum impulsowy, zachowując krawędzie. Filtry gradientowe (Sobel, Scharr, Laplacian) aproksymują pochodne obrazu.

### Wykrywanie krawędzi (Sobel, Canny)
- Sobel szacuje gradient jasności w kierunkach X/Y, a moduł gradientu wskazuje krawędzie. Canny: (1) odszumianie Gaussowskie, (2) gradient Sobela, (3) supresja niemaksymalna, (4) podwójny próg i histereza łączenia krawędzi. Progi dobieramy eksperymentalnie lub adaptacyjnie.

### Progowanie globalne i adaptacyjne, Otsu
- Progowanie binarne: `cv2.threshold(img, T, maxVal, typ)`. Otsu automatycznie dobiera próg minimalizując wariancję wewnątrzklasową. Adaptacyjne progowanie (`cv2.adaptiveThreshold`) wyznacza lokalny próg w sąsiedztwie piksela (np. metoda średniej lub Gaussa), dobre przy nierównomiernym oświetleniu.

### Morfologia matematyczna
- Operacje na obrazach binarnych (i nie tylko) z elementem strukturalnym: erozja (zmniejsza białe obszary), dylatacja (powiększa), otwarcie (erozja→dylatacja – usuwa drobne szumy), domknięcie (dylatacja→erozja – wypełnia dziury). Top-hat wydobywa jasne detale; black-hat – ciemne detale na jasnym tle.

### Kontury i momenty geometryczne
- `cv2.findContours` zwraca kontury (zarysy) na obrazie binarnym. Analiza konturów: pole, obwód, prostokąty ograniczające, dopasowanie elipsy, momenty geometryczne (np. środek masy). Przydatne do segmentacji i śledzenia obiektów.

### Detektory obiektów: Haar Cascades
- Klasyfikatory kaskadowe Haar opierają się na cechach Haar i algorytmie AdaBoost, wykorzystując kaskadową strukturę do szybkiego odrzucania negatywów. W repo znajdują się gotowe pliki kaskad (np. twarze, oczy). Parametry: `scaleFactor`, `minNeighbors`, `minSize` wpływają na czułość i precyzję.

## Licencja
Materiały edukacyjne – przeznaczone do nauki i demonstracji. Prawa do obrazów i kaskad zgodnie z ich źródłami/licencjami.
