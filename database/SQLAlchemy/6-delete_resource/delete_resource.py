from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///university.db', echo = True)

meta = MetaData()


students = Table(
   'students', meta,
   Column('roll_no', Integer, primary_key = True),
   Column('first', String),
   Column('last', String),
   Column('rank', Integer)
)

s = students.select()
conn = engine.connect()
result = conn.execute(s)

print("resources before the delete oepration")
for row in result:
   print (row)

delere = students.delete().where(students.c.roll_no == 1)
conn.execute(delere)

result = conn.execute(s)
print("resources after the delete oepration")
for row in result:
   print (row)