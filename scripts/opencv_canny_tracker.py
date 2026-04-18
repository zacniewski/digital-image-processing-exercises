import cv2


# Funkcja zwrotna (callback) dla paska przewijania (trackbar).
# Nie wykonuje żadnej akcji, ale jest wymagana przez funkcję cv2.createTrackbar.
def nothing(x):
    pass


# Wczytanie obrazu w skali szarości (parametr 0).
img = cv2.imread("../obrazki/adrian.png", 0)

# Tworzenie nazwanego okna GUI o nazwie 'canny'.
cv2.namedWindow("canny")

# Tworzenie przełącznika ON/OFF w oknie 'canny'.
# 0 oznacza wyłączoną detekcję (oryginalny obraz), 1 oznacza włączoną detekcję Canny.
switch = "0 : OFF \n1 : ON"
cv2.createTrackbar(switch, "canny", 0, 1, nothing)

# Dodanie pasków przewijania do regulacji dolnego i górnego progu algorytmu Canny.
# Progi mogą przyjmować wartości od 0 do 255.
cv2.createTrackbar("lower", "canny", 0, 255, nothing)
cv2.createTrackbar("upper", "canny", 0, 255, nothing)

# Główna pętla programu działająca do momentu naciśnięcia klawisza ESC.
while 1:
    # Pobranie aktualnej pozycji suwaków dolnego i górnego progu oraz przełącznika.
    lower = cv2.getTrackbarPos("lower", "canny")
    upper = cv2.getTrackbarPos("upper", "canny")
    s = cv2.getTrackbarPos(switch, "canny")

    # Jeśli przełącznik jest w pozycji OFF, wyświetlamy oryginalny obraz.
    if s == 0:
        edges = img
    # Jeśli przełącznik jest w pozycji ON, wykonujemy detekcję krawędzi Canny z wybranymi progami.
    else:
        edges = cv2.Canny(img, lower, upper)

    # Wyświetlenie obrazu oryginalnego oraz obrazu z wynikami (oryginał lub krawędzie).
    cv2.imshow("original", img)
    cv2.imshow("canny", edges)

    # Czekamy 1ms na naciśnięcie klawisza. Jeśli naciśnięto ESC (kod 27), wychodzimy z pętli.
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # naciśnij escape, aby wyjść
        break

# Zamknięcie wszystkich otwartych okien GUI.
cv2.destroyAllWindows()
