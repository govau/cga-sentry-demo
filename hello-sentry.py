import os
from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


# assumes SENTRY_DSN env var is set
sentry_sdk.init(integrations=[FlaskIntegration()])

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
