# Importowanie biblioteki argparse do obsługi argumentów wiersza poleceń
import argparse

# Importowanie biblioteki OpenCV do przetwarzania obrazów
import cv2

# Importowanie biblioteki imutils, która ułatwia operacje takie jak obracanie czy przesuwanie
import imutils

# Inicjalizacja parsera argumentów
ap = argparse.ArgumentParser()
# Dodanie argumentu --image (lub -i), określającego ścieżkę do obrazu wejściowego
ap.add_argument("-i", "--image", required=True, help="path to input image")
# Parsowanie argumentów i konwersja na słownik
args = vars(ap.parse_args())

# Wczytanie obrazu z dysku
image = cv2.imread(args["image"])

# Przesunięcie obrazu o -50 pikseli w poziomie (w lewo) i 0 w pionie przy użyciu imutils
shifted = imutils.translate(image, -50, 0)
# Wyświetlenie oryginalnego obrazu
cv2.imshow("Original", image)
# Wyświetlenie przesuniętego obrazu
cv2.imshow("Translated", shifted)

# Obrócenie obrazu o -33 stopnie (zgodnie z ruchem wskazówek zegara)
rotated = imutils.rotate(image, -33)
# Wyświetlenie obróconego obrazu (może dojść do ucięcia rogów)
cv2.imshow("Rotated by 180 Degrees", rotated)

# Obrócenie obrazu o -33 stopnie z zachowaniem całego obrazu (bez ucinania rogów)
rotated2 = imutils.rotate_bound(image, -33)
# Wyświetlenie obróconego obrazu bez ucinania
cv2.imshow("Rotated Without Cropping", rotated2)

# Wyświetlenie wymiarów oryginalnego obrazka w konsoli
print(f"Wymiary oryginalnego obrazka to: {image.shape}")

# Definiowanie nowej szerokości obrazu
nowa_szerokosc = 500

# Obliczenie współczynnika proporcji, aby zachować skalę obrazu
r = nowa_szerokosc / image.shape[1]
# Wyświetlenie współczynnika proporcji w konsoli
print(f"Współczynnik proporcji r = {r}")

# Obliczenie nowych wymiarów (szerokość, wysokość) na podstawie współczynnika r
dim = (nowa_szerokosc, int(image.shape[0] * r))
# Wyświetlenie nowych wymiarów w konsoli
print(f"Nowe wymiary to: {dim}")

# Zmiana rozmiaru obrazu przy użyciu funkcji OpenCV cv2.resize i interpolacji INTER_AREA
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
# Wyświetlenie przeskalowanego obrazu
cv2.imshow("Resized", resized)

# Zmiana rozmiaru obrazu przy użyciu funkcji pomocniczej imutils (automatycznie zachowuje proporcje)
resized2 = imutils.resize(image, width=500)
# Wyświetlenie obrazu przeskalowanego przez imutils
cv2.imshow("Resized 2", resized2)

# Wykonanie odbicia lustrzanego w poziomie (oś Y) - parametr 1
flipped = cv2.flip(image, 1)
# Wyświetlenie odbicia poziomego
cv2.imshow("Odbicie poziome", flipped)

# Wykonanie odbicia lustrzanego w pionie (oś X) - parametr 0
flipped = cv2.flip(image, 0)
# Wyświetlenie odbicia pionowego
cv2.imshow("Odbicie pionowe", flipped)

# Wykonanie odbicia lustrzanego w obu osiach jednocześnie - parametr -1
flipped = cv2.flip(image, -1)
# Wyświetlenie odbicia podwójnego
cv2.imshow("Odbicia: poziome i pionowe", flipped)

# Oczekiwanie na naciśnięcie dowolnego klawisza przed zamknięciem okien
cv2.waitKey(0)
