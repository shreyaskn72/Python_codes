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

    con.commit()


con.close()