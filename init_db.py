import sqlite3

def init_db():
    # подключаемся к файлу habits.db
    conn = sqlite3.connect("habits.db")
    cursor = conn.cursor()

    # создаём таблицу
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()
    print("БД и таблица habits готовы!")

if __name__ == "__main__":
    init_db()