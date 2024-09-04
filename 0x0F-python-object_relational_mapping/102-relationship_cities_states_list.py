#!/usr/bin/python3
"""
Script that lists all City objects
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
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")
