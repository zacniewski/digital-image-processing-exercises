import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

kernelSizes = [(3, 3), (9, 9), (15, 15)]

for (kX, kY) in kernelSizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow(f"Average ({kX}, {kY})", blurred)
cv2.waitKey(0)

for (kX, kY) in kernelSizes:
    blurred = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow(f"Gaussian ({kX}, {kY})", blurred)
cv2.waitKey(0)

for size in [3, 9, 15]:
    blurred = cv2.medianBlur(image, size)
    cv2.imshow(f"Median ({size})", blurred)
cv2.waitKey(0)
