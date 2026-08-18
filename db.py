import sqlite3

def get_connection():
    conn = sqlite3.connect("taskflow.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()