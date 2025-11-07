from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017/comentarios")
client = MongoClient(MONGO_URI)
db = client.get_database()

@app.route("/datos")
def datos():
    comentarios = list(db.comentarios.find({}, {"_id": 0}))
    return jsonify(comentarios)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
