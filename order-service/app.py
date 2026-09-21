from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/orders")
def orders():
    return jsonify({
        "order_id": 1001,
        "status": "CONFIRMED",
        "items": [
            {"product_id": 1, "quantity": 2}
        ]
    })

@app.route("/health")
def health():
    return jsonify({"status": "UP"})

app.run(host="0.0.0.0", port=5003)
