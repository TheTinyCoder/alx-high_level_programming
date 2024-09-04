#!/usr/bin/python3
"""
Script that lists all State objects and corresponding City objects
from the database hbtn_0e_101_usa
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
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
