#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
in the database hbtn_0e_100_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == "__main__":
    args = sys.argv
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(args[1], args[2], args[3]))
    engine.connect()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    city = City(name="San Francisco", state=State(name="California"))
    session.add(city)
    session.commit()
