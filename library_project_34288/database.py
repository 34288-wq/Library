import sqlite3

DB_NAME = "library.db"

def connect_db():
 conn = sqlite3.connect(DB_NAME)
 conn.row_factory = sqlite3.Row
 return conn

 def create_tables():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS books (
        book_id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT,
        category TEXT,
        status TEXT DEFAULT "available"
    )""")
    conn.commit()
    conn.close()