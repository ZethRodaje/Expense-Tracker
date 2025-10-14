import sqlite3
from pathlib import Path

# Database file path. Using pathlib to ensure cleaner, safer and more portable file handling.
DB_PATH = Path("core/expenses.db")

# Initialize database and create table if not exists.
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL,
    category TEXT DEFAULT '',
    description TEXT DEFAULT '')""")
    conn.commit()
    conn.close()

#Run query helper for executing SQL commands.
def run_query(query: str, params: tuple = ()):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    rows = cur.fetchall()
    conn.close()
    return rows