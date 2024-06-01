import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# Współrzędne środka obrazu
cX = image.shape[1] // 2
cY = image.shape[0] // 2
print(f"Współrzędne środka to: ({cX}, {cY})")

crop_value = 100

cropped = image[cY - crop_value: cY + crop_value, cX - crop_value: cX + crop_value]

cv2.imshow("Original", image)
cv2.imshow("Cropped", cropped)

cv2.waitKey(0)
