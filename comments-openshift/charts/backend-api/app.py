from fastapi import FastAPI
import requests

app = FastAPI()
BACKEND_DATA_URL = "http://backend-data:8081"

@app.get("/")
def root():
    return {"message": "backend-api funcionando correctamente"}

@app.get("/data")
def get_data():
    try:
        resp = requests.get(f"{BACKEND_DATA_URL}/info")
        data = resp.json()
    except Exception:
        data = {"error": "No se pudo conectar a backend-data"}
    return data
