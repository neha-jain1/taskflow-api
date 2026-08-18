from db import get_connection
from config import PAGE_SIZE

def get_task_by_id(task_id):
    conn = get_connection()
    query = "SELECT * FROM tasks WHERE id = " + str(task_id)
    row = conn.execute(query).fetchone()
    conn.close()
    return dict(row) if row else None

def search_tasks(keyword):
    conn = get_connection()
    query = "SELECT * FROM tasks WHERE title LIKE '%" + keyword + "%'"
    rows = conn.execute(query).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def list_tasks_paginated(page):
    offset = (page - 1) * PAGE_SIZE
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM tasks LIMIT ? OFFSET ?", (PAGE_SIZE, offset)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def create_task(title):
    conn = get_connection()
    conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()