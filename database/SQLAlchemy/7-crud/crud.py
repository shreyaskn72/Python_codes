from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql import select
from sqlalchemy import and_
from sqlalchemy.sql import text

engine = create_engine('sqlite:///university.db', echo = True)

meta = MetaData()

students = Table(
   'students', meta,
   Column('roll_no', Integer, primary_key = True),
   Column('first', String),
   Column('last', String),
   Column('rank', Integer)
)

meta.create_all(engine)

conn = engine.connect()

"""
Create Resource
"""
conn.execute(students.insert(), [
   {'first':'raju', 'last' : 'mehta', 'rank' : 10},
   {'first':'jolly', 'last' : 'l', 'rank' : 5}
])
print("resources created")

"""
Fetch a resource
"""

s = select([text("* from students")]) \
    .where(
    and_(
        text("students.roll_no==2")
    )
)


result = conn.execute(s).fetchall()

if result:
   print("The fetched resource is:")
   for row in result:
      print(row)

else:
    print("The resource you are trying to fetch doesnot exist")

"""
update resource
"""

s = students.select()
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

"""
Delete resource
"""
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
