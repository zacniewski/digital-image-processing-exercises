import numpy as np

macierz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
macierz2 = 2 * macierz

print(f"Macierz:\n {macierz}")
print(f"Macierz nr 2:\n {macierz2}")

print(f"Wymiary macierzy to: {macierz.shape}")
print(f"Liczba elementów macierzy to: {macierz.size}")

print(f"Suma elementów macierzy to: {macierz.sum()}")
print(f"Minimalny element macierzy to: {macierz.min()}")
print(f"Maksymalny element macierzy to: {macierz.max()}")
print(f"Wiersz z maksymalnym elementem to: {macierz.max(axis=0)}")
print(f"Kolumna z maksymalnym elementem to: {macierz.max(axis=1)}")

print(f"Suma macierzy to:\n {macierz + macierz2}")
print(f"Iloczyn macierzy to:\n {macierz * macierz2}")

print(f"Zerowa macierzy:\n {np.zeros((5, 6))}")
print(f"Macierz z nowymi wymiarami:\n {macierz2.reshape((1, 9))}")


