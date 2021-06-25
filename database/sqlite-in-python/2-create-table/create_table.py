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


con.close()