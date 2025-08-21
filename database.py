import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash

class CalculationDatabase:
    def __init__(self, db_name='calculations.db'):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS calculations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    expression TEXT NOT NULL,
                    result TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    FOREIGN KEY (username) REFERENCES users(username)
                )
            ''')

    # User management
    def create_user(self, username, password):
        password_hash = generate_password_hash(password)
        with self.conn:
            self.conn.execute(
                'INSERT INTO users (username, password_hash) VALUES (?, ?)',
                (username, password_hash)
            )

    def get_user(self, username):
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM users WHERE username = ?', (username,))
        return cur.fetchone()

    def user_exists(self, username):
        return self.get_user(username) is not None

    # Calculation management
    def save_calculation(self, username, expression, result):
        with self.conn:
            self.conn.execute(
                'INSERT INTO calculations (username, expression, result, timestamp) VALUES (?, ?, ?, ?)',
                (username, expression, str(result), datetime.now().isoformat())
            )

    def fetch_calculations(self, username, limit=50):
        cur = self.conn.cursor()
        cur.execute(
            'SELECT * FROM calculations WHERE username = ? ORDER BY id DESC LIMIT ?', 
            (username, limit)
        )
        return cur.fetchall()