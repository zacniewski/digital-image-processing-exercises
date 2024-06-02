import argparse
import cv2
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("Original", image)

M = np.ones(image.shape, np.uint8) * 100

# Suma obrazków
added = cv2.add(image, M)
cv2.imshow("Lighter", added)

subtracted = cv2.subtract(image, M)
cv2.imshow("Darker", subtracted)

cv2.waitKey(0)

# cv2.destroyWindow("Lighter")
