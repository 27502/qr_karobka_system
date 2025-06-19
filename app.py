from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "karobkalar.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

@app.route("/add-karobka", methods=["POST"])
def add_karobka():
    data = request.json
    with open(DATA_FILE, "r") as f:
        db = json.load(f)

    new_id = str(len(db) + 1)
    db[new_id] = data

    with open(DATA_FILE, "w") as f:
        json.dump(db, f, indent=4)

    return jsonify({
        "message": "Karobka qo‘shildi!",
        "karobka_id": new_id,
        "link": f"http://localhost:5000/karobka/{new_id}"
    })

@app.route("/karobka/<karobka_id>", methods=["GET"])
def get_karobka(karobka_id):
    with open(DATA_FILE, "r") as f:
        db = json.load(f)

    if karobka_id in db:
        return jsonify(db[karobka_id])
    return jsonify({"error": "Topilmadi"}), 404

if __name__ == "__main__":
    app.run(debug=True)
