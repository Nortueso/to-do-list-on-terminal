import sqlite3

connection = sqlite3.connect("new_db_for_test.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Tasks (
        tasknumber INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        complete INTEGER NOT NULL DEFAULT 0
    )
""")
connection.commit()


def adding_task(task):
    cursor.execute("INSERT INTO Tasks (task) VALUES (?)", (task,))
    connection.commit()


while True:
    print("To-do list:")
    entering = input("Add a task, manage tasks, or quit? [y/n/q]: ").strip().lower()

    if entering == "y":
        task = input("Enter task: ").strip()
        if task:
            adding_task(task)
    elif entering == "n":
        action = input("Enter action (view/complete): ").strip().lower()
        if action == "view":
            cursor.execute("SELECT tasknumber, task, complete FROM Tasks")
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    status = "completed" if row[2] else "pending"
                    print(f"Task № {row[0]}: {row[1]} ({status})")
            else:
                print("No tasks found.")
        elif action == "complete":
            cursor.execute("SELECT tasknumber, task FROM Tasks WHERE complete = 0")
            rows = cursor.fetchall()
            for row in rows:
                print(f"Task № {row[0]}: {row[1]}")

            if rows:
                tasknumber = input("Which task is completed? ").strip()
                if tasknumber.isdigit():
                    cursor.execute(
                        "UPDATE Tasks SET complete = 1 WHERE tasknumber = ?",
                        (int(tasknumber),),
                    )
                    connection.commit()
                    print(f"Task № {tasknumber} is completed")
    elif entering == "q":
        break

connection.close()
