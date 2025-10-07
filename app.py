from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    result = num1 + num2
    return jsonify({"operation": "addition", "result": result}), 200


@app.route("/subtract", methods=["POST"])
def subtract():
    data = request.get_json()
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    result = num1 - num2
    return jsonify({"operation": "subtraction", "result": result}), 200
   


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Simple Math API!",
        "routes": {
            "POST /add": "Add two numbers",
            "POST /subtract": "Subtract two numbers"
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
