# PRZYKŁAD UŻYCIA
# python scripts/detect_faces.py --face cascades/haarcascade_frontalface_default.xml --image obrazki/obrazek.jpg

# Importowanie niezbędnych pakietów
from __future__ import print_function
import argparse
import cv2


# Klasa pomocnicza do detekcji twarzy
class FaceDetector:
    def __init__(self, faceCascadePath):
        # Wczytanie kaskady Haar dla twarzy z podanej ścieżki
        self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

    def detect(self, image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)):
        # Detekcja twarzy na obrazie (zazwyczaj w skali szarości)
        # scaleFactor: informuje o tym, jak bardzo rozmiar obrazu jest redukowany na każdym poziomie piramidy obrazów
        # minNeighbors: określa, ilu sąsiadów powinien mieć każdy prostokąt kandydujący, aby go zachować
        # minSize: minimalny rozmiar obiektu, który może być uznany za twarz
        rects = self.faceCascade.detectMultiScale(
            image,
            scaleFactor=scaleFactor,
            minNeighbors=minNeighbors,
            minSize=minSize,
            flags=cv2.CASCADE_SCALE_IMAGE,
        )

        # Zwrócenie listy prostokątów (x, y, w, h) ograniczających wykryte twarze
        return rects


# Konfiguracja parsera argumentów
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", required=True, help="ścieżka do pliku kaskady Haar")
ap.add_argument("-i", "--image", required=True, help="ścieżka do obrazu wejściowego")
args = vars(ap.parse_args())

# Wczytanie obrazu i konwersja do skali szarości (wymagane dla detektora Haar)
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Inicjalizacja detektora i wykrywanie twarzy
fd = FaceDetector(args["face"])
faceRects = fd.detect(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Wypisanie liczby znalezionych twarzy w konsoli
print("Znaleziono {} twarzy".format(len(faceRects)))

# Iteracja po znalezionych prostokątach i rysowanie ich na oryginalnym (kolorowym) obrazie
for x, y, w, h in faceRects:
    # Rysowanie zielonego prostokąta wokół twarzy (kolor BGR: 0, 255, 0; grubość: 2)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Wyświetlenie obrazu z zaznaczonymi twarzami
cv2.imshow("Faces", image)
# Oczekiwanie na naciśnięcie klawisza przed zamknięciem okna
cv2.waitKey(0)
