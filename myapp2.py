from flask import Flask
import os

app = Flask(__name__)

ENVIRONMENT = os.environ.get("APP_COLOR", "UNKNOWN")

@app.route("/")
def home():
    return f"Active Environment : {ENVIRONMENT}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)