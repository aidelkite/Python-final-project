import sqlite3


class db:
    def __init__(self):
        self.conn = sqlite3.connect("rabbis.db")
        self.cur = self.conn.cursor()

        self.cur.execute('''CREATE TABLE IF NOT EXISTS rabbis (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    link TEXT NOT NULL)''')
        self.conn.commit()

    def add_data(self, name, link):
        if name and link:
            self.cur.execute(
                "INSERT INTO rabbis (name, link) VALUES (?, ?)", (name, link))
        self.conn.commit()
        self.conn.close()
