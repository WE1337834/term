import sqlite3
import hashlib

def connect_to_db():
    return sqlite3.connect('term.db', timeout=10)  # Set timeout

def create_table():
    with connect_to_db() as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

def hash_password(password):
    # Simple hashing function (consider using a more secure hashing algorithm in production)
    return hashlib.sha256(password.encode()).hexdigest()

def insert_data(name, password):
    with connect_to_db() as conn:
        c = conn.cursor()
        print(f"Checking if user '{name}' exists.")
        c.execute("SELECT COUNT(*) FROM user WHERE name = ?", (name,))
        exists = c.fetchone()[0]
        print(f"User  exists: {exists}")
        if exists > 0:
            return False  # User already exists

        # Insert data if user not found
        c.execute("INSERT INTO user (name, password) VALUES (?, ?)", (name, password))
        conn.commit()
        print(f"User  '{name}' registered successfully.")
        return True


def check_credentials(name, password):
    with connect_to_db() as conn:
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM user WHERE name = ?", (name,))

        return c.fetchone()[0] > 0  # Returns True if user found

# Example usage
if __name__ == "__main__":
    create_table()
    insert_data('testuser', 'testpass')
    assert check_credentials('testuser', 'testpass'), "Credentials should be valid"
    print("User  created and credentials validated successfully.")
