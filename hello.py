import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/error")
def error():
    raise Exception("Dont do that!")


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port=int(os.getenv("PORT")))
