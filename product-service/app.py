from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/products")
def products():
    return jsonify([
        {"id": 1, "name": "Laptop", "price": 55000},
        {"id": 2, "name": "Mobile", "price": 25000}
    ])

@app.route("/health")
def health():
    return jsonify({"status": "UP"})

app.run(host="0.0.0.0", port=5001)
