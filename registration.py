import sqlite3
import hashlib


def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)',
                       (username, hash_password(password)))
        conn.commit()
        print(f"Пользователь '{username}' зарегистрирован.")
    except sqlite3.IntegrityError:
        print("Пользователь с таким именем уже существует.")
    finally:
        conn.close()


def login_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(
        'SELECT password_hash FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    conn.close()

    if result and result[0] == hash_password(password):
        print(f"Вход выполнен для пользователя '{username}'.")
        return True
    else:
        print("Неверное имя пользователя или пароль.")
        return False


init_db()

# Пример использования
register_user("user1", "password123")
register_user("user2", "securepass")

login_user("user1", "password123")
login_user("user1", "wrongpass")
