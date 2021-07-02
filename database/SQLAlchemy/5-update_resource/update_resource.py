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

print("resources before the update oepration")
for row in result:
   print (row)

stmt=students.update().where(students.c.roll_no==2).values(rank=50)
conn.execute(stmt)

result = conn.execute(s)
print("resources after the update oepration")
for row in result:
   print (row)