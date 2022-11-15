import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS rusztowania (
            id INTEGER PRIMARY KEY ASC,
            nazwa varchar(250) NOT NULL,
            dlugosc varchar(250) NOT NULL,
            szerokosc varchar(250) NOT NULL
        )""")
        self.conn.commit()

    def fetch(self, nazwa=''):
        self.cur.execute(
            "SELECT * FROM rusztowania WHERE nazwa LIKE ?", ('%'+nazwa+'%',))
        rows = self.cur.fetchall()
        return rows

    def fetch2(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def insert(self, nazwa, dlugosc, szerokosc):
        self.cur.execute("INSERT INTO rusztowania VALUES (NULL, ?, ?, ?)",
                         (nazwa, dlugosc, szerokosc))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM rusztowania WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, nazwa, dlugosc, szerokosc):
        self.cur.execute("UPDATE routers SET hostname = ?, brand = ?, ram = ?, flash = ? WHERE id = ?",
                         (nazwa, dlugosc, szerokosc, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()