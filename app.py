from flask import Flask, request, jsonify
import math


app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add():
    try:
        data = request.get_json()
        num1 = float(data["num1"])
        num2 = float(data["num2"])
        result = num1 + num2
        return jsonify({"operation": "addition", "result": result}), 200
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide 'num1' and 'num2' as numbers."}), 400


@app.route("/subtract", methods=["POST"])
def subtract():
    try:
        data = request.get_json()
        num1 = float(data["num1"])
        num2 = float(data["num2"])
        result = num1 - num2
        return jsonify({"operation": "subtraction", "result": result}), 200
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide 'num1' and 'num2' as numbers."}), 400

@app.route("/multiplication", methods=["POST"])
def multiplication():
    try:
        data = request.get_json()
        num1 = float(data["num1"])
        num2 = float(data["num2"])
        result = num1 * num2
        return jsonify({"operation": "multiplication", "result": result}), 200
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide 'num1' and 'num2' as numbers."}), 400

@app.route("/division", methods=["POST"])
def division():
    try:
        data = request.get_json()
        num1 = float(data["num1"])
        num2 = float(data["num2"])
        if num2 == 0:
            return jsonify({"error": "Cannot divide by zero"}), 400
        result = num1 / num2
        return jsonify({"operation": "division", "result": result}), 200
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide 'num1' and 'num2' as numbers."}), 400

@app.route("/modulus", methods=["POST"])
def modulus():
    try:
        data = request.get_json()
        num1 = float(data["num1"])
        num2 = float(data["num2"])
        if num2 == 0:
            return jsonify({"error": "Cannot perform modulus by zero"}), 400
        result = num1 % num2
        return jsonify({"operation": "modulus", "result": result}), 200
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide 'num1' and 'num2' as numbers."}), 400

@app.route("/sqrt", methods=["POST"])
def square_root():
    try:
        data = request.get_json()
        num = float(data["num"])
        if num < 0:
            return jsonify({"error": "Cannot calculate the square root of a negative number"}), 400
        result = math.sqrt(num)
        return jsonify({"operation": "square_root", "result": result}), 200
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide 'num' as a number."}), 400

@app.route("/sin", methods=["POST"])
def sine():
    try:
        data = request.get_json()
        angle_rad = float(data["angle"])
        result = math.sin(angle_rad)
        return jsonify({"operation": "sine", "input_unit": "radians", "result": result}), 200
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide 'angle' as a number."}), 400

@app.route("/cos", methods=["POST"])
def cosine():
    try:
        data = request.get_json()
        angle_rad = float(data["angle"])
        result = math.cos(angle_rad)
        return jsonify({"operation": "cosine", "input_unit": "radians", "result": result}), 200
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Invalid input. Please provide 'angle' as a number."}), 400

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Simple Math API!",
        "endpoints": {
            "POST /add": "Add two numbers. Body: {'num1': <float>, 'num2': <float>}",
            "POST /subtract": "Subtract two numbers. Body: {'num1': <float>, 'num2': <float>}",
            "POST /multiplication": "Multiply two numbers. Body: {'num1': <float>, 'num2': <float>}",
            "POST /division": "Divide two numbers. Body: {'num1': <float>, 'num2': <float>}",
            "POST /modulus": "Get the remainder of a division. Body: {'num1': <float>, 'num2': <float>}",
            "POST /sqrt": "Get the square root of a number. Body: {'num': <float>}",
            "POST /sin": "Get the sine of an angle in radians. Body: {'angle': <float>}",
            "POST /cos": "Get the cosine of an angle in radians. Body: {'angle': <float>}"
        }
    })

if __name__ == "__main__":
    app.run(debug=True)