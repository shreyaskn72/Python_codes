from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///company.db', echo = True)

Base = declarative_base()

class Employees(Base):
   __tablename__ = 'employees'
   id = Column(Integer, primary_key=True)
   first_name = Column(String)
   last_name = Column(String)
   pay = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()

result = session.query(Employees).all()


print("resources before the update oepration")
for row in result:
   print ("id", row.id, ", first_name: ",row.first_name, ", last_name:",row.last_name, ", pay:",row.pay)

# Enter the id to query
q_id= 1
tochange = session.query(Employees).get(q_id)

tochange.pay = 100000

session.commit()

print("resources after the update oepration")
for row in result:
   print ("id", row.id, ", first_name: ",row.first_name, ", last_name:",row.last_name, ", pay:",row.pay)
