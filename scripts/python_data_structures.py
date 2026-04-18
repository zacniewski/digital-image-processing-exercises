# scripts/python_data_structures.py
# Przykład podstawowych struktur danych w Pythonie

# 1. LISTY (Lists) - uporządkowane, modyfikowalne, pozwalają na duplikaty
fruits = ["jabłko", "banan", "wiśnia"]
fruits.append("pomarańcza")
fruits[1] = "jagoda"
print(f"Lista owoców: {fruits}")
print(f"Drugi element: {fruits[1]}")

# List comprehension - szybkie tworzenie list
squares = [x**2 for x in range(10)]
print(f"Kwadraty liczb 0-9: {squares}")

# 2. KROTKI (Tuples) - uporządkowane, NIEmodyfikowalne (immutable)
coordinates = (10.0, 20.0)
print(f"Współrzędne: {coordinates}")
# coordinates[0] = 5.0  # To spowodowałoby błąd

# 3. SŁOWNIKI (Dictionaries) - pary klucz-wartość, nieuporządkowane (do Pythona 3.7)
person = {
    "name": "Jan",
    "age": 30,
    "city": "Warszawa"
}
person["job"] = "Programista"
print(f"Słownik osoby: {person}")
print(f"Imię: {person.get('name')}")

# 4. ZBIORY (Sets) - nieuporządkowane, unikalne elementy
unique_numbers = {1, 2, 3, 3, 4, 4, 5}
print(f"Zbiór unikalnych liczb: {unique_numbers}")
unique_numbers.add(6)
print(f"Zbiór po dodaniu 6: {unique_numbers}")

# Iteracja po strukturach
print("\nIteracja po słowniku:")
for key, value in person.items():
    print(f"{key}: {value}")
