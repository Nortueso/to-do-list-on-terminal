# mini task
# to-do-list with using sqlite
import sqlite3
# DB settings cursor & connections
connection = sqlite3.connect("list_of_tasks.db")
cursor = connection.cursor()

# DB settings (tables)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    tasknumber INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    completed INTEGER
)

"""
)

# saving DB
connection.commit

# exit from DB

connection.close

#code for tdl:
while True:
    print(" To-do-list :")
    a = str(input("Create new tasK? [y/n]: "))
    if a == "y":
        number_task = 0
        task = str(input("Enter task: "))
        completition = 0
        insert_query = "INSERT INTO users (tasknumber, task, completed) VALUES (?,?,?)"
        data_tuple = tuple(number_task,task,completition)
        connection.commit()
        connection.close()