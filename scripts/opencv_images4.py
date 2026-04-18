# Importowanie biblioteki argparse do obsługi argumentów wiersza poleceń
import argparse

# Importowanie biblioteki OpenCV do przetwarzania obrazów
import cv2

# Importowanie biblioteki numpy do operacji na macierzach
import numpy as np

# Inicjalizacja parsera argumentów
ap = argparse.ArgumentParser()
# Dodanie argumentu --image (lub -i), określającego ścieżkę do obrazu wejściowego
ap.add_argument("-i", "--image", required=True, help="path to input image")
# Parsowanie argumentów i konwersja na słownik
args = vars(ap.parse_args())

# Wczytanie obrazu z dysku
image = cv2.imread(args["image"])

# Wyświetlenie oryginalnego obrazu
cv2.imshow("Original", image)

# Tworzenie macierzy o tych samych wymiarach co obraz, wypełnionej wartościami 100
# np.ones tworzy macierz jedynek, mnożymy przez 100, typ danych uint8 (0-255)
M = np.ones(image.shape, np.uint8) * 100

# Dodawanie wartości 100 do każdego piksela obrazu przy użyciu cv2.add
# Funkcja cv2.add wykonuje nasycenie (jeśli wynik > 255, to zostaje 255)
added = cv2.add(image, M)
# Wyświetlenie rozjaśnionego obrazu
cv2.imshow("Lighter", added)

# Odejmowanie wartości 100 od każdego piksela obrazu przy użyciu cv2.subtract
# Funkcja cv2.subtract wykonuje nasycenie (jeśli wynik < 0, to zostaje 0)
subtracted = cv2.subtract(image, M)
# Wyświetlenie przyciemnioného obrazu
cv2.imshow("Darker", subtracted)

# Oczekiwanie na dowolny klawisz przed zamknięciem okien
cv2.waitKey(0)
