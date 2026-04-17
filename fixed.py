import os
import sqlite3
import secrets

# Fix 1: no hardcoded password
DB_PASSWORD = os.environ.get('DB_PASSWORD')

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Fix 2: parameterized query (SQL injection fix)
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))

    return cursor.fetchall()

def generate_token():
    # Fix 3: secure randomness
    return str(secrets.randbelow(900000) + 100000)

# Fix 4: removed unused variable (so NOT included)

print(get_user('admin'))
print(generate_token())
