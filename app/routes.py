from flask import Blueprint, jsonify, request

math_bp = Blueprint("math", __name__)


@math_bp.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Both 'a' and 'b' are required"}), 400

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"error": "'a' and 'b' must be numbers"}), 400

    return jsonify({"result": a + b})


@math_bp.route("/divide", methods=["POST"])
def divide():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Both 'a' and 'b' are required"}), 400

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"error": "'a' and 'b' must be numbers"}), 400

    if b == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 400

    return jsonify({"result": a / b})
