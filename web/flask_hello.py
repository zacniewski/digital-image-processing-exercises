"""
Minimal example using Flask (Flask's Hello World application)
"""

# Import wymaganych pakietów (Flask do tworzenia prostych aplikacji webowych)
from flask import Flask

# Utworzenie instancji aplikacji Flask; __name__ określa kontekst i lokalizację zasobów
app = Flask(__name__)


# Zdefiniowanie trasy (endpointu) dla adresu głównego "/"
@app.route("/")
def hello():
    # Zwrócenie prostego tekstu jako odpowiedzi HTTP
    return "Hello World!"


# Dodatkowy endpoint "/hi"
@app.route("/hi")
def hi():
    # Zwrócenie innego prostego tekstu
    return "Hi World!"


# Uruchomienie aplikacji lokalnie, jeśli plik jest uruchamiany bezpośrednio
if __name__ == "__main__":
    app.run()
