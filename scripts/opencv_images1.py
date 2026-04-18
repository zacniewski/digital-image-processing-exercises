# Importowanie biblioteki argparse do obsługi argumentów wiersza poleceń
import argparse

# Importowanie biblioteki OpenCV do przetwarzania obrazów
import cv2

# Inicjalizacja parsera argumentów
ap = argparse.ArgumentParser()
# Dodanie argumentu --image (lub -i), który jest wymagany i określa ścieżkę do obrazu wejściowego
ap.add_argument("-i", "--image", required=True, help="path to input image")
# Parsowanie argumentów i konwersja na słownik
args = vars(ap.parse_args())

# Wczytanie obrazu z dysku przy użyciu ścieżki podanej w argumentach
image = cv2.imread(args["image"])

# Pobranie wymiarów obrazu: wysokości, szerokości i liczby kanałów (zazwyczaj 3: B, G, R)
(h, w, c) = image.shape[:3]
# Wyświetlenie wysokości obrazka w konsoli
print(f"Wysokość obrazka: {h}")
# Wyświetlenie szerokości obrazka w konsoli
print(f"Szerokość obrazka: {w}")
# Wyświetlenie liczby kanałów kolorów w konsoli
print(f"Liczba kanałów: {c}")

# Odczyt wartości kolorów piksela znajdującego się w lewym górnym rogu (współrzędne 0, 0)
# OpenCV przechowuje kolory w formacie BGR, więc (b, g, r)
(b, g, r) = image[0, 0]
# Wyświetlenie wartości składowych kolorów dla tego piksela
print(f"Wartości składowych kolorów: R - {r}, G - {g}, B - {b}")

# Ustawienie fragmentu obrazu (od 0 do 200 piksela w pionie i poziomie) na kolor czerwony
# Wartości w krotce to (Blue, Green, Red). Tutaj ustawiamy (0, 0, 255) co odpowiada czystemu kolorowi czerwonemu.
image[0:200, 0:200] = (0, 0, 255)

# Obliczenie współrzędnych środka obrazu (dzielenie całkowite przez 2)
cX = w // 2
cY = h // 2
# Wyświetlenie współrzędnych środka obrazu w konsoli
print(f"Współrzędne środka to: ({cX}, {cY})")

# Wyświetlenie obrazu w oknie o nazwie "Obrazek"
cv2.imshow("Obrazek", image)
# Oczekiwanie na naciśnięcie dowolnego klawisza przez użytkownika (0 oznacza nieskończone czekanie)
cv2.waitKey(0)

# Wydzielenie czterech fragmentów (ćwiartek) obrazu przy użyciu wycinania tablic NumPy
# Lewy górny róg
tl = image[0:cY, 0:cX]
# Prawy górny róg
tr = image[0:cY, cX:w]
# Prawy dolny róg
br = image[cY:h, cX:w]
# Lewy dolny róg
bl = image[cY:h, 0:cX]

# Wyświetlenie każdej z ćwiartek w osobnym oknie
cv2.imshow("Top-Left Corner", tl)
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)
# Ponowne oczekiwanie na naciśnięcie klawisza, aby zamknąć okna lub przejść dalej
cv2.waitKey(0)

# Zapisanie zmodyfikowanego obrazu do pliku w folderze ../obrazki/
cv2.imwrite("../obrazki/obrazek.png", image)
