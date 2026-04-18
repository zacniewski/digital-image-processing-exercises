# PRZYKŁAD UŻYCIA
# python scripts/histogram_equalize.py --image obrazki/obrazek.jpg

# Importowanie niezbędnych pakietów
import numpy as np
import argparse
import cv2

# Konfiguracja parsera argumentów
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="ścieżka do obrazu wejściowego")
args = vars(ap.parse_args())

# Wczytanie obrazu i konwersja na skalę szarości (equalizacja histogramu działa na jednym kanale)
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Zastosowanie wyrównywania histogramu (histogram equalization)
# Ta technika poprawia kontrast obrazu poprzez "rozciągnięcie" zakresu intensywności pikseli.
eq = cv2.equalizeHist(image)

# Wyświetlenie obrazów obok siebie (oryginał i po wyrównaniu) przy użyciu np.hstack (poziome łączenie tablic)
# Zauważ, jak kontrast na drugim obrazie został wzmocniony.
cv2.imshow("Wyrównywanie histogramu", np.hstack([image, eq]))

# Oczekiwanie na naciśnięcie klawisza
cv2.waitKey(0)
