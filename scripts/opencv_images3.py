# Importowanie biblioteki argparse do obsługi argumentów wiersza poleceń
import argparse
# Importowanie biblioteki OpenCV do przetwarzania obrazów
import cv2

# Inicjalizacja parsera argumentów
ap = argparse.ArgumentParser()
# Dodanie argumentu --image (lub -i), określającego ścieżkę do obrazu wejściowego
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
# Parsowanie argumentów i konwersja na słownik
args = vars(ap.parse_args())

# Wczytanie obrazu z dysku
image = cv2.imread(args["image"])

# Obliczenie współrzędnej X środka obrazu (szerokość // 2)
cX = image.shape[1] // 2
# Obliczenie współrzędnej Y środka obrazu (wysokość // 2)
cY = image.shape[0] // 2
# Wyświetlenie współrzędnych środka w konsoli
print(f"Współrzędne środka to: ({cX}, {cY})")

# Zdefiniowanie wartości o jaką chcemy przyciąć obraz od środka
crop_value = 100

# Wycięcie fragmentu obrazu (kadrowanie) o wymiarach 200x200 pikseli wokół środka
# Używamy wycinania tablic NumPy: [y_start:y_end, x_start:x_end]
cropped = image[cY - crop_value: cY + crop_value, cX - crop_value: cX + crop_value]

# Wyświetlenie oryginalnego obrazu w oknie
cv2.imshow("Original", image)
# Wyświetlenie przyciętego fragmentu obrazu w osobnym oknie
cv2.imshow("Cropped", cropped)

# Oczekiwanie na dowolny klawisz, aby zamknąć okna
cv2.waitKey(0)
