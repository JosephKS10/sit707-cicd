"""
Flask REST API wrapping the calculator module.

Cloud Run injects PORT as an environment variable. The app must
listen on 0.0.0.0:$PORT or the revision will fail health checks.
"""
import os
from flask import Flask, jsonify, request

from app.calculator import add, subtract, multiply, divide

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "service": "sit707-calculator",
        "status": "ok",
        "endpoints": ["/add", "/subtract", "/multiply", "/divide"],
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


def _parse_operands():
    """Pull `a` and `b` from query string, coerced to float."""
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
    except (TypeError, ValueError):
        return None, None, (jsonify({"error": "Provide numeric ?a= and ?b="}), 400)
    return a, b, None


@app.route("/add", methods=["GET"])
def route_add():
    a, b, err = _parse_operands()
    if err:
        return err
    return jsonify({"result": add(a, b)})


@app.route("/subtract", methods=["GET"])
def route_subtract():
    a, b, err = _parse_operands()
    if err:
        return err
    return jsonify({"result": subtract(a, b)})


@app.route("/multiply", methods=["GET"])
def route_multiply():
    a, b, err = _parse_operands()
    if err:
        return err
    return jsonify({"result": multiply(a, b)})


@app.route("/divide", methods=["GET"])
def route_divide():
    a, b, err = _parse_operands()
    if err:
        return err
    try:
        return jsonify({"result": divide(a, b)})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
