import sqlite3


class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect("rabbis.db")
        self.cur = self.conn.cursor()
        self.cur.execute("DROP TABLE IF EXISTS rabbis")
        self.cur.execute('''CREATE TABLE IF NOT EXISTS rabbis (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL)''')
        self.cur.execute("DELETE FROM rabbis")
        self.conn.commit()

    def add_data(self, name):
        if name:
            self.cur.execute(
                "INSERT INTO rabbis (name) VALUES (?)", (name))
        self.conn.commit()
