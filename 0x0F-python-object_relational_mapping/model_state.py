#!/usr/bin/python3
"""
State module linked to database
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
import sys


Base = declarative_base()

class State(Base):
    __tablename__='states'
    id = Column(Integer, unique=True, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    args = sys.argv
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(args[1], args[2], args[3]))
    engine.connect()
    Base.metadata.create_all(engine)

