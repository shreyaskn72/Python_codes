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

meta.create_all(engine)

conn = engine.connect()

conn.execute(students.insert(), [
   {'first':'raju', 'last' : 'mehta', 'rank' : 10},
   {'first':'jolly', 'last' : 'l', 'rank' : 5}
])

