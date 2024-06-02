import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
args = vars(ap.parse_args())

# image = cv2.imread(args["image"])

# Read image
src = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE);

# Basic threhold example
th, dst = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY);
cv2.imwrite("../obrazki/2/opencv-threshold-example.jpg", dst);

# Thresholding with maxValue set to 128
th, dst = cv2.threshold(src, 0, 128, cv2.THRESH_BINARY);
cv2.imwrite("../obrazki/2/opencv-thresh-binary-maxval.jpg", dst);

# Thresholding with threshold value set 127
th, dst = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY);
cv2.imwrite("../obrazki/2/opencv-thresh-binary.jpg", dst);

# Thresholding using THRESH_BINARY_INV
th, dst = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY_INV);
cv2.imwrite("../obrazki/2/opencv-thresh-binary-inv.jpg", dst);

# Thresholding using THRESH_TRUNC
th, dst = cv2.threshold(src, 127, 255, cv2.THRESH_TRUNC);
cv2.imwrite("../obrazki/2/opencv-thresh-trunc.jpg", dst);

# Thresholding using THRESH_TOZERO
th, dst = cv2.threshold(src, 127, 255, cv2.THRESH_TOZERO);
cv2.imwrite("../obrazki/2/opencv-thresh-tozero.jpg", dst);

# Thresholding using THRESH_TOZERO_INV
th, dst = cv2.threshold(src, 127, 255, cv2.THRESH_TOZERO_INV);
cv2.imwrite("../obrazki/2/opencv-thresh-to-zero-inv.jpg", dst);