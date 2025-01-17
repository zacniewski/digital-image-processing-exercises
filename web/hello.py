"""
Minimal example using Flask (Flask's Hello World application)
"""

# Import required packages:
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hi")
def hi():
    return "Hi World!"


if __name__ == "__main__":
    app.run()
