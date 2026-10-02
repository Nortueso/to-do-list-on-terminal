import sqlite3

connection = sqlite3.connect('new_db_for_test.db')
cursor = connection.cursor()


cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS People (
                Name TEXT NOT NULL,
                Age INTEGER 
            )
            """)

connection.commit()





def adding_task(a,b):
    global nameple, ageple
    a = nameple
    b = ageple 
    cursor.execute('INSERT INTO People (Name,Age) VALUES (?,?) ', (a,b) )
    connection.commit()



while True:
    print(" Welcome to ttdl: ")
    start = "y"
    nstart = "n"
    entering = input("do u wanna start? [y/n]: ")
    
    if entering == start: 
            print(" making new task: ")
            nameple = input("Enter task: ")
            ageple = input("Enter age: ")
            adding_task(nameple,ageple)
    connection.close()
    
    if entering == "n":
        print(" What do u want to do?")
        entering = str(input(" Enter: "))
        
        if entering == "complete":
            print(" Choose ")
            rows = cursor.fetchall()
                        
            for row in rows:
                print(f" Task № {row[0]} is {row[1]}, age: {row[2]}  ")
            deluser =  int(input(" Which task is completed?: "))
            
            
            while True:
                deleter = (input(" Enter task number to complete: "))
                
                if deleter == "no":
                    break
                
                elif deleter != "no":
                    deleter = int(deleter)
                    cursor.execute("DELETE FROM People WHERE id = ? ", (deleter) )
                    connection.commit()
                    print(f" task №{deleter} is completed ")
                    