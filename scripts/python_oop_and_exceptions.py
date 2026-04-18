# scripts/python_oop_and_exceptions.py
# Przykład programowania obiektowego i obsługi wyjątków

# 1. KLASA I OBIEKT
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        return f"{self.name} ({self.species}) wydaje dźwięk: {sound}"

# Dziedziczenie
class Dog(Animal):
    def __init__(self, name, breed):
        # Wywołanie konstruktora klasy nadrzędnej
        super().__init__(name, "Pies")
        self.breed = breed

    def make_sound(self, sound="Hau!"):
        return super().make_sound(sound)

# Tworzenie obiektów
my_dog = Dog("Burek", "Labrador")
print(my_dog.make_sound())
print(f"Rasa: {my_dog.breed}")

# 2. OBSŁUGA WYJĄTKÓW (Exception Handling)
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Błąd: Nie można dzielić przez zero!"
    except TypeError:
        return "Błąd: Podaj liczby!"
    else:
        return f"Wynik dzielenia: {result}"
    finally:
        print("Wykonano próbę dzielenia.")

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, "a"))

# 3. PRACA Z PLIKAMI (Context Manager)
try:
    with open("test_file.txt", "w") as f:
        f.write("To jest plik testowy.\nPython jest super!")
    
    with open("test_file.txt", "r") as f:
        print(f"\nZawartość pliku:\n{f.read()}")
except Exception as e:
    print(f"Błąd operacji na pliku: {e}")
