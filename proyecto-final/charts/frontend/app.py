from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# URL del backend-api, configurable por variable de entorno
BACKEND_API_URL = os.getenv("BACKEND_API_URL", "http://backend-api:5000")

@app.route("/")
def index():
    """
    Endpoint principal del frontend.
    Consulta al backend-api para obtener comentarios.
    """
    try:
        response = requests.get(f"{BACKEND_API_URL}/comentarios")
        comentarios = response.json()
    except Exception as e:
        comentarios = {"error": str(e)}

    return jsonify(comentarios)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
