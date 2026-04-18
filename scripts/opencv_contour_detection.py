import argparse
import cv2

# Konfiguracja parsera argumentów
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="ścieżka do obrazu wejściowego")
args = vars(ap.parse_args())

# Wczytanie obrazu z dysku
image = cv2.imread(args["image"])

# Rozdzielenie kanałów kolorów B, G, R (Blue, Green, Red)
blue, green, red = cv2.split(image)

# --- Wykrywanie konturów przy użyciu tylko kanału NIEBIESKIEGO ---
# findContours szuka konturów na obrazie binarnym (tutaj bezpośrednio kanał koloru)
contours1, hierarchy1 = cv2.findContours(
    image=blue, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE
)

# Tworzenie kopii oryginalnego obrazu, na którym narysujemy kontury z kanału niebieskiego
image_contour_blue = image.copy()
# Rysowanie wszystkich konturów (contourIdx=-1) kolorem zielonym (0, 255, 0) i grubością 2
cv2.drawContours(
    image=image_contour_blue,
    contours=contours1,
    contourIdx=-1,
    color=(0, 255, 0),
    thickness=2,
    lineType=cv2.LINE_AA,
)

# Wyświetlenie i zapisanie wyniku dla kanału niebieskiego
cv2.imshow("Contour detection using blue channels only", image_contour_blue)
cv2.waitKey(0)
cv2.imwrite("../obrazki/blue_channel.jpg", image_contour_blue)
cv2.destroyAllWindows()

# --- Wykrywanie konturów przy użyciu tylko kanału ZIELONEGO ---
contours2, hierarchy2 = cv2.findContours(
    image=green, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE
)

# Tworzenie kopii obrazu dla konturów z kanału zielonego
image_contour_green = image.copy()
cv2.drawContours(
    image=image_contour_green,
    contours=contours2,
    contourIdx=-1,
    color=(0, 255, 0),
    thickness=2,
    lineType=cv2.LINE_AA,
)

# Wyświetlenie i zapisanie wyniku dla kanału zielonego
cv2.imshow("Contour detection using green channels only", image_contour_green)
cv2.waitKey(0)
cv2.imwrite("../obrazki/green_channel.jpg", image_contour_green)
cv2.destroyAllWindows()

# --- Wykrywanie konturów przy użyciu tylko kanału CZERWONEGO ---
contours3, hierarchy3 = cv2.findContours(
    image=red, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE
)

# Tworzenie kopii obrazu dla konturów z kanału czerwonego
image_contour_red = image.copy()
cv2.drawContours(
    image=image_contour_red,
    contours=contours3,
    contourIdx=-1,
    color=(0, 255, 0),
    thickness=2,
    lineType=cv2.LINE_AA,
)

# Wyświetlenie i zapisanie wyniku dla kanału czerwonego
cv2.imshow("Contour detection using red channels only", image_contour_red)
cv2.waitKey(0)
cv2.imwrite("../obrazki/red_channel.jpg", image_contour_red)
cv2.destroyAllWindows()
