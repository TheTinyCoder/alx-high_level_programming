#!/usr/bin/python3
"""
State module linked to database
"""

from model_state import Base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
import sys


class City(Base):
    """
    Defines table states and its constraints
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
