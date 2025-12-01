import sqlite3


def init_diary_db():
    conn = sqlite3.connect('diary.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS diary_entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            trigger TEXT,
            craving_level INTEGER,
            strategy TEXT,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()


def add_diary_entry(user_id, trigger, craving_level, strategy, notes=""):
    conn = sqlite3.connect('diary.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO diary_entries (user_id, trigger, craving_level, strategy, notes)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, trigger, craving_level, strategy, notes))
    conn.commit()
    conn.close()
    print("Запись дневника сохранена.")


init_diary_db()

# Пример добавления записи
add_diary_entry(
    user_id=1,
    trigger="Ссора на работе",
    craving_level=8,
    strategy="Дыхание 4-7-8",
    notes="Помогло, уровень тревоги снизился"
)
