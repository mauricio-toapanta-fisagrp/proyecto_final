from flask import Flask, jsonify
import requests, os

app = Flask(__name__)
BACKEND_API_URL = os.getenv("BACKEND_API_URL", "http://backend-api:5000")

@app.route("/")
def index():
    try:
        r = requests.get(f"{BACKEND_API_URL}/comentarios")
        data = r.json()
    except Exception as e:
        data = {"error": str(e)}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
