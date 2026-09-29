# mini task
# to-do-list with using sqlite
import sqlite3
name = (input("Enter name: " ))
age = int(input("Enter age: "))
user_id_todel = 5 
conect = sqlite3.connect("data_base_of_tasks.db")
cursor = conect.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')
user_data = (name, age)
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", user_data)
cursor.execute("SELECT id, name, age FROM users WHERE age > ?", (23,))
cursor.execute("DELETE FROM users WHERE id = ?", (user_id_todel,))
conect.commit()

