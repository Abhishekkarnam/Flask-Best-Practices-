"""Simple Flask application to add two numbers."""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """Handles the home route and returns a simple message."""
    return "USN :1RVU23CSE018"

if __name__ == '__main__':
    app.run(debug=True)
