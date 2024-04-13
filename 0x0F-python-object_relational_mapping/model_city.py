#!/usr/bin/python3
"""
class definition of a City
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey


class City(Base):
    """
    Inherits from Base (imported from model_state) and
    links to the MySQL table cities
    id (Integer): column of uniquie integers
    name (String): column of a string
    state_id (Integer): column of an integer(foreign key to states.id)
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
