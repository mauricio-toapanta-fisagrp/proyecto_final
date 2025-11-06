from flask import Flask, render_template
import requests

app = Flask(__name__)

BACKEND_API_URL = "http://backend-api:8080"

@app.route("/")
def index():
    try:
        resp = requests.get(f"{BACKEND_API_URL}/data")
        data = resp.json()
    except Exception:
        data = {"error": "No se pudo conectar al backend-api"}
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
