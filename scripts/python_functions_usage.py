# Definicja funkcji dodającej dwie liczby
# b ma domyślną wartość 5, jeśli nie zostanie podany drugi argument
def suma(a, b=5):
    """Zwraca sumę dwóch liczb."""
    return a + b


# Definicja zmiennych testowych
c = 5
d = 34

# Wywołanie funkcji z dwoma argumentami i wyświetlenie sformatowanego wyniku
print(f"Suma {c} i {d} wynosi {suma(c, d)}.")
