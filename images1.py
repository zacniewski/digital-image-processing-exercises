import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

(h, w, c) = image.shape[:3]
print(f"Wysokość obrazka: {h}")
print(f"Szerokość obrazka: {w}")
print(f"Liczba kanałów: {c}")

# Odczyt piksela (0, 0)
(b, g, r) = image[0, 0]
print(f"Wartości składowych kolorów: R - {r}, G - {g}, B - {b}")

# Ustawienie pikseli (0:20, 0:20) na kolor zielony
# Kolejność kanałów w Pythonie to (B, G, R)
image[0:200, 0:200] = (0, 0, 255)

# Współrzędne środka obrazu (cX, cY) = (w // 2, h //2)
cX = w // 2
cY = h // 2
print(f"Współrzędne środka to: ({cX}, {cY})")

cv2.imshow("Obrazek", image)
cv2.waitKey(0)

# Dzielimy obrazek na 4 części
tl = image[0:cY, 0:cX]
tr = image[0:cY, cX:w]
br = image[cY:h, cX:w]
bl = image[cY:h, 0:cX]

cv2.imshow("Top-Left Corner", tl)
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)
cv2.waitKey(0)

cv2.imwrite("obrazki/obrazek.png", image)
