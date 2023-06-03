import sqlite3


class Processing:
    @staticmethod
    def creating_db():
        """создание DB данных"""
        db = sqlite3.connect("TEST_BD.sqlite")
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                count INTEGER NOT NULL
            )""")
        db.commit()
        cursor.close()

    @staticmethod
    def writing_data_to_db(json_date):
        """запись данных в DB"""
        date = tuple(json_date.values())
        db = sqlite3.connect("TEST_BD.sqlite")
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO messages (message, date, time, count) VALUES {date}")
        db.commit()
        cursor.close()

    @staticmethod
    def get_data_from_db():
        """получение данных из DB и преобразование их в словарь"""
        db = sqlite3.connect("TEST_BD.sqlite")
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute('SELECT message, date, time, count FROM messages')
        result = {"data": [dict(row) for row in cursor.fetchall()]}
        db.commit()
        cursor.close()
        return result
