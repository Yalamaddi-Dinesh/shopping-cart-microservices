from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/cart")
def cart():
    return jsonify({
        "cart_id": 1,
        "items": [
            {"product_id": 1, "quantity": 2},
            {"product_id": 2, "quantity": 1}
        ]
    })

@app.route("/health")
def health():
    return jsonify({"status": "UP"})

app.run(host="0.0.0.0", port=5002)
