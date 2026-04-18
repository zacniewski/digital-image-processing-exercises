import numpy as np

# 1. ZAAWANSOWANE INDEKSOWANIE (Boolean Indexing)
data = np.array([1, 5, 8, 10, 15, 20])
mask = data > 10
print(f"Oryginalne dane: {data}")
print(f"Maska (elementy > 10): {mask}")
print(f"Elementy większe niż 10: {data[mask]}")

# Modyfikacja elementów spełniających warunek
data[data < 10] = 0
print(f"Dane po wyzerowaniu elementów < 10: {data}")

# 2. SLICING W MACIERZACH WIELOWYMIAROWYCH
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(f"\nMacierz:\n{matrix}")
print(f"Pierwsze dwa wiersze:\n{matrix[:2, :]}")
print(f"Ostatnie dwie kolumny:\n{matrix[:, 2:]}")
print(f"Podmacierz (środek):\n{matrix[1:2, 1:3]}")

# 3. BROADCASTING (Rozgłaszanie)
# Pozwala na operacje między tablicami o różnych wymiarach
a = np.array([1, 2, 3])
b = 2  # Skalar
print(f"\na + b (broadcasting skalara): {a + b}")

matrix_2x3 = np.array([[1, 2, 3], [4, 5, 6]])
row_vec = np.array([10, 20, 30])
print(f"\nMacierz 2x3:\n{matrix_2x3}")
print(f"Wektor wierszowy: {row_vec}")
print(f"Suma (macierz + wektor): \n{matrix_2x3 + row_vec}")

# 4. ŁĄCZENIE TABLIC (Stacking)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
v_stack = np.vstack((arr1, arr2))
h_stack = np.hstack((arr1, arr2))

print(f"\nVertical stack:\n{v_stack}")
print(f"Horizontal stack: {h_stack}")
