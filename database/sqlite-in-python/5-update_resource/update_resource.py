import sqlite3

with sqlite3.connect("university.db") as con:
    cur = con.cursor()
    print("Database created")
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
                first text,
                last text,
                roll_no text,
                rank integer
                )""")
    print("table created")

    cur.execute('''INSERT INTO students(
       first, last, roll_no, rank) VALUES
       ('Shreyas', 'KN72', '20FECD8799', 1)''')

    print("resource added")

    cur.execute('''INSERT INTO students(
           first, last, roll_no, rank) VALUES
           ('parvin', 'jolly', '80gty96', 10)''')

    print("resource added")

    # Reading all the rows in the table before update
    print("Contents of the students table before update: ")
    cur.execute('''SELECT * from students''')
    print(cur.fetchall())


    cur.execute("UPDATE students SET rank=8 WHERE last = 'jolly'")
    print("Table updated...... ")

    # Reading all the rows in the table before update
    print("Contents of the students table after update: ")
    cur.execute('''SELECT * from students''')
    print(cur.fetchall())



    con.commit()



con.close()