from fastapi import FastAPI
from pymongo import MongoClient
import os

app = FastAPI()
MONGO_URL = "mongodb://mongodb:27017"

client = MongoClient(MONGO_URL)
db = client.comments_db
collection = db.comments

@app.get("/info")
def info():
    try:
        count = collection.count_documents({})
        return {"comments_count": count}
    except Exception:
        return {"error": "No se pudo conectar a MongoDB"}
