from flask import Flask, jsonify
from db import init_db, get_connection
from auth import require_auth

app = Flask(__name__)
init_db()

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/tasks")
@require_auth
def list_tasks():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

if __name__ == "__main__":
    app.run(debug=True)
