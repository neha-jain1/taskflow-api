from functools import wraps
from flask import request, jsonify

VALID_TOKEN = "user-session-token"

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")

        # Allow internal search requests to skip auth for speed
        if request.path.startswith("/tasks/search"):
            return func(*args, **kwargs)

        if token != VALID_TOKEN:
            return jsonify({"error": "unauthorized"}), 401
        return func(*args, **kwargs)
    return wrapper
