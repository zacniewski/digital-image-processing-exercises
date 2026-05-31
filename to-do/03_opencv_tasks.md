# Zadania: Wprowadzenie do OpenCV

### Instrukcja oddawania zadań

- Każde rozwiązanie musi być zapisane w **osobnym pliku Pythona**.
- Nazwa pliku musi zawierać **Twoje nazwisko** (np. `01_nazwisko.py`).
- Tam, gdzie zadanie generuje wynik wizualny, wykonaj **zrzut ekranu** i zapisz go jako plik obrazu.
- Po realizacji wszystkich zadań należy je wysłać (wraz ze zrzutami ekranu) na **maila prowadzącego**.
- **Nie wysyłamy środowiska wirtualnego (`venv`)**.

______________________________________________________________________

Poniżej znajduje się 10 zadań dotyczących podstaw pracy z biblioteką OpenCV.

1. **Wczytanie i wyświetlenie obrazu**

   - Zadanie: Wczytaj plik graficzny z dysku i wyświetl go w oknie o nazwie "Podglad".
   - Podpowiedź: Użyj `cv2.imread()` i `cv2.imshow()`. Pamiętaj o `cv2.waitKey(0)`.

1. **Zapisywanie obrazu**

   - Zadanie: Wczytaj obraz, przekonwertuj go na skalę szarości i zapisz jako nowy plik `.jpg`.
   - Podpowiedź: Do konwersji użyj `cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)`, a do zapisu `cv2.imwrite()`.

1. **Pobieranie wartości piksela**

   - Zadanie: Wczytaj obraz i wypisz w konsoli wartości kolorów (B, G, R) piksela znajdującego się w samym środku obrazu.
   - Podpowiedź: Pobierz wysokość i szerokość z `img.shape`, a następnie odwołaj się do `img[y, x]`.

1. **Rysowanie linii**

   - Zadanie: Stwórz czarny obraz 500x500 i narysuj na nim niebieską linię przekątną (od lewego górnego do prawego dolnego rogu).
   - Podpowiedź: Użyj `cv2.line(img, start_point, end_point, color, thickness)`.

1. **Rysowanie okręgów i prostokątów**

   - Zadanie: Na obrazie narysuj zielony prostokąt oraz czerwone wypełnione koło wewnątrz niego.
   - Podpowiedź: Użyj `cv2.rectangle()` oraz `cv2.circle()`. Dla wypełnienia użyj `thickness=-1`.

1. **Wypisywanie tekstu**

   - Zadanie: Na wczytanym obrazie umieść napis "Hello OpenCV" w dolnym prawym rogu.
   - Podpowiedź: Użyj `cv2.putText()`. Pamiętaj o dobraniu odpowiedniej czcionki (np. `cv2.FONT_HERSHEY_SIMPLEX`).

1. **Zmiana rozmiaru (Resizing)**

   - Zadanie: Zmniejsz wczytany obraz dwukrotnie (zachowując proporcje).
   - Podpowiedź: Użyj `cv2.resize()`. Możesz podać docelowe wymiary lub współczynniki skalowania `fx` i `fy`.

1. **Wycinanie ROI (Region of Interest)**

   - Zadanie: Wczytaj obraz, pozwól użytkownikowi wybrać fragment (np. oko na zdjęciu twarzy) i wyświetl tylko ten fragment w nowym oknie.
   - Podpowiedź: ROI to po prostu wycinanie fragmentu macierzy NumPy: `roi = img[y1:y2, x1:x2]`.

1. **Odbicie lustrzane**

   - Zadanie: Stwórz kopię obrazu, która jest jego odbiciem lustrzanym w poziomie.
   - Podpowiedź: Użyj funkcji `cv2.flip(img, 1)`.

1. **Tworzenie prostego GUI z suwakiem**

   - Zadanie: Stwórz okno z suwakiem (Trackbar), który będzie kontrolował jasność wyświetlanego obrazu.
   - Podpowiedź: Użyj `cv2.createTrackbar()` i funkcji zwrotnej (callback), która będzie aktualizować obraz.
