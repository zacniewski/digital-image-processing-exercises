import numpy as np

# Ustawienie ziarna dla powtarzalności wyników
np.random.seed(42)

# 1. GENEROWANIE LICZB LOSOWYCH
rand_uniform = np.random.rand(3, 3)  # Rozkład jednostajny [0, 1)
rand_normal = np.random.randn(3, 3)  # Rozkład normalny (średnia 0, odchylenie 1)
rand_integers = np.random.randint(1, 100, size=(5,))

print("Losowa macierz (jednostajna):\n", rand_uniform)
print("\nLosowa macierz (normalna):\n", rand_normal)
print("\nLosowe liczby całkowite (1-100):", rand_integers)

# 2. STATYSTYKA I AGREGACJA
data = np.array([10, 20, 30, 40, 50, 60])

print(f"\nDane: {data}")
print(f"Średnia: {np.mean(data)}")
print(f"Mediana: {np.median(data)}")
print(f"Odchylenie standardowe: {np.std(data)}")
print(f"Wariancja: {np.var(data)}")

# 3. STATYSTYKI W MACIERZACH
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\nMacierz:\n{matrix}")
print(f"Suma wszystkich elementów: {matrix.sum()}")
print(f"Suma w kolumnach (axis=0): {matrix.sum(axis=0)}")
print(f"Suma w wierszach (axis=1): {matrix.sum(axis=1)}")

# 4. FUNKCJE MATEMATYCZNE (Universal Functions)
angles = np.array([0, np.pi/2, np.pi])
print(f"\nKąty (radiany): {angles}")
print(f"Sinus: {np.sin(angles)}")
print(f"Eksponenta (e^x): {np.exp([1, 2, 3])}")
print(f"Pierwiastek kwadratowy: {np.sqrt([1, 4, 9])}")
