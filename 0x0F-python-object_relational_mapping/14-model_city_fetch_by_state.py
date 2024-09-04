#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
and their respective State
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State
from model_city import City
import sys


if __name__ == "__main__":
    args = sys.argv
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(args[1], args[2], args[3]))
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(
        State.name, City.id, City.name).join(State).order_by(City.id).all()
    for city in cities:
        print(f"{city[0]}: ({city[1]}) {city[2]}")
