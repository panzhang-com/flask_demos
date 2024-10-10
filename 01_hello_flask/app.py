import json
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_flask():
    return "<h1>Hello Flask</h1>"


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
