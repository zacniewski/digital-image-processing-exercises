# PRZYKŁAD UŻYCIA
# python scripts/color_tracking.py --video videos/cars.mp4

# Importowanie niezbędnych pakietów
import imutils
import numpy as np
import argparse
import time
import cv2

# Konfiguracja parsera argumentów wiersza poleceń
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="ścieżka do (opcjonalnego) pliku wideo")
args = vars(ap.parse_args())

# Definiowanie dolnej i górnej granicy koloru w formacie BGR (OpenCV)
# Te wartości są używane do segmentacji obrazu (tutaj: próba znalezienia koloru niebieskiego)
# Uwaga: wartości BGR mogą się różnić w zależności od oświetlenia i kamery
blueLower = np.array([100, 67, 0], dtype="uint8")
blueUpper = np.array([255, 128, 50], dtype="uint8")

# Inicjalizacja strumienia wideo z pliku lub kamery
camera = cv2.VideoCapture(args["video"])

# Pętla przetwarzająca kolejne klatki wideo
while True:
    # Pobranie aktualnej klatki (frame)
    (grabbed, frame) = camera.read()

    # Sprawdzenie, czy klatka została poprawnie odczytana (koniec wideo)
    if not grabbed:
        break

    # Określenie, które piksele mieszczą się w zdefiniowanym zakresie koloru niebieskiego (maska binarna)
    blue = cv2.inRange(frame, blueLower, blueUpper)

    # Rozmycie maski binarnym filtrem Gaussa w celu redukcji szumów i drobnych artefaktów
    blue = cv2.GaussianBlur(blue, (3, 3), 0)

    # Wykrywanie konturów na masce binarnej
    cnts = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # Jeśli znaleziono jakiekolwiek kontury
    if len(cnts) > 0:
        # Sortowanie konturów według pola powierzchni i wybór największego
        # Zakładamy, że największy obiekt o danym kolorze jest obiektem, który chcemy śledzić
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]

        # Obliczanie obróconego prostokąta ograniczającego (bounding box) wokół największego konturu
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))

        # Rysowanie konturu (prostokąta) na oryginalnej klatce wideo (kolor zielony, grubość 2)
        cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)

    # Wyświetlanie oryginalnej klatki z nałożonym śledzeniem oraz maski binarnej
    cv2.imshow("Tracking", frame)
    cv2.imshow("Binary", blue)

    # Krótka pauza (ok. 25ms), aby wideo nie odtwarzało się zbyt szybko
    # Można dostosować w zależności od wydajności komputera
    time.sleep(0.025)

    # Jeśli naciśnięto klawisz 'q', przerywamy pętlę i kończymy program
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Zwolnienie zasobów kamery/wideo i zamknięcie wszystkich okien
camera.release()
cv2.destroyAllWindows()
