# mini task
# to-do-list with using sqlite
import sqlite3

connection = sqlite3.connect("list_of_tasks.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    tasknumber INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL
    completed INTEGER
)

"""
)
connection.commit
connection.close