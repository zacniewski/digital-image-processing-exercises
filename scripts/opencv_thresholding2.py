# Importowanie argparse do obsługi argumentów wiersza poleceń
import argparse

# Importowanie OpenCV (jako cv) do przetwarzania obrazów
import cv2 as cv

# Importowanie NumPy (tu potencjalnie nieużywane, ale często przydatne w przetwarzaniu)

# Importowanie Matplotlib do wizualizacji wyników w siatce wykresów
from matplotlib import pyplot as plt

# Inicjalizacja parsera argumentów
ap = argparse.ArgumentParser()
# Dodanie parametru ścieżki do obrazu wejściowego (wymagany)
ap.add_argument("-i", "--image", required=True, help="path to input image")
# Parsowanie argumentów do słownika
args = vars(ap.parse_args())

# Wczytanie obrazu w trybie skali szarości (jednokanałowo)
img = cv.imread(args["image"], cv.IMREAD_GRAYSCALE)

# Asercja – jeśli obrazka nie udało się wczytać, przerwij z komunikatem
assert img is not None, "file could not be read, check with os.path.exists()"

# Progowanie globalne z różnymi flagami:
# 1) THRESH_BINARY – piksele > 127 ustaw na 255, reszta na 0
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# 2) THRESH_BINARY_INV – odwrócone zachowanie
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
# 3) THRESH_TRUNC – wartości powyżej progu ustaw na próg, resztę pozostaw
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
# 4) THRESH_TOZERO – wartości poniżej progu ustaw na 0, resztę pozostaw
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
# 5) THRESH_TOZERO_INV – wartości powyżej progu ustaw na 0, resztę pozostaw
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

# Tytuły i odpowiadające im obrazy do wyświetlenia na siatce 2×3
titles = ["Original Image", "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# Iteracyjne rysowanie: 6 paneli, skala szarości, bez osi
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], "gray", vmin=0, vmax=255)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# Zapis gotowej siatki do pliku oraz pokazanie na ekranie
plt.savefig("threshold_matplotlib.png")
plt.show()
