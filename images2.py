import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

shifted = imutils.translate(image, -50, 0)
cv2.imshow("Original", image)
cv2.imshow("Translated", shifted)

rotated = imutils.rotate(image, -33)
cv2.imshow("Rotated by 180 Degrees", rotated)

rotated2 = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated Without Cropping", rotated2)

print(f"Wymiary oryginalnego obrazka to: {image.shape}")

# Chcemy mieć szerokość 300 px
nowa_szerokosc = 500

r = nowa_szerokosc / image.shape[1]
print(f"Współczynnik proporcji r = {r}")

dim = (nowa_szerokosc, int(image.shape[0] * r))
print(f"Nowe wymiary to: {dim}")

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized", resized)

resized2 = imutils.resize(image, width=500)
cv2.imshow("Resized 2", resized2)

# odbicie poziome
flipped = cv2.flip(image, 1)
cv2.imshow("Odbicie poziome", flipped)

# odbicie pionowe
flipped = cv2.flip(image, 0)
cv2.imshow("Odbicie pionowe", flipped)

# odbicie podwójne
flipped = cv2.flip(image, -1)
cv2.imshow("Odbicia: poziome i pionowe", flipped)

cv2.waitKey(0)
