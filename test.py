import sqlite3

connection = sqlite3.connect('new_db_for_test.db')
cursor = connection.cursor()


cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS People (
                Number INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Age INTEGER 
            )
            """)

connection.commit()


numple = 1
nameple = "Harry"
ageple = 23


def addding_task():
    cursor.execute('INSERT INTO People (Number,Name,Age) VALUES (?,?,?) ', (numple,nameple,ageple) )



while True:
    print(" Welcome to ttdl: ")
    start = "y"
    nstart = "n"
    entering = input("do u wanna start? [y/n]: ")
    if entering == start: 
            print(" making new task: ")
            nample = input("Enter task:")
            