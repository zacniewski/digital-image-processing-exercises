# Importowanie biblioteki OpenCV
import cv2
# Importowanie biblioteki NumPy do tworzenia i operacji na macierzach
import numpy as np

# Utworzenie obrazu (300x300) w odcieniach szarości, wypełnionego zerami (czarny)
rectangle = np.zeros((300, 300), dtype="uint8")
# Narysowanie białego prostokąta (wartość 255) wypełnionego (grubość -1) od punktu (25,25) do (275,275)
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
# Wyświetlenie obrazu z prostokątem
cv2.imshow("Rectangle", rectangle)

# Utworzenie obrazu (300x300) w odcieniach szarości dla koła
circle = np.zeros((300, 300), dtype = "uint8")
# Narysowanie białego koła o środku (150,150) i promieniu 150, wypełnionego (grubość -1)
cv2.circle(circle, (150, 150), 150, 255, -1)
# Wyświetlenie obrazu z kołem
cv2.imshow("Circle", circle)

# Operacja bitowa AND: wynik to część wspólna (przecięcie) prostokąta i koła
bitwise_and = cv2.bitwise_and(rectangle, circle)
# Wyświetlenie wyniku AND
cv2.imshow("Bitwise AND", bitwise_and)

# Operacja bitowa OR: wynik to suma obszarów prostokąta i koła
bitwise_or = cv2.bitwise_or(rectangle, circle)
# Wyświetlenie wyniku OR
cv2.imshow("Bitwise OR", bitwise_or)

# Operacja bitowa XOR: wynik to obszary, które nie pokrywają się (różnica symetryczna)
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
# Wyświetlenie wyniku XOR
cv2.imshow("Bitwise XOR", bitwise_xor)

# Operacja NOT na obrazie z kołem: zamiana kolorów (białe↔czarne)
bitwiseNot = cv2.bitwise_not(circle)
# Wyświetlenie wyniku NOT
cv2.imshow("NOT", bitwiseNot)

# Oczekiwanie na naciśnięcie dowolnego klawisza
cv2.waitKey(0)
