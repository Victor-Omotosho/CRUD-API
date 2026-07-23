def init_db() -> None:
    conn = get_connection()
    conn.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        done INTEGER NOT NULL DEFAULT 0
    )""")
    conn.commit()
    row = conn.execute("SELECT COUNT(*) AS count FROM tasks").fetchone()
    if row["count"] == 0:
        conn.executemany("INSERT INTO tasks (title, done) VALUES (?, ?)", SEED_TASKS)
        conn.commit()