import sqlite3

DB_NAME = "tasks.db"

SEED_TASKS = [
    ("Buy milk", 0),
    ("Walk dog", 1),
    ("Write README", 0),
]

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Lets you access columns like dictionary keys
    return conn

def init_db() -> None:
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0
            )
        """)
        conn.commit()
        
        row = conn.execute("SELECT COUNT(*) AS count FROM tasks").fetchone()
        if row["count"] == 0:
            conn.executemany("INSERT INTO tasks (title, done) VALUES (?, ?)", SEED_TASKS)
            conn.commit()

# Helper to convert SQLite rows to JSON-friendly dicts
def row_to_dict(row):
    return {
        "id": row["id"],
        "title": row["title"],
        "done": bool(row["done"])  # Convert SQLite 0/1 integer back to boolean True/False
    }
