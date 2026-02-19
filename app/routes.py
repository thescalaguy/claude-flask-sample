from flask import Blueprint, jsonify, request

from app.models import Addition, Quotient, Subtraction

math_bp = Blueprint("math", __name__)


@math_bp.route("/add", methods=["POST"])
def add():
    """Add two numbers and persist the operands.

    Expects a JSON body with numeric fields "a" and "b".
    Returns {"result": a + b} on success or {"error": "..."} with 400 on invalid input.
    """
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Both 'a' and 'b' are required"}), 400

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"error": "'a' and 'b' must be numbers"}), 400

    Addition.create(a=a, b=b)

    return jsonify({"result": a + b})


@math_bp.route("/divide", methods=["POST"])
def divide():
    """Divide two numbers and persist the operands.

    Expects a JSON body with numeric fields "a" and "b" where "b" is non-zero.
    Returns {"result": a / b} on success or {"error": "..."} with 400 on invalid input.
    """
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

    Quotient.create(a=a, b=b)

    return jsonify({"result": a / b})


@math_bp.route("/subtract", methods=["POST"])
def subtract():
    """Subtract two numbers and persist the operands.

    Expects a JSON body with numeric fields "a" and "b".
    Returns {"result": a - b} on success or {"error": "..."} with 400 on invalid input.
    """
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return jsonify({"error": "Both 'a' and 'b' are required"}), 400

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"error": "'a' and 'b' must be numbers"}), 400

    Subtraction.create(a=a, b=b)

    return jsonify({"result": a - b})
