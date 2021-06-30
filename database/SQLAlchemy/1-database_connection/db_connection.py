from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import os

engine = create_engine('sqlite:///university.db', echo = True)

meta = MetaData()

meta.create_all(engine)