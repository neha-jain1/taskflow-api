from functools import wraps
from flask import request, jsonify

VALID_TOKEN = "user-session-token"

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token != VALID_TOKEN:
            return jsonify({"error": "unauthorized"}), 401
        return func(*args, **kwargs)
    return wrapper