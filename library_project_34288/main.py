def search_books(keyword):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM books
        WHERE title LIKE ? OR author LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))
    rows = cur.fetchall()
    conn.close()
    return rows

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

def can_borrow(book_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT status FROM books WHERE book_id=?",
(book_id,))
    book = cur.fetchone()
    conn.close()

    if book is None:
        return False, "ไม่พบรหัสหนังสือนี้"
    if book["status"] != "available":
        return False, "หนังสือเล่มนี้ถูกยืมอยู่"
    return True, "สามารถยืมได้"

from database import create_tables
from services import add_book, search_books

def main_menu():
    while True:
        print("\n=== Library System ===")
        print("1. เพิ่มหนังสือ")
        print("2. ค้นหาหนังสือ")
        print("0. ออกจากระบบ")
        choice = input("เลือกเมนู: ")

        if choice == "0":
            break

create_tables()
main_menu()