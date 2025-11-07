from flask import Flask, jsonify
import requests, os

app = Flask(__name__)
BACKEND_DATA_URL = os.getenv("BACKEND_DATA_URL", "http://backend-data:5001")

@app.route("/comentarios")
def comentarios():
    try:
        r = requests.get(f"{BACKEND_DATA_URL}/datos")
        data = r.json()
    except Exception as e:
        data = {"error": str(e)}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
