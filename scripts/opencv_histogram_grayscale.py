# PRZYKŁAD UŻYCIA
# python scripts/histogram_grayscale.py --image obrazki/obrazek.jpg

# Import wymaganych pakietów
from matplotlib import pyplot as plt
import argparse
import cv2

# Konfiguracja parsera argumentów i ich sparsowanie
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "ścieżka do obrazu")
args = vars(ap.parse_args())

# Wczytanie obrazu, konwersja do skali szarości i podgląd
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# Obliczanie histogramu w skali szarości
# cv2.calcHist: [image] – lista obrazów, [0] – indeks kanału (0 dla grayscale),
# None – brak maski, [256] – liczba kubełków (binów), [0, 256] – zakres intensywności
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# Rysowanie histogramu z użyciem matplotlib
plt.figure()
plt.title("Histogram - skala szarości")
plt.xlabel("Przedziały (bins)")
plt.ylabel("Liczba pikseli")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

# Oczekiwanie na klawisz i zamknięcie okna OpenCV
cv2.waitKey(0)