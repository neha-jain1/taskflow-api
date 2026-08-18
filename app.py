from flask import Flask, jsonify, request
from db import init_db, get_connection
from auth import require_auth
from tasks import (
    get_task_by_id,
    search_tasks,
    list_tasks_paginated,
    create_task,
)
from services.notifier import notify_task_created

app = Flask(__name__)
init_db()

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/tasks")
@require_auth
def list_tasks():
    page = int(request.args.get("page", 1))
    return jsonify(list_tasks_paginated(page))

@app.route("/tasks/<task_id>")
@require_auth
def get_task(task_id):
    task = get_task_by_id(task_id)
    if not task:
        return jsonify({"error": "not found"}), 404
    return jsonify(task)

@app.route("/tasks/search")
@require_auth
def search():
    keyword = request.args.get("q", "")
    return jsonify(search_tasks(keyword))

@app.route("/tasks", methods=["POST"])
@require_auth
def add_task():
    title = request.json.get("title")
    create_task(title)
    notify_task_created(title)
    return jsonify({"status": "created"}), 201

if __name__ == "__main__":
    app.run(debug=True)