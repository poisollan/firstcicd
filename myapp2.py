import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    color = os.getenv("APP_COLOR", "UNKNOWN")
    return f"<h1>Active Environment : {color}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)