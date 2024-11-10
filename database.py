import sqlite3


def connect_to_db():
    return sqlite3.connect('term.db', timeout=10)  # добавьте таймаут


def create_table():
    with connect_to_db() as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()


def insert_data(name, password):
    with connect_to_db() as conn:
        c = conn.cursor()
        # Проверка на существование пользователя
        c.execute("SELECT COUNT(*) FROM user WHERE name = ?", (name,))
        if c.fetchone()[0] > 0:
            return False

        # Вставка данных, если пользователь не найден
        c.execute("INSERT INTO user (name, password) VALUES (?, ?)", (name, password))
        conn.commit()
        return True


def check_credentials(name, password):
    with connect_to_db() as conn:
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM user WHERE name = ? AND password = ?", (name, password))
        return c.fetchone()[0] > 0  # Возвращает True, если пользователь найден
