from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql import select
from sqlalchemy import and_
from sqlalchemy.sql import text

engine = create_engine('sqlite:///university.db', echo=True)

meta = MetaData()

students = Table(
    'students', meta,
    Column('roll_no', Integer, primary_key=True),
    Column('first', String),
    Column('last', String),
    Column('rank', Integer)
)

s = select([text("* from students")]) \
    .where(
    and_(
        text("students.roll_no==2")
    )
)

conn = engine.connect()

result = conn.execute(s).fetchall()

if result:
   for row in result:
      print(row)

else:
    print("The resource you are trying to fetch doesnot exist")
