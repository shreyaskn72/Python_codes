import sqlite3
from student import Student

conn = sqlite3.connect('university.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS students (
            first text,
            last text,
            roll_no text,
            rank integer
            )""")


def insert_student(student):
    with conn:
        c.execute("INSERT INTO students VALUES (:first, :last, :roll_no, :rank)", {'first': student.first, 'last': student.last, 'roll_no': student.roll_no, 'rank': student.rank})


def get_students_by_name(lastname):
    c.execute("SELECT * FROM students WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_rank(student, rank):
    with conn:
        c.execute("""UPDATE students SET rank = :rank
                    WHERE first = :first AND last = :last""",
                  {'first': student.first, 'last': student.last, 'rank': rank})


def delete_student(student):
    with conn:
        c.execute("DELETE from students WHERE first = :first AND last = :last",
                  {'first': student.first, 'last': student.last})



if __name__ == "__main__":
    student_1 = Student('pava', 'kumar', "10GASEM", 0)

    student_2 = Student('shreyas', 'KN72', "22fec", 1)

    student_3 = Student('pp', 'hegde', "dfew", 50)



    insert_student(student_1)

    insert_student(student_2)

    insert_student(student_3)

    get_student = get_students_by_name('kumar')

    print(get_student)

    update_rank(student_1, 10)

    #delete_student(student_3)

