import sqlite3

with sqlite3.connect("university.db") as con:
    cur = con.cursor()
    print("Database created")


con.close()
