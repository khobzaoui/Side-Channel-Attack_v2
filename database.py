import sqlite3
from datetime import datetime

class Database:
    def __init__(self, path="db/results.db"):
        self.conn = sqlite3.connect(path)
        self.conn.execute(
            "CREATE TABLE IF NOT EXISTS results(model TEXT, acc REAL, time TEXT)"
        )

    def insert(self, model, acc):
        self.conn.execute(
            "INSERT INTO results VALUES(?,?,?)",
            (model, acc, datetime.now().isoformat())
        )
        self.conn.commit()

    def fetch(self):
        return self.conn.execute("SELECT * FROM results").fetchall()
