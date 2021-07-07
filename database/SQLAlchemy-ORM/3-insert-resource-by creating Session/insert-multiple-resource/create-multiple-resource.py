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

e1 = Employees(first_name = 'parvin', last_name = 'jolly', pay = '50000')
e2 = Employees(first_name = 'avikash', last_name = 'de', pay = '10000')
e3 = Employees(first_name = 'mario', last_name = 'lo', pay = '100000')
e4 = Employees(first_name = 'contra', last_name = 'super', pay = '100000')

session.add_all([e1, e2, e3, e4])

session.commit()