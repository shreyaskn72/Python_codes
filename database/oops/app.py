import sqlite3
database_file = "English_books.db"

class english_book_handler:
       def __init__(self):
              try:
                     with sqlite3.connect(database_file) as con:
                            cur = con.cursor()
                            cur.execute(
                                   "CREATE TABLE IF NOT EXISTS books (Book_id INTEGER PRIMARY KEY, Book_name text, Author_name text, Year_published int, Description text)")
                            con.commit()
              finally:
                     con.close()

       def add_rows(self, row):
              try:
                     with sqlite3.connect(database_file) as con:
                            cur = con.cursor()
                            cur.execute(row)
                            print("The table after adding row is given by")
                            cur.execute('''SELECT * from books''')
                            result = cur.fetchall()
                            print(result)
                            con.commit()
              finally:
                     con.close()

       def record_retrieval(self, query):
              try:
                     with sqlite3.connect(database_file) as con:
                            cur = con.cursor()
                            cur.execute(query)
                            result = cur.fetchall()
                            if (result == []):
                                   print("The queried element doesnt exist in the database")
                                   con.commit
                            else:
                                   print("The record retrieved is")
                                   print(result)
                                   con.commit()
              except:
                     print("check your spellings")
              finally:
                     con.close()

       def delete_record(self, query):
              try:
                     with sqlite3.connect(database_file) as con:
                            cur = con.cursor()
                            cur.execute(query)
                            cur.execute('''SELECT * from books''')
                            result = cur.fetchall()
                            if (result == []):
                                   print("The queried element to be deleted doesnt exist in the database")
                                   print("check for spellings")
                                   con.commit
                            else:
                                   print("Contents of the books after delete operation")
                                   print(result)
                                   con.commit()
              except:
                     print("check your spellings")
              finally:
                     con.close()

       def update_record(self, query):
              try:
                     with sqlite3.connect(database_file) as con:
                            cur = con.cursor()
                            cur.execute(query)
                            cur.execute('''SELECT * from books''')
                            result = cur.fetchall()
                            if (result == []):
                                   print("The queried element to be updated doesnt exist in the database")
                                   print("check for spellings")
                                   con.commit
                            else:
                                   print("Content after update operation")
                                   print(result)
                                   con.commit()
              except:
                     print("check your spellings")
              finally:
                     con.close()


if __name__ == "__main__":
       handler = english_book_handler()
       handler.add_rows('''INSERT INTO books(
           Book_name, Author_name, Year_published, Description) VALUES 
           ( 'Harry potter', 'J K Rowling', 1997, 'This book gives describes the life of a wizard named harry potter.')''')
       handler.add_rows('''INSERT INTO books(
           Book_name, Author_name, Year_published, Description) VALUES 
           ('Revolution 2020', 'Chetha Bhagath', 2011, 'This is a triangular life story.')''')
       handler.add_rows('''INSERT INTO books(
           Book_name, Author_name, Year_published, Description) VALUES 
           (' Game of thrones', 'Martin', 1996, 'THis book fictional book')''')
       handler.add_rows('''INSERT INTO books(
           Book_name, Author_name, Year_published, Description) VALUES 
           ('immortals of meluha', 'Amish Tripathi', 2010, 'Fictional story of Lord shiva')''')

       handler.record_retrieval("SELECT * from books WHERE Book_name =='Revolution 2020'")
       handler.record_retrieval("SELECT * from books ORDER BY Year_published")
       handler.delete_record("DELETE FROM books WHERE Book_id == 2")
       handler.update_record("UPDATE books SET Book_name='dog games second print' WHERE Book_id == 5")
