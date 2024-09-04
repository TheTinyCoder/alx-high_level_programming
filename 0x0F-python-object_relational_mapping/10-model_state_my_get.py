#!/usr/bin/python3
"""
Script that prints id of State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import Base, State
import sys


if __name__ == "__main__":
    args = sys.argv
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(args[1], args[2], args[3]))
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == args[4]).all()
    if len(states) != 0:
        for state in states:
            print(state.id)
    else:
        print("Not found")
