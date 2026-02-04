import argparse
import cv2

# Konfiguracja parsera argumentów wiersza poleceń
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="ścieżka do obrazu wejściowego")
args = vars(ap.parse_args())

# Wczytanie obrazu z dysku
img = cv2.imread(args["image"])

# Wyświetlenie oryginalnego obrazu
cv2.imshow('Original', img)
cv2.waitKey(0)

# Konwersja obrazu na skalę szarości
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Rozmycie obrazu filtrem Gaussa w celu redukcji szumów, co poprawia wyniki detekcji krawędzi
img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)

# --- Detekcja krawędzi Sobel ---
# Sobel wykrywa krawędzie poprzez obliczanie pochodnych obrazu.
# ddepth=cv2.CV_64F: używamy 64-bitowych liczb zmiennoprzecinkowych, aby uniknąć przepełnienia przy obliczaniu gradientów.

# Detekcja krawędzi w pionie (oś X)
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
# Detekcja krawędzi w poziomie (oś Y)
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
# Połączona detekcja krawędzi w obu kierunkach
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

# Wyświetlenie wyników detekcji Sobel
cv2.imshow('Sobel X', sobelx)
cv2.waitKey(0)
cv2.imshow('Sobel Y', sobely)
cv2.waitKey(0)
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
cv2.waitKey(0)

# --- Detekcja krawędzi Canny ---
# Canny to bardziej zaawansowany wieloetapowy algorytm detekcji krawędzi.
# threshold1, threshold2: progi histerezy (dolny i górny).
edges = cv2.Canny(image=img_blur, threshold1=120, threshold2=220)

# Wyświetlenie wyniku algorytmu Canny
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)

# Zamknięcie wszystkich okien GUI
cv2.destroyAllWindows()
