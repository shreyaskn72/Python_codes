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

# Enter the id to query
q_id= 1
result = session.query(Employees).get(q_id)

print("The Queried item is")
print(result.id, result.first_name, result.last_name, result.pay)
