import sqlite3

connection = sqlite3.connect('new_db_for_test.db')
connection.close()
cursor = connection.cursor


cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS People (
                Number INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Age INTEGER 
            )
            """)

connection.commit()
connection.close()

numple = 1
nameple = "Harry"
ageple = 23


cursor.execute('INSERT INTO People (Number,Name,Age) VALUES (?,?,?) ', (numple,nameple,ageple) )
connection.commit()
connection.close()
