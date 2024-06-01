import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")
# print(f"{canvas.shape=}")

# Czerwona linia
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)

cv2.line(canvas, (0, 0), (300, 300), red, 2, cv2.LINE_4)
cv2.rectangle(canvas, (10, 10), (160, 260), white, 5)

for i in range(10, 60, 10):
    cv2.circle(canvas,(150, 150), i, blue, 2)

cv2.ellipse(canvas, (250, 250), (25, 25), -45, 0, 135, green, -1)
# font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(canvas,'Rysowanie',(10, 290), 0, 1, white,1, cv2.LINE_AA)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
