#!/usr/bin/python3
"""
Script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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
    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    print(state.id)
