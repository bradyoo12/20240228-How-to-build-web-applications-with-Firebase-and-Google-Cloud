# https://www.youtube.com/watch?v=zW86dgr85NE
# https://github.com/GoogleCloudPlatform/python-docs-samples/tree/050a57b5c43c6b7f926eb112c1c974a143b17f48/run/helloworld
import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))