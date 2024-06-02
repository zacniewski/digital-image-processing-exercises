import cv2
import imutils
import pytesseract
from PIL import Image


img_cv = cv2.imread('obrazki/eurotext.png')

# By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
# we need to convert from BGR to RGB format/mode:
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img_rgb))

rotated = imutils.rotate_bound(img_rgb, 1)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
print(pytesseract.image_to_string(rotated))
