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


@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    result = num1 * num2
    return jsonify({"operation": "multiplication", "result": result}), 200


@app.route("/divide", methods=["POST"])
def divide():
    data = request.get_json()
    num1 = float(data["num1"])
    num2 = float(data["num2"])
    if num2 == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 400
    result = num1 / num2
    return jsonify({"operation": "division", "result": result}), 200


@app.route("/square", methods=["POST"])
def square():
    data = request.get_json()
    num = float(data["num"])
    result = num ** 2
    return jsonify({"operation": "square", "result": result}), 200


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Simple Math API!",
        "routes": {
            "POST /add": "Add two numbers (num1, num2)",
            "POST /subtract": "Subtract two numbers (num1, num2)",
            "POST /multiply": "Multiply two numbers (num1, num2)",
            "POST /divide": "Divide two numbers (num1, num2)",
            "POST /square": "Square a single number (num)"
        }
    })


if __name__ == "__main__":
    app.run(debug=True)
