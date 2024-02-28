# https://www.youtube.com/watch?v=zW86dgr85NE
import os
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Example Hello World route."""
    return f"Hello World!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))