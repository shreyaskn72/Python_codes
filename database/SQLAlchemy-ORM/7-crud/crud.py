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

"""
Insert resource
"""
Session = sessionmaker(bind = engine)
session = Session()

e1 = Employees(first_name = 'parvin', last_name = 'jolly', pay = '50000')
e2 = Employees(first_name = 'avikash', last_name = 'de', pay = '10000')
e3 = Employees(first_name = 'mario', last_name = 'lo', pay = '100000')
e4 = Employees(first_name = 'contra', last_name = 'super', pay = '100000')

session.add_all([e1, e2, e3, e4])

session.commit()

"""
Read resource by id
"""

# Enter the id to query
q_id= 1
result = session.query(Employees).get(q_id)

print("The Queried item is")
print(result.id, result.first_name, result.last_name, result.pay)


"""
update resource by id
"""


before_update = session.query(Employees).all()


print("resources before the update oepration")
for row in before_update:
   print ("id", row.id, ", first_name: ",row.first_name, ", last_name:",row.last_name, ", pay:",row.pay)

# Enter the id to query
q_id= 1
tochange = session.query(Employees).get(q_id)

tochange.pay = 100000

session.commit()

after_update = session.query(Employees).all()

print("resources after the update oepration")
for row in after_update:
   print ("id", row.id, ", first_name: ",row.first_name, ", last_name:",row.last_name, ", pay:",row.pay)


"""
Delete resource by id
"""

result = session.query(Employees).all()


print("resources before the delete oepration")
for row in result:
   print ("id", row.id, ", first_name: ",row.first_name, ", last_name:",row.last_name, ", pay:",row.pay)

try:
    # Enter the id to delete

    q_id = 3

    todelete = session.query(Employees).get(q_id)

    session.delete(todelete)

    session.commit()

    endresult = session.query(Employees).all()

    print("resources after the delete oepration")

    for row in endresult:

          print ("id", row.id, ", first_name: ",row.first_name, ", last_name:",row.last_name, ", pay:",row.pay)

except:
    print("resource with the id doesnot exist. Please check the id")
