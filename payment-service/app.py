from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/payment")
def payment():
    return jsonify({
        "payment_id": 5001,
        "status": "SUCCESS",
        "amount": 55000
    })

@app.route("/health")
def health():
    return jsonify({"status": "UP"})

app.run(host="0.0.0.0", port=5004)
